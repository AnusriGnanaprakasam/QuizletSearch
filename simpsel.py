# Selenium tut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path=r"/home/nunu/Tools/geckodriver")

driver.get("https://github.com")
print(driver.title)

def makegitaccount(email):
    search = driver.find_element(by=By.ID,value="user_email")#name is the same as id
    search.send_keys(email)
    search.send_keys(Keys.ENTER)#enter made you go to next pg
    try:
    # wait 10 seconds before looking for element
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
    finally:
    # else quit
        driver.quit()            
        print(driver.page_source)
        time.sleep(6)

makegitaccount("anusri.gnanaprakasom@gmail.com")


