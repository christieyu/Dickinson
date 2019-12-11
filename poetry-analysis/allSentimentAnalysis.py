#Masayuki Nagase
#Final Project: CPSC 376
# This file calculates the sentiment of each of the poems in the Emily Dickinson database
# To run this file, run flask run in terminal and have a template folder with index.html
from __future__ import print_function
import logging
from pycorenlp import StanfordCoreNLP

from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo, MongoClient

import csv

#Defines the Flask app and the MongoDB parameters. 
#Additionally, allows for connection to stanford path.
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test"
mongo = PyMongo(app)
app.config["CLIENT"] = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="gretabrowne", password="henry811", authSource="admin")
local_corenlp_path = r'/Users/Masayuki/stanford-corenlp-full-2018-10-05'

def poemAnalysis(poemObject):
	#https://stackoverflow.com/questions/32879532/stanford-nlp-for-python
	#Connect to the Stanford NLP server. Note that in order to run this code,
	#The Stanford NLP server must be run. The local_corenlp_path above must be
	#changed, and the instructions must be followed from the link above.
	nlp = StanfordCoreNLP('http://localhost:9000')
	#Set the analysis to be of sentiment. 
	pros = {'annotators': 'sentiment', 'outputFormat': 'json'}
	poem = poemObject.get('poems')[0]
	res = nlp.annotate(poem, properties=pros)
	totalSentiment = 0
	count = 0
	# calculate the average sentiment across the sentences. 
	for s in res["sentences"]:
		totalSentiment = totalSentiment + float(s["sentimentValue"])
		count = count + 1
	averageSentiment = totalSentiment/count
	# 0: Very Negative
	# 1: Negative
	# 2: Neutral
	# 3: Positive
	# 4: Very Positive
	title = poemObject.get('title')
	fascicle = poemObject.get('fasc')
	publication_date = poemObject.get('pubdate')
	# returns all relevant information.
	return [title, fascicle, publication_date, averageSentiment, count]

#When flask run is run, we can go to the URL displayed in terminal to run the rest of the program
#Since this data is precomputed, this format of running the file is not required, however, 
#it still works as is. 
@app.route("/")
def home():
	#connect to mongo db 
	client = app.config["CLIENT"]
	#defines the collection from which we are reading. 
	db = client.DickinsonDB
	col = db.DickinsonCOLL
	poems = list(col.find())
	rows = []
	# To get all the poems, set the range from 0 instead of 1600. However,
	# This took an incredibly long time, so I did it in increments of 200
	# poems. Len(poems) is approximately 1800.
	for i in range(1600,len(poems)):
		print(i)
		if poems[i] is None:
			continue
		if poems[i].get('poems') is None:
			continue
		if len(poems[i].get('poems')) == 0:
			continue
		#Some of these poems were too large and had to be skipped
		#because the stanford analysis would time out.
		if i == 53:
			continue
		if i == 223:
			continue
		if i == 1261:
			continue
		rows.append(poemAnalysis(poems[i]))
	# writes to a different csv in each block of 200. 
	# I appended them all together at the end.
	with open('poems8.csv', 'w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(rows)
	writeFile.close()
	print(rows)
	return render_template("index.html")

#Useful resources: 
#https://stanfordnlp.github.io/CoreNLP/download.html
#https://stackoverflow.com/questions/74829/how-to-run-a-script-as-root-on-mac-os-x
#https://stanfordnlp.github.io/CoreNLP/history.html maybe??
#code: https://github.com/Lynten/stanford-corenlp/blob/master/test.py
#https://stanfordnlp.github.io/CoreNLP/other-languages.html

