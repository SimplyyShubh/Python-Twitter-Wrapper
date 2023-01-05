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


def saveTweet(tweetID, driver):
    tweetURL = driver.current_url
    row = tweetID + 1
    sheet.wks.update_cell(row, 1, tweetURL)