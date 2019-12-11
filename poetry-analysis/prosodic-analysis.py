# Christie Yu

from pymongo import MongoClient
import poetrytools
import unicodedata

'''
This program performs poetry analysis on the poems, using the poetrytools package. Just as in commonwords.py, the program loads the poems
from the database, performs analysis, and then stores the analysis results in the database. 
'''

client = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="xiuchen", password="helloworld", authSource="admin")
db = client.DickinsonDB
col = db.DickinsonCOLL
poems = {}
for entry in col.find():
    print("inside entry")
    if (entry['poems']):
        # only add the first poem
        i = entry['_id']
        poems[i] = entry['poems'][0]
count = 0

analysis_coll = db.analysisCOLL
for key in poems:
    poem_dict = {"poem_id": key}
    print(count)
    if count == 1234 or count == 1034:
        # randomly blank poems so skip them
        count = count + 1
        continue
    mypoem = poetrytools.tokenize(poems[key])

    # rhyme_scheme returns "X a b X X a X a b c X c"
    rhyme_scheme = ' '.join(poetrytools.rhyme_scheme(mypoem))
    poem_dict["rhyme_scheme"] = rhyme_scheme

    # scanscion returns "0 1 1 10 10 / 1 10 1 01 / 0 1 01 1 10 / 1 1 1 0 10 1 / 1 1 0 1 010 / 0 100 1 1 / 1 1 1 01 1 / 0 1 1 1 0 1 / 1 1 1 1 1 10 / 1 1 1 1 1 1 / 10 10 10 / 1 1 1 1 1"
    scanscions = []
    for item in poetrytools.scanscion(mypoem):
        scanscion = ' '.join(item)
        scanscions.append(scanscion)
        # print("scanscion: " + scanscion)
    poem_dict["scanscion"] = scanscions

    # stanza_lengths returns "12"
    stanza_lengths = poetrytools.stanza_lengths(mypoem)
    poem_dict["stanza_lengths"] = stanza_lengths

    # meter_guess returns "iambic trimeter" (as a very rough guess)
    meter_guess = poetrytools.guess_metre(mypoem)[3]
    poem_dict["meter_guess"] = meter_guess
    print(poem_dict)
    count += 1
    # load results in database
    x = analysis_coll.insert_one(poem_dict)







