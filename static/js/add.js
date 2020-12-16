$(document).ready(function () {
    let categorySelect = $("#createGenreSelect")
    let locationSelect = $("#createLocationSelect")
    let conditionSelect = $("#createConditionSelect")

    $.ajax({
        url: '/offers/categories',
        type: 'GET',
        success: function (data) {
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                categorySelect.append("<option data-meta=\"" + data[i].id + "\">" + data[i].name + "</option>")
            }
        }
    });

    $.ajax({
        url: '/offers/localizations',
        type: 'GET',
        success: function (data) {
            for (let i = 0; i < data.length; i++) {
                locationSelect.append("<option data-meta=\"" + data[i].id + "\">" + data[i].name + "</option>")
            }
        }
    });

    $.ajax({
        url: '/offers/conditions',
        type: 'GET',
        success: function (data) {
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                conditionSelect.append("<option data-meta=\"" + data[i].id + "\">" + data[i].condition + "</option>")
            }
        }
    });
});

$("#createSubmit").click(function (e) {
    console.log("asdasdasd??????")
    let button = $(this);
    button.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>');

    let titleField = $("#createTitle")
    let authorField = $("#createAuthor")
    let categorySelect = $("#createGenreSelect")
    let locationSelect = $("#createLocationSelect")
    let conditionSelect = $("#createConditionSelect")
    let descriptionField = $("#createDescription")
    let fileInput = $("#fileInput")

    let payload = {
        title: titleField.val(),
        author: authorField.val(),
        category: categorySelect.children("option:selected").attr("data-meta"),
        location: locationSelect.children("option:selected").attr("data-meta"),
        condition: conditionSelect.children("option:selected").attr("data-meta"),
        description: descriptionField.val()
    }

    let fd = new FormData();
    let files = fileInput[0].files

    for (let i = 0; i < files.length; i++) {
        fd.append('file' + i, files[i])
    }

    fd.append('payload', JSON.stringify(payload))

    $.ajax({
        url: '/offers/create',
        type: 'POST',
        data: fd,
        file: fileInput.files,
        contentType: false,
        processData: false,
        success: function (data) {
            window.location.reload()
        },
        error: function (data) {
            alert("Się popsuło ¯\\_(ツ)_/¯")
        },
    });
});