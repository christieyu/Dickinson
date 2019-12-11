# Masayuki Nagase
# Final Project: CPSC 376
# This file calculates the readability of the data from the Coleman scale
# The data calcualtion is based on the CS50 PSET.
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

# Note that the next four functions are from the CS50 Vault
def count_letters(text):
    ## CODE CANNOT BE RELEASED AS IT IS CURRENTLY USED IN CS50 ASSIGNMENTS”
    return 0

def count_sentences(text):
    ## CODE CANNOT BE RELEASED AS IT IS CURRENTLY USED IN CS50 ASSIGNMENTS”
    return 0

def count_words(text):
    ## CODE CANNOT BE RELEASED AS IT IS CURRENTLY USED IN CS50 ASSIGNMENTS”
    return 0

def coleman(poemObject):
    ## CODE CANNOT BE RELEASED AS IT IS CURRENTLY USED IN CS50 ASSIGNMENTS”
    #return {'_id': _id, 'Title': title, 'Fascicle': fascicle, 'Date': publication_date, 'Letters': letters, 'Sentences': sentences, 'Words': words, 'Coleman': coleman}
    return 0

#When flask run is run, we can go to the URL displayed in terminal to run the rest of the program
#Since this data is precomputed, this format of running the file is not required, however, 
#it still works as is. 
@app.route("/")
def home():
    #connect to mongo db 
    client = app.config["CLIENT"]
    #defines the collection from which we are reading. 
    db = client.ReadabilityDB
    col = db.DickinsonReadCOLL
    col.remove({})
    #defines the collection to which we are writing to.s
    dbGet = client.DickinsonDB
    colGet = dbGet.DickinsonCOLL

    poems = list(colGet.find())
    #skips the poem objects that do not have any poems in them
    for i in range(len(poems)):
        print(i)
        if poems[i] is None:
            continue
        if poems[i].get('poems') is None:
            continue
        if len(poems[i].get('poems')) == 0:
            continue
        #calculates the coleman readability value
        data = coleman(poems[i])
        col.insert(data, check_keys=False)
    return render_template("index.html")

