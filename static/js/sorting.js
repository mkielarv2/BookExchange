window.addEventListener('load', () => {
    getLocalizations();
    getConditions();
    getCategories();
});

//funkcja szukająca według wpisanej kwerendy
const getSearchInput = () => {
    const input = document.querySelector("body > div.search_bar > input[type=text]");

    return input.value;
}

const sortString = () => {
    let string = '/offers';
    let category = '?category=' + getCategory();
    let condition = '&condition=' + SortConditions.selection;
    let localization = '&localization=' + getLocalization();
    let sort = '&sort=' + SortSettings.selection + SortOptions.selection;
    let title = '&title=' + getSearchInput();

    const stringFinished = string + category + condition + localization + sort + title;

    return stringFinished;
}