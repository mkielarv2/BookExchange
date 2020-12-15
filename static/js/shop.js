window.addEventListener('load', () => {
    Shop.fetch()
});
const Shop = {
    fetch() {
        const string = sortString();
            
        $.ajax({
            url: string,
            type: 'GET',
            success: function (data) {
                for (let i = 0; i < data.length; i++) {
                    console.log(data[i])
                    let imgSrc = data[i].images[0] || "https://via.placeholder.com/600x500";
                    let id = data[i].id;
                    let title = data[i].title;
                    let author = data[i].author;
                    let condition = data[i].condition;
                    let category = data[i].category;

                    let template = '<div data-data="' + id + '"><div class="product_image" ><img src="' + imgSrc + '" alt=""></div><div class="product_info"><div>' + author + '</div><div>' + title + '</div><div>' + condition + '</div><div>' + category + '</div><div>' + localization + '</div></div>';

                    $(".shop").innerHTML += template;
                }
                LoadProductsOpeners();
            },
            error: function (data) {
            },
        });
    }
}