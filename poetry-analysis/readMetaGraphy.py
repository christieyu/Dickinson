#Masayuki Nagase
#Final Project: CPSC 376
#This file creates the readability graphs that will be able to be displayed in the UI
#This can be run through a simple python command
from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo, MongoClient

#Defines the Flask app and the MongoDB parameters. 
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test"
mongo = PyMongo(app)
app.config["CLIENT"] = MongoClient("mongodb+srv://scarlettexperiment-1pxrx.mongodb.net/test", username="gretabrowne", password="henry811", authSource="admin")

import plotly.graph_objects as go
import numpy as np
import plotly.express as px

#connect to mongo db 
client = app.config["CLIENT"]
#defines the collection from which we are reading. 
db = client.ReadabilityDB
readColl = db.DickinsonReadCOLL
readability = list(readColl.find())
#https://stackoverflow.com/questions/34283627/how-to-convert-list-of-dictionaries-into-list-of-lists
list_readability = [list(col) for col in zip(*[d.values() for d in readability])]
color_vals = [float(i) for i in list_readability[7]]
fasc_vals = [i[:3] for i in list_readability[2]]
fig = go.Figure()

# This figure graphs Year, Fascicle, and Readability of all poems
fig.add_trace(go.Scatter(
    x=list_readability[3],
    y=fasc_vals,
    hovertext = list_readability[1],
    marker=dict(
        size=16,
        cmax=16,
        cmin=0,
        color=color_vals,
        opacity=0.50,
        colorbar=dict(
            title="Readability"
        ),
        colorscale="viridis"
    ),
    mode="markers"))

fig.update_layout(
    title={
        'text': "Readability of Emily Dickinson's Poems by Year and Fascicle",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_xaxes(tickvals=[1890, 1891, 1896, 1914,1929, 1935,1945])
fig.update_xaxes(title_text='First Publication of Poem')
fig.update_yaxes(title_text='Fascicle')

fig.show()

#This figure graphs average readability and count per date published 
readAvgColl = db.yearMetaReadCOLL
sent_avg= list(readAvgColl.find())
list_sent_avg= [list(col) for col in zip(*[d.values() for d in sent_avg])]
fig = go.Figure([go.Bar(
    x=list_sent_avg[1], 
    y=list_sent_avg[2],     
    marker=dict(
        cmax=7.2,
        cmin=4.8,
        color=list_sent_avg[3],
        opacity=0.75,
        colorbar=dict(
            title="Readability"
        ),
        colorscale='agsunset'
    ),)])
fig.update_xaxes(tickvals=[1890, 1891, 1896, 1914,1929, 1935,1945])
fig.update_xaxes(title_text='First Publication of Poem')
fig.update_yaxes(title_text='Number of Poems')
fig.update_layout(
    title={
        'text': "Average Readability of Emily Dickinson's Poems Over the Years",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.show()

# This figure graphs average readability and count per fascicle 
readAvgColl = db.fascMetaReadCOLL
sent_avg= list(readAvgColl.find())
list_sent_avg= [list(col) for col in zip(*[d.values() for d in sent_avg])]
print(list_sent_avg)
fig = go.Figure([go.Bar(
    x=list_sent_avg[1], 
    y=list_sent_avg[2],     
    marker=dict(
        cmax=2,
        cmin=8,
        color=list_sent_avg[3],
        opacity=0.75,
        colorbar=dict(
            title="Readability"
        ),
        colorscale='portland'
    ),)])

fig.update_xaxes(title_text='Fascicles')
fig.update_yaxes(title_text='Number of Poems')
fig.update_layout(
    title={
        'text': "Average Readability of Emily Dickinson's Poems Over the Fascicles",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.show()