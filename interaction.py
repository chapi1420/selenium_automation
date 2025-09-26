'''using selenium, why not find out how many articles are published in wikipedia page. I think this is gonna be greate for learning selenium'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import time

print("Launching Chrome...")
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
print(f"Page title is: {driver.title}")
article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(f"Number of articles in wikipedia is: {article_count.text}")
driver.quit()
print("Browser closed. Setup successful! ✅")