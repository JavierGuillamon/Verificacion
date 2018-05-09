#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 05:01:29 2018

@author: Javier Guillamón
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = "adsadas@air2token.com"
password = "qwer1234"

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("http://twitter.com")

element  = driver.find_element_by_name("session[username_or_email]")
element.send_keys(user)

element  = driver.find_element_by_name("session[password]")
element.send_keys(password)

element.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)

element  = wait.until(EC.element_to_be_clickable((By.NAME, "tweet")))
element.send_keys("I'm using Selenium!!")

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tweet-action")))
element.click()




driver.close()