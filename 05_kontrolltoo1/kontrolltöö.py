#Harmooniline keskmine
#1. Koosta funktsioon, mille sisendiks on kahe kilomeetripikkuse lõigu läbimise kiirused (km/h), väljundiks nende kahe kilomeetri läbimise keskmine kiirus.
#2. Funktsioonile antakse ette kilomeetripikkuste lõikude läbimiste keskmised kiirused kogumina (km/h). Väljasta kogu selle tee läbimise keskmine kiirus.
#3. Koosta klass, millele saab lisada kilomeetritepikkuste lõikude keskmisi kiirusi. Kuva joonisel sõiduki asukoht iga minuti järel (väljund võib olla teksti kujul).


#Arvutan kahe kilomeetrilõigu keskmise kiiruse harmoonilise kiiruse abil ehk sama teepikkus, erinev kiirus ehk ka erinev aeg teepikkuse läbimiseks.

def harmooniline_keskmine(v1, v2):
    return 2/ ((1/v1) + (1/v2))

print("Kahe lõigu keskmine kiirus on", harmooniline_keskmine(70, 90))
    
   
#Annan funktsioonile sisendiks massiivi/listi kiirustega ning arvutan nende põhjal kogu tee keskmise kiiruse.

def keskmine_kiirus(kiirused):
    summa = 0
    for v in kiirused:
        summa += 1/v #summa = summa + 1/v
        
    return len(kiirused) / summa

        
kiirused = [50, 70, 90]
print("Kogu tee läbimise keskmine kiirus on", keskmine_kiirus(kiirused))
        

#Klassi saab lisada erinevate teelõikude keskmisi kiirusi ning arvutab iga minuti järel sõiduki läbitud vahemaa.

class Soiduk:
    def __init__(self):
        self.kiirused = []

    def lisa_kiirus(self, v):
        self.kiirused.append(v)
      
        
    def kuva_asukoht(self):
        asukoht = 0
        minut = 0
        
        #mitu minutit kulub ühe kilomeetri läbimiseks
        for kiirus in self.kiirused:
            km_jääk = 1 #iga lõik 1km pikkusega
            while km_jääk > 0: #et tsükkel töötaks, kuni lõik täielikult läbitud
                minut += 1 #suurendab minuteid iga korraga kui tsükkel läbitud
                km_liikumine = kiirus / 60 #km minutisse teisendus
                asukoht += km_liikumine #igal minutil läbitud vahemaa lisamine
                km_jääk -= km_liikumine #järelejäänud lõigu km vähendamine
                print("Minut", minut, "- asukoht", round(asukoht, 2), "km")
                
                
        

auto = Soiduk()
auto.lisa_kiirus(30) #lõik kiirusega 30km/h
auto.lisa_kiirus(70)
auto.lisa_kiirus(100)
auto.lisa_kiirus(110)

auto.kuva_asukoht()
