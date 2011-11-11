==========
Picalytics
==========

Picalytics (short for picture analytics) is a simple application for helping you track visits to your posts on sites which allow use of the <img> tag.  It can also be used to track the number of times your emails are opened.  

I created this program to allow me to track my craigslist ads, as there is currently no other way to analyze ad performance on craigslist. 

At some point, I might add some email tracking capabilities, but the email_tracker has not been implemented yet.

If you like this application, or have suggestions, let me know, and I will try to make improvements.  You can reach me at bearle2009 (at) gmail (dot) com.  

============
Installation
============

Should be very simple.  Make sure you have Django installed - I used Django-1.3, so earlier versions may not work properly.  

You'll need to create a file called 'localsettings.py' in the pix directory to hold your database access details.  

Make sure to run 'python manage.py syncdb' from the pix directory.  

That's it!  Now just restart your server - make sure its set up properly for your Django application.  

It should be pretty straightforward to use this application in an existing Django project, but I haven't done it yet.  Most of the functionality is in the folder pix/craigalytics, with a few essential stylesheets and scripts in the Media folder.  Images are currently set up to be uploaded to the Media/Images/Uploads folder

================
Using Picalytics
================

Basically this application let's you upload images, and then host them for use in craigslist ads.  Every time your ad is viewed, the image will be fetched from your website, and if you count the number of times it is fetched, you will know how often your ad has been viewed.  

I used Twitter's Bootstrap to style the application.  
If you'd like to use your own style, or edit the templates,
you can find the important ones in pix/craigalytics/Templates and pix/main/Templates

To create an image once the site is launched, go to 
{{your_domain_name}}/my_images
You'll be able to upload your desired image there.
Next a few keywords which will be used to generate the shortcode URL that gets tracked.  Every time the image is viewed through this URL, the application will save details about the visitor, and the total number of visits will be counted.  

You can use Title and Description to store information about the ad you are tracking.  

Once you've created your image, you'll be taken to a page with details about the image.  This will include the <img> tag code to copy for use in the ad you want to track.  

=====
Tests
=====

I like tests.  Tests are good.  To run tests, go to the pix directory, and run the command 'python manage.py test --verbosity 2 craigalytics'.  Currently I have one test, which is not particularly useful, but someday my tests will grow and mature into good, decent, grown-up tests that do what they are supposed to.  I think having one test is better than zero tests.  If you would like to add more tests I will love you forever.  Also, if you create a test fixture, I will love you forever again.  I use high verbosity because I get bored waiting for the database to be set up, so I like to see something get printed while I'm waiting.  

=====
To Do
=====

I'd like to add some more tests.  I'd also like to put in some javascript that will let you copy the <img> code with a single click.  Finally, I want to include some code to convert ip addresses to city names.  
