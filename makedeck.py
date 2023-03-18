import re
from playwright.sync_api import  sync_playwright

def rate_decks(splitdecks):
    '''Return specific deck number and the start,end indexs within the string'''
    teachdeck = []
    stardeck = []
    for dindex, deck in enumerate(splitdecks):
        terms_decimal_match = re.search(r"terms\d.\d", deck)
        terms_match = re.search(r"terms\d", deck)

        if "Images" in deck:
            continue
                
        if "Teacher" in deck:
            teachdeck.append(dindex)
            continue

        if terms_decimal_match:
            print(deck)
            num = deck[terms_decimal_match.start()+5:terms_decimal_match.end()]
            print(num)
            stardeck.append((dindex,num))
            continue

        if terms_match:
            print(deck)
            num = deck[terms_match.start()+5]
            print(num)
            stardeck.append((dindex,num))
#nothings wrong it's just that eerything is teach or images
    print(stardeck,"check")
    findmax = [ float(starnum[1]) for starnum in stardeck]
    max_value = max(findmax)
    print(max_value,"m")
    for dtuple in stardeck:
        if float(dtuple[1]) == max_value:
            the_deck = splitdecks[dtuple[0]]
            print(the_deck,"iii")
    return stardeck,teachdeck 
    
def click_scrap(wanted_deck):
    pass
    
def open_quizlet_in_browser(playwright, query, authorname):

    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(f"https://quizlet.com/search?query={query}+{authorname}&type=sets")
    alldecks = page.locator("div.SetsView-resultList")
    decks =   alldecks.text_content()
    splitdecks = re.split("Preview",decks)
    stardeck,teachdeck = rate_decks(splitdecks)
    if len(teachdeck) != 0:
        wanted_deck = splitdecks[teachdeck[0]]
    if len(stardeck) != 0:
        pass
        #wanted_deck = splitdecks[stardeck[]]

    browser.close()

def main(query, authorname=''):
    with sync_playwright() as playwright:
        open_quizlet_in_browser(playwright, query, authorname)


main('ap-gov')
