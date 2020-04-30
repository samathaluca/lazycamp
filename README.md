travis 

[![Build Status](https://travis-ci.org/samathaluca/lazycamp.svg?branch=master)](https://travis-ci.org/samathaluca/lazycamp)

Lazy camp - Last minute campspot booking app.
Link to Milestone Project 4

Project purpose

Camping on the spur of the moment is currently very difficult unless you are a seasoned camper who may or not be familiar with the area they want to visit.
Even the large caravan and camping clubs either discourage last minute bookings by making it difficult or insist on arrival times that do not suit everybody.
The freedom of the open road and the wonderment of spontaneity can be exhilerating. 

This project will roll out in Scotland first where the number of tourists in the summer months excedes the number of overnight accommodation so visitors who are not very organised can even find themselves sleeping in police cells overnight.


Quick guide
Home Page
About Page
Campspots Page
Individual Campspot Page
Register Page
Login Page
User Dashboard

To Add
Enquiry and contact PageBlog
Idea Page
Testiminial Page
Checkout Page


Ux
User stories
Lazy camp is for the spontaneous. Last minute plans to fit the weather or the call of the wild.

Coming out of the covid pandemic travellers may not wish to book abroad and may be keen to get away for a few days. If i can be ready for the end of lockdown the site may get a lot of interest. 

The scottish 500 is an aspirational road trip with world class sunsets, wild beaches, cliffs, accessible islands with turquoise seas, mountains, culture, heritage, castles and legend. 
To prebook this is tricky and limits the enjoyment of the trip.
A last minute decision to divert or stay an extra night is bliss. lazy camp allows for this.

Many people do not know how to prepare for a camping trip and so never experience the freedom it offers. Lazy camp will offer a set up ready to arrive with no kit and leave with your back back.

Late arrival is currently difficult. This will be one of the features on offer. 24/7 pitches will be available

On the road trip to greece last summer we often found ourselves scaling fences with locked gates. Lazy camp will offer spots on the edge of campsites where late arrival is possible.





All visitors to the site will expect/want/need:


Professionals/Business Users


Feedback and comments from user groups


Development planes

The strategy plane- is this still in favour to go for 5 planes?
The scope plane
Structure
Kkeleton
surface

Wireframes


Defensive design planning

DATABASE

Features and design elements

index.html page features

Future features


Tech Used
HTML5 Semantic markup language as the shell of the site.
CSS -This was used to style the elements of the HTML code.
MATERIALIZE -HTML forms, cards, templates with nav bar, buttons etc. js materiliaze
PYTHON3
FLASK Framework to construct and render pages.
MONGODB_ATLAS for nonsql database
GITPOD IDE
HEROKU - deployment
GITHUB - used for version control
VSC used to help format and beautify the code using extensions. Also as a back up IDE when internet access was limited.
GIMP -This was used for resizing, cropping, fading and changing images to fit the site.
PHOTOSHOP - For digital image production.
FAVICON- used to develop tab icons which were replaced by photoshop 64px by 64px image.
MARKDOWN -Language for Readme.md file
PYMONGO - to make communication between Python and MongoDB possible
[PIP and Pypi libraries]
JQUERY -This added functionality to the site e.g. navigation toggle.
JINJA - to simplify displaying data from the backend of this project smoothly and effectively in html.
BEAUTIFIER - to check code and improve code readability.
BALSAMIQ - wireframe design
HEX CODES - different colours experimentation. 22, GOOGLE FONTS
Testing
Chrome Devtools
HTML Validator
CSS Validator
HTML and CSS Beautifier use format selection in beautify code
AutoPrefixer -This project used AutoPrefixer to make sure the css code is valid for all browsers.
Markdown live-preview -This project used markdown previewer to check the rendering of the readme.md file content.
PEP8 online- Not secure but ok for testing console errors.
Gitpod- IDE used throughout the project.
VSC code extensions- To test code when gitpod was not working well.
IDLE- to check python code
Javascript- Tested to check Materialize initialization.
Early development testing.


Responsive Design - Recipes for Recovery app is fully responsive;




Compatibility
To ensure a broad range of users can successfully use this site, I tested it across the 6 major browsers in desktop, tablet and mobile configuration. Different versions used by friends, family and other students. No issues.

Chrome

Edge

Firefox

Safari

Opera

Devices tested
Mobile phones

Samsung S9,
Iphone 6
Iphone7
Iphone 7S plus,
Sony XA42
Tablets tested

Ipad = LNBEI 10 inch Android tablet
Laptop tested

MacBook pro,
Sony Vaio
HP Pavillion DV6
Desktop (unbranded Windows 7 OS) with different monitors 21 and 27inch.

Version control and Heroku Deployment
For version control Github has been used. Github is a distributed Version Control Systems (DVCSs) recommended by Code Institute which ensures we have a store of all significant changes made during development. Using Gitpod alongside Github had major advantages in terms of how easy it was to stage, commit and push versions but I did get confused in the early days of using Gitpod because opening up previous versions and trying to save them did not commit as the most recent version which led to a number of different worskpaces for the same repository listed in gitpod.io associated with one repository.

I found it easier to copy and paste previous changes in to the most recent worksspace which left clean development path releative to timeline.

In summary, gitpod offers all opened versions of a respository within https://gitpod.io/workspaces/. There is one master and numerous detached, previous versions that have been opened. I only worked within master after losing track of some changes within previous versions.

I was careful to use commit messages that I could find again if needed. I did notice some students had 800-900 commits for their projects. I have only made commits when there is a change made I believe is a step forward in development. The most basic changes such as, spellings, form questions, colour tests, link changes etc. have not been saved individually because I use version control as a working tool and want it as lean and easy to find amendments as possible.

As detailed below I moved from version control and deployment via the command line terminal to setting up IDE to DVSC commits with automated deployment. This made version control and deployment effortless.

Github repository

Milestone 3 final deployed app

Github initial commit to repository and first heroku build were created on the same day. Version control and Heroku deployment were initially done separately in the command line (Method one below) then as better understanding of gitpod and heroku was grasped, all significant version changes were pushed to github and automatically deployed to heroku once the app was connected to the github repository (Method two below).

Version control was relied upon throughout the development process. A number of times changes were aborted and an old version was reverted to. For example github commit 50 reverted to app.py in commit 44.

Many times previous version code was reused. This was particularly useful when gitpod refresh was not working as expected which created unexpected issues. For example, styling did not appear until 90 minutes after the change had been made or was only noticeable in the deployed app.

In summary, two methods of deployment were used. Both were successful but the second method was favoured because it allowed version control and deployment at the same time.

To deploy Recipes for Recovery app to heroku, the following steps were taken:

Method one . Initially, for each version I initially pushed separately to either github and and heroku.
I began deployment via the CLI in gitpod workspace terminal using the following commands until I saw the build log in heroku or github repository showed successful deployment and/or new version commit:

npm install -g heroku

heroku login -i

git status

git add

git commit -m "initial commit"

git remote add heroku https://git.heroku.com/fallen-but-not-broken

git push -u heroku master

git remote -v

pip3 freeze --local > requirements.txt

echo web: python app.py > Procfile

Initially I separately added to the github repository.

git add git commit -m "" git remote add (my repository named fallen) git push -u origin master

Method two
When I tried to work out how to combine git push and heroku deploy I worked out a simpler method possible using the SOURCE CONTROL:Git branch icon in the gitpod workspace.

This was achieved by connecting heroku to github and selecting automatic deploys.

Github and heroku connected

From that point on gitpod push to github automatically deployed to heroku and so github version control and heroku build log mirrored each other perfectly.

Gitpod and github/heroku commit/deploy

click on branch icon
Hover on changes and click + (plus) to stage changes
Type commit message
Hover on tick reveals commit tooltip. Click to commit.
Hover on more actions '...' click reveals dropdown with push option. Click on push.
Check that Build has succeeded in heroku dashboard. It may take a couple of minutes. Open app to check changes. Do not forget to refresh. Often F5 is needed to see the recent changes in the deployed app.

Step by Step deployment from fresh gitpod terminal workspace would be.

Checked requirements.txt file using the terminal command pip freeze > requirements.txt.

Checked Procfile with the terminal command echo web: python app.py > Procfile.

Stage changes in gitpod. Write a commit message, click on the tick icon then push to Github.

Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

Confirm the linking of the heroku app to the correct GitHub repository.

In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

Set the following config vars:

Key Value

IP 0.0.0.0

MONGO_URI mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority

PORT 5000

In the heroku dashboard, click "Deploy".

In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

The site is now successfully deployed.

Environment variables, dependencies and any other differences between the dev and live versions.
The only difference is that the MongoDb key values are stored in env.py for dev version (.gitignore file ensures MongoDB password is not revealed on github). For the live version MongoDB key values are stored and accessed in the config vars.

Credits
Content
The recovery recipes (recovery stories) were written anonymously by people in recovery. All other content is original.

Media
The photograph images used in this site were mostly obtained from pixabay.com. All the wok/fire digital images and logos were created to bespoke spec, using photoshop, by Paris Lyons. The photograph/digital mix images were created using the image manipulation program GIMP (gimp.org) from google and pixabay images origins.

Inspiration
I received inspiration for this project after years personally witnessing the struggle people have to find recovery from addiction, in all of the many forms. The prognosis for recovery is very poor and data collection to find out why, could make a difference. A few days before submitting my final project, my neighbour set his house on fire cooking while drunk. He has been trying to stop drinking for many years. After hearing his smoke alarms through the walls, my son and I looked over the fence and saw his house filled with smoke. My neighbour had collapsed and was lying next to the fire unconscious. I called 999 and watched 3 fire engines, 2 ambulances and 2 police cars arrive. The fire officers bust his door down and prevented our adjoining houses burning to the ground. My neighbour called me the next day and could not remember anything other than getting a taxi back from the hospital and going to buy a morning bottle of vodka. Different methods need to be developed to help and I believe the more stories we can collect from people who have recovered, the more chance they is of alleviating suffering within this vunerable group.

Acknowledgements
Paris Lyons for the digital images, My mentor Brian Macharia for his thorough checks and clear direction. Thank you for the invaluable new screen share sessions offered by Code institute. Helpful when I hit a brick wall in my understanding a) when I was new to gitpod with Michael and Luca b) getting my update function working with Tim. The tutor team support has been excellent. Knowing I can access Michael very early and Anna in the evenings has meant no problem has gone unsolved for long. Slack has been an asset and the final decision making help at the end the final push. I looked at other students work and particularly liked Shane Muirhead's design. (https://milestone4.herokuapp.com). My early balsamiq designes were inspired by this project. I did experiment using some of shane's code but it did contain some of the materiliaze card bug issues on zoom I mention in the responsiveness section. His recipe card page layout inspired my story_detail.html page but he hard coded his recipes and mine were pulled from the details in the database.

Submission
Assessment Criteria review
I have aimed to fulfil all the assessment criteria below to a standard beyond that expected. Final review and readnme checks done. Your Data Centric Development project will be assessed based on the following criteria:

Usability and Visual Impact:

Project Purpose, UX design, Suitability for purpose, Navigation, Ease of use, Information Architecture, Defensive Design,

Layout and Visual Impact:

Responsive Design, Image Presentation, Colour scheme and typography

Code Quality:

Appropriate use of HTML, Appropriate use of CSS, Appropriate use of Python, Appropriate use of the template language

Software Development practices:

Directory Structure and File Naming, Version control, Testing implementation, Testing write-up, Readme file, Comments, Data store integration, Deployment implementation, Deployment write-up
















Database plan. 

MODEL/ DB FIELDS (rows)

CAMPING SPOTS

id: INT
title: STR
Pitch type: STR (rural/ town/ airport/ farm/ river/ seaside/ beach/ cliff)
Pitch mood : STR (relaxed/ vibrant/ solitude)
Owner type : STR (friendly/ remote/)
Extras offered : STR ( collection from public transport, washing, breakfast, kit hire)
Utilities on pitch : STR
Utilities nearby : STR
(Amenities on pitch : STR)
Amenities nearby : STR
Parking or public transport details : STR
Address: STR
Description: TEXT
Price: FLOAT
Photo_main: STR
Photo_1: STR
Photo_2: STR
Photo_3: STR
Photo_4: STR
Photo_5: STR
Total pitches available: STR
Good choice for: STR (families, young couples, early birds, nightowls, nature lovers, wild swimming)
Is late arrival: Boolean
Is 24 hours: Boolean
Full Set up available: INT[0] (default of zero)
Year of set up: INT

Owner name: STR
Owner photo: STR
Owner Description: STR
Owner Phone: INT
Owner email : STR

General Contact enquiries
id: INT
(user_id: INT)
name: STR
message: TEXT
email: INT
Phone: INT

SPOT Specific Contact enquiries
id: INT
user_id: INT
camping spot: STR
camping spot id: INT
name: STR
message: TEXT
email: INT
Phone: INT
date: DATE

USER 
name: STR
visits: STR
Favourite Spot: STR
Bio: TEXT















