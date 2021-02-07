function sendMail(contactForm){
    email.js.send("gmail", "explore_london", {
    "from_name": contactForm.name.value,
    "from_email": contactForm.emailaddress.value,
    "message": contactForm.message.value
    })
    return false;
} 


