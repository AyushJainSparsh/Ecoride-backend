from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

def get_db(app=None):
    from flask import current_app
    if app:
        app.config["MONGO_URI"] = os.getenv("MONGO_URI")
        mongo = PyMongo(app)
        #print("Mongo Instance:", mongo)  # Check if it's initialized
        #print("Mongo Database:", mongo.db)
        return mongo.db
    else:
        mongo = PyMongo(current_app)
        return mongo.db
