const getConditions = () => {
    const conditionSelect = document.querySelector("body > div.sorting.tab.tabIsShown > div.container > div:nth-child(9)");

    $.ajax({
        url: '/offers/conditions',
        type: 'GET',
        success: function (data) {
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                conditionSelect.append('<div><div class="bullet" data-bullet="' + data[i].id + '"></div><div>' + data[i].condition + '</div></div>')
            }
            const SortConditions = new Bullet(Bullets[1]);
        }
    });
}