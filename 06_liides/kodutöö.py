#liides
from abc import ABC, abstractmethod

class Calculation(ABC):

    @abstractmethod
    def calculate(self, a, b):
        pass


class Add(Calculation):
    def calculate(self, a, b):
        return a + b


class Multiply(Calculation):
    def calculate(self, a, b):
        return a * b


class Subtract(Calculation):
    def calculate(self, a, b):
        return a - b


ops = [Add(), Multiply(), Subtract()]

for op in ops:
    print(op.calculate(6, 5))


#Abstraktne klass Calculation, mis toimib liidesena.
#See sisaldab meetodit calculate(a, b), mida kõik tehete klassid peavad realiseerima.
#Seejärel tegin 3 klassi - Add, Multiply ja Subtract, mis pärivad Calculation klassi ja teevad vastava arvutuse.
#Lõpuks panin nende objektid listi ja kasutasin tsüklit, et kutsuda calculate meetodit.
