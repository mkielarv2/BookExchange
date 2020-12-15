$('.register input[name=name], .register input[name=email], .register input[name=pass1], .register input[name=pass2]').on('keyup', function () {
    $(this).removeClass('is-invalid');

    let usernameField = $('.register input[name=name]');
    let emailField = $('.register input[name=email]');
    let passwordField = $('.register input[name=pass1]');
    let repeatPasswordField = $('.register input[name=pass2]');
    let submit = $('.register button');

    if (usernameField.val() !== '' && emailField.val() !== '' &&
        passwordField.val() !== '' && repeatPasswordField.val() !== '') {

        if (passwordField.val() === repeatPasswordField.val()) {
            submit.removeAttr('disabled');
            repeatPasswordField.removeClass('is-invalid');
        } else {
            submit.attr('disabled', 'disabled');
            repeatPasswordField.addClass('is-invalid');
        }
    } else {
        submit.attr('disabled', 'disabled');
    }

});

$('.register button').click(function (e) {
    e.preventDefault();
    let button = $(this);
    button.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>');

    let usernameField = $('.register input[name=name]');
    let emailField = $('.register input[name=email]');
    let passwordField = $('.register input[name=pass1]');

    let payload = {
        username: usernameField.val(),
        email: emailField.val(),
        password: passwordField.val(),
    };

    $.ajax({
        url: '{% url 'apiRegister' %}',
        type: 'POST',
        data: payload,
        dataType: 'json',
        success: function (data) {
            $('#container')
                .html('<div class="card border-success" id="formCard">\n    <div class="card-body">\n        <div class="card-body text-success">\n            <h5 class="card-title">Success</h5>\n            <p class="card-text">Registration completed successfully!</p>\n            <a href="{% url 'login' %}"><button type="button" class="btn btn-primary btn-block">Login</button></a>\n        </div>\n    </div>\n</div>');
        },
        error: function (data) {
            let err = JSON.parse(data.responseText);
            $('#' + err.cause + 'Feedback').text(err.desc);
            $('#' + err.cause).addClass('is-invalid');
            button.html('Submit');
        },
    });
});