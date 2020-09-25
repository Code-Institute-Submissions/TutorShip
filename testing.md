# Testing

## Contents

1.  [Browsers](#Browsers "Goto Browsers")
2.  [Responsiveness](#Responsiveness "Goto Responsiveness")
3.  [Code Validation](#Code-Validation "Goto Code Validation")
4.  [User Story Testing](#User-Story-Testing "Goto User Story Testing")
5.  [Manual Testing](#Manual-Testing "Goto User Manual Testing")
    * [Design](#Design "Goto Design")
    * [Responsiveness](#Responsiveness "Goto Responsiveness")
    * [Functionality](#Functionality "Goto Functionality")

## Browsers
The site was tested across multiple browsers - Chrome, Safari, Firefox and Opera to ensure each page displayed correctly.
Browser compatibility was also tested using the Lambdatest App.

## Responsiveness
The site's reponsiveness was continuously monitored during the development stage using Chromes *Dev Tools*.
Media queries have been added to ensure all elements resize with any issues at the various Bootstrap breakpoints.
Further testing was done using [Responsive Test Tool](http://responsivetesttool.com/) which allowed for testing on additional devices - no errors were recorded.
Responsiveness was also tested using the Lambdatest App.

![Responsiveness Testing](https://raw.githubusercontent.com/JustinMcC066/TutorShip/master/readme_images/site-responsiveness.jpg)
![Testing Feedback Table](https://raw.githubusercontent.com/JustinMcC066/TutorShip/master/readme_images/site-testing.jpg)

## Code Validation
All html pages were checked using [W3C Markup Validation](https://validator.w3.org/) and passed with no errors.

The CSS file was checked using [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) and passed with no errors.

All JavaScript files were checked using [JS Hint](https://jshint.com/) No errors were reported.

The Python apppy file was checked using [PEP8 Online](http://pep8online.com/) to ensure it met PEP8 requirements. No errors were reported.

## User Story Testing

* "As a user I want to be engaged by the landing screen."
  * Landing is colourful, vibrant and complete with subtle animations.

* "As a user I want immediate information about the service."
  * Hero display text features on the landing page header and announces the service features.

* "As a user I want a website that is easy to navigate from the landing page."
  * The hero header section has an option select form that links a user to the tutor list based on the category they choose from the dropdown.

* "As a user I want easy navigation throughout each page."
  * The navbar is accessible from all pages across the site.
  * The navbar is static so it is in view on all areas of the page.

* "As a user I want to see a list of subjects that are covered by the service."
  * Along with the subject category option select form, the tutor directory has a sidbar that lists all the subjects catered for.

* "As a user I want to know about the tutors."
  * Each tutor has a complete profile page which lists their full name a bio, the subject they are tutoring, their qualifications and how long they have been tutoring.

* "As a user I want to know if the tutors have qualifications."
  * The tutor profile lists the tutors qualification.

* "As a user I want to easily contact the tutor to organise booking."
  * A *Book Me* button is included on every tutors profile page which allows users to contact the tutor directly by email.

* "As a user I want to receive updates about the service."
  * A notification section where users can subscribe to receive updtes via email about the TutorShip service is featured on the home page.
  * Flash messaging is included to inform the user if they have subscribed successfully.
  * If the user has already signed up for this notification/newsletter then a flash message informs them that they are already signed up.

* "As a user I and tutor I want to know the cost of the service."
  * A pricing tier page is featured for tutors to see the cost of hosting a profile. The page features 3 subscription tiers where the differnces between them are noted.

* "As a user and tutor I want to easily create my profile."
  * Once registered, a tutor is brought straight to the *Create Profile* page where they can fill in their details and launch thir profile.

* "As a user and tutor I want to easily update my profile."
  * Once a tutor profile is created the user can update their informaiton from their profile page where an *Edit* button is featured.

* "As a user and tutor I want to be able to delete my profile if needed."
  * From their profile page, a tutor can also delete their profile using the *Delete* button.

* "As a user and tutor I want the ability to be contacted."
  * A * Book Me* button is located across all tutors profiles. When creating a profile the user has the option to us the email they used to registered or chnge it to a preferred email address to be contact on.

* "As a user and tutor I want the ability to be recommended."
  * A *Share* button is located on all tutor profiles which shares their profile to facebook.


## Manual Testing

Manual testing was completed at various stages throughout development. This ensured all elements responded correctly to each interaction as intended and functions ouput the correct result.
Printing values to the python terminal was key to identifying incorrect calculations and outcomes. [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) Chrome Developer Tools was used throughout all stages of development.
The site was shared with real users to test usability and reveal any bugs.

#### Design

1.  ##### Issue
  * Hero image was not scaling proportionately and becoming squashed below a certain screen dimension.
1.  ##### Fix
  * The bootstrap img-fluid class was used. Further stuling was used - viewport width and auto height used to achieve the desired result.


#### Responsiveness

1.  ##### Issue
  * JavaScript animation library user (aos.js) was causing the container to break and add white space to the right of the screen.
1.  ##### Fix
  * The animation position was changed from fade-left to fade-right and fade-up.


#### Functionality

1.  ##### Issue
  * The edit and delete buttons were present across all tutor profiles which allowed any logged in user to delete a profile.
1.  ##### Fix
  * Using Flask Session I added a condition that only allows the logged in user to see these butons on their page.

2.  ##### Issue
  * Users could set any text input information as all spaces to create or edit their profile.
2.  ##### Fix
  * I wrote a javascript function to check the input data of the forms and show an error to the user asking for a valid input.

3.  ##### Issue
  * A logged in user could easliy delete their profile with an accidentl clck of the delete button on their page.
3.  ##### Fix
  * A modal was created to house the actual delete button. When the user clicks delete they are presented with a modal instead asking to confirm if they want to proceed with deleting their profile.

4.  ##### Issue
  * An Uncaught TypeError: Cannot read property 'addEventListener' of null at form_validation.js:9 was presented when the site loaded. This was due to the script looking for an #id that was not present on the page.
4.  ##### Fix
  * The Javascript script link from the base.html template and placed it in the template that had the form. This fixed the issue.

5.  ##### Issue
  * When the user registered they were brought directly to the *Create Profile* page. However, if they navigated away from same then they didn't have anylink to return.
5.  ##### Fix
  * I added a key *'has_profile'* to the users database and stored a value of *'no'*. This was then queried and if the user in session didn't have a profile the nav bar now had a link to *Create Profile*. This link updates to *My Profile* when the user successfully creates their profile. The *has_profile* value is also update to *'yes'*.

6.  ##### Issue
  * When the user deleted their profile the session maintained the status of *has_profile* so the nav link did not change back to *Create Profile*.
6.  ##### Fix
  * Session.pop() was used to clear has_profile from session object.

7.  ##### Issue
  * A dropdown nav was used on the home page and tutos directory to link t the tutors listed by subject however the list felt too long to house in a scrolling dropdown navbar.
7.  ##### Fix
  * A form with select opton inputs was created which makes for a much better user experience.