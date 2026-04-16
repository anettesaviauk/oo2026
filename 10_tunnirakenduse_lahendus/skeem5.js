"use strict";
class AbstractResistor {
    name;
    u = 0;
    i = 0;
    p = 0;
    constructor(name) {
        this.name = name;
    }
    getDataString() {
        return this.name + " " + this.getR() + " Ω";
    }
    calculate() {
        this.i = this.u / this.getR();
        this.p = this.u * this.i;
    }
    setU(u) {
        this.u = u;
        this.calculate();
    }
    getU() {
        return this.u;
    }
}
class Resistor extends AbstractResistor {
    r;
    constructor(name, r) {
        super(name);
        this.r = r;
    }
    draw(g, startx, y) {
        g.beginPath();
        g.moveTo(startx, y);
        g.lineTo(startx + this.getWidth() / 4, y);
        g.rect(startx + this.getWidth() / 4, y - 10, this.getWidth() / 2, 20);
        g.fillText(this.getDataString(), startx + this.getWidth() / 4 + 1, y + 2);
        g.moveTo(startx + this.getWidth() * 3 / 4, y);
        g.lineTo(startx + this.getWidth(), y);
        g.stroke();
        g.fillText(this.u.toFixed(3) + " V, " + this.i.toFixed(3) + " A", startx + this.getWidth() / 4, y - this.getHeight() / 4 - 2);
        g.fillText(this.p.toFixed(3) + " W", startx + this.getWidth() / 4, y + this.getHeight() / 2 - 6);
    }
    getWidth() { return 100; }
    getHeight() { return 50; }
    getR() { return this.r; }
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
        return Math.max(...this.resistors.map(r => r.getHeight())) + 25;
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
        g.fillText(this.getDataString() + " " + this.u.toFixed(3) + " V  " + this.i.toFixed(3) + " A  " + this.p.toFixed(3) + " W  ", startx + 10, y + this.getHeight() / 2);
    }
    getR() {
        let sum = 0;
        for (let resistor of this.resistors) {
            sum += resistor.getR();
        }
        return sum;
    }
    calculate() {
        super.calculate();
        for (let resistor of this.resistors) {
            resistor.setU(this.i * resistor.getR());
        }
    }
}
