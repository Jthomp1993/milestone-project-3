## Table Of Contents

- [User Stories from UX section](#User-Stories-from-UX-section)
    - [Project Stakeholders](#Project-Stakeholders)
    - [New users](#New-users)
    - [Returning Users](#Returning-Users)
    - [Mobile User](#Mobile-User)
- [W3C HTML Validator](#W3C-HTML-Validator)
    - [contact.html](#contact.html)
    - [base.html](#base.html)
- [W3C CSS Validator](#W3C-CSS-Validator)
- [JavaScript Testing (JSHint)](#JavaScript-Testing-(JSHint))
    - [Contact.js](#Contact.js)
    - [maps.js](#maps.js)
    - [script.js](#script.js)
    -[Python](#Python)
- [Compatibility Tests](#Compatibility-Tests)
    - [Testing Different Browsers](#Testing-Different-Browsers)
    - [Testing With Different Devices](#Testing-With-Different-Devices)
    - [Using DevTools Throughout Development](#Using-DevTools-Throughout-Development)
- [Testing EmailJS](#Testing-EmailJS)
- [Manual Testing](#Manual-Testing)
    - [Navigation Bar](#Navigation-Bar)
    - [Footer](#Footer)
    - [Home page](#Home-page)
    - [Profile page](#Profile-page)
    - [Add Recommendation](#Add-Recommendation)
    - [Manage Categories](#Manage-Categories)
    - [Contact](#Contact)
    - [Register](#Register)
    - [Login](#Login)
***

## User Stories from UX section

The following tests were carried out in order to make sure the user stories mentioned in the README.md file were being met. 

### Project Stakeholders

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

### Python 

I ran my python code through the following validators to ensure it met the PEP8 standards. The tests returned no errors in my code. 

* [PEP8 Online Check](http://pep8online.com/checkresult)
* [PythonChecker](https://www.pythonchecker.com/)

## Compatibility Tests

### Testing Different Browsers

I manually tested my project to ensure it was compatible with the following browsers. I also made sure that the project was 
fully responsive accross all screen sizes by using each browsers version of developer tools. There were no issues found during these
tests. 

* Google Chrome 
* Mozilla Firefox 
* Safari 

### Testing With Different Devices

I tested my project on all of the devices that I had access to which were the following. There were no issues found during these 
tests.

* Apple Macbook Pro 13"
* Apple Iphone 11 
* Apple Ipad 
* Apple Ipad Mini 

### Using DevTools Throughout Development 

I used Google Chromes Developer Tools extensively throughout the development process of my project. This tool really helped 
me to achieve the responsivess that I wanted my project to have. After adding each new feature I would check in Devtools to see
how that paticular feature behaved accross the different screen sizes. Through a combination of CSS, media queries and the Materialize 
CSS Grid System I was able to adapt my project accross all the different screen sizes. 

## Testing EmailJS

On the contact page of my project I have an EmailJS form set up which allows the users to contact the Explore London team with any
queries that they may have. Throughout the installation of EmailJS I was sending test emails to ensure they were 
being sent and received. 

Below you can see an example of a test email being sent directly to my own google email account. 

[EmailJS Test](static/images/readme-images/emailjs-test1.png)
[EmailJS Test](static/images/readme-images/emailjs-test2.png)
[EmailJS Test](static/images/readme-images/emailjs-test3.png)

I ran into a bug when I added the modal to my EmailJS form which was preventing the emails from sending. It turned out that this was due to Materialize which I have learned 
is quite a common issue. With the help of Johann from tutor support we managed to solve the problem. To get around what we did was 
to get the form and store it inside the form variable. Then in the event listener for the modal close button we used emailjs.sendForm 
instead of emailjs.send and then passed the whole form in there via the form variable. The form is then reset to allow it to be used again.

## Manual Testing

### Navigation Bar 

* Logo - I tested this by clicking on it to ensure it led me back to the home page. 

* Home -  I tested this by clicking on it to ensure it directs the user back to the Home page. 

* Profile - I tested this by clicking on it to ensure that it directs the user back to their profile. 

* Add recommendation - I tested this by clicking on it to ensure it directs the user to the add recommendation page. 

* Manage Categories - I tested this by clicking on it to ensure that it directs the Admin for the website to the Manage Categories page.

Contact - I tested this by clicking on it to ensure that it directs the user to the contact page. 

Register - I tested this by clicking on it to ensure that it directs the user to the regsiter page. 

Log in - I tested this by clicking on it to ensure that it directs the user to the log in page. 

Log out - I tested this by clicking on it to ensure that it logs the out of the current session. 

### Footer 

To test the functionality of my footer section I clicked on each of the social media icons to ensure that 
it directs the user to the correct website. 

### Home page 

* Categories - I tested this by clicking each of the categoeries to ensure it filter the recommendations correctly. 

* Search bar - I tested this by searching for various items in the recommendations which worked efficiently. 

* Recommendations - I tested this by clicking on each recommendation to ensure it directs the user to the correct page. 

### Profile page 

* Add recommendation button - I tested this by clicking on it to ensure it directed the user to the add recommendation page. 

* Edit button - I tested this by clicking on the edit button to ensure that it directs the user to the edit recommendation page. 

* Delete Button - I tested this by clicking on the delete button to ensure that the modal was presented allowing the user to delete their recommendation. 

### Add Recommendation 

I tested the Add Recommendation functionality by adding multiple recommendations to the website which works efficiently. 

### Manage Categories 

* Edit button - I tested this by clicking on the edit button to ensure that it directs the Admin for the website to the edit category page. 

* Delete button - I tested this by clicking on it to ensure that it presneted the modal to the Admin of the page enabling them to delete the category. 

* Add Category button - I tested this by clicking on it to ensure that it directs the Admin for the website to the Add Category page. 

### Contact 

* EmailJS - The testing for EmailJS can be seen in the testing EmailJS section on this page. 

* Google Maps API - I tested this by clicking each of the buttons to ensure it dropped the appropriate marker onto the map 
and appended in the correct data from the JavaScript file. 

### Register 

I tested the functionality of the Register page by creating a number of accounts which works correctly. 

### Login 

I tested the functionality of the Login page by logging in with some of the of accounts that i created which works as expected. 

