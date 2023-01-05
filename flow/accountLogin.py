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
            time.sleep(3)
            ## twitter update, add one more try catch block
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
        errBox = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        if (payload["data"][i]["creds"]["user"] == ""):
            errBox.send_keys(str(payload["data"][i]["creds"]["phone"]))
        else:
            errBox.send_keys(payload["data"][i]["creds"]["user"])
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        time.sleep(2)
        _password = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        _password.send_keys(payload["data"][i]["creds"]["pass"])
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()