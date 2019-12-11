from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo, MongoClient
from flask import jsonify
from requests import get

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test"
mongo = PyMongo(app)
app.config["CLIENT"] = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="xiuchen", password="helloworld", authSource="admin")

@app.route("/")
@app.route("/<path:filename>")
def home(filename = "HelloWorld.vue"):
	return get("http://localhost:8080/" + filename).content

@app.route("/poems")
def poems():
	client = app.config["CLIENT"]
	db = client.DickinsonDB
	col = db.DickinsonCOLL
	poems = []
	for entry in col.find():
		o = entry["_id"]
		entry_id = str(o)
		entry["objectID"] = entry_id
		entry.pop('_id')
		if entry["poems"]:
			formatted_poems = []
			for p in entry["poems"]:
				formatted_poems.append(p.split("\n"))
			entry["poems"] = formatted_poems
		poems.append(entry)
	# print(poems)
	return jsonify(poems)

@app.route("/frequent_words")
def frequent_words():
	client = app.config["CLIENT"]
	db = client.DickinsonDB
	col = db.wordsFrequency
	words = []
	for entry in col.find():
		words.append({"word": entry["word"], "frequency": entry["freq"]})
	return jsonify(words)

@app.route("/analysis")
def analysis():
	client = app.config["CLIENT"]
	db = client.DickinsonDB
	col = db.analysisCOLL
	analysis = []
	for entry in col.find():
		o = entry["poem_id"]
		poem_id = str(o)
		analysis.append({"poem_id": poem_id, 
						"stanza_lengths": entry["stanza_lengths"],
						"scanscion": entry["scanscion"],
						"rhyme_scheme": entry["rhyme_scheme"],
						"meter_guess": entry["meter_guess"],
						})
	return jsonify(analysis)


@app.route("/sentiment")
def sentiment():
	client = app.config["CLIENT"]
	db = client.SentimentDB
	col = db.DickinsonSentCOLL
	analysis = []
	for entry in col.find():
		analysis.append({"title": entry["Title"], 
						"sentiment": entry["Sentimental Value"],
						})
	return jsonify(analysis)


@app.route("/alliterations")
def alliterations():
	client = app.config["CLIENT"]
	db = client.DickinsonDB
	col = db.newalliterationCOLL
	alliterations = []
	for entry in col.find():
		o = entry["poem_id"]
		poem_id = str(o)
		alliterations.append({"poem_id": poem_id, "alliterations": entry["alliterations"]})
	return jsonify(alliterations)


@app.route("/similes")
def similes():
	client = app.config["CLIENT"]
	db = client.DickinsonDB
	col = db.simileCOLL
	similies = []
	for entry in col.find():
		o = entry["poem_id"]
		poem_id = str(o)
		similies.append({"poem_id": poem_id, "similies": entry["similes"]})
	return jsonify(similies)



# @app.route("/alliterations/")
# @app.route("/alliterations/<poem>")
# def alliterations(poem):
# 	print("HEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHERE?")
# 	client = app.config["CLIENT"]
# 	db = client.DickinsonDB
# 	col = db.alliterationCOLL
# 	print(poem)
# 	poem_query = {"poem": poem}
# 	alliterations_result = col.find(poem_query)
# 	print("ALLITERATIONS RESULT: ", alliterations_result)
# 	pass
# 	return 
