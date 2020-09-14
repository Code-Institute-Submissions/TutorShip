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


# Index
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

# Tutor profile page
@app.route('/tutors/<username_id>/')
def tutor_page(username_id):
    profile = mongo.db.profile
    tutor = profile.find_one({'_id': ObjectId(username_id)})
    return render_template('profile.html', tutor=tutor)

# Subject category profiles
@app.route('/<subject>')
def tutors_subject(subject):
    subjects = mongo.db.subjects
    subject_list = subjects.find({"subject_name": subject})
    return render_template('tutors.html', subject_list=subject_list, subjects_desktop=mongo.db.subjects.find())

# Pricing
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

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

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # function to find a user from the database
    def registered_user(username):
        user = mongo.db.users
        return user.find_one({"username": username})

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = registered_user(username)

        # check if user is registered
        if user:
            if check_password_hash(user['password'], password):
                flash(f'Welcome back {username}!', 'success')
                session['username'] = username
                return redirect(url_for('home', username=session['username']))

            # flash error message if password is incorrect
            else:
                flash('Oops, there was a problem logging in. Please try again.')
                return redirect(url_for('login'))
        else:
            # flash error if username is not on file - prompt to register
            flash(f"We don't seem to have a {username} on file. Want to regitser?")
            return redirect(url_for('login'))

    return render_template('login.html')

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

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)