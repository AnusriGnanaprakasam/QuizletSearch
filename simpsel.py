from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains
import csv
import re
import time

#open firefox browser
service = Service(r"/home/nunu/Tools/geckodriver" )
driver = webdriver.Firefox(service=service)

def sortdecks():
    '''sorts deck based on number of terms and stars. Stores indexes of cards where term or star num = n'''
    setview = driver.find_element(By.CLASS_NAME,value="SetsView-resultList") 
    Decks = setview.find_elements(By.CLASS_NAME,value="SearchResultsPage-result")
    #Decks are on the left. There are multiple that many people make on one topic
    diffdeck = []
    for deck in range(len(Decks)):
        diffdeck.append(Decks[deck].text)

    terms_per_deck = [] 
    stars_per_deck = []
    #filter by num of terms and see if there are stars:
    for element_text in diffdeck:
        termraw= list(re.findall(r'(\d+ terms)',element_text)) 
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
    return terms_per_deck,stars_per_deck

def autodeck(query):
    '''chooses the best deck for a topic based on number of stars'''

    driver.get(f"https://quizlet.com/search?query={query}&type=sets")
    terms_per_deck,stars_per_deck = sortdecks()
    maxstars = max(stars_per_deck)
    index_max_stars = stars_per_deck.index(maxstars)
    #use the index of max stars to get term num
    termnum = terms_per_deck[index_max_stars]
    #find the specific deck that is to be used
    specdeck = driver.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[1]/div/div[{index_max_stars }]/div/div/div") 
    #multiple buttons with name preview so I had to find element within element
    deck = specdeck.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[1]/div/div[{index_max_stars}]/div/div/div/div[2]/button/span")
    #find preview button
    deck.click()
    #after clicking on preview
    #making file to host cards
    cardlist =[]
    for i in range(1,termnum+1): #this is a scroll problem
        time.sleep(0.4) #i really need to put a webdriver wait here
        cards = driver.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[3]/div[{i}]")
        driver.execute_script("return arguments[0].scrollIntoView(true);", cards)
        cardlist.append(cards.text)
    #make frontandback distinctions to turn into csv file
    csvlist = []
    for card in cardlist:
        spliter = card.index("\n")
        frontback = {"front":0,"back":0}
        frontback["front"] = card[0:spliter]
        frontback["back"] = card[spliter+1:]
        csvlist.append(frontback) 
    print(csvlist)

    fields = ["front","back"]
    
    with open("yourdeck.csv",'w') as csvfile:

        writer = csv.DictWriter(csvfile,fieldnames = fields)
        writer.writeheader()
        writer.writerows(csvlist)
#11/25: i need to use csv python lib and turn my csv file to an apkg file
#11/30 : i need to make a choose deck function to choose whatever deck I want
        # by number on the page or the text in the deck
autodeck('AP-Calc')# query should be given with - where the spaces should be
                                                                                              
