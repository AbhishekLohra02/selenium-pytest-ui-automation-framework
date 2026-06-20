# Selenium Pytest UI Automation Framework

UI automation framework for the [Rahul Shetty Academy Angular practice site](https://rahulshettyacademy.com/angularpractice/). It uses Python, Selenium, pytest, Page Object Model, HTML reporting, and GitHub Actions.

## Tech Stack

- Python 3.11
- Selenium WebDriver
- pytest
- pytest-html
- Page Object Model
- GitHub Actions

## Project Structure

```text
Framework/
  config/          Environment and runtime configuration
  pages/           Page Objects and reusable browser actions
  tests/
    smoke/         Critical availability checks
    sanity/        Focused feature checks
    regression/    End-to-end business-flow coverage
  reports/         Generated HTML reports and failure screenshots
  conftest.py      pytest fixtures and browser setup
  pytest.ini       pytest markers and test configuration
```

## Setup

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r Framework/requirements.txt
```

## Run Tests

Run all tests:

```bash
cd Framework
pytest
```

Run individual suites:

```bash
pytest -m smoke
pytest -m sanity
pytest -m regression
```

Run tests in headless mode:

```bash
pytest -m smoke --headless
```

Generate an HTML report:

```bash
pytest -m regression --html=reports/regression-report.html --self-contained-html
```

## Test Coverage

| Suite | Coverage |
| --- | --- |
| Smoke | Home page availability and Shop page navigation |
| Sanity | Valid form submission and cart count updates |
| Regression | Name validation, cart total validation, and end-to-end order placement |

## CI/CD

GitHub Actions runs the smoke, sanity, and regression suites on pushes and pull requests to `main`. Test reports and failure screenshots are uploaded as workflow artifacts.

Workflow: [ui-tests.yml](.github/workflows/ui-tests.yml)
