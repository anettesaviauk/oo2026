# Salat
# 1. Koosta klass toiduaine tarbeks (nimetus, valkude, rasvade ja süsivesikute protsent). Protsent kokku ei saa ületada 100 -
# muidu antakse veateade. Loo mõni toiduaine (nt. kartul, hapukoor, vorst). Andmed saab nt (https://tka.nutridata.ee/et/).
# Sealt kartul (https://tka.nutridata.ee/et/toidud/280). Kontrolli toiduaine loomist automaattestiga.
# 2. Koosta klass toidukomponendi tarbeks (kogus, viit toiduainele). Loo mõned toidukomponendid (nt. 100 g kartuleid, 
# 30 g hapukoort, 50 g vorsti). Lisa toidukomponendile käsklus selle sees leiduva rasvakoguse arvutamiseks. Kontrolli 
# tulemust automaattestiga.
# Koosta klass toidu jaoks (nimetus, toidukomponendid). Toidule käsklused küsimaks sisalduvate valkude, rasvade ja 
# süsivesikute kogust. Loo retsepti järgi toit (nt. kartulisalat), küsi salatis leiduvate toitainete kogused. 
# Koosta rakendus, kus näidatakse valitud toidu etteantud koguse (nt. 5 kg kartulisalati) jaoks vajalikud toiduained.

class Toiduaine:
    def __init__(self, nimetus, valgud, rasvad, süsivesikud):
        kokku = valgud + rasvad + süsivesikud 
        if kokku > 100:
            raise ValueError("Toitainete protsent kokku ei saa ületada 100%")
        
        self.nimetus = nimetus
        self.valgud = valgud
        self.rasvad = rasvad
        self.süsivesikud = süsivesikud

    def __str__(self):
        return f"{self.nimetus}: valgud {self.valgud}%, rasvad {self.rasvad}%, süsivesikud {self.süsivesikud}%"
    
kartul = Toiduaine("Kartul", 1.9, 0.1, 15.5)
hapukoor = Toiduaine("Hapukoor", 3.3, 21.5, 3.8)
vorst = Toiduaine("Vorst", 25, 35, 1)
print(kartul)


class Toidukomponent:
    def __init__(self, kogus, toiduaine):
        self.kogus = kogus
        self.toiduaine = toiduaine

    def rasva_kogus(self):
        return self.kogus * self.toiduaine.rasvad / 100 
    
kartuli_komponent = Toidukomponent(100, kartul)
hapukoore_komponent = Toidukomponent(30, hapukoor)
vorsti_komponent = Toidukomponent(50, vorst)

print("Rasva kogus kartulis:", kartuli_komponent.rasva_kogus(), "g")
print("Rasva kogus hapukoores:", hapukoore_komponent.rasva_kogus(), "g")
print("Rasva kogus vorstis:", vorsti_komponent.rasva_kogus(), "g")


class Toit:
    def __init__(self, nimetus):
        self.nimetus = nimetus
        self.toidukomponendid = []

    def lisa_komponent(self, komponent):
        self.toidukomponendid.append(komponent)

    def kogu_valgud(self):
        summa = 0
        for komponent in self.toidukomponendid:
            summa += komponent.kogus * komponent.toiduaine.valgud / 100
        return summa
    
    def kogu_rasvad(self):
        summa = 0
        for komponent in self.toidukomponendid: 
            summa += komponent.rasva_kogus()
        return summa
    
    def kogu_süsivesikud(self):
        summa = 0
        for komponent in self.toidukomponendid:
            summa += komponent.kogus * komponent.toiduaine.süsivesikud / 100
        return summa
    

kartulisalat = Toit("Kartulisalat")

kartulisalat.lisa_komponent(kartuli_komponent)
kartulisalat.lisa_komponent(hapukoore_komponent)
kartulisalat.lisa_komponent(vorsti_komponent)

print("\nKartulisalati koostisosade toitained:")
print("Valke:", round(kartulisalat.kogu_valgud(), 2), "g")
print("Rasvu:", round(kartulisalat.kogu_rasvad(), 2), "g")
print("Süsivesikuid:", round(kartulisalat.kogu_süsivesikud(), 2), "g")

print("\n5 kg kartulisalati jaoks vajalikud toiduained:")

algne_kogus = (kartuli_komponent.kogus + hapukoore_komponent.kogus + vorsti_komponent.kogus)

kordaja = 6000 / algne_kogus

print("Kartul:", round(kartuli_komponent.kogus * kordaja, 1), "g")
print("Hapukoor:", round(hapukoore_komponent.kogus * kordaja, 1), "g")
print("Vorst:", round(vorsti_komponent.kogus * kordaja, 1), "g")




import unittest


class TestToiduaine(unittest.TestCase):

    def test_toiduaine_loomine(self):

        kartul = Toiduaine("Kartul", 1.9, 0.1, 15.5)

        self.assertEqual(kartul.nimetus, "Kartul")
        self.assertEqual(kartul.valgud, 1.9)
        self.assertEqual(kartul.rasvad, 0.1)
        self.assertEqual(kartul.süsivesikud, 15.5)

    def test_protsent_yle_100(self):

        with self.assertRaises(ValueError):
            Toiduaine("Vigane", 50, 40, 20)


class TestToidukomponent(unittest.TestCase):

    def test_rasva_kogus(self):

        vorst = Toiduaine("Vorst", 25, 35, 1)

        komponent = Toidukomponent(50, vorst)

        self.assertEqual(komponent.rasva_kogus(), 17.5)


if __name__ == "__main__":
    unittest.main()
