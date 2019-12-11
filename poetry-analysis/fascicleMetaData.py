# Masayuki Nagase
# Final Project: CPSC 376
# To run this file, run flask run in terminal and have a template folder with index.html
from __future__ import print_function
import logging

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
    db = client.SentimentDB
    readColl = db.DickinsonSentCOLL
    sentiments = list(readColl.find())

    #defines the collection to which we are writing to.s
    writeColl = db.fascMetaSentCOLL
    writeColl.remove({})

    #key: value
    # fascicle: [total sentiment, count]
    # Creates a dictinary where the key is the fascicle and then the value is the total sentiment
    # and the number of poems published in that fascicle.
    fascDict = {}
    for sentObj in sentiments:
        fasc = sentObj.get('Fascicle')[:3]
        sent = float(sentObj.get('Sentimental Value'))
        if not fasc in fascDict.keys():
            fascDict[fasc] = [sent,1]
        else:
            fascDict[fasc][0] = fascDict[fasc][0] + sent
            fascDict[fasc][1] = fascDict[fasc][1] + 1

    # Once the dictionary is defined, then the average is able to be computed per fascicle and written to the mongo db
    # collection that the front end is later able to read. 
    for key in fascDict:
        avg = fascDict[key][0]/fascDict[key][1]
        avg_dict = {'Fascicle': key, 'Count': fascDict[key][1], 'Total': fascDict[key][0], 'Average': avg}
        writeColl.insert(avg_dict, check_keys=False)
    return render_template("index.html")
