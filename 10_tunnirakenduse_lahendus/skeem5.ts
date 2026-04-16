abstract class AbstractResistor {
    protected u: number = 0;
    protected i: number = 0;
    protected p: number = 0;
    constructor(public name: string) { }
    abstract draw(g: any, startx: number, y: number): void;
    abstract getWidth(): number;
    abstract getHeight(): number;
    abstract getR(): number;
    getDataString(): string {
        return this.name + " " + this.getR() + " Ω";
    }
    calculate(): void {
        this.i = this.u / this.getR();
        this.p = this.u * this.i;
    }
    setU(u: number) {
        this.u = u;
        this.calculate();
    }
    getU(): number {
        return this.u;
    }
}

class Resistor extends AbstractResistor {
    constructor(name: string, protected r: number) {
        super(name);
    }
    draw(g: any, startx: number, y: number): void {
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
    getWidth(): number { return 100; }
    getHeight(): number { return 50; }
    getR() { return this.r; }
}

class SeriesConnection extends AbstractResistor {
    protected resistors: AbstractResistor[] = [];
    constructor(name: string) {
        super(name);
    }
    addResistor(r: AbstractResistor): void {
        this.resistors.push(r);
    }
    getWidth(): number {
        let sum = 0;
        for (let r of this.resistors) {
            sum += r.getWidth();
        }
        return sum + 10;
    }
    getHeight(): number {
        return Math.max(...this.resistors.map(r => r.getHeight())) + 25;
    }
    draw(g: any, startx: number, y: number) {
        let x = startx;
        g.beginPath();
        g.moveTo(x, y);
        x += 5;
        g.lineTo(x, y);
        g.stroke()
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
        g.stroke()
        g.fillText(this.getDataString() + " " + this.u.toFixed(3) + " V  " + this.i.toFixed(3) + " A  " + this.p.toFixed(3) + " W  ", startx + 10, y + this.getHeight() / 2);
    }
    getR(): number {
        let sum = 0;
        for (let resistor of this.resistors) {
            sum += resistor.getR();
        }
        return sum;
    }
    calculate(): void {
        super.calculate();
        for (let resistor of this.resistors) {
            resistor.setU(this.i * resistor.getR());
        }
    }
}
