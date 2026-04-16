import unittest
import math

class Kalkulaator:
    sisu= '0'
    def vajutus(self,nupp):
        if self.sisu == '0':
            self.sisu = nupp
        else:
            self.sisu += nupp
    def ekraan(self):
        return self.sisu
    def liitmine(self):
        self.sisu
        result = sum(int(x) for x in self.sisu.split('+'))
        ##print (result)
        self.sisu= str(result)
    def lahutamine(self):
        numbrid = [int(x) for x in self.sisu.split('-')]
        tulemus = numbrid[0]
        for arv in numbrid[1:]:
            tulemus -= arv
        self.sisu= str(tulemus)
    def korrutamine(self):
        self.sisu
        numbrid = (int(x) for x in self.sisu.split('*'))
        ##print (result)
        result = math.prod(numbrid)
        self.sisu= str(result)
    def jagamine(self):
        self.sisu
        numbrid = [int(x) for x in self.sisu.split('/')]
        tulemus = numbrid[0]
        # Käime läbi kõik arvud alates teisest
        for arv in numbrid[1:]:
            if arv == 0:
                self.sisu = "Viga: nulliga jagamine"
                return
            result /= arv
            self.sisu=str(result)
    def jagamine(self):
        numbrid = [int(x) for x in self.sisu.split('/')]
        tulemus = numbrid[0]
        for arv in numbrid[1:]:
            if arv == 0:
                self.sisu = "Viga: nulliga jagamine"
                return
        tulemus /= arv
        if tulemus == int(tulemus):
            tulemus = int(tulemus)
            self.sisu = str(tulemus)

class TestKalkulaator(unittest.TestCase):
    def setUp(self):
        self.k = Kalkulaator()
        self.k.sisu = '0'
        k = Kalkulaator()
    def test_algus(self):
        self.assertEqual(self.k.ekraan() , "0")
        print('Addition test passed')
    def test_vajutus(self):
        self.k.vajutus('1')
        self.assertEqual(self.k.ekraan(), "1")
    def test_vajutus2(self):
        self.k.vajutus('2')
        self.assertEqual(self.k.ekraan(), "2")
    def test_vajutus3(self):
        self.k.vajutus('1')
        self.k.vajutus('2')
        self.assertEqual(self.k.ekraan(), "12")
    def test_vajutus4(self):
        self.k.vajutus('1')
        self.k.vajutus('0')
        self.k.vajutus('+')
        self.k.vajutus('1')
        self.k.vajutus('5')
        self.k.liitmine()
        self.assertEqual(self.k.ekraan(), "25")
    def test_vajutus5(self):
        self.k.vajutus('1')
        self.k.vajutus('5')
        self.k.vajutus('-')
        self.k.vajutus('1')
        self.k.vajutus('0')
        self.k.lahutamine()
        self.assertEqual(self.k.ekraan(), "5")
    def test_vajutus6(self):
        self.k.vajutus('1')
        self.k.vajutus('0')
        self.k.vajutus('*')
        self.k.vajutus('1')
        self.k.vajutus('0')
        self.k.korrutamine()
        self.assertEqual(self.k.ekraan(), "100")
    def test_vajutus7(self):
        self.k.vajutus('1')
        self.k.vajutus('0')
        self.k.vajutus('/')
        self.k.vajutus('1')
        self.k.vajutus('0')
        self.k.jagamine()
        self.assertEqual(self.k.ekraan(), "1")
suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')