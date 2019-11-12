from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo, MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test"
mongo = PyMongo(app)
app.config["CLIENT"] = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="gretabrowne", password="henry811", authSource="admin")

@app.route("/")
def home():
	return get("http://localhost:3000")

	# return get(f"localhost vue server)

@app.route("/poems")
def poems():
	client = app.config["CLIENT"]
	print(client)
	db = client.DickinsonDB
	col = db.DickinsonCOLL
	poems = list(col.find())
	return poems