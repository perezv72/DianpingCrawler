#!/usr/bin/env python2
# -*- coding: utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import codecs
from selenium.common.exceptions import NoSuchElementException
import os
import os.path

chrome_options = Options()
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wait = WebDriverWait(driver, 10)

# The file containing the links should be in the working directory or make sure that the command has the correct path.
with open("urls.txt") as f:
    urls = f.readlines()

# Checks if directory name "html" exists, if not, it creates directory.
newpath = r'html'
if not os.path.exists(newpath):
    os.makedirs(newpath)

driver.get("http://www.dianping.com/search/keyword/58/0_%E6%B1%89%E5%A0%A1")
Print("Diangping recently changed the architecture of their website. The old web site looks like Yelp while the new website looks more like Google Maps. Please review website before continuing")
conti = input("Press 1 if page is new format (Looks like Google Maps), 2 if page is old style (Looks like Yelp), 0 to quit ")

if conti==0:
    driver.quit()
    quit()
elif conti == 2:
    snext = "next"
elif conti == 1:
    snext = "NextPage"

# function checks if there is more than one page with results
def checkpages(url):
    try:
        driver.find_element_by_class_name(snext)
        return True
    except NoSuchElementException:
        return False

# function saves every html page and names it by numerical order
def htmlwriter():
    n = len([name for name in os.listdir('.') if os.path.isfile(name)]) 
    n1 = "%04d"%n
    html = driver.page_source
    html_file = codecs.open(str(n1) +".html", "w", "utf-8")
    print "retrieved " +str(n1)
    print driver.current_url
    html_file.write(html)
    html_file.close()

for item in urls:
    driver.get(item)
    time.sleep(10)
    htmlwriter()
    while checkpages(driver)==True: 
            try:
                time.sleep(10)
                element = driver.find_element_by_class_name(snext)
                element.click()
            except NoSuchElementException:
                htmlwriter()
                break
            time.sleep(2)
            htmlwriter()

driver.quit()
    
