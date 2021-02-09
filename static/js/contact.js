let form = document.getElementById("contact-form");

document.getElementById('modal-close-btn').addEventListener('click', function (event) {
    emailjs.sendForm('gmail', 'explore_london', form);
    form.reset()

});


// ** Sources of guidance used to create this code ** 

// ** Johann from tutor support helped me to fix the bug that the materialize modal was causing **
// ** https://www.emailjs.com/docs/tutorial/creating-contact-form/ **



