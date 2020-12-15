const getLocalizations = () => {
    const localizationSelect = document.querySelector('.sorting [name=localization]');

    $.ajax({
        url: '/offers/localizations',
        type: 'GET',
        success: function (data) {
            for (let i = 0; i < data.length; i++) {
                localizationSelect.append("<option value=" + data[i].id + ">" + data[i].name + "</option>")
            }
        }
    });


}

const getLocalization = () => {
    return document.querySelector('.sorting [name=localization]').value;
}