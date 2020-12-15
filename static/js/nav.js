const Nav = {
  tab: document.querySelector('nav'),
  bg: document.querySelector("body > nav > div:nth-child(3)"),

  show()
  {
    const { tab, bg } = this;

    this.tab.classList.add('nav_shown');
    setTimeout(() => { bg.classList.add('black_bg_shown') }, 500)
  },

  hide()
  {
    const { tab, bg } = this;
    bg.classList.remove('black_bg_shown')

    setTimeout(() => { this.tab.classList.remove('nav_shown'); }, 200)
  },
}

// event listenery dla akcji
document.querySelector('header').addEventListener('click', () => Nav.show());
Nav.bg.addEventListener('click', () => Nav.hide());
