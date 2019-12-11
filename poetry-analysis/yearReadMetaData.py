# Masayuki Nagase
# Final Project: CPSC 376
# This file calculates the average readability per year published
# To run this file, run flask run in terminal and have a template folder with index.html
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

#When flask run is run, we can go to the URL displayed in terminal to run the rest of the program
#Since this data is precomputed, this format of running the file is not required, however, 
#it still works as is. 
@app.route("/")
def home():
    # connect to mongo db 
    client = app.config["CLIENT"]
    #defines the collection from which we are reading. 
    db = client.ReadabilityDB
    readColl = db.DickinsonReadCOLL
    readability = list(readColl.find())
    #defines the collection to which we are writing to.
    writeColl = db.yearMetaReadCOLL
    writeColl.remove({})

    # key: value
    # year: [readability, letters, sentences, words, count]
    # Creates a dictinary where the key is the year and then the value is the values
    # listed above. 
    yearDict = {}
    for readObj in readability:
        year = readObj.get('Date')
        read = float(readObj.get('Coleman'))
        letters = float(readObj.get('Letters'))
        sentences = float(readObj.get('Sentences'))
        words = float(readObj.get('Words'))
        if not year in yearDict.keys():
            yearDict[year] = [read,letters, sentences, words, 1]
        else:
            yearDict[year][0] = yearDict[year][0] + read
            yearDict[year][1] = yearDict[year][1] + letters
            yearDict[year][2] = yearDict[year][2] + sentences
            yearDict[year][3] = yearDict[year][3] + words
            yearDict[year][4] = yearDict[year][4] + 1
    
    # Once the dictionary is defined, then the averages are able to be computed per year and written to the mongo db
    # collection that the front end is later able to read. 
    for key in yearDict:
        avgRead = yearDict[key][0]/yearDict[key][4]
        avgLet = yearDict[key][1]/yearDict[key][4]
        avgSent = yearDict[key][2]/yearDict[key][4]
        avgWords = yearDict[key][3]/yearDict[key][4]
        avg_dict = {'Year': key, 'Count': yearDict[key][4], 'Average Read': avgRead, 'Average Letters': avgLet, 'Average Sentiment': avgSent, 'Average Words': avgWords}
        writeColl.insert(avg_dict, check_keys=False)
    return render_template("index.html")
