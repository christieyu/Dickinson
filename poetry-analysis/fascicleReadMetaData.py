#Masayuki Nagase
#Final Project: CPSC 376
#This file gets the average readability per fascicle
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

#When flask run is run, we can go to the URL displayed in terminal to run the rest of the program
#Since this data is precomputed, this format of running the file is not required, however, 
#it still works as is. 
@app.route("/")
def home():
    #connect to mongo db 
    client = app.config["CLIENT"]
    #defines the collection from which we are reading. 
    db = client.ReadabilityDB
    readColl = db.DickinsonReadCOLL
    readability = list(readColl.find())

    #defines the collection to which we are writing to.
    writeColl = db.fascMetaReadCOLL
    writeColl.remove({})

    # key: value
    # fasc: [coleman, letters, sentences, words, count]
    # Creates a dictinary where the key is the fascicle and then the value is the list above
    fascDict = {}
    for readObj in readability:
        #Fascicles are just the first 3 characters in string
        fasc = readObj.get('Fascicle')[:3]
        read = float(readObj.get('Coleman'))
        letters = float(readObj.get('Letters'))
        sentences = float(readObj.get('Sentences'))
        words = float(readObj.get('Words'))
        if not fasc in fascDict.keys():
            fascDict[fasc] = [read,letters, sentences, words, 1]
        else:
            fascDict[fasc][0] = fascDict[fasc][0] + read
            fascDict[fasc][1] = fascDict[fasc][1] + letters
            fascDict[fasc][2] = fascDict[fasc][2] + sentences
            fascDict[fasc][3] = fascDict[fasc][3] + words
            fascDict[fasc][4] = fascDict[fasc][4] + 1
    
    # Once the dictionary is defined, then the averages are able to be computed per year and written to the mongo db
    # collection that the front end is later able to read. 
    for key in fascDict:
        avgRead = fascDict[key][0]/fascDict[key][4]
        avgLet = fascDict[key][1]/fascDict[key][4]
        avgSent = fascDict[key][2]/fascDict[key][4]
        avgWords = fascDict[key][3]/fascDict[key][4]
        avg_dict = {'fasc': key, 'Count': fascDict[key][4], 'Average Read': avgRead, 'Average Letters': avgLet, 'Average Sentiment': avgSent, 'Average Words': avgWords}
        writeColl.insert(avg_dict, check_keys=False)
    return render_template("index.html")


