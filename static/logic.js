
// when clicking navbar link, set class of it to active, and remove active class from other links
document.addEventListener("DOMContentLoaded", function() {
    var title = document.getElementsByTagName("title")[0].innerHTML.trim();
    var navLinks = document.getElementsByClassName("navlink");
    var current = document.getElementsByClassName("activeLink");
    current[0].className = current[0].className.replace(" activeLink", "");
    for (var i = 0; i < navLinks.length; i++) {
        if (navLinks[i].innerHTML == title) {
            navLinks[i].className += " activeLink";
        }
    }
});

    