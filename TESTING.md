## User Stories from UX section

The following tests were carried out in order to make sure the user stories mentioned in the README.md file were being met. 

### **Project Stakeholders** 

* Being the creator of this project, I wanted to ensure that I created a platform that was intuitive to use and would encourage users to return 
to the website. I feel I acheived this through carefully designing the information architecture and overall desgin of the website 
to ensure the website is easy to navigate and use appropriately. The fixed Navbar enables a user to navigate to any section of the website at any given 
moment whilst they are using the website. The back to top buttons featured throught the website enable users to easily navigate back to the top of the page. 
The user is able to add a recommendation from any page on the website by using the link in the Navbar or the from the add receommendation 
button within their profile. The users recommendations are easy for them to update or delete from their profile where all of their recommendations are displayed. 

### New users 

* For the user who is going to be visiting London for the first time. They will be able to visit the Explore London app where they will
be able to register and make their account. From their they will be able to explore all of the recommendations on the Home page 
and begin to plan where they are going to stay, where they are going to go for drinks, where they are going to go to eat and what they are
going to do. Then if they wish to after they stay in London they can add recommendations of anything else they discovered during their stay. 

* For the user who lives in London and wants to discover new places to drink with their partner. The user will be able to register and create
their own account. From there they will be able to filter the recommendations on the home page by clicking on the Drink tab. This will display 
all of the recommendations of places to drink in London. If the user happens to discover any other new places to drink in London they 
will be able to add their own recommendations. 

* For the user who wants to plan things to do with their children during the summer holidays. The user would be able to register and make an account.
From there they would be able to go to the home page and filter the recommendations to display all of the Explore recommendations. 
This would provide the user with all of the recommendations of things to do in London and could decide what they wanted to do. 
The user could also add any recommendations of their own. 

### Returning Users 

* For the user who wants to add a recommendation for the restaraunt that they ate at in Shoreditch. The user would be able to login to 
their own account. From their profile or by selecting Add Recommendation from the Navbar, they would be able to add the recommendation for 
the restaruant that they ate at in Shoreditch. The user will then have the option to update the recommendation or delete the 
recommendation if they wish to do so. 

* For the user who wants to use the website to plan their upcoming trip to London after using it to plan their trip last year. 
The user would be able to login into their account and from their would be able to navigate to the home page. The user would be presented 
with all of the recommendations where they would be able to begin planning everything for their upcoming vist. After their visit the user 
would be able to add recommendations for anything new that they discovered during their trip. 

* For the user who travels to London on business and uses the app to find the best places to stay. The user would be able to login 
to their account and from there can navigate to the Home page. From there the user would be able to filter the recommendations by clicking 
the Hotels tab and that would display all of the hotels recommendations. Here the user would be able to choose where they were going to stay during 
their upcoming business trip. 

### Mobile User 

* For the user who wanted to use the app on their mobile device. Throughout the development process I made use of the 
Materialize CSS grid system to ensure that the app is fully responsive accross all screen sizes. This means the 
user can recieve the same experience using the app on mobile as to using it on a desktop. 

## W3C HTML Validator

When my HTML code was passed through the W3C HTML validator it returned the following errors. All of these errors can be overlooked as they are due
to the jinja template inheritance. These errors occured throughout all of the HTML pages which was fully expected. 

* Error: Bad value {{ url_for('edit_recommendation', recommendation_id=recommendation._id) }}#recommendations-wrapper for attribute action on element form: Illegal character in path segment: { is not allowed.

* Error: Element head is missing a required instance of child element title.

* Error: Non-space characters found without seeing a doctype first. Expected <!DOCTYPE html>.

* Warning: Consider adding a lang attribute to the html start tag to declare the language of this document.

* Error: Text not allowed in element select in this context.

### contact.html

The following error was returned when the contact.html file was passed through the HTML validator. This can be overlooked as the data is being 
appended into the element with JavaScript. 

* Warning: Empty heading.

### base.html 

The following error was returned when passing the base.html code through the validator. This may be overlooked as this code is copied from 
the EmailJS documentation. The other 3 errors may also be overlooked due to jinja template inheritence. 

* Warning: The type attribute is unnecessary for JavaScript resources.

* Error: Stray end tag head.

* Error: Start tag body seen but an element of the same type was already open.

* Fatal Error: Cannot recover after last error. Any further errors will be ignored.

## W3C CSS Validator 

All of my CSS files passed through the validator without any errors. 

## JavaScript Testing (JSHint)

### Contact.js 

The code from contact.js return an error for a missing semi colon which I ammended and the following error which may be overlooked. 

* 	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).

### maps.js 

The code from maps.js returned a series of ES6 errors when passed through JSHitn which call be overlooked. It also returned two undefined
variables which one of is from Jquery and the other from the google maps api code. Both of these can also be overlooked. 

### script.js 

The code from script.js returned two ES6 errors which may be overlooked and also a series of undefined variable errors due to the 
Jquery $ syntax, this may also be overlooked. 




