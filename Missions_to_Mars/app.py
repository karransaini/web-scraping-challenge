import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from mission_to_mars import scrape
import pymongo
from pymongo import MongoClient


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)



# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    db = client.missionToMarsDB
    collection = db.scrape

    data = collection.find_one()

    
    return render_template("index.html", data=data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape_route():

    #drop database
    client.drop_database("missionToMarsDB")
    # Run the scrape function
    db = client.missionToMarsDB
    collection = db.scrape

    scrape_results = scrape()

    collection.insert_one(scrape_results)

    # # Update the Mongo database using update and upsert=True
    # mongo.db.mars_info.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
