"use strict";
class AbstractResistor {
    name;
    constructor(name) {
        this.name = name;
    }
}
class Resistor extends AbstractResistor {
    constructor(name) {
        super(name);
    }
    draw(g, startx, y) {
        g.beginPath();
        g.moveTo(startx, y);
        g.lineTo(startx + this.getWidth() / 4, y);
        g.rect(startx + this.getWidth() / 4, y - 10, this.getWidth() / 2, 20);
        g.fillText(this.name, startx + this.getWidth() / 4 + 1, y + 2);
        g.moveTo(startx + this.getWidth() * 3 / 4, y);
        g.lineTo(startx + this.getWidth(), y);
        g.stroke();
    }

    getWidth() {
        if (this.name.length > 10) {
            return 60;
        }
        return 50;
    }
}
