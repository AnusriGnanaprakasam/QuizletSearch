from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
# i want to try chrome with the headless option so that no window opens
import os
import csv
import re
import time

chrome_options = Options()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(options=chrome_options)

#driver = webdriver.Chrome(ChromeDriverManager().install())

def printdecks():
    setview = driver.find_element(By.CLASS_NAME, value="SetsView-resultList")
    Decks = setview.find_elements(By.CLASS_NAME, value="SearchResultsPage-result")
    # Decks are on the left. There are multiple that many people make on one topic
    diffdeck = []
    for deck in range(len(Decks)):
        diffdeck.append(Decks[deck].text)
    return diffdeck

def sortdecks():
    '''sorts deck based on number of terms and stars. Stores indexes of cards where term or star num = n'''
    terms_per_deck = [] 
    stars_per_deck = []
    #filter by num of terms and see if there are stars
    for element_text in printdecks():
        termraw= list(re.findall(r'(\d+ terms)',element_text)) 
        starsraw= re.findall(r"(terms\n\d{1})",element_text)
    
        if len(starsraw) == 0 and len(termraw) > 0:
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

def find_deck(decknum,decklen=100000):
    specdeck = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[1]/div/div[{decknum+ 1}]/div/div/div")))
    #multiple buttons with name preview so I had to find element within element
    deck = specdeck.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[1]/div/div[{decknum+ 1 }]/div/div/div/div[2]/button/span")
    #find preview button
    deck.click()
    #after clicking on preview
    #making file to host cards
    cardlist =[]

#selenium.common.exceptions.NoSuchElementException
    try:
        for i in range(1,decklen+1):
            time.sleep(0.5)
            cards = driver.find_element(By.XPATH,f"/html/body/div[4]/main/div/section[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[3]/div[{i}]")
            driver.execute_script("return arguments[0].scrollIntoView(true);", cards)
            cardlist.append(cards.text)

        return cardlist

    except NoSuchElementException:
        print(":))")
        return cardlist

def makecsv(cardlist):
    csvlist = []
    try:
        cardlist.remove('')
    except ValueError:
        pass
    for card in cardlist:
        print(card)
        spliter = card.index("\n")
        frontback = {"front": card[0:spliter], "back": card[spliter + 1:]}
        csvlist.append(frontback)
    print(csvlist)

    fields = ["front","back"]
    try:
        os.chdir("C:\yourdecks")
    except FileNotFoundError:
        os.mkdir("C:\yourdecks")

    with open("C:\yourdecks\yourdeck.csv",'w') as csvfile: #change name yourdeck.csv to the input name
        writer = csv.DictWriter(csvfile,fieldnames = fields)
        writer.writeheader()
        writer.writerows(csvlist)

def autodeck(query):
    '''chooses the best deck for a topic based on number of stars'''

    driver.get(f"https://quizlet.com/search?query={query}&type=sets")
    terms_per_deck,stars_per_deck = sortdecks()
    maxstars = max(stars_per_deck)
    #termnum is equal to the first index with 0 stars in somecases
    index_max_stars = stars_per_deck.index(maxstars)
    #use the index of max stars to get term num
    termnum = terms_per_deck[index_max_stars]
    #find the specific deck that is to be used
    cardlist = find_deck(index_max_stars,termnum)
    makecsv(cardlist)


def choosedeck(query,authorname):
    '''chooses a deck using the name of the deck and the author's name'''
    driver.get(f"https://quizlet.com/search?query={query} {authorname}&type=sets")
    cardlist = find_deck(0)
    makecsv(cardlist)


