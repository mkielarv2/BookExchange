$('.register button').click(function (e) {
    e.preventDefault();

    let button = $(this);
    button.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>');

    let emailField = $('.register input[name=name]');
    let passwordField = $('.register input[name=pass1]');

    let payload = {
        email: emailField.val(),
        password: passwordField.val(),
    };

    $.ajax({
        url: '{% url 'apiLogin' %}',
        type: 'POST',
        data: payload,
        dataType: 'json',
        success: function (data) {
            console.log(data.redirect);
            window.location = data.redirect;
        },
        error: function (data) {
            let err = JSON.parse(data.responseText);
            $('.invalid-feedback').text(err.desc);
            $('.register input[name=pass1], .register input[name=name]').addClass('is-invalid');
            button.html('Submit');
        },
    });
});

$('.register input[name=name], .register input[name=pass1]').on('keyup', function () {
    $('.register input[name=name], .register input[name=pass1]').removeClass('is-invalid');
});