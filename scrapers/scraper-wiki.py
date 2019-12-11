# Christie Yu, Oct 31 2019

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
# boilerplate from https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486


page_link = 'https://en.wikipedia.org/wiki/List_of_Emily_Dickinson_poems'
page_response = requests.get(page_link, timeout=5)
soup1 = BeautifulSoup(page_response.content, "html.parser")

textContent = []
output = []

table = soup1.find('table')
fields = ["title", "fasc", "pubdate", "first_ID", "collect_ID", "J_ID", "F_ID"]

# Connect to Database (must include username, password, authSource parameters) as shown in example
# Example: client = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username=<username>, password=<password>, authSource="admin")
client = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test")
db = client['DickinsonDB']
collection = db['DickinsonCOLL']

for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 7:
        data = {}
        for i in range(6):
            data[fields[i]] = tds[i].text.strip()

        ahref = tr.find('a')
        if ahref != None:
            poem_link = ahref['href']
            poem_response = requests.get(poem_link)
            soup2 = BeautifulSoup(poem_response.content, "html.parser")

            poemdivs = soup2.find_all('div', {'class':'poem'})

            poem_list = []

            for poem in poemdivs:
                poem_version = poem.find('p').text.strip()
                poem_list.append(poem_version)

            data["poems"] = poem_list

        else:
            data["poems"] = None

        output.append(data)
        collection.insert(data)

# output = [{'first_ID': u'1.127', 'pubdate': u'1945', 'title': u'A Bee his burnished Carriage', 'collect_ID': u'', 'poems': [u'A Bee his burnished Carriage\nDrove boldly to a Rose \u2014\nCombinedly alighting \u2014\nHimself \u2014 his Carriage was \u2014\nThe Rose received his visit\nWith frank tranquillity\nWithholding not a Crescent\nTo his Cupidity \u2014\nTheir Moment consummated \u2014\nRemained for him \u2014 to flee \u2014\nRemained for her \u2014 of rapture\nBut the humility.'], 'fasc': u'S13.01.002', 'J_ID': u'1339'}]

# You can access a list of dicts (one dict per row entry) with "output"
# The field names are: "title", "fasc", "pubdate", "first_ID", "collect_ID", "J_ID", "F_ID", "poems"
# "poems" is a list of poem versions given by Wikipedia
