const getOffersList = (id) => {
    $.ajax({
        url: '/chat/getChats/' + id,
        type: 'GET',
        success: function (data) {
            for (let i = 0; i < data.length; i++) {
                const user_id = data[i].id;
                const user_name = data[i].username;

                var element = '<div data-id="' + user_id + '"><div>' + user_name + '</div><div></div></div>';

                $("div.user_messages > div.container").innerHTML += element;
            }
            LoadProductsOpeners();
        },
        error: function (data) {
        },
    });
}
