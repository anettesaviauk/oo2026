//npm install typescript
//npx tsc jada1.ts
class Resistor {
    readonly height: number = 30
    readonly width: number = 60;
    constructor(protected r: number) {
    }
    getResistance() { return this.r; }
    draw(g: any, startx: number, y: number) {
        g.clearRect(startx, y - this.height / 2, this.width, this.height);
        g.beginPath();
        g.moveTo(startx, y);
        g.lineTo(startx + this.width / 4, y);
        g.rect(startx + this.width / 4, y - 10, this.width / 2, 20);
        g.fillText(this.r + " Ω", startx + this.width / 4 + 1, y + 2);
        g.moveTo(startx + this.width * 3 / 4, y);
        g.lineTo(startx + this.width, y);
        g.stroke();
    }
    getWidth() { return this.width; }
}

class SeriesCircuit {
    protected resistors: Resistor[] = [];
    protected width: number = 0;
    constructor(protected g: any, protected startx: number, protected y: number) {
    }
    push(r: Resistor) {
        this.resistors.push(r);
        this.width += r.getWidth();
        this.draw();
    }
    draw() {
        if (this.resistors.length == 0) { return; }
        let x = this.startx;
        for (let i = 0; i < this.resistors.length; i++) {
            this.resistors[i].draw(this.g, x, this.y);
            x += this.resistors[i].getWidth();
        }
    }
}
