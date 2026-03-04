#Libisev keskmine
#1. Funktsioon kolme arvu keskmise leidmiseks ehk aritmeetilise keskmise leidmine.
def keskmine(a, b, c):
    return (a + b + c) / 3

print("Kolme arvu keskmine (2,4,6):", keskmine(2, 4, 6))

#2. Funktsioon massiivi libiseva keskmise leidmiseks ehk võetakse võimalikud 3 järjestikust arvu
#ning arvutatakse nende keskmine. 
def libisev_keskmine(arvud):
    keskmised = []
    for i in range(2, len(arvud)):
        keskmised.append(keskmine(arvud[i-2], arvud[i-1], arvud[i]))
    return keskmised

print("Libisev keskmine [2,4,6,8]:", libisev_keskmine([2, 4, 6, 8]))

#3. Klass
class LibisevKeskmine:
    def __init__(self):
        self.arvud = []
        self.keskmised = []

    def lisa_arv(self, arv):
        self.arvud.append(arv)
        n = len(self.arvud) #massiivis olevate arvude kogusumma

        if n >= 3: #tingimus - massiivis vähemalt 3 arvu
            uusKeskmine = keskmine(
                self.arvud[n-3],
                self.arvud[n-2],
                self.arvud[n-1]
            )
            self.keskmised.append(uusKeskmine)

    def leia_keskmised(self):
        return self.keskmised

lk = LibisevKeskmine()
lk.lisa_arv(2)
lk.lisa_arv(4)
lk.lisa_arv(6)
lk.lisa_arv(8)
lk.lisa_arv(16)

print("Libisev keskmine klassiga:", lk.leia_keskmised())
