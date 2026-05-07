# Pane näide käima, muuda andmeid.
# Koosta jadaühenduse klassist kaks eksemplari, katseta tulemusi mitmesuguse pinge korral. Võrdle käsitsi arvutatud tulemusi programmi pakutuga.
# Lisa jadaühenduse klassile käsklus kogu eralduva võimsuse leidmiseks.
# Väljasta jadaühenduse takistitest suurim takistus
# Väljasta jadaühendusest suurim ühele takistile langev pinge 5-voldise kogupinge juures
# Väljasta jadaühendusest suurim ühelt takistilt eralduv võimsus 5-voldise kogupinge juures


class Resistor:
    def __init__(self, r, maxN):
        self.r = r              # takistus (oomides)
        self.maxN = maxN        # max võimsus (W)

    def getCurrent(self, u):
        return u / self.r       # I = U / R

    def getPower(self, u):
        return u**2 / self.r    # P = U ruudus / R

    def isVoltageAllowed(self, u):
        return self.getPower(u) <= self.maxN


class SeriesCircuit:
    def __init__(self):
        self.resistors = []

    def addResistor(self, r):
        self.resistors.append(r)

    def getTotalResistance(self):
        total = 0
        for t in self.resistors:
            total += t.r
        return total

    def getTotalPower(self, u):
        total = 0
        current = u / self.getTotalResistance()
        for t in self.resistors:
            voltage = current * t.r
            total += t.getPower(voltage)
        return total

    def getMaxResistance(self):
        maxRes = 0
        for t in self.resistors:
            if t.r > maxRes:
                maxRes = t.r
        return maxRes

    def getMaxVoltage(self, u):
        current = u / self.getTotalResistance()
        maxVoltage = 0
        for t in self.resistors:
            voltage = current * t.r
            if voltage > maxVoltage:
                maxVoltage = voltage
        return maxVoltage

    def getMaxPower(self, u):
        current = u / self.getTotalResistance()
        maxPower = 0
        for t in self.resistors:
            voltage = current * t.r
            power = t.getPower(voltage)
            if power > maxPower:
                maxPower = power
        return maxPower


r1 = SeriesCircuit()
r1.addResistor(Resistor(100, 0.25))
r1.addResistor(Resistor(200, 0.25))
r1.addResistor(Resistor(1000, 100))

r2 = SeriesCircuit()
r2.addResistor(Resistor(50, 0.5))
r2.addResistor(Resistor(150, 0.5))
r2.addResistor(Resistor(300, 1))

print("Jadaühendus 1")
print("Kogutakistus:", r1.getTotalResistance(), "Ohmi")
print("Koguvõimsus:", round(r1.getTotalPower(5), 3), "W")
print("Suurim takistus:", r1.getMaxResistance(), "Ohmi")
print("Suurim pinge takistil:", round(r1.getMaxVoltage(5), 3), "V")
print("Suurim võimsus takistil:", round(r1.getMaxPower(5), 5), "W")

print("Jadaühendus 2")
print("Kogutakistus:", r2.getTotalResistance(), "Ohmi")
print("Koguvõimsus:", round(r2.getTotalPower(5), 3), "W")
print("Suurim takistus:", r2.getMaxResistance(), "Ohmi")
print("Suurim pinge takistil:", round(r2.getMaxVoltage(5), 3), "V")
print("Suurim võimsus takistil:", round(r2.getMaxPower(5), 5), "W")
