import re
import time
from playwright.sync_api import  sync_playwright

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
    

def search_decks(browser,authorname,query):

    quizlet_search = browser.new_page()
    quizlet_search.goto(f"https://quizlet.com/search?query={query}+{authorname}&type=sets")
    alldecks = quizlet_search.locator("div.SetsView-resultList")
    #^-- assumes that search is successful
    decks =   alldecks.text_content()
    splitdecks = re.split("Preview",decks)
    if authorname == "":
        wanted_deck = rate_decks(splitdecks)
    else:
        wanted_deck = splitdecks[0]
    csv_deck = alldecks.get_by_text(wanted_deck)
    preview = csv_deck.get_by_role("button",name="Preview")
    preview.click()
    study = quizlet_search.get_by_role("button",name="Study")
    study.click() 

def create_email_quizlet_login(browser):

    guerilla_mail = browser.new_page()
    guerilla_mail.goto("https://www.guerrillamail.com/inbox")
    name = guerilla_mail.get_by_title("Click to Edit")
    name = name.text_content()
    email = name+"@sharklasers.com"
    print(email)
    #if the number of cards is greater than 9, then the first 8 are only shown
    #if the number is less than 9 or equal to 9, everything but the last card is shown
    quizlet_login = browser.new_page()
    quizlet_login.goto("https://quizlet.com/")
    signup = quizlet_login.get_by_role("button",name="Sign up", exact= True)
    signup.click()
    quizlet_login.get_by_role("combobox", name="birth_month").select_option("May")
    quizlet_login.get_by_role("combobox", name="birth_day").select_option("15")
    quizlet_login.get_by_role("combobox", name="birth_year").select_option("2002")
    quizlet_login.get_by_placeholder("user@quizlet.com").click()
    quizlet_login.get_by_placeholder("user@quizlet.com").fill(email)
    quizlet_login.get_by_placeholder("●●●●●●●●").click()
    quizlet_login.get_by_placeholder("●●●●●●●●").fill("ul**%$^%%^JAFDh")
    quizlet_login.get_by_role("button",name="Sign up").click()

    #https://quizlet.com/432773133/ap-gov-unit-2-flash-cards/ all you need is the number and name of deck + flash-cards

def main(query, authorname=''):
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False)
        create_email_quizlet_login(browser)
        search_decks(browser,authorname,query)
        browser.close()

main('ap-gov')
