#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://pixelscan.net/"
driver.get(url)
time.sleep(1500)
driver.quit()