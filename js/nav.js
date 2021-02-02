window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {

        document.getElementById("header").style.padding = "8px";
    } else {
        document.getElementById("header").style.padding = "15px";
    }
}