// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("callback");
var a_callback_line = document.getElementById("callback_line");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close") [0];

var close_success = document.getElementById("close_success_btn");

close_success.onclick = function () {
    success_modal.style.display = "none";
}

var send = document.getElementById("send_callback");

var success_modal = document.getElementById("success_modal");


// When the user clicks the button, open the modal
btn.onclick = function () {
    modal.style.display = "flex";
}
a_callback_line.onclick = function () {
    modal.style.display = "flex";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
    success_modal.style.display = "none";
}

send.onclick = function () {
    modal.style.display = "none";
    success_modal.style.display = "flex";
}



// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
    if (event.target === success_modal) {
        success_modal.style.display = "none";
    }
}
