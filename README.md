# Enterprise Playwright Python Automation Framework

An enterprise-style QA automation framework built with **Playwright, Python, Pytest, API automation, JSON Schema validation, GitHub Actions CI/CD, and reusable framework components**.

This project is being developed as a hands-on automation engineering project, with the goal of creating a maintainable framework suitable for modern web and API testing.

---

## 🚀 Tech Stack

* **Python**
* **Playwright**
* **Pytest**
* **Requests**
* **REST API Automation**
* **JSON / JSON Schema**
* **Page Object Model (POM)**
* **Git & GitHub**
* **GitHub Actions**
* **Docker** *(in progress)*

---

## 🧪 Current Automation Coverage

### UI Automation

* SauceDemo login automation
* Page Object Model implementation
* Reusable Base Page
* Products page automation
* Cart automation
* Checkout workflow
* JSON-based test data
* Pytest parameterization
* Environment configuration using `.env`

### API Automation

* GET requests
* POST requests
* PUT requests
* PATCH requests
* DELETE requests
* Query parameters
* Custom request headers
* Authentication/header handling
* Reusable API Client
* `requests.Session`
* Centralized API request handling
* JSON response assertions
* JSON Schema validation

### CI/CD

The project is integrated with **GitHub Actions**.

Current pipeline:

```text
Git Push
   ↓
GitHub Actions
   ↓
Checkout Repository
   ↓
Setup Python
   ↓
Install Dependencies
   ↓
Install Playwright
   ↓
Run Pytest
   ↓
Test Result
```

The automated test suite is executed in a GitHub Actions runner.

---

## 📁 Project Structure

```text
Enterprise-Playwright-Framework/
│
├── .github/
├── api/
├── config/
├── data/
├── database/
├── locators/
├── logs/
├── pages/
├── reports/
├── resources/
├── schemas/
├── screenshots/
├── tests/
├── utils/
├── venv/
│
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## 🏗️ Framework Architecture

```text
                Enterprise Automation Framework
                           │
          ┌────────────────┴────────────────┐
          │                                 │
      UI Automation                    API Automation
          │                                 │
      Playwright                         Requests
          │                                 │
     Page Objects                       API Client
          │                                 │
        Pytest                         Assertions
          │                                 │
          └────────────────┬────────────────┘
                           │
                     Test Execution
                           │
                        Pytest
                           │
                    GitHub Actions
                           │
                       CI Pipeline
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Prem123e/Enterprise-Playwright-Framework.git
```

### 2. Navigate to the project

```bash
cd Enterprise-Playwright-Framework
```

### 3. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright browsers

```bash
playwright install
```

### 6. Run the test suite

```bash
pytest -v
```

---

## 📊 Current Test Status

The current local test suite contains:

**11 automated tests**

Latest local execution:

```text
11 passed
```

The same project is also configured to execute automatically through GitHub Actions.

---

## 🔐 Configuration

Environment-specific configuration is maintained through `.env`.

Example:

```text
BASE_URL=https://www.saucedemo.com
API_BASE_URL=https://jsonplaceholder.typicode.com
```

Sensitive configuration is excluded from source control using `.gitignore`.

---

## 🎯 Project Goals

The framework is continuously being enhanced with additional enterprise automation capabilities.

Planned areas include:

* Docker-based test execution
* Advanced CI/CD
* Cloud execution
* SQL/database validation
* AI-assisted test automation
* Advanced reporting
* Additional API automation
* Framework scalability improvements

---

## 👨‍💻 About

This project is part of my hands-on journey toward becoming a modern **SDET / QA Automation Engineer**.

The focus is on building practical automation solutions rather than learning tools in isolation.

**Playwright → API Automation → CI/CD → Docker → Cloud → AI for Test Automation**

---

## 📌 Repository

GitHub:

https://github.com/Prem123e/Enterprise-Playwright-Framework
