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
