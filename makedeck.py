import re
import time
import os
from playwright.sync_api import  sync_playwright, TimeoutError

def rate_decks(splitdecks):
    '''Return specific deck number and the start,end indexs within the string'''
    teachdeck = [] #contains the indexes of values in splitdecks that contain "teacher"
    stardeck = []#contains the indexes of values in splitdecks that contain stars
    for dindex, deck in enumerate(splitdecks):
        terms_decimal_match = re.search(r"terms\d.\d", deck)
        terms_match = re.search(r"terms\d", deck)

        if "Images" in deck:
            continue
        elif "Teacher" in deck:
            teachdeck.append(dindex)

        elif terms_decimal_match:
            print(deck)
            num = deck[terms_decimal_match.start()+5:terms_decimal_match.end()]
            print(num)
            stardeck.append((dindex,num))

        elif terms_match:
            print(deck)
            num = deck[terms_match.start()+5]
            print(num)
            stardeck.append((dindex,num))

    if len(teachdeck) != 0:
        print(splitdecks[teachdeck[0]])
        return splitdecks[teachdeck[0]]
    if len(teachdeck) == 0:
        findmax = [ float(starnum[1]) for starnum in stardeck]
        max_value = max(findmax)
        for dtuple in stardeck:
            if float(dtuple[1]) == max_value:
                return splitdecks[dtuple[0]]
    
def sign_up(email,password,browser):
    quizlet_signup = browser.new_page()
    quizlet_signup.goto("https://quizlet.com/")
    signup = quizlet_signup.get_by_role("button",name="Sign up", exact= True)
    signup.click()
    quizlet_signup.get_by_role("combobox", name="birth_month").select_option("May")
    quizlet_signup.get_by_role("combobox", name="birth_day").select_option("15")
    quizlet_signup.get_by_role("combobox", name="birth_year").select_option("2002")
    quizlet_signup.get_by_placeholder("user@quizlet.com").click()
    quizlet_signup.get_by_placeholder("user@quizlet.com").fill(email)
    quizlet_signup.get_by_placeholder("●●●●●●●●").click()
    quizlet_signup.get_by_placeholder("●●●●●●●●").fill(password)
    quizlet_signup.get_by_role("button",name="Sign up").click()

def login(email,password,quizlet_login):
    quizlet_login.goto("https://quizlet.com/")
    login= quizlet_login.get_by_role("button",name="Log In")
    login.click()
    quizlet_login.get_by_placeholder("Type your email address or username").fill(email)
    #user.fill(email)
    quizlet_login.get_by_placeholder("Type your password").fill(password)
    quizlet_login.get_by_test_id("login-form").get_by_role("button",name="Log in").click()

def search_decks(email,password,browser,query):
    quizlet_search = browser.new_page()
    login(email,password,quizlet_search)
    searchbar = quizlet_search.get_by_placeholder("Study sets, textbooks, questions")
    searchbar.click()
    searchbar.fill(query)
    quizlet_search.keyboard.press("Enter")
    quizlet_search.get_by_role("tab",name="Study sets").click()
    #alldecks = quizlet_search.locator("div.SetsView-resultList")
    alldecks = []
    for i in range(8):
        card = quizlet_search.get_by_test_id("SetsView-resultItem").nth(i)
        alldecks.append(card.text_content())
    #^-- assumes that search is successful
    #decks =   alldecks.text_content()
    #splitdecks = re.split("Preview",decks)
    print(alldecks)
    wanted_deck = rate_decks(alldecks)
    print(wanted_deck)
    csv_deck = quizlet_search.get_by_text(wanted_deck)
    preview = csv_deck.get_by_role("button",name="Preview")
    preview.click()
    study = quizlet_search.get_by_role("button",name="Study")
    study.click() 
    card_number = quizlet_search.get_by_test_id("progress-header").first
    number = card_number.text_content()
    number = number[-3:]
    front = []
    back = []
    for i in range(int(number)):
        #quizlet_search = quizlet_search.locator("div.SetPageTerms-term").nth(i)
        front = quizlet_search.locator("a.SetPageTerm-wordText").nth(i)
        print(front.text_content())
        back = quizlet_search.locator("a.SetPageTerm-definitionText").nth(i)
        print(back.text_content())
        #under = quizlet_search.locator("div.SetPageTermChunk SetPageTermChunk--notStudied")
        #print(under.text_content())
        

    #if the number of cards is greater than 9, then the first 8 are only shown
    #if the number is less than 9 or equal to 9, everything but the last card is shown
def main(query):
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False)
        password = ""
        with open("email.txt",'r') as email_file:
            email = email_file.read()
            print(email)
        with open("accountfile.txt",'r+') as made:
            print(type(made.read()))
            made.seek(0)
            if int(made.read()) == 1:
                search_decks(email,password,browser,query)
            else:
                sign_up(email,password,browser)
                made.write("1")
main('ap bio')
