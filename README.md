# Milestone Three

### Code Institute: Data Centric Development Milestone Project

![TutorShip Logo](https://justinmcc066.github.io/TutorShip/assets/images/tutorship-logo.png)

## TutorShip - [Live Site](https://tutorship-app.herokuapp.com/)

TutorShip is an online portal for tutors, mentors, and grinds teachers to reach an audience of students looking for their services.

The aim of this website is to give students a place to find tutors, mentors and grinds teachers in the Dublin area.

 - - - - 

## Contents

1. [UX](#UX "Goto UX")
    * [User Stories](#User-Stories "Goto User Stories")
    * [Wireframes](#Wireframes "Goto Wireframes")
    * [Surface](#Surface "Goto Surface")

2. [Features](#Features "Goto Features")
    * [Existing Features](#Existing-Features "Goto Existing Features")
    * [Features Left to Implement](#Features-Left-to-Implement "Goto Features Left to Implement")

3. [Technologies Used](#Technologies-Used "Goto Technologies Used")

4. [Testing](#Testing "Goto Testing")

5. [Deployment](#Deployment "Goto Deployment")

6. [Credits](#Credits "Goto Credits")
    * [Code](#Code "Goto Code")
    * [Media](#Media "Goto Media")
    * [Acknowledgements](#Acknowledgements "Goto Acknowledgements")

 - - - -

## UX

The goal of this website is to:

* Identify potential tutors to students looking for additional tutoring.

* Provide a clear, easy tutor search.

* Provide a straight forward profile register for tutors.

* Allow students to contact and book tutors directly.


### User Stories

* "As a user I want to be engaged by the landing screen."

* "As a user I want immediate information about the service."

* "As a user I want a website that is easy to navigate from the landing page."

* "As a user I want easy navigation throughout each page."

* "As a user I want to see a list of subjects that are covered by the service."

* "As a user I want to know about the tutors."

* "As a user I want to know if the tutors have qualifications."

* "As a user I want to easily contact the tutor to organise booking."

* "As a user I and tutor I want to know the cost of the service."

* "As a user I and tutor I want to easily create my profile."

* "As a user I and tutor I want to easily update my profile."

* "As a user I and tutor I want to be able to delete my profile if needed."

* "As a user I and tutor I want the ability to be contacted."

* "As a user I and tutor I want the ability to be recommended."



### Wireframes

Wireframes were created using [Whimsical](https://whimsical.com/) wireframe editor and [Sketch](https://www.sketch.com/).
Layouts were created for mobile, tablet and desktop to assist the design decisions before coding.

**Desktop**

* [Home Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/desktop/)
* [Tutors Directory Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/desktop/)
* [Tutor Profile Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/desktop/)
* [Pricing Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/desktop/)
* [Login Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/desktop/)
* [Register Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/desktop/)
* [Create/Edit Profile Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/desktop/)

**Tablet**

* [Home Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/tablet/)
* [Tutors Directory Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/tablet/)
* [Tutor Profile Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/tablet/)
* [Pricing Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/tablet/)
* [Login Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/tablet/)
* [Register Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/tablet/)
* [Create/Edit Profile Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/tablet/)


**Mobile**

* [Landing Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/mobile/)
* [Tutors Directory Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/mobile/)
* [Tutor Profile Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/mobile/)
* [Pricing Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/mobile/)
* [Login Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/mobile/)
* [Register Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/mobile/)
* [Create/Edit Profile Page](https://github.com/JustinMcC066/TutorShip/blob/master/readme_images/wireframes/mobile/)


### Surface

#### Tone/Colours

The landing/home page is vibrant, colourful and engaging.

The design is clean, minimal and refined.

Tones of purple are offset with bright orange and green, evoking a sense of quality and comfort.

White is used for the body background colour for easy readability and allows the graphics, imagery and information take centre stage.

#### Typography

A single sans serif font is used throughout the site - colour, weight and size create the visual hierarchy.

Font used :
* [Poppins](https://fonts.google.com/specimen/Poppins)

The font is linked from [Google Fonts](https://fonts.google.com/) in the Style Sheet.

#### Animation

Subtle fade-in animations are triggered on scroll which provide an engaging experience.

 - - - - 

## Features

### Existing Features:

#### Landing Screen:
   - The landing page contains a hero section with a select dropdown listing all the available subjects that are catered for.
   - An about section follows the hero with a clickable image that opens a video modal.
   - A testimonials section is next on the page and has two student testimonials.
   - An email subscription section is last to feature on the page. Users can submit their email address to be used for notification about new tutors and subjects. The emails are stored in a seperate collection int the Mongo database.

#### Navigation:
   - The navbar is static and features across all pages.
   - The initial navbar links are: Tutors | Pricing | About | Login | Register.
   - The navbar links change depending on the user state:
      * If the user is logged in but *does not yet have* a profile then the navbar links are: Tutors | Student Dashboard | Creat Profile | Logout
      * If the user is logged in and *has created their profile* the navbar links are: Tutors | Student Dashboard | My Profile | Logout

#### Footer:
   - The footer features on each page and updates its links based on the users logged in state.
      * The *Tutor Register* link changes to *Create Profile* if the user is logged in but does not yet have a profile. When the user creates a profile the link updates to *My Profile*.

#### Animations:
   - Subtle animations are used on the home and pricing pages. The JavaScript library, Animate on Scroll is used to create these simple fade in animations.

#### Tutor Directory:
   - The *Tutors* link brings the user to the full directory of tutors. A profile card features for each registered tutor.
   - A sidebar is used to display all the subjects catered for allowing the user to filter by subject.
   - When the window is resised for mobile the sidebar is hidden and a select dropdown takes its place - again, allowing the user to filter by subject.

#### Tutor Profile Cards:
   - Each tutor profile card features a profile image, their name, the subject they tutor, a short about them which is truncated and a star rating.
   - The star rating is static but I would like to implement this in a furute version.

#### Tutor Profile:
   - Each tutor profile features their profile image, their name and their full bio. The subject they tutor and qualifications along with how long they have been tutoring for are also included.
   - *Book Me* and *Facebook Share* buttons are next in the layout and allow a user to contact the tutor via email.
   - The *Facebook Share* shares the profile to facebook. The Javascript library sharer.js is used for this. This allows the user to recommend the tutor to friends.
   - If a tutor is registered, signed in and looking at their profile there are two additional buttions in view - Edit and Delete.
   - The edit button brings the user to a page with a prefilled form with their profile information which they can update.
   - The delete button opens a modal thats questions the user if they are sure they want to delete their profile. A *"Yes I'm Sure"* button is included on the modal which deletes the their profile. The user is still registered and can remake their profile at a later date.

#### Pricing Page:
   - The pricing page is a mockup of how the full featured subscription TutorShip site would work.
   - Three pricing tiers are featured: Basic, Premium and Platinium.
   - Accepted payments are listed below the price table cards.

#### Student Dashboard:
   - The student dashboard is not an active page but placeholder for a possible future implementation. This would be an area where tutors could track the students they are currently tutoring, take notes, track payments and issue receipts to their students.

#### Login/Register:
   - The login and register pages are visually similar. Tey are a centered form with brief instruction.
   - The Register page requires a unique username, a unique email and a password that must be 5 or more characters in length and include at least one number. If all requirements are met then your form details are inserted to a *Users* collection on the database.
   - The login page only requires your username and password to log you in. The details are checked against the details stored on the database. 

### Create/Edit Profile
   - The create profile and edit profile pages are identical except for their buttons. The create profile submit button inserts the form data to to *Users* collection on the database. 
   - The edit profile has two buttons - *Cancel* and *Update*. The cancel button links the user back to their profile cancelling the edit profile process. The update button updates the databas with the new form information.

### Flash Messaging
   - Flash messaging is used to respond to user form inputs highlighting any issues or providing positive feedback on form submission. Two flash messaging styles are used, *success* and *warning* Bootstrap alerts.

### Features Left to Implement
* A feature I would like to implement is on scroll lazy loading for the tutors page so the page would not need to load all profile cards at once. 

* Another feature I would like to add would be a student dashboard where tutors can track the students they are currently tutoring, take notes, track payments and issue receipts to their students.

* A rating system for the tutors is something I would like to implement in the future. This would be included through the student dashboard section. The students that the tutor has worked with would receive a review form where they could submit a rating based on their experience with the tutor.

 - - - - 

 ## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * For structuring the site pages.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  * For styling the content of each page.

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * For creating interactivity on the site.

* [aos.js](https://michalsnik.github.io/aos/)
  * Javascript animated scroll library.

* [sharer.js](https://ellisonleao.github.io/sharer.js/)
  * Javascript social media share button library.

* [Python](https://www.python.org/)
  * For developing and coding the backend.

* [Bootstrap 4](https://getbootstrap.com/)
  * Framework used to form the layout of each page.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  * For jinja templating and page construction.

* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/)
  * For jinja templating and page construction.

* [Werkzeug Security](https://github.com/pallets/werkzeug/blob/master/src/werkzeug/security.py)
  * For password hashing.

* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
  * For creating and storing NoSQL database information.

* [Autoprefixer CSS](https://autoprefixer.github.io/)
  * USed for adding prefixes to CSS classes to ensure browser consistency and compatibility.

* [Google Fonts](https://fonts.google.com/)
  * For linking fonts for use on the site.

* [Favicon.io](https://favicon.io/favicon-converter/)
  * For generating favicon images and ico file.

* [Tiny PNG](https://tinypng.com/)
  * For reducing image file sizes.

* [Adobe Illustrator](https://www.adobe.com/ie/products/illustrator.html)
  * For logo and element design.

* [Sketch](https://www.sketch.com/)
  * For UI design.

* [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html)
  * For image editing and resizing.

* [Visual Studio Code](https://code.visualstudio.com/)
  * Integrated development environment (IDE) used for development.

* [Git](https://git-scm.com/)
  * Used for version control.

* [GitHub](https://github.com/)
  * Used for managing and storing my code.

* [Heroku](https://www.heroku.com/)
  * Used to deploy the web app.

 - - - - 

## Testing
Various methods of testing were used throughout all stages of development.

All methods of testing can be viewed within the [testing.md](https://github.com/JustinMcC066/TutorShip/blob/master/testing.md) file.

 - - - - 

## Deployment
Visual Studio Code IDE was used to develop the website. The code was committed to git and pushed to GitHub within Visual Studio Code.

The site is hosted and deployed through [Heroku](https://www.heroku.com/). The Heroku app is connected to the Git Repository and updates automatically as new commits are pushed to Github.

To deploy this site the following steps were taken:

1. A```Procfile``` was created inform Heroku what type of app is being deployed. Inside the Procfile insert ```web: python <your_app_name>.py```.
2. A ```requirements.txt``` was created using the the command ```sudo pip freeze > requirements.txt```. This holds all the dependencies used in the app.
3. A env.py was created to store the MONGO_DBNAME, MONGO_URI and SECRET_KEY. This was linked to from the main app.py file.
4. These files were then committed to the TutorShip Git Repository.
5. A Heroku account was set up and a new App created using a unique name and choosing a region.
7. The *config vars* were then configured in the settings section of the Heroku app.
8. The Heroku app was then connected to the git repository allowing the app to update/build as new commits are pushed to the repository.

The live site can be viewed here: [TutorShip](https://tutorship-app.herokuapp.com/)

### Local

To run this project locally the following steps are required:
*Please note: You will need to install the following in order to run this app on your local machine:*
*A virtual environment is also recommended for development.*

- Git
- MongoDB
- Python 3
- PIP

1. Navigate to [https://github.com/JustinMcC066/TutorShip.git](https://github.com/JustinMcC066/TutorShip.git)
2. Click the green 'Clone or Download' button and copy the text url in the dropdown.
3. Open up a terminal window in your IDE of choice.
4. Navigate to your desired file location.
5. Paste the following code and input it into your terminal to clone.
```
git clone https://github.com/JustinMcC066/TutorShip.git
```
6. Install the required dependencies for this project by running the following command in your terminal:
```
pip3 install -r requirements.txt
```
6. Create an env.py file to store your MONGO_DBNAME, MONGO_URI and SECRET_KEY.
The env file should include the following:
```
import os

os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>.@<cluster_name>.w9nsx.mongodb.net/<database_name>?retryWrites=true&w=majority"
os.environ["MONGO_DBNAME"] = "<MONGO_DB_NAME>"
os.environ["SECRET_KEY"] = "<SECRET_KEY>"
```
7. For development and debugging, set the debug=True in the app.py file.

#### To deploy the app, follow the steps below:

1. Commit all files to your Git Repository.
2. Sign up and log in to Heroku.
3. ```Create new app``` in Heroku using a unique name. Select your region and create your app.
4. Connect your Github Repo to the Heroku app from the app dashboard on Heroku.
5. From the app dashboard on Heroku select *Settings* and then click *Reveal Config Vars*.
6. Set the following key/value settings for the config vars - see below

#### Heroku Config Vars

Key   | Value   |
:-:|:-:|
 IP  |0.0.0.0 |
 PORT  | 5000  |
 MONGO_DBNAME  | <YOUR_DB_NAME>  |
 MONGO_URI  | ```mongodb+srv://<username>:<password>.@<cluster_name>.w9nsx.mongodb.net/<database_name>retryWrites=true&w=majority```   |
 SECRET_KEY  | <YOUR_SECRET_KEY>  |

The app should now be up and running and available at: ```https://<unique_app_name>.herokuapp.com/```

 - - - - 


## Credits

### Code

The following sites were used for inspiration and assistance:

* [Stack Overflow](https://stackoverflow.com/)
* [Miguel Grinberg Blog](https://blog.miguelgrinberg.com/)
* [Pythonise](https://pythonise.com/)

### Media
The images used on this site are royalty free and were obtained from [Unsplash](https://unsplash.com/)

### Disclaimer
This site has been developed for educational purposes as part of the [Code Institute](https://codeinstitute.net/) Full-stack Software Development course.