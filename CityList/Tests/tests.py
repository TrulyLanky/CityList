from django.test import LiveServerTestCase

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.quit()


"""
class HostTest(LiveServerTestCase):

    def testhomepage(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Optional: run Chrome in headless mode
        chrome_driver_path = './Tests/chrome-win64/chrome.exe'  # Update the path accordingly

        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get('http://127.0.0.1:8000/')

        time.sleep(5)  # Give time for the browser to open before running check

        assert "Hello World!" in driver.title
"""