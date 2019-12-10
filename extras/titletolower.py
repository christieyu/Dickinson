# Christie Yu, Dec 10, 2019
# This script adds a column to all our entries with the title in lower case, for case-sensitive querying

from pymongo import MongoClient

client = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="xiuchen", password="helloworld", authSource="admin")
db = client.DickinsonDB
col = db.DickinsonCOLL


myDocs = col.find({},{"u'_id'": 1, u'title':1})

for x in myDocs:
    id = x['_id']
    myquery = { '_id' : id }
    lower = x['title'].lower()
    col.update_one({'_id' : id}, {'$set' : {'lowertitle' : lower}})

for x in col.find():
  print(x['lowertitle'])

# # The field names are: "title" and "text"; both are strings
