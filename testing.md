# Testing

## Contents

1.  [Browsers](#Browsers "Goto Browsers")
2.  [Responsiveness / Mobile-Friendly](#Responsiveness-/-Mobile-Friendly "Goto Responsiveness / Mobile-Friendly")
3.  [Code Validation](#Code-Validation "Goto Code Validation")
4.  [User Story Testing](#User-Story-Testing "Goto User Story Testing")
5.  [Manual Testing](#Manual-Testing "Goto User Manual Testing")
    * [Design](#Design "Goto Design")
    * [Responsiveness](#Responsiveness "Goto Responsiveness")
    * [Functionality](#Functionality "Goto Functionality")

## Browsers
The site was tested across multiple browsers - Chrome, Safari, Firefox and Opera to ensure each page displayed correctly.
Browser compatibility was also tested using the Lambdatest App.

## Responsiveness / Mobile-Friendly
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
  * A *Share* button is located on all tutor profiles which shares their profile to to facebook.


## Manual Testing

Manual testing was completed at various stages throughout development. This ensured all elements responded correctly to each interaction as intended and functions ouput the correct result.
Logging values to the console was key to identifying incorrect calculations and outcomes. [Chrome Developers Tools](https://developers.google.com/web/tools/chrome-devtools)Chrome Developers Tools was used throughout all stages of development.

#### Design

1.  ##### Issue
  * Images became squashed and didn't scale proportionately on Safari and apple devices.
1.  ##### Fix
  * Align-self classes were used to fix this issue.

#### Responsiveness

1.  ##### Issue
  * 
1.  ##### Fix
  * 

#### Functionality

1.  ##### Issue
  * 
1.  ##### Fix
  * 