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
            productLoad(e);
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
const LoadOrderMessages = {
    addListeners() {
        const Openers = document.querySelectorAll("[data-data]")

        for (const opener of Openers)
            opener.addEventListener('click', (e) => SeeMessages.show(e))
    }
}
const LoadProductsOpeners = {
    addListeners() {
        const Openers = document.querySelectorAll("[data-id]")

        for (const opener of Openers)
            opener.addEventListener('click', (e) => Product.show(e))
    }
}

//Zbieranie wszystkich okienek w jeden obiekt
const Tabs = document.querySelectorAll('.tab');
const funcProductShow = (e) => {
    Product.show(e);
}
//Nowe obiekty na bazie klasy
const Sorting = new Tab(Tabs[0]);
const Product = new Tab(Tabs[1], LoadProductsOpeners.addListeners);
const Register = new Tab(Tabs[2]);
const Login = new Tab(Tabs[3]);
const AddProduct = new Tab(Tabs[4]);
const CheckProducts = new Tab(Tabs[5]);
const CheckMessages = new Tab(Tabs[6], LoadOrderMessages.addListeners);
const SeeMessages = new Tab(Tabs[7]);


//EventListenery
document.querySelector("div.search_bar > div").addEventListener('click', () => Sorting.show());
document.querySelector("div.shop").addEventListener('click', () => Product.show());
document.querySelector(".add_products").addEventListener('click', () => AddProduct.show());
document.querySelector(".manage_products").addEventListener('click', () => CheckProducts.show());
document.querySelector(".check_messages").addEventListener('click', () => CheckMessages.show());
document.querySelector("body > nav > div:nth-child(1) > div:nth-child(3)").addEventListener('click', () => Register.show());
document.querySelector("body > nav > div:nth-child(1) > div:nth-child(4)").addEventListener('click', () => Login.show());
// document.querySelector(".product_messages_owner > .container > div > div:nth-child(2) > .product_actions > div").addEventListener('click', () => SeeMessages.show())
