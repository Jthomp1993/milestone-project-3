//    function sendMail(contactForm){
//        email.js.send("gmail", "explore_london", {
//        "from_name": contactForm.name.value,
//        "from_email": contactForm.emailaddress.value,
//        "message": contactForm.message.value
//        })
//        return false;
//    } 

window.onload = function () {
    document.getElementById('contact-form').addEventListener('submit', function (event) {
        event.preventDefault();
        emailjs.sendForm('gmail', 'explore_london', this);
        this.reset()
    });
};

