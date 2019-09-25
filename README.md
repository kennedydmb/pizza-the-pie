# Django Frameworks

[![Build Status](https://travis-ci.org/kennedydmb/pizza-the-pie.svg?branch=master)](https://travis-ci.org/kennedydmb/pizza-the-pie)

## Milestone Project 4: Pizza The Pie
### Goal 
Build a fullstack web application based around business logic used to control a centrally owned dataset.
With an authentication mechanism and provide paid access to a service.

External users goals
- Find courses to further their knowledge of pizza making process and some business lessons.
- Find courses to send staff on in regards to customer service and making pizzas.

Site owners goals
- Earn money selling courses on the ecommerce web app.

### The application
An application that allows users to browse training courses. 
Create and account to purchase training courses.
Allows users to purchase courses using Stripe.

[Deployed on Heroku](https://pizza-the-pie.herokuapp.com)

## UX
![Device Responsiveness Display](https://imgur.com/qQaScKQ.png "Device displays")

### Users
At this stage the intended users are anyone that would like to view or purchase courses.
This app would allow a training business a platform to showcase their services, and 
would allow pizza shop owners to browse potential courses for their business..
The app could also be joined with the [previous project.](https://github.com/kennedydmb/pizza-database-project)

### User Stories.
- As a training business owner I want a platform to showcase our training programs. 
I would want potential customers to have the ability to ourchase courses and leave reviews.
- As small pizza shop owner I would like to see available training courses for my business.

### Wireframe
Wireframe can be found [here](/WIREFRAME.md "Original Web App Wireframe")

#### Difference To Deployed Version
- Overall: "P.I.Y" is replaced with a logo. The order of profile, cart, and logout have changed. They also have logos.
- Welcome page: Footer is now a darker color and there is an image in the background. 
- Courses Page: Things remain mostly the same here. The sort bar has arrows instead of "Asc" and "Desc". The descriptions are now in a blue box.
- Courses Detail Page: Same as the courses page changes. 
- Cart Page: Same changes as Courses Page. Review title removed.
- Checkout Page: Summary and payment are now side by side on desktop.


### Design
For the color palate I used this [color scheme website](http://colorschemedesigner.com/csd-3.5/)
With the main color being #0E53A7

## Features

### Existing Features

#### Admin
- With the admin feature, the admin can log in and add/remove courses from the database. 
- They can also remove reviews.
- They can check any orders that have been made. Within the order they can see the address of the customer, when they ordered and what they ordered. If necessary, they can add or remove items from the order 

#### Course Display
- Customers can browse training courses.

#### Login/Register
- Cusotmers need to log in before purchasing services or leaving reviews.

#### Pagination
- Customers when browsing will be displayed 6 services max at a time.

#### Search
- Customers can search the database for courses.

#### Sort
- Customers can sort the courses by name or cost, by ascending or descending.

#### Leave Review
- Customers can leave reviews for services. They can be rated out of 5. The results of all the reviews are used to show the average. This can be useful for customers when picking a service.

#### Payments
- Customers can pay for orders using and API called Stripe (However at the moment it is in testing mode)

#### Account Reset
- If users would like to reset their password they can go to their profile and select the option to do so. They will then recieve a link to change their password by email.

### Future Features

#### Sort by review
- In future customers will have the option to sort services by review, either in ascendeing or descending order.

#### Upload profile image
- An option to upload a profile picture to users accounts.

#### Payment information
- The ability to retain card information for future payments.

#### Confirmation emails
- Once a user places an order they will recieve a confirmation email with their order summary.

#### Deactivate account
- Ability for users to deactivate account.

#### Expanded website
- An expanded website to include utensils that would be needed for a pizza shop.
- An area of the website to place an order of ingredients.

## Technologies Used
The project makes use of:
 - [HTML](https://www.w3schools.com/html/)
 -- To build the structure of the content.
 - [CSS](https://www.w3schools.com/css/default.asp) 
 -- To style the content.
 - [Django](https://www.djangoproject.com/)
 -- The framework used to put this project together.
 - [Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=CjwKCAjwg-DpBRBbEiwAEV1_-HRKc5kuXoGrUIbi1QWzng3ZEvw3Obv1qmhUoXJa2iqrfZ4IxfgntRoC_hYQAvD_BwE&gclsrc=aw.ds)
 -- A cross-platform web browser developed by Google. Used as the main browser for dev tools, and to test responsiveness.
 - [AWS cloud9](https://aws.amazon.com/cloud9/)
 -- An online IDE.
 - [GitHub](https://github.com/)
 -- Provides hosting for software development version control using Git.
 - [Responsive Design](http://ami.responsivedesign.is/)
 -- Used to screenshot web application on different devices.
 - [Google Fonts](https://fonts.google.com/)
 -- Used for 'Nunito' font.
 - [Heroku](https://www.heroku.com)
 -- Used to deploy, and host app.
 - [Bootstrap](https://getbootstrap.com/)
 -- Used for premade CSS styling
 - [Font Awesome](https://fontawesome.com/)
 -- Used for premade icons.
 - [Travis](https://travis-ci.org/)
 -- A hosted continuous integration service used to build and test software projects hosted at GitHub
 - [Stripe](https://stripe.com)
 -- An API that allows individuals and businesses to make and receive payments over the Internet.
 - [AWS](https://aws.amazon.com)
 -- Used for hosting images and static data. 
 - [Postgres](https://www.postgresql.org/)
 -- A free and open-source relational database management system emphasizing extensibility and technical standards compliance.

## Testing

### Responsiveness
[Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=CjwKCAjwg-DpBRBbEiwAEV1_-HRKc5kuXoGrUIbi1QWzng3ZEvw3Obv1qmhUoXJa2iqrfZ4IxfgntRoC_hYQAvD_BwE&gclsrc=aw.ds)
Was used to test:
- Galaxy S5
- Pixel 2
- Pixel 2XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro
- Desktop

[Responsive Design](http://ami.responsivedesign.is/) was used to check viewports:

- Desktop
1600x992px scaled down to scale(0.3181)
- Laptop
1280x802px scaled down to scale(0.277)
- Tablet
768x1024px scaled down to scale(0.219)
- Mobile
320x480px scaled down to scale(0.219)

Page is fully responsive.

### Code Testing
[HTML Validator](https://www.freeformatter.com/html-validator.html) -- No issues

[CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) -- No issues

### User Testing
Tested a small group of people (3-4)

### Known Bugs
- Pagination does not yet work correctly when using the search function. 

## Deployment
- The code was developed locally using the AWS Cloud9 IDE.
- Code was then pushed to GitHub.
- Static files and user uploads where then configured to be hosted by AWS S3 buckets.
- Travis was then used for continuous integration.
- Code was then deployed on heroku.

Deployed app can be viewed [here.](https://pizza-the-pie.herokuapp.com)

GitHub Repo [here](https://github.com/kennedydmb/pizza-the-pie/)

### For local deployment
- Clone the project:
` git clone https://github.com/kennedydmb/pizza-database-project`
- Arrange contents so that the cloned document is in the root of the environment.
- Following need to be installed

`sudo pip3 install django=1.11` The framework used.

`sudo pip3 install Pillow` A python package that allows images to be uploaded. 

`sudo pip3 install django-forms-bootstrap` To render our forms with bootstrap styling.

- Create AWS account. Configure an S3 bucket for public access as a place to store user uploads and static files.

`sudo pip3 install django-storages` To set up media and static transfer on S3

`python3 manage.py collectstatic` To send all media and static directories to S3

`sudo pip3 install psycopg2`
`sudo pip3 install dj-database-url==0.5.0` To handle postgres database.

- Create a new app on Heroku and link to your local repo.
- Create a requirements.txt and Procfile.

`sudo pip3 freeze --local > requirements.txt` To tell Heroku what packages are required to run this program.

`echo web: python app.py > Procfile` To tell Heroku what type of application this is.

- Push to github
- Create a new app on Heroku.
- Add postgres database as a resource.

Set up environment variables on Heroku for:
- STRIPE_PUBLISHABLE
- STRIPE_SECRET
- EMAIL_ADDRESS
- EMAIL_PASSWORD
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

- Link up GitHub
- Run deploy.

### Content
- Data created using current pizza shop knowledge. 
- Course images sourced from [Unsplash.](https://unsplash.com/)
- Logo made using [Paint.NET.](https://www.getpaint.net/) 

## Acknowledgements
- Code Institute for the lessons and basis for the app.
- Code Institute tutors from helping me out of difficult spots.
- Code Institues student Slack, extremely helpful for picking up ideas and debugging issues.
- Stack Overflow and W3Schools for finding answers to issues I was having, or to brush up on the basics.
