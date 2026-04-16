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
    getWidth() { return 50; }
    getHeight() { return 30; }
}
class SeriesConnection extends AbstractResistor {
    resistors = [];
    constructor(name) {
        super(name);
    }
    addResistor(r) {
        this.resistors.push(r);
    }
    getWidth() {
        let sum = 0;
        for (let r of this.resistors) {
            sum += r.getWidth();
        }
        return sum + 10;
    }
    getHeight() {
        return Math.max(...this.resistors.map(r => r.getHeight())) + 20;
    }
    draw(g, startx, y) {
        let x = startx;
        g.beginPath();
        g.moveTo(x, y);
        x += 5;
        g.lineTo(x, y);
        g.stroke();
        let areaStartX = x;
        for (let i = 0; i < this.resistors.length; i++) {
            this.resistors[i].draw(g, x, y);
            x += this.resistors[i].getWidth();
        }
        g.strokeStyle = "lightgray";
        g.beginPath();
        g.rect(areaStartX, y - this.getHeight() / 2, x - areaStartX, this.getHeight());
        g.stroke();
        g.strokeStyle = "black";
        g.beginPath();
        g.moveTo(x, y);
        x += 5;
        g.lineTo(x, y);
        g.stroke();
        g.fillText(this.name, startx + this.getWidth() / 2 - 10, y + this.getHeight() / 2);
    }
}
