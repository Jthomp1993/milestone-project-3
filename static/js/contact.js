let form = document.getElementById("contact-form");

document.getElementById('modal-close-btn').addEventListener('click', function (event) {
    emailjs.sendForm('gmail', 'explore_london', form);
    form.reset()
});

