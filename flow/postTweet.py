from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import requests
import csv
import accounts
import time, os
from csv import writer
import sheet
import json
import urllib.request

def postTweet(i, tweetID, driver, payload):
    driver.get(payload["data"][i]["tweets"][tweetID]["inf-tweet-url"])
    time.sleep(2)

    ## TRICKY PART TO CLICK ON THE TWEET AREA, USES HOTKEYS FOR THIS PART
    driver.switch_to.active_element.send_keys("r")
    time.sleep(1)
    tweetBox = driver.switch_to.active_element

    ## Sends in the Tweet

    tweetBox.send_keys(payload["data"][i]["tweets"][tweetID]["tweet"])
    time.sleep(1)

    ## IF img-url is empty, then send in the tweet without the attaching any image.
    ## + Attach image under pipeline


    # Adds in the Image
    try:
        addImg = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input')
    except:
        addImg = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[1]/input')
        
    urllib.request.urlretrieve(payload["data"][i]["tweets"][tweetID]["img-url"], "tweetImg.jpg")
    time.sleep(3)

    ## Adding image for linux will be different
    try:
        addImg.send_keys("//app//tweetImg.jpg")
    except:
        addImg.send_keys("C:\\Users\\BlackHacker\\Desktop\\python-twitter-bh\\tweetImg.jpg")
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