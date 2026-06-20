import os


BASE_URL = os.getenv("BASE_URL", "https://rahulshettyacademy.com/angularpractice/")
BROWSER = os.getenv("BROWSER", "chrome")
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
