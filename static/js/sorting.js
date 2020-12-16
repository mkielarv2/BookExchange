$(document).ready(function () {
    $.ajax({
        url: '/offers/localizations',
        type: 'GET',
        success: function (data) {
            let sortLocationSelect = $('#sortLocationSelect');
            for (let i = 0; i < data.length; i++) {
                sortLocationSelect.append("<option value=" + data[i].id + ">" + data[i].name + "</option>");
            }
        }
    });

    $.ajax({
        url: '/offers/categories',
        type: 'GET',
        success: function (data) {
            let categorySelect = $('#sortGenreSelect');
            for (let i = 0; i < data.length; i++) {
                categorySelect.append("<option value=" + data[i].id + ">" + data[i].name + "</option>");
            }
        }
    });

    $.ajax({
        url: '/offers/conditions',
        type: 'GET',
        success: function (data) {
            let conditionSelect = $('#sortConditionSelect')
            for (let i = 0; i < data.length; i++) {
                conditionSelect.append('<option value="' + data[i].id + '">' + data[i].condition + '</option>');
            }
        }
    });
})

$('#sortSubmitButton').click(function (e) {
    let genre = $("#sortGenreSelect option:selected").attr('value');
    let condition = $("#sortConditionSelect option:selected").attr('value');
    let location = $("#sortLocationSelect option:selected").attr('value');
    let attribute = $('#sortAttributeSelect option:selected').attr('value');
    let sort = (attribute === '') ? undefined : '' + $('#sortOrderSelect option:selected').attr('value') + attribute;

    filter = {
        category: (genre === '') ? undefined : genre,
        condition: (condition === '') ? undefined : condition,
        localization: (location === '') ? undefined : location,
        sort: sort
    }

    Shop.fetch()
    Sorting.hide()
});

$("#searchField").keyup(function () {
    filter = {
        title: $('#searchField').val()
    }

    Shop.fetch()
});


