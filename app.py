import os
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, \
     check_password_hash

from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tutorshipDB'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# iIndex
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# Tutors
@app.route('/tutors')
def tutors():
    return render_template('tutors.html',
    subjects_desktop=mongo.db.subjects.find(),
    subjects_mobile=mongo.db.subjects.find(),
    tutor_profile=mongo.db.profile.find())

# Tutor profile
@app.route('/tutors/<username_id>/')
def tutor_profile(username_id):
    profile = mongo.db.profile
    tutor = profile.find_one({'_id': ObjectId(username_id)})
    return render_template('profile.html', tutor=tutor)

# Pricing
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    users = mongo.db.users

    if request.method == 'POST':
        new_user = request.form.get('username')
        password = request.form.get('password')
        username_exists = users.find_one({'username': request.form.get('username')})

        # check if username exists - if not, the redirect to create_profile page
        if username_exists is None:
            users.insert_one(
                { 'username': new_user, 'password': generate_password_hash(password) })
            session['username'] = new_user
            return redirect(url_for('create_profile', username=session["username"]))
        
        # if username exists flash try again message
        else:
            flash('Username already exists. Please try another username.', 'warning')
            return redirect(url_for('register'))

    return render_template('register.html')

# Create profile
@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if 'username' in session:
        flash('You have sucessfully registered', 'info')
        return render_template('create_profile.html')

# Insert profile
@app.route('/insert_profile', methods=['POST'])
def insert_profile():
    profile = mongo.db.profile
    profile.insert_one(request.form.to_dict())
    return redirect(url_for('tutors'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)