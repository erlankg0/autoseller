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
