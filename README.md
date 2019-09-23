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

[Deployed on Heroku]()

## UX
![Device Responsiveness Display]("Device displays")

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
Wireframe can be found [here]( "Original Web App Wireframe")

#### Difference To Deployed Version


### Design
For the color palate I used this [color scheme website](http://colorschemedesigner.com/csd-3.5/)

![Color Scheme]( "Color Scheme")

## Features

### Existing Features

#### Login/Register

#### Pagination

#### Payments

#### Search

#### Sort

#### Leave Review

#### Account Reset

### Future Features

#### Future Tech here


## Technologies Used
The project makes use of:
 - [HTML](https://www.w3schools.com/html/)
 -- To build the structure of the content.
 - [CSS](https://www.w3schools.com/css/default.asp) 
 -- To style the content.
 - [Django]()
 -- The framework used to put this project together
 - [Chrome](https://www.google.co.uk/chrome/?brand=CHBD&gclid=CjwKCAjwg-DpBRBbEiwAEV1_-HRKc5kuXoGrUIbi1QWzng3ZEvw3Obv1qmhUoXJa2iqrfZ4IxfgntRoC_hYQAvD_BwE&gclsrc=aw.ds)
 -- A cross-platform web browser developed by Google. Used as the main browser for dev tools, and to test responsiveness.
 - [AWS cloud9](https://aws.amazon.com/cloud9/)
 -- An online IDE.
 - [GitHub](https://github.com/)
 -- Provides hosting for software development version control using Git.
 - [GitHub Pages](https://pages.github.com/)
 -- A static web hosting service offered by GitHub
 - [Responsive Design](http://ami.responsivedesign.is/)
 -- Used to screenshot web application on different devices.
 - [Google Fonts](https://fonts.google.com/)
 -- Used for 'Nunito' font.
 - [Heroku](https://www.heroku.com)
 -- Used to deploy app.
 - [Bootstrap]()
 -- Used for premade CSS styling
 - [Travis]()
 -- 
 - [Stripe]()
 -- 

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
[HTML Validator](https://www.freeformatter.com/html-validator.html) -- 

[CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) -- 

### User Testing
Tested a small group of people (3-4)

### Known Bugs

## Deployment
The code was developed using the AWS Cloud9 IDE.

Deployed app can be viewed [here.]()

GitHub Repo [here]()

### For local deployment
- Clone the project:
` git clone https://github.com/kennedydmb/pizza-database-project`
- Arrange contents so that the cloned document is in the root of the environment.
- Make sure f
```
sudo pip3 install flask

sudo pip3 install pymongo

sudo pip3 install flask_pymongo

sudo pip3 install dnspython

```
- Create a new app on Heroku and link to your local repo.
- Create a requirements.txt and Procfile.
```
sudo pip3 freeze --local > requirements.txt

echo web: python app.py > Procfile
```
- Set up evironment variables for MONGO_URI and SECRET_KEY, keep them hidden so sensitive data does not get pushed to Heroku.
- On Heroku set up config variables for PORT, ID, MONGO_URI, and SECRET_KEY.
- Push commits to Heroku:
`git push heroku master`


### Content
- Data created using current pizza shop knowledge. 
- Background image of pizza cards from unsplash found [here.](https://unsplash.com/photos/JnAJSWiio64)
- Image was edited using [Paint.NET.]() 
- 
## Acknowledgements
- Code Institute for the lessons and basis for the app.
- Code Institues student Slack, extremely helpful for picking up ideas and debugging issues.
- Stack Overflow and W3Schools for finding answers to issues I was having, or to brush up on the basics.
