#Masayuki Nagase
#Final Project: CPSC 376
# This file computes the sentiment of the top 100 words that Emily Dickinson uses
# To run this file, run flask run in terminal and have a template folder with index.html
from __future__ import print_function
import logging
#from stanfordcorenlp import StanfordCoreNLP
from pycorenlp import StanfordCoreNLP

from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo, MongoClient

#Defines the Flask app and the MongoDB parameters. 
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test"
mongo = PyMongo(app)
app.config["CLIENT"] = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="gretabrowne", password="henry811", authSource="admin")
local_corenlp_path = r'/Users/Masayuki/stanford-corenlp-full-2018-10-05'

def wordAnalysis(wordObject):
	#https://stackoverflow.com/questions/32879532/stanford-nlp-for-python
    nlp = StanfordCoreNLP('http://localhost:9000')
    # sets annotation to be based on sentiment.
    pros = {'annotators': 'sentiment', 'outputFormat': 'json'}
    word = wordObject.get('word')
    res = nlp.annotate(word, properties=pros)
    totalSentiment = 0
    count = 0
    # calculates average sentiment across sentences.
    for s in res["sentences"]:
        totalSentiment = totalSentiment + float(s["sentimentValue"])
        count = count + 1
    averageSentiment = totalSentiment/count
	# 0 Very Negative
	# 1 Negative
	# 2 Neutral
	# 3 Positive
    # 4 Very Positive

    freq = wordObject.get('freq')
    # returns the important information
    return {'freq': freq, 'word': word, 'sentiment': averageSentiment}

#When flask run is run, we can go to the URL displayed in terminal to run the rest of the program
#Since this data is precomputed, this format of running the file is not required, however, 
#it still works as is. 
@app.route("/")
def home():
    #connect to mongo db 
    client = app.config["CLIENT"]
    #defines the collection from which we are reading and writing
    db = client.DickinsonDB
    writeColl = db.TopWordsSentimentCOLL
    readColl = db.wordsFrequency
    writeColl.remove({})
    words = list(readColl.find())
    # goes through each of the top 100 words and writes the data
    for i in words:
        data = wordAnalysis(i)
        writeColl.insert(data)
        print(data)
    return render_template("index.html")

#Useful resources:
#https://stanfordnlp.github.io/CoreNLP/download.html
#https://stackoverflow.com/questions/74829/how-to-run-a-script-as-root-on-mac-os-x
#https://stanfordnlp.github.io/CoreNLP/history.html maybe??
#code: https://github.com/Lynten/stanford-corenlp/blob/master/test.py
#https://stanfordnlp.github.io/CoreNLP/other-languages.html

