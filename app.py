import os
from flask import Flask, render_template, redirect, \
    request, session, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, \
     check_password_hash

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Index
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html', subjects_in_sidebar=mongo.db.subjects.find())


# Tutors
@app.route('/tutors')
def tutors():
    return render_template(
        'tutors.html', tutor=mongo.db.profile.find(),
        subjects=mongo.db.subjects.find(),
        subjects_in_sidebar=mongo.db.subjects.find(),
        active='tutors')


# Individual subject tutor list
@app.route('/tutors/<subject>')
def tutor_by_subject(subject):
    tutor = mongo.db.profile.find({'subject': subject})
    return render_template('tutors.html', tutor=tutor, subject=subject)


# Tutor profile page
@app.route('/tutors/<username_id>/')
def tutor_page(username_id):
    profile = mongo.db.profile
    tutor = profile.find_one({'_id': ObjectId(username_id)})
    return render_template('profile.html', tutor=tutor)


# Individual subject tutor list
@app.route('/tutors/subject', methods=["GET"])
def subject_dropdown():
    # store dictionary object of the query string
    subject_selected = request.args.get('subject_selected')
    # pass the subject selected as the value for
    # the subject key in subjects db collection
    subject = mongo.db.subjects.find_one({'subject_name': subject_selected})
    # pass the subject selected as the value for
    # the subject key in profile db collection
    tutor = mongo.db.profile.find({'subject': subject_selected})
    # store subject list in variable to loop through in template
    subjects = mongo.db.subjects.find()
    subjects_in_sidebar = mongo.db.subjects.find()
    return render_template(
        'tutors.html', tutor=tutor, subjects=subjects,
        subject=subject, subjects_in_sidebar=subjects_in_sidebar,
        subject_selected=subject_selected)


# Search function
# https://gist.github.com/cpatrick/5719077
@app.route('/tutors/search', methods=['POST'])
def search():
    return redirect(url_for(
        'search_tutors', search_for=request.form.get('search_input')))


# Search form results page
@app.route('/tutors/search/<search_for>')
def search_tutors(search_for):
    profile = mongo.db.profile

    # Create index for first and last name
    profile.create_index([
        ('first_name', 'text'),
        ('last_name', 'text')
    ])

    # Assign search term to variable used in loop to display tutor profiles
    search_results = profile.find({"$text": {"$search": search_for}})
    search_number = profile.count_documents({"$text": {"$search": search_for}})
    return render_template(
        'tutors.html', search_for=search_for, tutor=search_results,
        search_number=search_number,
        subjects_in_sidebar=mongo.db.subjects.find())


# My profile page
@app.route('/tutors/my_profile/<creator_id>/')
def my_profile(creator_id):
    profile = mongo.db.profile
    tutor = profile.find_one({'created_by': creator_id})
    return render_template('profile.html', tutor=tutor, active='my_profile')


# Pricing
@app.route('/pricing')
def pricing():
    return render_template('pricing.html', active='pricing')


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    users = mongo.db.users

    if request.method == 'POST':
        new_user = request.form.get('username')
        new_email = request.form.get('email')
        password = request.form.get('password')
        username_exists = users.find_one(
            {'username': request.form.get('username')})
        email_exists = users.find_one({'email': request.form.get('email')})

        # check if password is 5 characters or more
        if len(password) < 5:
            flash(
                'Please use 5 or more characters for your password.')
            return redirect(url_for('register'))

        # check if password includes 1 or more numbers
        if not any(char.isdigit() for char in password):
            flash('Password must include at least one number.')
            return redirect(url_for('register'))

        # prevent user from entering characters that are not alphanumeric
        for name in new_user:
            if not name.isalnum():
                flash('Only letters (a-z) and numbers (0-9) allowed.')
                return redirect(url_for('register'))

        # check if username exists - if so, flash warning.
        # If username doesn't exist then check if email exists -
        # if so, flash warning. If email doesn't exist then
        # inserts form data to users collection and redirect to create profile
        # create key for has_profile and set to no -
        # to be later updated when user creates profile
        if username_exists:
            flash('''Username already exists.''')
            return redirect(url_for('register'))

        # if email exists flash try again message
        if email_exists:
            flash('''Email already exists.''')
            return redirect(url_for('register'))

        else:
            users.insert_one(
                {'username': new_user,
                    'email': new_email, 'has_profile': 'no', 'password':
                    generate_password_hash(password)})
            session['username'] = new_user
            session['email'] = new_email
            return redirect(url_for(
                    'create_profile', username=session['username']))

    return render_template('register.html', active='register')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # function to find a user from the database
    def registered_user(username):
        user = mongo.db.users
        return user.find_one({'username': username})

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = registered_user(username)

        # check if user is registered
        if user:
            if check_password_hash(user['password'], password):
                flash(f'Welcome back {username}!')
                session['username'] = username

                # check if user has profile value and asign
                # session value and log user in
                if user['has_profile'] == 'yes':
                    session['has_profile'] = 'yes'
                return redirect(url_for('home', username=session['username']))

            # flash error message if password is incorrect
            else:
                flash('''Oops, there was a problem logging in.
                Please try again.''')
                return redirect(url_for('login'))
        else:
            # flash error if username is not on file - prompt to register
            flash(f'''We don't seem to have a {username}
            on file. Want to regitser?''')
            return redirect(url_for('login'))

    return render_template('login.html', active='login')


# Create profile
@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if 'username' in session:
        flash("You're registered! Let's create your profile")
        return render_template('create_profile.html', active='create_profile')


# Insert profile
@app.route('/insert_profile', methods=['POST'])
def insert_profile():
    profile = mongo.db.profile
    users = mongo.db.users
    # insert form input information to profile collection in the database
    if request.method == 'POST':
        profile.insert_one({
            'first_name': request.form.get('first_name').lower(),
            'last_name': request.form.get('last_name').lower(),
            'email': session['email'],
            'about': request.form.get('about'),
            'subject': request.form.get('subject'),
            'qualification': request.form.get('qualification').lower(),
            'years_tutoring': request.form.get('years_tutoring'),
            'profile_image': request.form.get('profile_image'),
            'created_by': session['username']
        })

        # updates has_profile value to yes when profile is created
        users.update({'username': session[
            'username']}, {'$set': {'has_profile': 'yes'}})
        session['has_profile'] = 'yes'

        flash("Your tutor profile is live!")

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
    # update database values with form input information
    # and flash success message
    profile.update({'_id': ObjectId(username_id)}, {
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

    flash('Success! Your profile has been updated!')

    return redirect(url_for('my_profile', creator_id=session['username']))


# Delete profile
@app.route('/delete_profile/<username_id>')
def delete_profile(username_id):
    profile = mongo.db.profile
    users = mongo.db.users
    profile.remove({'_id': ObjectId(username_id)})

    # updates has_profile value to 'no' when profile is deleted
    users.update({'username': session[
        'username']}, {'$set': {'has_profile': 'no'}})

    # clear has_profile from session object
    # so user sees create profile link in nav
    session.pop('has_profile', None)

    # flash success message
    flash("Success, your profile has been deleted.")

    return redirect(url_for('tutors'))


# Email subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():

    # adds email address to 'subscribers' collection in database
    # flash successful message to user if email is unique
    # if email is already subscribed then flash 'alredy signed up' message
    subscriber = mongo.db.subscribers
    subscriber_exists = subscriber.find_one(
            {'email': request.form.get('email')})
    if subscriber_exists:
            flash('''Looks like you're already signed up.''')
            return redirect(url_for('home'))
    else:
        subscriber.insert_one(request.form.to_dict())
        flash('Thanks for subscribing!')
        return redirect(url_for('home'))


# Logout
@app.route('/logout')
def logout():

    # clear the session and log user out
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
