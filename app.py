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
	# TO-DO: the ports will need to be more generic in the future
	return get("http://localhost:8080/" + filename).content

@app.route("/poems")
def poems():
	client = app.config["CLIENT"]
	# print(client)
	db = client.DickinsonDB
	col = db.DickinsonCOLL
	poems = []
	for entry in col.find():
		entry.pop('_id')
		if entry["poems"]:
			formatted_poems = []
			for p in entry["poems"]:
				formatted_poems.append(p.split("\n"))
			entry["poems"] = formatted_poems
		poems.append(entry)
		# print(entry["poems"])
		# formatted_poems =
		# entry["poems"]
	# print(poems)
	return jsonify(poems)
