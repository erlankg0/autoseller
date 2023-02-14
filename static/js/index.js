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

const send_question = document.getElementById("question_btn_send");
send_question.onclick = function () {
    var phone = $('#question_phone').val();
    var name = $('#question_name').val();
    $.ajax({
        url: '/credit/callback',
        type: 'GET',
        async: false,
        data: {
            name: name,
            phone: phone
        },
        success: function (data) {
            const modal_ = document.getElementById("success_modal");
            modal_.style.display = "flex";
        }
    });
    // stop action form
    phone.val(''); // clear input
    name.val(''); // clear input
    return false;
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

function showModal(image, price, pk) {
    const modal = `
 <div class="modal_views modal" id="auto_reserve" style="display: flex;">
    <div class="container_modal" style="border-radius: 25px;">
        <span class="close" id="close_auto_reserve">&times;</span>
        <div class="modal-content" style="border-radius: 25px; height: 400px;">
            <div class="content_modal" style="background: url('static/img/city.svg'); border-radius: 25px;">
                <div class="left_">
                    <p class="title -bold title_modal">Получить предложение</p>
                    <input type="text" name="pk" id="pk" value="${pk}" hidden>
                    <label>
                        <input type="text" id="reserve_name" name="name" class="input space-10" placeholder="Ваше Имя Фамилия">
                    </label>
                    <label>
                        <input type="text" id="reserve_phone" name="phone" class="input space-10" placeholder="Номер телефона">
                    </label>
                    <button type="submit" class="button padding-20" id="send_reservation">Получить предложение</button>
                    <p class="info_text">
                        Нажимая кнопку “Получить предложение” Вы даете согласие на обработку своих персональных данных
                    </p>
                </div>
                <div class="right_reserve">
                    <div class="flex_right" >
                        <p class="title -bold title_modal" style="text-align: end; margin-bottom: 40px;">${price}</p>
                        <img src="${image}" style="max-width: 440px; max-height: 250px; object-fit: fill;" alt="Тёлка">
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
 `;


    document.body.insertAdjacentHTML("beforeend", modal);
    const closeBtn = document.getElementById("close_auto_reserve")
    const modalWindow = document.getElementById("#auto_reserve")
    const send_reservation = document.getElementById("send_reservation")

    closeBtn.addEventListener("click", function () {
        modal.remove();
        alert("close")
    });
    document.addEventListener("click", function (event) {
        if (!modalWindow.contains(event.target)) {
            modalWindow.style.display = "none";
            // refresh page
            location.reload();
        }
    });


    document.getElementById('close_auto_reserve').addEventListener('click', function () {
        document.getElementById('auto_reserve').style.display = 'none';
        // refresh page
        location.reload();
    });

    window.addEventListener('click', function (event) {
        if (event.target === document.getElementById('auto_reserve')) {
            document.getElementById('auto_reserve').style.display = 'none';
            // refresh page
            location.reload();
        }
    });

    document.getElementById('send_reservation').addEventListener('click', function () {
        var name = document.getElementById('reserve_name').value;
        var phone = document.getElementById('reserve_phone').value;
        var pk = document.getElementById('pk').value;
        $.ajax({
            url: '/credit/car_reservation',
            type: 'GET',
            data: {
                name: name,
                phone: phone,
                pk: pk
            },
            success: function (data) {
                send_reservation.onclick = function () {
                    document.getElementById('auto_reserve').style.display = 'none';
                    success_modal.style.display = "flex";
                }
            }
        });
    });
}


$('#send_callback').click(function () {
    // send callback
    var name = $('#name_callback').val();
    var phone = $('#phone_callback').val();
    $.ajax({
        url: '/credit/callback',
        type: 'GET',
        data: {
            name: name,
            phone: phone
        },
        success: function (data) {
            $('#name').val('');
            $('#phone').val('');
        }
    });
});

const send_competitively = document.getElementById("send_competitively");

send_competitively.onclick = function () {
    var phone = $('#competitively_phone').val();
    $.ajax({
        url: '/credit/competitively',
        type: 'GET',
        async: false,
        data: {
            phone: phone
        },
        success: function (data) {
            const modal_ = document.getElementById("success_modal");
            modal_.style.display = "flex";
        }
    });
    // clear input
    phone.val('');
    return false;
}

const question_btn = document.getElementById("question_btn");
question_btn.onclick = function () {
    var phone = $('#phone_question').val();
    var name = $('#name_question').val();
    $.ajax({
        url: '/credit/question',
        type: 'GET',
        data: {
            phone: phone,
            name: name
        },
        success: function (data) {
            success_modal.style.display = "flex";
        }
    });
}
