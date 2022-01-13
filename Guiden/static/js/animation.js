var divs = document.querySelectorAll("nav > div");
console.log(divs);
divs.forEach(function (e) {
    try {
        e.querySelector("span").addEventListener("mouseover", function () {
            e.querySelector("div").classList.add("nav-animation");
        });
        e.querySelector("span").addEventListener("mouseout", function () {
            e.querySelector("div").classList.remove("nav-animation");
        });
    }
    catch (error) {
        if (error instanceof TypeError) {
            console.log("skipping logo....");
        }
    }
});
