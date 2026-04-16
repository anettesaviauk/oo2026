abstract class AbstractResistor {
    constructor(public name: string) { }
    abstract draw(g: any, startx: number, y: number): void;
    abstract getWidth(): number;
}

class Resistor extends AbstractResistor {
    constructor(name: string) {
        super(name);
    }
    draw(g: any, startx: number, y: number): void {
        g.beginPath();
        g.moveTo(startx, y);
        g.lineTo(startx + this.getWidth() / 4, y);
        g.rect(startx + this.getWidth() / 4, y - 10, this.getWidth() / 2, 20);
        g.fillText(this.name, startx + this.getWidth() / 4 + 1, y + 2);
        g.moveTo(startx + this.getWidth() * 3 / 4, y);
        g.lineTo(startx + this.getWidth(), y);
        g.stroke();

    }
    getWidth(): number { return 50; }
}
