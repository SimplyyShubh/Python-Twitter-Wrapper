from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import requests
import csv
import accounts
import time, os
from csv import writer
import sheet
import json
import urllib.request

# _payload = open('payload.json')
# payload = json.load(_payload)
# Runs the script headlessly

# options = Options()
# options.headless = True

# driver = webdriver.Firefox() # (options = options)


def getInfTweets(i, payload):
    tweet = payload["data"][i]["inf-tweet-url"]

def accountLogin(i, driver, payload):

    ## Login functionality working
    ## 'Something went wrong' errors handeled
    ## 'Unusual Login Activity' - Enter username/phone also added

    try:
        twitter = "https://twitter.com/i/flow/login"
        driver.get(twitter)
        time.sleep(5)
        try:
            ## try except block to avoid "Something went wrong errors"
            driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').click()
        except:
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div').click()
            driver.find_element(By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div/span/span').click()
            time.sleep(4)
            driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').click()
        username = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        
        if payload["data"][i]["creds"]["email"] == "":
            username.send_keys(payload["data"][i]["creds"]["user"])
        else:
            username.send_keys(payload["data"][i]["creds"]["email"])

        ## username.send_keys(payload["data"][i]["creds"]["email"])
        try:
            driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div').click()

        ## NOT TESTED

        except:
            driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        time.sleep(1)
        password = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(payload["data"][i]["creds"]["pass"])
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
    except:
        time.sleep(2)
        errBox = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        if (payload["data"][i]["creds"]["user"] == ""):
            errBox.send_keys(str(payload["data"][i]["creds"]["phone"]))
        else:
            errBox.send_keys(payload["data"][i]["creds"]["user"])
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div').click()
        time.sleep(2)
        _password = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        _password.send_keys(payload["data"][i]["creds"]["pass"])
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()

def postTweet(i, driver, payload):
    inf_tweet_url = payload["data"][i]["inf-tweet-url"]
    driver.get(inf_tweet_url)
    time.sleep(2)

    ## TRICKY PART TO CLICK ON THE TWEET AREA, USES HOTKEYS FOR THIS PART
    driver.switch_to.active_element.send_keys("r")
    time.sleep(1)
    tweetBox = driver.switch_to.active_element

    ## Sends in the Tweet

    tweetBox.send_keys(payload["data"][i]["tweet"])
    time.sleep(1)

    # Adds in the Image
    try:
        addImg = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input')
    except:
        addImg = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input')
        
    urllib.request.urlretrieve(payload["data"][i]["img-url"], "tweetImg.jpg")
    time.sleep(3)
    addImg.send_keys("//usr//src//app//tweetImg.jpg")
    time.sleep(3)
    ## os.remove("C:\\Users\\BlackHacker\\Desktop\\python-twitter-bh\\tweetImg.jpg")
    replyBtn = driver.find_element(By.XPATH, '//span[text()="Reply"]')
    replyBtn.click()

    ## driver.switch_to.active_element.send_keys(Keys.CONTROL + Keys.ENTER)
    time.sleep(13)

    #ADD ERROR HANDLING (NEEDS FIXING)
    try:
        viewTweet = driver.find_element(By.XPATH, '//div[text()="Replying to "]')
        viewTweet.click()
    except:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]').click()

# Saves the Tweets to a desired google sheet
def saveTweet(i, driver):
    tweetURL = driver.current_url
    row = i + 1
    sheet.wks.update_cell(row, 1, tweetURL)

"""
    list = [tweetURL]
    with open('output_tweets.csv', 'a') as file:
        OutputTweets = writer(file)
        OutputTweets.writerow(list)
        file.close()
"""

def postFlow(payload):
    for i in range(0, len(payload["data"])):
       # FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')
        options = FirefoxOptions()
        options.binary_location = '/opt/firefox/firefox'
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options) # (options = options)
        accountLogin(i, driver, payload)
        print("Login Successful")
        time.sleep(2)
        postTweet(i, driver, payload)
        print("Tweet Posted!")
        saveTweet(i, driver)
        print("Tweet Saved!")
        time.sleep(1)
        driver.close()
        time.sleep(1)