class Bullet {
    constructor(obj) {
        this.bullets = obj.querySelectorAll('.bullet');
        this.selection = undefined;

        for (const i of this.bullets)
            i.addEventListener('click', (e) => this.set(e));
    }

    set(e) {
        const choice = e.target;

        for (const i of this.bullets) {
            if (i != choice)
                i.classList.remove('bullet_active');
            else {
                i.classList.add('bullet_active');
                this.selection = i.dataset['bullet'];
            }
        }
        Shop.fetch();
    }

    update(obj) {
        this.bullets = obj.querySelectorAll('.bullet');
        this.selection = undefined;

        for (const i of this.bullets)
            i.addEventListener('click', (e) => this.set(e));
    }
}

//chwycenie obiektów
const Bullets = document.querySelectorAll('.bullets');
//utworzenie obiektów

const SortSettings = new Bullet(Bullets[0]);
const SortOptions = new Bullet(Bullets[2]);