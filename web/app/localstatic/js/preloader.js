document.addEventListener("DOMContentLoaded", function() {
    const preloader = document.getElementById("preloader");
    const content = document.getElementById("content");

    window.addEventListener("load", function() {
        preloader.style.display = "none";
        content.style.display = "block";
    });
});