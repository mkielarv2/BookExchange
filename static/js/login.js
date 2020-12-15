console.log("test login.js")

$('#loginSubmit').click(function (e) {
    e.preventDefault();

    console.log("button login pressed")

    let emailField = $('#loginEmail');
    let passwordField = $('#loginPassword');

    let payload = {
        email: emailField.val(),
        password: passwordField.val(),
    };

    $.ajax({
        url: $('#login').attr("action"),
        type: 'POST',
        data: payload,
        dataType: 'json',
        success: function (data) {
            Login.hide()
        },
        error: function (data) {
            let err = JSON.parse(data.responseText);
            $('.invalid-feedback').text(err.desc);
            $('#loginEmail, #loginPassword').addClass('input_wrong');
        },
    });
});

$('#loginEmail, #loginPassword').on('keyup', function () {
    $('#loginEmail, #loginPassword').removeClass('is-invalid');
});