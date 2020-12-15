$('#usernameField, #emailField, #passwordField, #repeatPasswordField').on('keyup', function () {
    $(this).removeClass('is-invalid');

    let usernameField = $('#usernameField');
    let emailField = $('#emailField');
    let passwordField = $('#passwordField');
    let repeatPasswordField = $('#repeatPasswordField');
    let submit = $('#registerSubmit')

    if (usernameField.val() !== '' && emailField.val() !== '' &&
        passwordField.val() !== '' && repeatPasswordField.val() !== '') {

        if (passwordField.val() === repeatPasswordField.val()) {
            submit.removeAttr('disabled');
            repeatPasswordField.removeClass('input_wrong');
        } else {
            submit.attr('disabled', 'disabled');
            repeatPasswordField.addClass('input_wrong');
        }
    } else {
        submit.attr('disabled', 'disabled');
    }

});

$('#registerSubmit').click(function (e) {
    e.preventDefault();

    let usernameField = $('#usernameField');
    let emailField = $('#emailField');
    let passwordField = $('#passwordField');
    let repeatPasswordField = $('#repeatPasswordField');

    let payload = {
        username: usernameField.val(),
        email: emailField.val(),
        password: passwordField.val(),
    };

    $.ajax({
        url: $("#register").attr("action"),
        type: 'POST',
        data: payload,
        dataType: 'json',
        success: function (data) {
            $('#genericRegisterError').html();

            usernameField.val('');
            emailField.val('');
            passwordField.val('');
            repeatPasswordField.val('');

            Register.hide();
            Login.show();
        },
        error: function (data) {
            let err = JSON.parse(data.responseText);
            $('#' + err.cause).addClass("input_wrong")
            $('#genericRegisterError').html(err.desc)
            $('#loginError').addClass('p_wrong');
            console.log(err)
        },
    });
});