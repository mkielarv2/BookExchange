class Tab {
  constructor(tab, smallTab)
  {
    this.tab = tab;
    this.htmlClass = 'tabIsShown';
    this.closer = tab.querySelector('.closer');

    this.closer.addEventListener('click', () => this.hide());
  }

  show()
  {
    this.tab.classList.add(this.htmlClass);
  }

  hide()
  {
    this.tab.classList.remove(this.htmlClass);
  }
}

//Zbieranie wszystkich okienek w jeden obiekt
const Tabs = document.querySelectorAll('.tab');

//Nowe obiekty na bazie klasy
const Product = new Tab(Tabs[0]);

//EventListenery
document.querySelector("body > div.shop").addEventListener('click', () => { Product.show() });
