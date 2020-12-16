﻿
const productLoad = (e) => {
    const id = e.target.dataset['id'];

    console.log(id);
    $.ajax({
        url: '/offers/' + id,
        type: 'GET',
        success: function (data) {
            let title = data.title;
            let author = data.author;

            let template = '<div class="photo">';

            let imgSrc;
            let j = 0;
            while (data.images[j] != null) {
                imgSrc = data.images[j];
                template += '<img src="' + imgSrc + '" alt="dupsko">';
                j++;
            }

            template += '</div><div class="bar"><div>' + title + '</div><div>' + author + '</div></div><div class="info"><div>Wystawone przez: <span style="font-weight: bold">' + username + '</span></div><hr/><div><p>Opis wystawiającego</p><p>' + description + '</p></div></div>';

            $('.product.tab > .container').innerHTML += template;
        },
        error: function (data) {
        },
    });
}

