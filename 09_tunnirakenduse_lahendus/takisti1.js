"use strict";
class Resistor {
    r;
    g;
    constructor(r, g) {
        this.r = r;
        this.g = g;
        this.draw();
    }
    draw() {
        this.g.beginPath();
        this.g.rect(20, 10, 100, 30); //(asukoht x, y, laius, kõrgus)
        this.g.stroke();
        this.g.fillText("" + this.r, 30, 20);
    }
}
