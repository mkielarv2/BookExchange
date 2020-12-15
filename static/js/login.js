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
            $('#loginError').val('')
            Login.hide()
            console.log(data.id)
        },
        error: function (data) {
            console.log(data)
            let err = JSON.parse(data.responseText);
            $('#loginError').addClass('p_wrong');
        },
    });
});

$('#loginEmail, #loginPassword').on('keyup', function () {
    $('#loginEmail, #loginPassword').removeClass('input_wrong');
});