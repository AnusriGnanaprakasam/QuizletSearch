# Selenium tut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path=r"/home/nunu/Tools/geckodriver")

def quizletdecks():
    driver.get("https://quizlet.com")
    search = driver.find_element(by=By.ID,value="GlobalSearchBar")
    search.send_keys("AP Bio")
    search.send_keys(Keys.ENTER)
   
    Tabs = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME,"AssemblyTabs"))
     ) #element is being changed dynamically everytime page is reloaded
    
    StudySets = Tabs.WebDriverWait(driver, 15).until(
     EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Study sets")]'))
     ) #e

   #j EC.presence_of_element_located((By.XPATH,value = '//*[contains(text(),"Study sets")]')))
               
    StudySets.click()    

    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "StudyModesNavItemName"))
     )
    
    
    
    
def makegitaccount(email):
    driver.get("https://github.com")
    search = driver.find_element(by=By.ID,value="user_email")#name is the same as id
    search.send_keys(email)
    search.send_keys(Keys.ENTER)#enter made you go to next pg
    try:
    # wait 10 seconds before looking for element
        element = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.CLASS_NAME, "d-flex flex-items-center flex-column flex-sm-row"))
        )
        print(element)
        element.send_keys(Keys.ENTER)
    except Exception as e:
        print(e)
        time.sleep(6)

quizletdecks()
# rip did not work cause no element found error makegitaccount("anusri.gnanaprakasom@gmail.com")

#WHY AM I DOING THIS: to get flashcards from quizlet and turn them into anki decks
#i need to look thru docs to see how to search text on page
#press continue button github signup

#9/11 : i should look at sel doc (look for nested elements ?)
