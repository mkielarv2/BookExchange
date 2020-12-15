console.log("test login.js")

const loggedIn = () => {
    const unloggedNav = document.querySelector("body > nav > div:nth-child(1)");
    const loggedNav = document.querySelector("body > nav > div:nth-child(2)");

    unloggedNav.classList.add('nav_displayed');
    loggedNav.classList.remove('nav_displayed');
}   

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
            console.log(data.id)
            loggedIn();
        },
        error: function (data) {
            console.log(data)
            let err = JSON.parse(data.responseText);
            $('#loginEmail, #loginPassword').addClass('input_wrong');
            $('#loginError').addClass('p_wrong');
        },
    });
});

$('#loginEmail, #loginPassword').on('keyup', function () {
    $('#loginEmail, #loginPassword').removeClass('input_wrong');
});