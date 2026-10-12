const themeButton = document.getElementById("theme-toggle");
const body = document.body;

function setTheme(theme) {

    body.classList.remove("nature-theme", "simple-theme");
    body.classList.add(theme);

    if (theme === "nature-theme") {
        themeButton.textContent = "Simple Theme";
    } else {
        themeButton.textContent = "Nature Theme";
    }

    localStorage.setItem("selectedTheme", theme);
}

themeButton.addEventListener("click", function () {

    if (body.classList.contains("nature-theme")) {
        setTheme("simple-theme");
    } else {
        setTheme("nature-theme");
    }

});

const savedTheme = localStorage.getItem("selectedTheme");

if (savedTheme === "nature-theme" || savedTheme === "simple-theme") {
    setTheme(savedTheme);
} else {
    setTheme("nature-theme");
}