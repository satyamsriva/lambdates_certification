import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

username = os.getenv("satyam0711")
access_key = os.getenv("oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW")

gridUrl = "hub.lambdatest.com/wd/hub"

capability = {
    "browserName": "Chrome",
    "browserVersion": "88.0",
    "LT:Options": {
        "username": "satyam0711",
        "accessKey": "oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW",
        "platformName": "Windows 10",
        "project": "Untitled"
    }
}

url = "http://satyam0711:oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW@hub.lambdatest.com/wd/hub"



serv_obj = Service("C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capability
)
driver.get("https://www.lambdatest.com/selenium-playground")
driver.maximize_window()
time.sleep(8)
driver.find_element(By.XPATH, "//a[normalize-space()='Simple Form Demo']").click()

# Validate that the URL contains “simple-form-demo”
print("Printing title of current page :"+driver.title)
driver.execute_script("lambda-status=passed")
print("Requesting to mark test : pass")
print(driver.current_url)

driver.find_element(By.ID, "user-message").send_keys("“Welcome to LambdaTest”.")
driver.find_element(By.ID, "showInput").click()

# Validate whether the same text message is displayed in the right-hand panel under the “Your Message:” section.

text = driver.find_element(By.ID, "message").text
print(text)
#driver.execute_script("lambda-status=passed")
#print("Requesting to mark test : pass")

time.sleep(5)

driver.quit()
