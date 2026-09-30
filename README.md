# Adra Product Studio - QA Automation Test Suite

## Project Overview

This project is a Selenium-based UI automation test suite created for testing the Signup and Login flows of the Adra Product Studio candidate portal.

The automation focuses on:

- Positive and negative test scenarios
- Form validation
- Authentication behavior
- Navigation
- Dynamic UI behavior
- Maintainable locators
- Page Object Model
- Explicit waits
- PyTest test execution
- HTML test reporting

## Application Under Test

**Application:** Adra Product Studio Candidate Portal

**URL:** https://admin.adraproductstudio.com/

The automated tests cover the candidate registration and login workflows.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| PyTest | Test framework |
| pytest-html | HTML test reporting |
| Chrome | Browser |
| Page Object Model | Test architecture |

## Project Structure

```text
adra_qa_automation/
│
├── pages/
│   ├── login_page.py
│   └── signup_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_signup.py
│
├── reports/
│   └── adra_qa_report.html
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Directory Description

**pages/**  
Contains Page Object classes, locators, and page-level actions.

**tests/**  
Contains the automated test cases.

**reports/**  
Contains generated HTML test reports.

**conftest.py**  
Contains the PyTest WebDriver fixture used by the tests.

## Test Coverage

### Login Test Cases

1. **Valid Login**
   - Verifies that a registered candidate can successfully log in.
   - Expected destination contains:
     `/candidates_home/qa-assessment`

2. **Invalid Credentials**
   - Verifies login behavior with invalid username and password.
   - Expected message:
     `User not found`

3. **Empty Username and Password**
   - Verifies that login does not occur when both fields are empty.

4. **Username Without Password**
   - Verifies that login does not occur when only the username is provided.

5. **Password Without Username**
   - Verifies that login does not occur when only the password is provided.

### Signup Test Cases

1. **Navigate to Candidate Registration**
   - Verifies navigation from the login page to candidate registration.

2. **Fresher Behavior**
   - Verifies that work-experience fields are hidden when Fresher is selected.

3. **Experienced Candidate Behavior**
   - Verifies that work-experience fields are displayed when Experienced is selected.

4. **Required Field Validation**
   - Verifies required-field validation messages when the form is submitted without required data.

5. **Phone Number Validation**
   - Verifies that a phone number containing fewer than 10 digits is rejected.
   - Expected message:
     `Mobile number should be 10 digit.`

   The application prevents additional input beyond 10 digits and restricts non-numeric input at the field level, so separate submission tests for those cases are not required.

6. **Invalid Email Format**
   - Verifies that an invalid email address is rejected.
   - Expected message:
     `Please enter valid email address`

7. **Valid Candidate Registration**
   - Verifies successful candidate registration.
   - Verifies return to the login page.
   - Verifies that the registered phone number is populated as the username.
   - Verifies that a generated password is populated.

## Test Summary

| Module | Tests | Status |
|---|---:|---|
| Login | 5 | Passed |
| Signup | 7 | Passed |
| **Total** | **12** | **12 Passed** |

Latest full-suite execution:

```text
12 passed
```

## Framework Design

### Page Object Model

The framework follows the Page Object Model (POM).

Page-specific locators and actions are separated from test cases:

```text
pages/
├── login_page.py
└── signup_page.py
```

The test files focus on test scenarios rather than directly interacting with Selenium elements.

This improves:

- Maintainability
- Reusability
- Readability
- Locator management

## Locator Strategy

The automation uses locator strategies based on element stability and uniqueness.

### ID

Used when a stable ID is available.

Example:

```python
(By.ID, "Fresher")
```

### NAME

Used for login fields where stable names are available.

Example:

```python
(By.NAME, "Username")
```

### CSS Selector

Used when meaningful attributes provide a stable selector.

Example:

```python
(By.CSS_SELECTOR, "button[title='Login']")
```

### Relative XPath

Used for signup fields where stable IDs or names are not available.

Example:

```python
(
    By.XPATH,
    "//label[contains(normalize-space(), 'Full Name')]/following-sibling::input"
)
```

The automation avoids relying on generic classes such as `form-control` when more specific locators are available.

## Synchronization Strategy

The framework uses Selenium explicit waits instead of fixed delays.

Example:

```python
WebDriverWait(
    driver,
    10
).until(
    EC.visibility_of_element_located(locator)
)
```

Explicit waits are used for:

- Element visibility
- Element presence
- Element clickability
- Post-login navigation

This helps reduce synchronization problems caused by dynamic page loading.

## Test Data Strategy

Signup tests generate unique phone numbers and email addresses using a timestamp.

Example:

```python
timestamp = str(int(time.time()))
```

This reduces duplicate-data failures during repeated test execution.

Valid login credentials are supplied through environment variables rather than being stored directly in the test source code.

## Running the Tests

### 1. Activate Virtual Environment

Windows PowerShell:

```powershell
.env\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run All Tests

```powershell
pytest -v
```

### 4. Run Login Tests Only

```powershell
pytest tests/test_login.py -v
```

### 5. Run Signup Tests Only

```powershell
pytest tests/test_signup.py -v
```

## HTML Test Report

The project uses `pytest-html` to generate an HTML execution report.

Create the report with:

```powershell
pytest -v --html=reports/adra_qa_report.html --self-contained-html
```

The report will be generated at:

```text
reports/adra_qa_report.html
```

## Environment Variables

Valid login credentials are not stored directly in the test source code.

Set them locally in PowerShell:

```powershell
$env:ADRA_TEST_USERNAME="your_username"
$env:ADRA_TEST_PASSWORD="your_password"
```

Then run:

```powershell
pytest tests/test_login.py -v
```

Do not commit real credentials to source control.

## Important Application Behaviors Observed

During testing, the following application behaviors were verified:

- Empty login fields do not display a validation message and login does not occur.
- Login with invalid credentials displays `User not found`.
- Candidate registration generates/populates login credentials.
- Successful candidate registration redirects to the login page.
- The registered phone number is populated as the username.
- The phone field accepts a maximum of 10 digits.
- A phone number with fewer than 10 digits produces a validation toast.
- Non-numeric phone input is restricted by the field.
- Invalid email format produces a validation toast.
- Fresher and Experienced selections control visibility of work-experience fields.
- Successful login redirects to the QA assessment page.

## Current Test Result

```text
12 test cases
12 passed
0 failed
```

Execution command:

```powershell
pytest -v
```

## Notes

This project focuses on the Signup and Login flows requested in the automation assignment.

The test suite prioritizes maintainability, meaningful functional coverage, stable locators, and clear test design rather than maximizing the number of test cases.
