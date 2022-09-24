#Selenium tut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path=r"/home/nunu/Tools/geckodriver")

def quizletdecks():
    driver.get("https://quizlet.com/search?query=AP-Calc&type=sets")
    #format: change url for whatever topic you want to search for
quizletdecks()
