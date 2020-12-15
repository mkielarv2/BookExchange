class Tab {
    constructor(tab, func) {
        this.tab = tab;
        this.htmlClass = 'tabIsShown';
        this.closer = tab.querySelector('.closer');

        this.closer.addEventListener('click', () => this.hide());

        if (typeof func === 'function')
            this.func = func;
        else
            this.func = () => { };
    }

    show(e) {
        // jeśli istnieje event, to zbiera dane
        if (typeof e === 'object') {
            inboxid = e.target.dataset['data'];

            console.log(inboxid);
        }
        Nav.hide()
        this.tab.classList.add(this.htmlClass);
        this.func();
    }

    hide() {
        this.tab.classList.remove(this.htmlClass);
    }

}

//funkcje wywołujące się po otwarciu któregoś tab'a
var inboxid = undefined;
const inbox_addListeners = () => {
    const Openers = document.querySelectorAll("[data-data]")

    for (const opener of Openers)
        opener.addEventListener('click', (e) => SeeMessages.show(e))
}
//Zbieranie wszystkich okienek w jeden obiekt
const Tabs = document.querySelectorAll('.tab');

//Nowe obiekty na bazie klasy
const Sorting = new Tab(Tabs[0]);
const Product = new Tab(Tabs[1]);
const AddProduct = new Tab(Tabs[4]);
const CheckProducts = new Tab(Tabs[5]);
const CheckMessages = new Tab(Tabs[6], inbox_addListeners);
const SeeMessages = new Tab(Tabs[7]);

//EventListenery
document.querySelector("div.search_bar > div").addEventListener('click', () => Sorting.show());
document.querySelector("div.shop").addEventListener('click', () => Product.show());
document.querySelector("nav > div:nth-child(2) > div:nth-child(7) > div").addEventListener('click', () => AddProduct.show());
document.querySelector("nav > div:nth-child(2) > div:nth-child(8) > div").addEventListener('click', () => CheckProducts.show());
document.querySelector("nav > div:nth-child(2) > div:nth-child(9) > div").addEventListener('click', (e) => CheckMessages.show());
// document.querySelector(".product_messages_owner > .container > div > div:nth-child(2) > .product_actions > div").addEventListener('click', () => SeeMessages.show())
