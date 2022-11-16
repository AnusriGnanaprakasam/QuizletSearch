#Selenium tut

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

service = Service(r"/home/nunu/Tools/geckodriver" )
driver = webdriver.Firefox(service=service)
def quizletdecks(query):

    driver.get(f"https://quizlet.com/search?query={query}&type=sets")

    #format: change url for whatever topic you want to search for
    # work but i don't need it bodyclass=  driver.find_element(By.XPATH,value="/html/body/div[4]/main/div")
    #site = driver.find_element(By.CLASS_NAME,value="site")
    #main = driver.find_element(By.ID,value="page") 
    #searchResultsPage = driver.find_element(By.CLASS_NAME,value="SearchResultsPage") 
    #i did try to go layer by layer to make sure it could find elements

    setview = driver.find_element(By.CLASS_NAME,value="SetsView-resultList") 
    Decks = setview.find_elements(By.CLASS_NAME,value="SearchResultsPage-result")
    print(type(Decks))
    previewsel = []
    for deck in range(len(Decks)):
        previewsel.append(Decks[deck].text)
    print(previewsel)

    stats_per_deck = [] 
    #filter by num of terms and see if there are stars:
    for element_text in previewsel:
        termraw= list(re.findall(r'(\d{2} terms)',element_text)) #need to figure out how to make it so that the thing in braces and be whatever num
        starsraw= re.findall(r"(terms\n\d{1})",element_text)
        if len(termraw) > 0:
            termnum = termraw[0]   
            termnum = str(termnum[0:2])
            stats = termnum
            stats_per_deck.append(stats)
        if len(starsraw) > 0 and len(termraw)> 0: 
            termnum = termraw[0]  
            termnum = str(termnum[0:2])
            starnum = starsraw[0]
            starnum = str(starnum[6:-1])
            stats = termnum +" "+ starnum
            stats_per_deck.append(stats)
quizletdecks('AP-Calc')# query should be given with - where the spaces should be
                                                                                              
'''first filter for highest amount of terms
[nunu@arch WebScraping]$ echo then filter for categorize 5 starts and lower
then filter for categorize 5 starts and lower
[nunu@arch WebScraping]$ echo then categorize for num of views
then categorize for num of views
[nunu@arch WebScraping]$ echo then check for name
then check for name
[nunu@arch WebScraping]$ echo and do the find element by txt thing
and do the find element by txt thing
'''
