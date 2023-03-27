# **Contact App** 

I built this website to the people for storing their contacts details.
In the Contacts app , you can view and edit your contacts lists from personal, business, and other accounts. You can also create contacts and set up a contact card with your own information.

[You can try it here on the live website!](https://contactapp.herokuapp.com/)

<img width="956" alt="image" src="https://user-images.githubusercontent.com/100950189/227890090-fc442356-1350-4a0f-b28a-0a4c262655f8.png">


## _**Contents**_

* [User Stories](#user-stories)
    * [Completed User Stories](#completed-user-stories)

* [Features](#features)
    * [Future ideas](#future-ideas)

* [Design](#design)
    * [Colors](#colors)
    * [Font](#font)
    * [Images](#images)
    * [Audio](#audio)

* [Testing](#testing)
    * [W3C Validator](#w3c-validator)
    * [CSS Validator](#css-validator)
    * [Lighthouse](#lighthouse)
    * [Manual testing](#manual-testing)
    * [Solved bugs](#solved-bugs)

* [Technology Used](#technology-used)

* [Deployment](#deployment)

* [Credits](#credits)


## _**User Stories**_

 ### _**Completed User Stories:**_
    
    * As a site user I can Store our contact details so that will store for long time

    * As a site user I can Add name of our contact so that will store for long time

    * As a site user I can add contact last-named so that will store for long time

    * As a site user I can add contact phone number so that will store for long time

    * AAs a site user I can add contact email so that will store for long time

    * As a site user I can add contact age so that will store for long time

    * As a site user I can add contact gender so that will store for long time

    * As a site user I can display all the details in another site so that will store for long time

    * As a site user I can edit that all details so that will store for long time

    * As a site user I can remove some contact details so that will remove from screen
    
    * As a site user I can Add account so that will store all contact details on specific account
    
    * As a site user I can sign to account so that will added on admin site


* You can find the agile method to my user stories on my github repo just click [here](https://github.com/users/ViktorMathe/projects/5/views/1)

## _**Features**_

The Contacts App lets you organize and manage your company's relationships with customers, vendors, and leads by creating and maintaining contacts for each. Method lets you maintain records of the names, phone numbers, emails and job titles of every person you do business with. 


   <img width="941" alt="image" src="https://user-images.githubusercontent.com/100950189/227898932-052494af-a617-4a5c-a0c2-24ad1420e7d9.png">


 The user can check if the booked appoitment either is still pending or has been approved.  

![Approve/Pending](./static/images/pending-approve-bookings.png)

And if the user wish can change the still pending booking but which has been approved can not been edited just delete it.  

![Edit](./static/images/edit-booking.png)
![Delete](./static/images/delete-booking.png)

I hope everybody found this website useful and easy to navigate on even if the cleaners will not turn up for the booked dates. As always there is so many things what I would like to do to improve my website with further features.

 
 ### _Future ideas:_
  * I would like to send e-mails when the user registered/booked an appoitment 
  * I would like to send an e-mail to confirm the booking.
  * Make a contact form where the user can ask anything from the cleaning staff
  * Add comment/answer option to the question forms.
  * The user can see which days and time slots are available to book.

  ## _**Design**_

  * ### _Colors:_
    * I choose a dark red color ( rgba(112, 13, 0, 0.9) ) with 90% of opacity to header and footer which I think it is a good eye catching colour with a light grey (#D7DDE0) writing on it so it is easy to read and looks quite good.
    * The box which contains the forms and the booking/review informations is the same light grey what I used for the fonts earlier so it is fit in the website design and I have a basic black writing on it.
    * The buttons have been style as the action for example the pending/edit sections are marked as yellow, the delete button is red and the approved button is green as success.

  * ### _Font:_
    * I used a Google Font called Lato with regular (400) weight and add Italic style to all of the headers and normal for rest of the page.
 
  * ### _Images:_
    * I used an image about a very nice clean, tidy kitchen so the users can see straight this company is trying to do the best service what they can.


## _**Testing**_

* ### _W3C Validator:_
    * I got back the following message : Document checking completed. No errors or warnings to show. from the official [W3C Website](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-deepest-cleaning-vm.herokuapp.com%2F)

* ### _CSS Validator:_
    * I got back the following message: Sorry! We found the following errors (16)
    URI : https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css from the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthe-deepest-cleaning-vm.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) which is bootstrap fault my own CSS has no Error!

* ### _Lighthouse:_
    * I done the lighthouse check through an incognito because that is when I got back the true result which were the following:

    ![Image about the lighthouse results](./static/images/lighthouse.png)

    The performance keep jumping up and down but always still in the green area the best practices is a bit lower because I used jQuery and the Google Maps API.

* ### _Manual testing:_

    #### **Register New Account**

    * Expected: As a User I want to able to register to the website to book my cleaning 
    * Test: Create new account with username, create new account with already existing username, create new account with and without email address.  
    * Outcome: If the new account has a username the account is created, if an email address is entered or not. When trying to create a new account with an existing username, the user is encouraged to choose a different username since it already exists. When the account is registered the user is logged in and is notified by an alert. 

    #### Login

    * Expected: As a registered site user you should be able to log in to your accout to be able to interact with the site.
    * Test: Check Login functionality as registered user. 
    * Outcome: When entering valid login details the user is logged in and redirected to the home page and an alert notifies the user that they are logged in. 

    #### Logout

    * Expected: As a registered and logged in user you should be able to log out of the site. 
    * Test: Check Logout functionality as logged in user. 
    * Result: When clicking Logout the user is redirected to Logout page and asked to confirm that they are want to log out. When Log Out button is clicked the user is logged out and redirected to home page and an alert notifies the user that they are logged out.  

    #### **Testing as a User**

    #### Make a Booking

    * Expected : The user can book an appoitment and can view it in the pending booking section until is not been approved and get a notification when the booking was done.
    * Test: Made the booking as a user.
    * Outcome: When the booking has been made I get the notification and it appeared in the pending booking section.

    #### Edit a Booking
    
    * Expected : The user can edit an appoitment if it has not been approved and can view it in the pending booking section and get a notification when the booking was done.
    * Test: Edit the booking as a user.
    * Outcome: When the booking has been edited I get the notification and it has been changed.

    #### Delete a Booking
    
    * Expected : The user can delete an appoitment if it either been approved or not and should disappear from the pending/approved booking sections and get a notification when the booking was done.
    * Test: Delete the booking as a user.
    * Outcome: When the booking has been deleted I get the notification and it has been deleted from the database.

    #### Add a Review

    * Expected : The user can write a review and can upload a picture if wish, and can view it on the review page.
    * Test: Write a review as a user and upload a picture.
    * Outcome: When the review has been wrote I get the notification and it appeared on the review page with or without picture.

    #### Edit a Review

    * Expected : The user can edit a review and can upload or delete picture if wish, and get a notification when it is done.
    * Test: Edit a review as a user and deleted a picture.
    * Outcome: When the review has been edited I get the notification and it appeared on the review page without picture.

    #### Delete a Review

    * Expected : The user can delete a review.
    * Test: Delete a review as a user.
    * Outcome: When the review has been deleted I get the notification and it disappeard from the review page.
    
    #### **Testing as a SuperUser**

    #### Approve Bookings

    * Expected: The superuser can see all the pending bookings and able to approve it.
    * Test: Approve the pending booking.
    * Outcome: The pending booking has been approved and appeared in the approved booking section.

    #### Edit Booking

    * Expected: The superuser can see all the pending bookings and able to edit it.
    * Test: Edit the pending booking.
    * Outcome: The pending booking has been edited and stayed in the pending booking section.

    #### Delete Booking

    * Expected: The superuser is able to delete any booking made by anyone if it is been or not been approved.
    * Test: Cancel booking in the pending and approved sections.
    * Outcome: Both booking has been deleted from the database and the frontend.

    #### Edit Review

    * Expected: The superuser can edit all the reviews do not matter who wrote it.
    * Test: Edit a review.
    * Outcome: The review has been edited and still on the review page.

    #### Delete Review
    
    * Expected: The superuser is able to delete any review made by anyone.
    * Test: Delete review.
    * Outcome: The review has been deleted from the database and the frontend.

 * ### _Solved bugs_:

    * Bug: When I wrote a review it has not been sent to the database.  
    Solution: I did the "makemigrations" command loads of times but did not actually "migrate" it. that is why the database was not connected properly.

    * Bug: I made the form to leave a review but it did not show up on the template.  
    Solution: I was using a class based formview to render the template but I have not get the context data so the form did not show up.

    * Bug: I had a problem with the edit review/booking I could not pull the data which was already been wrote in the review or been booked in a modal.  
    Solution: I had a nice session with the tutors about it and at the end Ger said the big issues was I had to make a separate html for the edit where I can bring up the review/booking with the right id.

    * Bug: When the user had to write the date for cleaning date there was no calendar just had to put in manually.  
    Solution: Lucky for me my mentor showed me a solution with a widget in the forms and all was good.

    * Bug: I coud not upload any images to the review page on the frontend.  
    Solution: As I spoke with the tutors they point me to the right direction to I have to include a tag in the form which was the following : enctype="multipart/form-data" and this tag is let me upload the image from the front end.

    * Bug: I couldn not show the validation message when the user choose a day in the past.  
    Solution: The issue was I redirected the site to the home page after form has been done and the user could not see any message but the easy solution wwas just render it.

    * Bug: Approve button not working.  
    Solution: Change the integerfield to boolean field and toggle instead of a form.

    * Bug: After deployment to heroku, the static files are not found.  
    Solution: It happaned because the Debug in the settings was on True and I deployed like that, after I changed it to False everything went perfect.


## _**Technology Used**_
* [Django](https://www.djangoproject.com/ "Django Project website")
    - Django was used to build the models, forms and views of the app, and was the backbone of this project.
* [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/ "Bootstrap")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes, but also other styling such as buttons etc.
* [Cloudinary](https://cloudinary.com/ "Cloudinary")
     - Cloudinary was used as free cloud storage for images uploaded to the site through the recipe forms.
* [Summernote](https://summernote.org "Summernote page")
     - Summernote was used to allow users to add styling when adding a recipe to the site. This is particularly useful for using bullet points for ingredients or numbering the steps for the recipe.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Crispy Forms documentation")
    - Crispy Forms was used to style the add and edit recipe forms, allowing more than one field to occupy a line on the form.
* [Google Fonts](https://fonts.google.com/ "Google Fonts")
    - Google fonts were used to import the fonts "Playfair Display" and "Lato" into the style.css file. These fonts were used throughout the project.
* [Font Awesome](https://fontawesome.com/ "FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
* [GitPod](https://git-scm.com/ "GitPod")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
* [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
* [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL Database")
    - ElephantSQL was used to the new database instead of the Heroku's Postgres
* [Google Maps API](https://developers.google.com/maps/documentation/javascript/marker-clustering/ "Google Maps API")
 -  Google Maps API was used to make the map visible on the site with the marker on it.

## _**Deployment**_

* Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

* Connect GitHub repo:
    - On the deploy tab you choose the deployment method GitHub
    - You type your GitHub repo name to connect with Heroku
    - Click Connect

* Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

* Attach the ElephantSQL database (instead of Postgre on Heroku):  
    - Login to the ElephantSQL website
    - Create New Instance
    - Have to give a name to the plan and had to choose the Tiny Turtle plan which is free
    - Select the region, and data center near your location
    - Click Review and Create Instance
    - Return to the dashboard and click on the instance name and copy the ElephantSQL database URL
    - Code Institute provided a Postgres Migration Tool repo what I had to open and run  a python3 reel2reel.py command in the terminal
    - On the Heroku website go to the settings, reveal config vars
    - At the DATABASE_URL config var have to paste the Postgres URL and copy it to the migration tool and click enter
    - When the terminal asked you had to paste the elephantSQL database url to the migration tool and click enter
    - If you done you go the resources tab on the Heroku site and remove the existing Postgres add-on
    - Write your app name to confirm the delete
    - Go to the settings tab reveal the config vars and the DATABASE_URL should have gone by now
    - Add a new config var called DATABASE_URL and paste your ElephantSQL database url and click Add
    - The database has been changed


* Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Had to the add the followings to the INSTALLED_APPS list:
            - Cloudinary
            - allauth ( for the register/login)
            - django summernote
            - crispy forms
        - MESSAGE_TAGS ( to get the pop up messages if some action happened)
        - CLOUDINARY_STORAGE (to upload the images )
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

* Deployment:
    - On the Heroku website you navigate to the deploy tab
    - You look for the Manual Deploy and choose the "main" branch
    - Click Deploy Branch

* Live website : [The Deepest Cleaning](https://the-deepest-cleaning-vm.herokuapp.com/)


* ## _**Credits**_

    * The background I found it on the [Pexels.com](https://www.pexels.com/photo/white-wooden-cupboards-2724749/)

    * The content on the deep/general cleaning page has been found on the following site: [Clean Sweep Of America](https://www.cleansweepofamerica.com/deep-cleaning-vs-regular-house-cleaning-what-youre-actually-missing/)

    * I would like to give credit to my mentor, the tutors helped me a lot during this project. I am really aprreciate it.

    * The logo was made by my wife, Roxana Mathe done it with Adobe Photoshop.

