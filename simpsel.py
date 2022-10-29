#Selenium tut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import copy
driver = webdriver.Firefox(executable_path=r"/home/nunu/Tools/geckodriver")

def quizletdecks(query):

    driver.get(f"https://quizlet.com/search?query={query}&type=sets")
    #format: change url for whatever topic you want to search for
    # work but i don't need it bodyclass=  driver.find_element(By.XPATH,value="/html/body/div[4]/main/div")
    site = driver.find_element(By.CLASS_NAME,value="site")
    main = site.find_element(By.ID,value="page") 
    searchResultsPage = main.find_element(By.CLASS_NAME,value="SearchResultsPage") 
    setview = searchResultsPage.find_element(By.CLASS_NAME,value="SetsView-resultList") 
    Decks = setview.find_elements(By.CLASS_NAME,value="SearchResultsPage-result")
    print(type(Decks))
    previewsel = []
    for deck in range(len(Decks)):
        previewsel.append(Decks[deck].text)
    print(previewsel)
    #make a dictionary and populate with element index and then the nums found in the element(if there is a 5 with another
    #nun then that means that it is five starts and should defn be picked regardless of num of terms
    for element_text in previewsel:
        for char in element_text:
            if char.isdigit(): 
                pass    
# Lesson 6.5: SET OPTI 
quizletdecks('AP-Calc')# query should be given with - where the spaces should be

