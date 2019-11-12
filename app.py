from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo, MongoClient
from flask import jsonify

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test"
mongo = PyMongo(app)
app.config["CLIENT"] = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="xiuchen", password="helloworld", authSource="admin")

@app.route("/")
def home():
	return get("http://localhost:8080")

@app.route("/poems")
def poems():
	client = app.config["CLIENT"]
	print(client)
	db = client.DickinsonDB
	col = db.DickinsonCOLL
	poems = []
	for entry in col.find():
		entry.pop('_id')
		poems.append(entry)
	print(poems)
	return jsonify(poems)