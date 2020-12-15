const getConditions = () => {
    const conditionSelect = document.querySelector(".sorting > .container > div:nth-child(12)");

    $.ajax({
        url: '/offers/conditions',
        type: 'GET',
        success: function (data) {
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                conditionSelect.innerHTML += '<div><div class="bullet" data-bullet="' + data[i].id + '"></div><div>' + data[i].condition + '</div></div>';
            }
            SortConditions.update(Bullets[1]);
        }
    });
}

const SortConditions = new Bullet(Bullets[1]);