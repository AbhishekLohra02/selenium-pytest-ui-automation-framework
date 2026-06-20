# Selenium Pytest Automation Framework

This framework automates the Rahul Shetty Academy Angular practice site with Python, Selenium, pytest, and Page Object Model.

## Install

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Run Tests

Run all tests:

```bash
pytest
```

Run a suite:

```bash
pytest -m smoke
pytest -m sanity
pytest -m regression
```

Run headless:

```bash
pytest -m smoke --headless
```

Generate reports:

```bash
pytest --junitxml=reports/results.xml --html=reports/report.html --self-contained-html
```

Failed-test screenshots are saved in `reports/screenshots`.
