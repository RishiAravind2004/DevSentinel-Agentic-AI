# 🛡️ DevSentinel — Minimal AI Testing Agent

An AI-powered API testing agent built with **Google ADK** and **httpx**.  
Give it a URL — it discovers, generates test cases, executes them, and reports results.

---

## ✨ How It Works

```
User gives URL
      │
      ▼
① Discover      — httpx pings the URL, checks reachability + content-type
      │
      ▼
② Plan Tests    — Gemini AI generates 5–8 relevant test cases
      │
      ▼
③ Execute Loop  — httpx runs each test (GET / POST / PUT / DELETE)
      │             reports ✅ PASS / ❌ FAIL live
      ▼
④ Report        — Final score + summary table
```

---

## 📁 Project Structure

```
Testing Agent/
├── .env                      ← your Gemini API key
├── README.md
└── dev_sentinel/
    ├── __init__.py
    └── agent.py              ← Agent + 3 tools (~160 lines)
```

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install google-adk httpx
```

### 2. Add your API key

Open `.env` and paste your key from [Google AI Studio](https://aistudio.google.com/app/apikey):

```env
GOOGLE_API_KEY=AIza...your_key_here
```

### 3. Run the agent

```bash
# Web UI (recommended)
adk web

# CLI
adk run dev_sentinel "Test https://jsonplaceholder.typicode.com"
```

Open **http://127.0.0.1:8000** in your browser.

---

## 🛠️ Tools

| Tool | Description |
|---|---|
| `discover_endpoints(base_url)` | Confirms URL is reachable via httpx, returns status + content-type |
| `run_test_case(base_url, method, path, expected_status, body)` | Runs one HTTP test, returns PASS/FAIL + response time (ms) |
| `generate_report(results_json)` | Aggregates all results into a score + summary |

---

## 💬 Example Prompts

```
Test https://jsonplaceholder.typicode.com
Check https://httpbin.org
Run tests on https://api.github.com
```

---

## 📊 Sample Output

```
✅ Discovering https://jsonplaceholder.typicode.com...
   Status: 200 | Content-Type: application/json

📋 Planned 6 test cases:
   1. GET  /posts          → expect 200
   2. GET  /posts/1        → expect 200
   3. POST /posts          → expect 201
   4. PUT  /posts/1        → expect 200
   5. DELETE /posts/1      → expect 200
   6. GET  /invalid        → expect 404

🔄 Running tests...
   ✅ GET  /posts       200  (312ms)
   ✅ GET  /posts/1     200  (289ms)
   ✅ POST /posts       201  (341ms)
   ✅ PUT  /posts/1     200  (298ms)
   ✅ DELETE /posts/1   200  (276ms)
   ✅ GET  /invalid     404  (261ms)

📊 Report: 6/6 passed ✅
```

---

## ⚙️ Requirements

- Python 3.10+
- `google-adk`
- `httpx`
- Gemini API key (free at [aistudio.google.com](https://aistudio.google.com/app/apikey))

---

## 📄 License

MIT
