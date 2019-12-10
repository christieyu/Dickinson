# Christie Yu, Dec 10, 2019
# Scrapes poems from https://www.bartleby.com/113/indexlines.html

from bs4 import BeautifulSoup
import requests
# boilerplate from https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="xiuchen", password="helloworld", authSource="admin")
db = client.DickinsonDB
col = db.DickinsonCOLL

# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

page_link = 'https://www.bartleby.com/113/indexlines.html'
page_response = requests.get(page_link, timeout=5)
soup1 = BeautifulSoup(page_response.content, "html.parser")

# textContent = []
output = []

table = soup1.find_all('table')[6]
# print(table)

for tr in table.find_all('tr'):
    links = tr.find_all('a')

    for poem in links:
        data = {}
        data["title"] = poem.text.strip().lower()
        # print(data["title"])

        poem_link = "https://www.bartleby.com" + poem['href']
        poem_response = requests.get(poem_link, timeout=5)
        soup2 = BeautifulSoup(poem_response.content, "html.parser")

        poem_table = soup2.find_all('table')[7]
        poem_trs = poem_table.find_all('tr')

        current_poem = []
        for poem_tr in poem_trs:
            poem_line = poem_tr.text.strip()
            poem_line = poem_line.strip("0 1 2 3 4 5 6 7 8 9")
            poem_line = poem_line.strip()
            current_poem.append(poem_line)

        my_poem = "\n"
        my_poem = my_poem.join(current_poem)

        data["text"] = my_poem

        # output.append(data)

        col.update_one({'lowertitle': data["title"]}, {'$push': {'poems': data["text"]}})
        # print(len(output))

# # The field names are: "title" and "text"; both are strings
