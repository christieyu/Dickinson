#Masayuki Nagase
#Final Project: CPSC 376
#This file gets the sentiment data of all of the poems from the mongo db database
#and then returns the the total count and average sentiment of all the poems published
#that year. To run this file, run flask run in terminal and have a template folder with index.html
from __future__ import print_function
import logging
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
#https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte

#When flask run is run, we can go to the URL displayed in terminal to run the rest of the program
#Since this data is precomputed, this format of running the file is not required, however, 
#it still works as is. 
@app.route("/")
def home():
    #connect to mongo db 
    client = app.config["CLIENT"]
    #defines the collection from which we are reading. 
    db = client.SentimentDB
    readColl = db.DickinsonSentCOLL
    #converts the sentimentality database data into a list.
    sentiments = list(readColl.find())

    #defines the collection to which we are writing to.
    writeColl = db.yearMetaSentCOLL
    writeColl.remove({})

    # key: value
    # year: [total sentiment, count]
    # Creates a dictinary where the key is the year and then the value is the total sentiment
    # and the number of poems published during that year.
    yearDict = {}
    for sentObj in sentiments:
        year = sentObj.get('Year')
        sent = float(sentObj.get('Sentimental Value'))
        if not year in yearDict.keys():
            yearDict[year] = [sent,1]
        else:
            yearDict[year][0] = yearDict[year][0] + sent
            yearDict[year][1] = yearDict[year][1] + 1
    
    #Once the dictionary is defined, then the average is able to be computed per year and written to the mongo db
    #collection that the front end is later able to read. 
    for key in yearDict:
        avg = yearDict[key][0]/yearDict[key][1]
        avg_dict = {'Year': key, 'Count': yearDict[key][1], 'Total': yearDict[key][0], 'Average': avg}
        writeColl.insert(avg_dict, check_keys=False)
    return render_template("index.html")
