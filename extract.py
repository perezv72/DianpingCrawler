#!/usr/bin/env python3
# FINAL
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from glob import glob
import codecs
import csv
from bs4 import BeautifulSoup
#from itertools import izip

for fname in glob('html/*html'):
    print(fname)
    html = codecs.open(fname, "r", "utf-8")
    soup = BeautifulSoup(html, "html.parser")
    address = soup.find_all("div", {"class":"tag-addr"})
    addr = soup.find_all("span", {"class":"addr"})
    city = soup.find("a", {"class": "city J-city"}).text
    name = soup.find_all("div", {"class":"pic"})
    price = soup.find_all("a", {"class":"mean-price"})
    url = soup.find_all("meta")
    baserow = []
    for item in baserow:
        baserow.append(item)

    arearow = []
    for item in address:
        arearow.append(item.text.split("\n")[3])

    addressrow = []
    for item in address:
        addressrow.append(item.text.split("\n")[4])

    namerow = []
    for item in name:
        namerow.append(str(item).split("title=\"")[2].split("\"")[0])

    cityrow = []
    for item in name:
        cityrow.append(city + "市")

    urlrow = []
    for item in url:
        urlrow.append(str(item))

    with codecs.open("thirdset_wurl.csv", "a", "utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(zip(namerow, addressrow, arearow, cityrow, urlrow))
