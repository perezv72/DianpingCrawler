#!/usr/bin/env python2
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import time
from selenium import webdriver
import os
import os.path
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
time.sleep(10)

with open("urls.txt") as f:
	urls = f.readlines()

urls = [x.strip() for x in urls]

for item in urls[1:992]:
        driver.set_page_load_timeout(10)
        try:
                driver.get(item) 
        except:
                print("skipped " + str(item))
                continue
	time.sleep(20)
	n = len([name for name in os.listdir('.') if os.path.isfile(name)])
	n2 = n + 1
	n3 = "%04d"%n2
	html = driver.page_source
	html_file = open(str(n3) +".html", "w")
	html_file.write(html)
	html_file.close()
	print("fetch count: " +str(n2))
	print(str(item))

driver.close()