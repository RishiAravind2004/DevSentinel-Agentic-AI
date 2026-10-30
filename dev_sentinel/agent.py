import json
import time
import httpx
from google.adk.agents import Agent


# ─────────────────────────────────────────────
# TOOL 1 — Discover what paths exist on the URL
# ─────────────────────────────────────────────
def discover_endpoints(base_url: str) -> dict:
    """Probes a base URL to confirm it is reachable and returns basic info.

    Args:
        base_url: Root URL of the web app or API (e.g. 'https://jsonplaceholder.typicode.com').

    Returns:
        Dict with reachability status and response details.
    """
    try:
        with httpx.Client(timeout=8, follow_redirects=True) as client:
            resp = client.get(base_url)
        return {
            "base_url": base_url,
            "reachable": True,
            "status_code": resp.status_code,
            "content_type": resp.headers.get("content-type", "unknown"),
            "response_preview": resp.text[:300],
        }
    except Exception as e:
        return {"base_url": base_url, "reachable": False, "error": str(e)}


# ─────────────────────────────────────────────
# TOOL 2 — Execute a single HTTP test case
# ─────────────────────────────────────────────
def run_test_case(
    base_url: str,
    method: str,
    path: str,
    expected_status: int,
    body: str = "",
) -> dict:
    """Executes one HTTP test case using httpx and validates the response.

    Args:
        base_url: Root URL (e.g. 'https://jsonplaceholder.typicode.com').
        method: HTTP method — GET, POST, PUT, DELETE, PATCH.
        path: Path to append to base_url (e.g. '/posts' or '/posts/1').
        expected_status: The HTTP status code we expect (e.g. 200, 201, 404).
        body: Optional JSON string body for POST/PUT requests.

    Returns:
        Dict with test name, result (PASS/FAIL), actual status, and details.
    """
    url = base_url.rstrip("/") + "/" + path.lstrip("/")
    test_name = f"{method} {path}"
    start = time.time()

    try:
        headers = {"Content-Type": "application/json"} if body else {}
        json_body = json.loads(body) if body else None

        with httpx.Client(timeout=8, follow_redirects=True) as client:
            resp = client.request(method.upper(), url, json=json_body, headers=headers)

        elapsed = round((time.time() - start) * 1000)
        passed = resp.status_code == expected_status

        return {
            "test": test_name,
            "url": url,
            "result": "PASS" if passed else "FAIL",
            "expected_status": expected_status,
            "actual_status": resp.status_code,
            "response_time_ms": elapsed,
            "response_preview": resp.text[:200],
        }
    except Exception as e:
        return {
            "test": test_name,
            "url": url,
            "result": "ERROR",
            "expected_status": expected_status,
            "actual_status": None,
            "response_time_ms": None,
            "error": str(e),
        }


# ─────────────────────────────────────────────
# TOOL 3 — Build a final report from results
# ─────────────────────────────────────────────
def generate_report(results_json: str) -> dict:
    """Aggregates test results into a structured report.

    Args:
        results_json: JSON string — a list of result dicts from run_test_case.

    Returns:
        A summary report dict with pass/fail counts and per-test details.
    """
    try:
        results = json.loads(results_json)
    except Exception as e:
        return {"error": f"Could not parse results: {e}"}

    total = len(results)
    passed = sum(1 for r in results if r.get("result") == "PASS")
    failed = sum(1 for r in results if r.get("result") == "FAIL")
    errors = sum(1 for r in results if r.get("result") == "ERROR")

    return {
        "summary": {
            "total": total,
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "score": f"{passed}/{total}",
        },
        "results": results,
    }


# ─────────────────────────────────────────────
# ROOT AGENT
# ─────────────────────────────────────────────
root_agent = Agent(
    name="dev_sentinel",
    model="gemini-2.0-flash",
    description="An AI-powered API testing agent that generates and runs test cases.",
    instruction="""
You are DevSentinel — an AI-powered API testing agent.

When the user gives you a URL, follow these exact steps IN ORDER:

**STEP 1 — Discover**
Call discover_endpoints(base_url) to confirm the URL is reachable.
Tell the user the URL is reachable (or not) and the content type.

**STEP 2 — Generate Test Cases**
Based on the URL and content type, think of 5–8 relevant HTTP test cases.
For a REST API, include: GET collection, GET single item, POST create, PUT update, DELETE.
For a plain website, test the homepage and common paths like /about, /contact, /404.
Show the user the list of planned test cases BEFORE running them.

**STEP 3 — Execute in Loop**
Run each test case ONE BY ONE using run_test_case().
After each call, tell the user: ✅ PASS or ❌ FAIL with the status code.

**STEP 4 — Report**
Collect ALL results into a JSON array string and call generate_report(results_json).
Display the final report clearly:
- Score (e.g. 6/8 passed)
- Table of each test: name | result | expected | actual | time
- Any failures highlighted.

Always be concise and developer-friendly.
""",
    tools=[discover_endpoints, run_test_case, generate_report],
)
