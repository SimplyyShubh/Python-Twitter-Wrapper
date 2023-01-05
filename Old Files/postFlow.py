from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
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
from flow import saveTweet, accountLogin, postTweet

def postFlow(payload):
    # payload = _payload.json()
    for i in range(0, len(payload["data"])):
        print("In PostFlow Loop")
        # FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')
        options = webdriver.FirefoxOptions()
        
        # options.binary_location = '/opt/firefox/firefox'
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)  # (options = options)

        # ## HEROKU CONFIGS

        # options.log.level = "trace"

        # options.add_argument("-remote-debugging-port=9224")
        # options.add_argument("-headless")
        # options.add_argument("-disable-gpu")
        # options.add_argument("-no-sandbox")

        # binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))
        # driver = webdriver.Firefox(
		# firefox_binary=binary,
		# executable_path=os.environ.get('GECKODRIVER_PATH'),
		# options=options)
        ## END OF HEROKU CONFIGS
        ## Test

        
     

        accountLogin.accountLogin(i, driver, payload)
        print("Login Successful")
        time.sleep(2)
        for tweetID in range(0, len(payload["data"][i]["tweets"])):
            # postTweet
            # print(payload["data"][i]["tweets"][tweetID]["tweet"])
            postTweet.postTweet(i, tweetID, driver, payload)
            print("Tweet Posted!")
            saveTweet.saveTweet(tweetID, driver)
            print("Tweet Saved!")
            time.sleep(1)
        driver.close()
        time.sleep(1)