// contact.js

document.addEventListener("DOMContentLoaded", function() {
    const contactForm = document.getElementById("contactForm");
    contactForm.addEventListener("submit", function(event) {
      event.preventDefault();
  
      const name = contactForm.querySelector("#name").value;
      const email = contactForm.querySelector("#email").value;
      const message = contactForm.querySelector("#message").value;
  
      // Replace with your actual email handling code
      // Here's a simple example that logs the data to the console
      console.log("Name:", name);
      console.log("Email:", email);
      console.log("Message:", message);
  
      // You can also use APIs or libraries to send emails
      // such as using the EmailJS library, or setting up a backend to handle email sending
    });
  });
  