# 🛡️ DevSentinel

### AI-Powered Application Testing Agent

DevSentinel is an **AI-powered testing agent** designed to reduce the repetitive effort involved in manually testing applications after frequent development changes.

The agent analyzes an application, generates relevant test cases, executes automated tests, detects failures, and provides actionable results to help developers validate their applications efficiently.

---

## 🚀 Features

- 🤖 AI-powered test planning and execution
- 🧪 Automatic test case generation
- 🌐 Web application testing
- 🔌 API testing
- 🔗 Web + API application testing
- 🎭 Browser automation using Playwright
- 📡 API testing using HTTPX
- ❌ Failure detection and reporting
- 📊 Actionable test results
- 🔄 Supports repeated testing after application changes

---

## 🎯 Problem Statement

During application development, developers frequently make changes to features, APIs, user interfaces, and backend logic.

Manually testing the entire application after every change can be:

- Time-consuming
- Repetitive
- Difficult to maintain
- Prone to human error

DevSentinel aims to reduce this manual effort by automating the application testing workflow.

---

## 💡 Solution

DevSentinel uses an **agent-based architecture** to analyze the application and determine the appropriate testing approach.

It currently supports three testing modes:

```text
WEB
└── Playwright

API
└── HTTPX

WEB + API
├── Playwright
└── HTTPX
```

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │     Developer   │
                    │ Application URL │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   DevSentinel   │
                    │   AI Agent      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Application     │
                    │ Discovery       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Test Planning   │
                    │ & Generation    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          Web Testing    API Testing    Web + API
              │              │              │
              ▼              ▼              ▼
         Playwright       HTTPX      Playwright
                                        +
                                      HTTPX
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Test Execution  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Results &       │
                    │ Failure Report  │
                    └─────────────────┘
```

---

## 🧠 Agent Workflow

```text
User Request
      │
      ▼
Application Discovery
      │
      ▼
Identify Application Type
      │
      ├── Web Application
      │
      ├── API
      │
      └── Web + API
             │
             ▼
      Generate Test Cases
             │
             ▼
       Execute Tests
             │
             ▼
      Analyze Results
             │
             ▼
       Generate Report
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangGraph | Agent workflow orchestration |
| Playwright | Web application testing |
| HTTPX | API testing |
| Pydantic | Data validation and state models |

---

## 📂 Project Structure

```text
DevSentinel-Agentic-AI/
│
├── app/
│   ├── agents/
│   │   └── testing_agent.py
│   │
│   ├── graph/
│   │   └── workflow.py
│   │
│   ├── nodes/
│   │   ├── discovery.py
│   │   ├── test_planner.py
│   │   ├── web_tester.py
│   │   ├── api_tester.py
│   │   ├── executor.py
│   │   └── reporter.py
│   │
│   ├── tools/
│   │   ├── playwright_tool.py
│   │   └── httpx_tool.py
│   │
│   ├── models/
│   │   └── state.py
│   │
│   └── main.py
│
├── tests/
│
├── reports/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RishiAravind2004/DevSentinel-Agentic-AI.git
```

### 2. Navigate to the Project

```bash
cd DevSentinel-Agentic-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Playwright Browsers

```bash
playwright install
```

---

## ▶️ Usage

Run the application:

```bash
python app/main.py
```

Example testing modes:

```text
1. Web Application Testing
2. API Testing
3. Web + API Testing
```

Provide the application URL or API endpoint, and DevSentinel will execute the appropriate testing workflow.

---

## 🧪 Supported Testing Types

### 🌐 Web Application

Uses **Playwright** to test:

- Page accessibility
- Navigation
- Forms
- User interactions
- UI functionality
- Application workflows

### 🔌 API

Uses **HTTPX** to test:

- API endpoints
- HTTP methods
- Response status codes
- Response data
- API behavior

### 🔗 Web + API

Combines:

- Playwright for frontend testing
- HTTPX for backend API testing

---

## 📊 Example Output

```text
DevSentinel Test Report

Application Type: Web + API

Tests Executed: 15
Passed: 12
Failed: 2
Skipped: 1

Status: PARTIAL FAILURE

Failures:

1. Login API returned HTTP 500
2. Profile update form validation failed
```

---

## 🎯 Project Goals

- Reduce repetitive manual testing
- Automate test case generation
- Validate applications after development changes
- Detect functional failures
- Provide useful test reports
- Support both frontend and backend testing

---

## 🔮 Future Enhancements

- [ ] AI-based intelligent test case generation
- [ ] Requirement-based testing
- [ ] Automatic regression testing
- [ ] Screenshot capture for failed tests
- [ ] Detailed HTML/PDF reports
- [ ] CI/CD integration
- [ ] Test history and analytics dashboard
- [ ] Database testing
- [ ] Authentication workflow testing
- [ ] Parallel test execution

---

## ⚠️ Scope

DevSentinel focuses on **functional application testing and validation**.

Current scope includes:

- Web application testing
- API testing
- Web + API testing
- Automated test execution
- Functional validation

It does **not** focus on penetration testing, vulnerability exploitation, or offensive security testing.

---

## 👨‍💻 Author

**Rishi Aravind P**

- GitHub: [RishiAravind2004](https://github.com/RishiAravind2004)
- LinkedIn: [rishi-aravind](https://linkedin.com/in/rishi-aravind)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐!

---

### 📌 Project Status

🚧 **Currently Under Development**
