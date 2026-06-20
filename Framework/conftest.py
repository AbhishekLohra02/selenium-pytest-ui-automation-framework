from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from config.config import BASE_URL, BROWSER, HEADLESS


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BROWSER)
    parser.addoption("--headless", action="store_true", default=HEADLESS)


def _create_chrome_driver(headless):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    if headless:
        options.add_argument("--headless=new")

    return webdriver.Chrome(options=options)


def _create_edge_driver(headless):
    options = webdriver.EdgeOptions()
    options.add_argument("--window-size=1920,1080")

    if headless:
        options.add_argument("--headless=new")

    return webdriver.Edge(options=options)


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        driver = _create_chrome_driver(headless)
    elif browser == "edge":
        driver = _create_edge_driver(headless)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    if not headless:
        driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("setup")
    if driver is None:
        return

    screenshot_dir = Path("reports/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = screenshot_dir / f"{item.name}_{timestamp}.png"
    driver.save_screenshot(str(screenshot_path))
