#Selenium tut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path=r"/home/nunu/Tools/geckodriver")

def quizletdecks(query):
    driver.get(f"https://quizlet.com/search?query={query}&type=sets")
    #format: change url for whatever topic you want to search for
    #bodyclass=  driver.find_element(By.XPATH,value="/html/body/div[4]/main/div")
    site = driver.find_element(By.CLASS_NAME,value="site")
    main = site.find_element(By.ID,value="page") 
    searchResultsPage = main.find_element(By.CLASS_NAME,value="SearchResultsPage") 
    setview = searchResultsPage.find_element(By.CLASS_NAME,value="SetsView-resultList") 
    Decks = setview.find_elements(By.CLASS_NAME,value="SearchResultsPage-result")
    print(type(Decks))
    for deck in range(len(Decks)):
        print(Decks[deck].text)
quizletdecks('AP-Calc')# query should be given with - where the spaces should be

