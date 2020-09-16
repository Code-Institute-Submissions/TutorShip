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

# My profile page
@app.route('/tutors/my_profile/<creator_id>/')
def my_profile(creator_id):
    profile = mongo.db.profile
    tutor = profile.find_one({'created_by': creator_id})
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
        new_email = request.form.get('email')
        password = request.form.get('password')
        email_exists = users.find_one({'email': request.form.get('email')})

        # check if password is 5 characters or more
        if len(password) < 5:
            flash('Please use 5 or more characters for your password.', 'warning')
            return redirect(url_for('register'))
        
        # check if password includes 1 or more numbers
        if not any(char.isdigit() for char in password):
            flash('Password must include at least one number.', 'warning')
            return redirect(url_for('register'))

        # check if email exists - if not, the redirect to create_profile page
        if email_exists is None:
            users.insert_one(
                { 'username': new_user, 'email': new_email, 'password': generate_password_hash(password) })
            session['username'] = new_user
            return redirect(url_for('create_profile', username=session["username"]))
        
        # if email exists flash try again message
        else:
            flash('Email already registered. Please try another email or sign-in.', 'warning')
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
        flash('You have sucessfully registered', 'success')
        return render_template('create_profile.html')

# Insert profile
@app.route('/insert_profile', methods=['POST'])
def insert_profile():
    profile = mongo.db.profile

    if request.method == 'POST':
        profile.insert_one({
            'first_name': request.form.get('first_name').lower(),
            'last_name': request.form.get('last_name').lower(),
            'email': request.form.get('email'),
            'about': request.form.get('about'),
            'subject': request.form.get('subject'),
            'qualification': request.form.get('qualification').lower(),
            'years_tutoring': request.form.get('years_tutoring'),
            'profile_image': request.form.get('profile_image'),
            'created_by': session['username']
        })

        flash("Your tutor profile is live!", 'success')

        return redirect(url_for('my_profile', creator_id=session['username']))

# Edit profile
@app.route('/edit_profile/<username_id>')
def edit_profile(username_id):
    profile = mongo.db.profile.find_one({'_id': ObjectId(username_id)})
    return render_template('edit_profile.html', profile=profile)

# Update profile
@app.route('/update_profile/<username_id>', methods=['GET', 'POST'])
def update_profile(username_id):
    profile = mongo.db.profile
    
    profile.update({'_id': ObjectId(username_id)},{
            'first_name': request.form.get('first_name').lower(),
            'last_name': request.form.get('last_name').lower(),
            'email': request.form.get('email'),
            'about': request.form.get('about'),
            'subject': request.form.get('subject'),
            'qualification': request.form.get('qualification').lower(),
            'years_tutoring': request.form.get('years_tutoring'),
            'profile_image': request.form.get('profile_image'),
            'created_by': session['username']
        })

    flash('Success! Your profile has been updated!', 'success')

    return redirect(url_for('my_profile', creator_id=session['username']))    

# Delete profile
@app.route('/delete_profile/<username_id>')
def delete_profile(username_id):
    profile = mongo.db.profile
    profile.remove({'_id': ObjectId(username_id)})
    flash("Success, your profile has been deleted.")

    return redirect(url_for('tutors'))

# Email subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    subscriber = mongo.db.subscribers
    subscriber.insert_one(request.form.to_dict())
    flash('Thanks for subscribing!', 'success')
    return redirect(url_for('home'))

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