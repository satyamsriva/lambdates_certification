import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

username = os.getenv("satyam0711")
access_key = os.getenv("oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW")

gridUrl = "hub.lambdatest.com/wd/hub"

capability = {
	"browserName": "MicrosoftEdge",
	"browserVersion": "87.0",
	"LT:Options": {
		"username": "satyam0711",
		"accessKey": "oTwI7nduWZDjeaMqoW9K3EWZucPp1tQCYucYT2zWMTgOxABzCW",
		"platformName": "macOS Sierra",
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

driver.find_element(By.XPATH,"//a[normalize-space()='Input Form Submit']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()

print("Printing title of current page :"+driver.title)
driver.execute_script("lambda-status=passed")
print("Requesting to mark test : pass")
print(driver.current_url)

#filling form
driver.find_element(By.NAME,"name").send_keys("Satyam Srivastava")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='inputEmail4']").send_keys("satyam0711@gmai.com")
time.sleep(3)
driver.find_element(By.ID,"inputPassword4").send_keys("abcdefg")
time.sleep(3)
driver.find_element(By.NAME,"company").send_keys("abc")
time.sleep(3)
driver.find_element(By.NAME,"website").send_keys("ABCD")
time.sleep(3)

element=driver.find_element(By.NAME,"country")
drp=Select(element)

#select by text
drp.select_by_visible_text("United States")
time.sleep(2)

driver.find_element(By.ID,"inputCity").send_keys("Gorakhpur")
time.sleep(2)

driver.find_element(By.ID,"inputAddress1").send_keys("Gorakhnath")
time.sleep(2)

driver.find_element(By.ID,"inputAddress2").send_keys("Ganga Nagar")
time.sleep(2)

driver.find_element(By.ID,"inputState").send_keys("Uttar Pradesh")
time.sleep(2)

driver.find_element(By.ID,"inputZip").send_keys("273015")
time.sleep(2)

driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()

text = driver.find_element(By.XPATH,"//p[contains(text(),'Thanks for contacting us, we will get back to you ')]").text
print(text)

driver.quit()