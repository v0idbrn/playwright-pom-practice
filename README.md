# Web Automation Framework: SauceDemo Authentication Suite 🚀

## 📝 Overview
This repository features a professional end-to-end (E2E) automation project for the **SauceDemo** web application. It is built using the **Page Object Model (POM)** architectural pattern to ensure that the test scripts are modular, easy to maintain, and scalable.

As an **Electronics Technician** transitioning into **QA Automation**, I developed this suite by applying the same systematic troubleshooting and logical rigor used in hardware diagnostics to software quality assurance.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Test Runner:** Pytest
* **Automation Library:** Playwright (Python)
* **Design Pattern:** Page Object Model (POM)

## 🏗 Project Structure
The project is organized to separate the UI logic from the test execution, following industry best practices:

    ├── pages/
    │   └── login_page.py      # UI Locators and interaction workflows
    ├── tests/
    │   └── test_login.py      # Functional test cases (Success & Failure)
    ├── requirements.txt       # Project dependencies
    └── README.md              # Project documentation

## 🧪 Test Coverage
* **Successful Authentication:** Validates that a user can access the inventory dashboard with correct credentials and verifies the final URL redirection.
* **Login Failure (Negative Testing):** Ensures the system correctly identifies invalid credentials and displays the expected error validation messages.

## 🚀 Getting Started

### 1. Clone the repository
    git clone https://github.com/v0idbrn/saucedemo-automation.git
    cd saucedemo-automation

### 2. Install dependencies
    pip install -r requirements.txt
    playwright install chromium

### 3. Run the tests
You can run the tests in headful mode (visible browser) to see the automation in action:

    pytest tests/test_login.py --headful

## 🔬 Technical Highlights
* **Logic-Driven Assertions:** Implementation of precise verification points to ensure system stability.
* **Resilient Locators:** Use of attribute-based selectors (`data-test`) to minimize test flakiness.
* **Professional Documentation:** All modules utilize Python Docstrings for enhanced code readability and maintainability.

---

**Developed by Gaetano Morelli** *Electronics Technician | AI Quality Auditor | QA Automation Enthusiast* [LinkedIn Profile](https://www.linkedin.com/in/gaemor) | [Upwork Profile](https://www.upwork.com/freelancers/~018fbb82ed714c18c8)