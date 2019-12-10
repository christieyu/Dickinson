# Christie Yu, Dec 10, 2019

from bs4 import BeautifulSoup
import requests
# boilerplate from https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="xiuchen", password="helloworld", authSource="admin")
# db = client.TestData
# col = db.TestCOLL
db = client.DickinsonDB
col = db.DickinsonCOLL

data = {"title": "a bee his burnished carriage", "text": "A TRAIN went through a burial gate,\nA bird broke forth and sang,\nAnd trilled, and quivered, and shook his throat\nTill all the churchyard rang;\n\nAnd then adjusted his little notes,\nAnd bowed and sang again.\nDoubtless, he thought it meet of him\nTo say good-by to men."}

# col.update_one({'lowertitle': data["title"]}, {'$push': {'poems': data["text"]}})

for x in col.find({"lowertitle": "a dew sufficed itself"}):
  print(x)

# # The field names are: "title" and "text"; both are strings
