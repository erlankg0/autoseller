
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

