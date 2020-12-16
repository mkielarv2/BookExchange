
const productLoad = (e) => {
    const id = e.target.parentNode.parentNode.dataset['id'];
    console.log(e.target.parentNode.parentNode.dataset['id']);
    console.log(id);
    $.ajax({
        url: '/offers/' + id,
        type: 'GET',
        success: function (data) {
            $('#productContainer').html('')
            let title = data.title;
            let author = data.author;
            let username = data.user.username;
            let description = data.description;

            let template = '<div class="photo">';

            let imgSrc;
            let j = 0;
            while (data.images[j] != null) {
                imgSrc = data.images[j];
                template += '<img src="' + imgSrc + '" alt="sdsd">';
                j++;
            }

            template += '</div><div class="bar"><div>' + title + '</div><div>' + author + '</div></div><div class="info"><div>Wystawone przez: <span style="font-weight: bold">' + username + '</span></div><hr/><div><p>Opis wystawiającego</p><p>' + description + '</p></div></div>';


            $('#productContainer').append(template);
        },
        error: function (data) {
        },
    });
}

