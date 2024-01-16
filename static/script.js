$(document).ready(function () {
  $("form").submit(function (event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    // Use Fetch API to send the form data to the server
    fetch("", {
      method: "POST",
      body: new FormData(this),
      headers: {
        "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val(),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response, update the page content as needed
        console.log(data);
        alert("Form submitted successfully!");
      })
      .catch((error) => console.error("Error:", error));
  });
});

let sections = document.querySelectorAll("section");
let navLinks = document.querySelectorAll("nav ul li a");
window.onscroll = () => {
  sections.forEach((sec) => {
    let top = window.scrollY;
    let offset = sec.offsetTop - 150;
    let height = sec.offsetHeight;
    let id = sec.getAttribute("id");
    if (top >= offset && top < offset + height) {
      navLinks.forEach((links) => {
        links.classList.remove("active");
        document
          .querySelector("nav ul li a[href*=" + id + "]")
          .classList.add("active");
      });
    }
  });
};
