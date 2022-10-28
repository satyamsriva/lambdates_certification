import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

username = os.getenv("satyam0711")
access_key = os.getenv("oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW")

gridUrl = "hub.lambdatest.com/wd/hub"

capability = {
	"browserName": "Internet Explorer",
	"browserVersion": "11.0",
	"LT:Options": {
		"username": "satyam0711",
		"accessKey": "oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW",
		"platformName": "Windows 10",
		"project": "Untitled"
	}
}

url = "http://satyam0711:oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW@hub.lambdatest.com/wd/hub"

serv_obj=Service("C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capability
)
driver.get("https://www.lambdatest.com/selenium-playground")
driver.maximize_window()
time.sleep(8)
driver.find_element(By.XPATH,"//a[normalize-space()='Drag & Drop Sliders']").click()

source_element=driver.find_element(By.XPATH,"//input[@value='15']")
target_element=driver.find_element(By.XPATH,"//output[@id='rangeSuccess']")

print("Printing title of current page :"+driver.title)
driver.execute_script("lambda-status=passed")
print("Requesting to mark test : pass")
print(driver.current_url)

actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()

driver.quit()