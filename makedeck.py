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
    
     
def open_quizlet_in_browser(playwright, query, authorname):

    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(f"https://quizlet.com/search?query={query}+{authorname}&type=sets")
    alldecks = page.locator("div.SetsView-resultList")
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
    study = page.get_by_role("button",name="Study")
    study.click() 
    card_number = page.get_by_test_id("progress-header")
    print(card_number)
    #if the number of cards is greater than 9, then the first 8 are only shown
    #if the number is less than 9 or equal to 9, everything but the last card is shown
    #https://quizlet.com/432773133/ap-gov-unit-2-flash-cards/ all you need is the number and name of deck + flash-cards
    new_page = browser.new_page()
    new_page.goto("https://www.guerrillamail.com/inbox")
    signup = page.get_by_role("button",name="Sign up")
    signup.click()

    time.sleep(35)
    browser.close()

def main(query, authorname=''):
    with sync_playwright() as playwright:
        open_quizlet_in_browser(playwright, query, authorname)


main('lol')
