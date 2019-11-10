from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ScarlettExperiment"
mongo = PyMongo(app)

@app.route("/")
def home():
	# print(mongo.db.DickinsonDB.find())
	# db = mongo.db.DickinsonDB
	# results = db.find()
	results = mongo.db.DickinsonDB.find()
	print(results)
	for r in results:
		print(r)
	return render_template("index.html")