from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ScarlettExperiment"
mongo = PyMongo(app)

@app.route("/")
def home():
	return render_template("index.html")