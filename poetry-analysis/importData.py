#Masayuki Nagase
#Final Project: CPSC 376
#This file takes the information in a csv file and then writes it to a 
#MongoDB database. To run this file, run flask run in terminal and have 
# a template folder with index.html
from __future__ import print_function
import logging

from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo, MongoClient

import csv

#Defines the Flask app and the MongoDB parameters. 
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test"
mongo = PyMongo(app)
app.config["CLIENT"] = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="gretabrowne", password="henry811", authSource="admin")
#https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte
csvfile = open('AllPoemsFull.csv', 'r', encoding = "ISO-8859-1")
reader = csv.DictReader(csvfile)

#When flask run is run, we can go to the URL displayed in terminal to run the rest of the program
#Since this data is precomputed, this format of running the file is not required, however, 
#it still works as is. 
@app.route("/")
def home():
	#connect to mongo db 
	client = app.config["CLIENT"]
	#defines the collection to which we are writing to.
	db = client.SentimentDB
	col = db.DickinsonSentCOLL
	col.remove({})
	for data in reader:
		# remove empty data
		del data['']
		# writes to MongoDB
		col.insert(data, check_keys=False)
	return render_template("index.html")

