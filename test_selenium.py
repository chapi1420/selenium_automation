from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Launching Chrome...")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com")
print(f"Page title is: {driver.title}")

time.sleep(5)

driver.quit()
print("Browser closed. Setup successful! ✅")