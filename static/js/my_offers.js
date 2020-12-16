$('#my_offers').click(function () {
    const id = $('#my_id').val();
    console.log('XD');
    console.log(id);
    $.ajax({
        url: '/offers/user/' + id,
        type: 'GET',
        success: function (data) {
            $('#productContainer2').html('');
            for (let i = 0; i < data.length; i++) {
                let imgSrc = data[i].images[0] || "https://via.placeholder.com/600x500";
                let id = data[i].id;
                let title = data[i].title;
                let author = data[i].author;
                let condition = data[i].condition.condition;
                let category = data[i].category.name;
                let localization = data[i].location.name;

                let template = '<div data-id="' + id + '"><div class="product_image" ><img src="' + imgSrc + '" alt=""></div><div class="product_info"><div>' + author + '</div><div>' + title + '</div><div>' + condition + '</div><div>' + category + '</div><div>' + localization + '</div></div>';

                template += '<button onclick="delete_my_offer('+ id +')">Aborcjuj mnie</button>'

                $('#productContainer2').append(template);
            }
        },
        error: function (data) {
        },
    });
})

function delete_my_offer(id) {
    $.ajax({
        url: '/offers/delete/' + id,
        type: 'DELETE',
        success: function (data) {
            console.log('gut');
            window.location.reload()
        },
        error: function (data) {
            console.log('nicht gut');
        },
    });
}