#Selenium tut

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains
import re
import time
#use ctrl c in browser and shift insert in arch
service = Service(r"/home/nunu/Tools/geckodriver" )
driver = webdriver.Firefox(service=service)


def autodeck(query):

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

    terms_per_deck = [] 
    stars_per_deck = []
    #filter by num of terms and see if there are stars:
    for element_text in previewsel:
        #please fix this so that one term things can be seen 
        termraw= list(re.findall(r'(\d+ terms)',element_text)) #need to figure out how to make it so that the thing in braces and be whatever num
        starsraw= re.findall(r"(terms\n\d{1})",element_text)
        if len(termraw) > 0:
            termnum = termraw[0]   
            termnum = int(termnum[0:2])
            terms_per_deck.append(termnum)
            stars_per_deck.append(0)
        if len(starsraw) > 0 and len(termraw)> 0: 
            termnum = termraw[0]  
            termnum = int(termnum[0:2])
            starnum = starsraw[0]
            starnum = int(starnum[-1])
            stars_per_deck.append(starnum)
            terms_per_deck.append(termnum)
    print(terms_per_deck,stars_per_deck)
    
    maxstars = max(stars_per_deck)
    if maxstars > 0:
        index_max_stars = stars_per_deck.index(maxstars)
        #use the index of max stars to get term num
        termnum = terms_per_deck[index_max_stars]
        specdeck = driver.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[1]/div/div[{index_max_stars }]/div/div/div") 
        #multiple buttons with name preview so i had to find element within element
        deck = specdeck.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[1]/div/div[{index_max_stars}]/div/div/div/div[2]/button/span")
        deck.click()
        #after clicking on preview
        for i in range(1,termnum+1): #this is a scroll prob
            time.sleep(0.1) 
            cards = driver.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[3]/div[{i}]")
            driver.execute_script("return arguments[0].scrollIntoView(true);", cards)
            print(cards.text) 
    else:
        maxterms = max(terms_per_deck)
        index_max_terms = terms_per_deck.index(maxterms) 
autodeck('AP-Calc')# query should be given with - where the spaces should be
                                                                                              
