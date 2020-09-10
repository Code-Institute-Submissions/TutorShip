import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tutorshipDB'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/tutors')
def tutors():
    return render_template('tutors.html',
    subjects_desktop=mongo.db.subjects.find(),
    subjects_mobile=mongo.db.subjects.find(),
    tutor_profile=mongo.db.profile.find())

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)