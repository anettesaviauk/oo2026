# Jalgratta tulede patarei pinge on 4,5 volti. Esituld läbiv vool 1 amper. Milline on esitule võimsus? Milline on esitule takistus?
# Sama jalgratta tagatuld läbib vool 0,5 amprit. Milline on tagatule võimsus? Milline on tagatule takistus?
# Milline on kahest rööbiti ühendatud jalgrattatulest koosneva lampide süsteemi võimsus kokku 4,5 voldi juures? Milline on selle lampide süsteemi kogutakistus oomides?

class Resistor:
    def __init__(self, u, i):
        self.u = u  # pinge (V)
        self.i = i  # vool (A)

    def getPower(self):
        return self.u * self.i   # võimsus P = U * I

    def getResistance(self):
        return self.u / self.i   # takistus R = U / I


class ParallelCircuit:
    def __init__(self):
        self.components = []

    def addComponent(self, r):
        self.components.append(r)

    def getTotalCurrent(self): # arvutan kogu voolu
        total = 0 # algväärtus
        for c in self.components:
            total += c.i # rööbiti ühenduses voolud liituvad
        return total # tagastab koguvoolu

    def getTotalPower(self): # arvutan kogu süsteemi võimsuse
        total = 0
        for c in self.components: # liidan kõikide lampide võimsused
            total += c.getPower()
        return total # tagastab koguvõimsuse

    def getTotalResistance(self): # arvutan kogu süsteemi takistuse
        if len(self.components) == 0:
            return 0 # kui pole elemente, siis tagastab 0
        u = self.components[0].u # võtab pinge, mis on kõigil sama rööbiti ühenduses
        return u / self.getTotalCurrent() # R = U / I


# Esitule andmed 
front = Resistor(4.5, 1)

# Tagatule andmed
rear = Resistor(4.5, 0.5)

print("Esituli:")
print("Võimsus:", front.getPower(), "W")
print("Takistus:", front.getResistance(), "Ohmi")

print("\nTagatuli:")
print("Võimsus:", rear.getPower(), "W")
print("Takistus:", rear.getResistance(), "Ohmi")


# Loon süsteemi rööpühenduseks ning lisan mõlemad tuled 
lights = ParallelCircuit()
lights.addComponent(front)
lights.addComponent(rear)

print("\nRööbiti süsteem:")
print("Koguvõimsus:", lights.getTotalPower(), "W")
print("Kogutakistus:", lights.getTotalResistance(), "Ohmi")
