const getCategories = () => {
    const categorySelect = document.querySelector('.sorting [name=genre]');

    $.ajax({
        url: '/offers/categories',
        type: 'GET',
        success: function (data) {
            for (let i = 0; i < data.length; i++) {
                categorySelect.append("<option value=" + data[i].id + ">" + data[i].name + "</option>")
            }
        }
    });


}

const getCategory = () => {
    return document.querySelector('.sorting [name=genre]').value;
}