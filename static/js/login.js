console.log("test login.js")

$('#loginSubmit').click(function (e) {
    e.preventDefault();

    console.log("button login pressed")

    // let button = $(this);
    // button.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>');

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
            console.log(data.redirect);
        },
        error: function (data) {
            let err = JSON.parse(data.responseText);
            //todo show error to user
            // $('.invalid-feedback').text(err.desc);
            // $('.login input[name=pass1], .login input[name=name]').addClass('is-invalid');
            // button.html('Zaloguj się');
        },
    });
});

$('#loginEmail, #loginPassword').on('keyup', function () {
    $('#loginEmail, #loginPassword').removeClass('is-invalid');
});