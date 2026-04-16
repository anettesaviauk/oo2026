import unittest
from main import Kalkulaator
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
    def test_vajutus8(self):
        self.k.vajutus('9')
        self.k.vajutus('0')
        self.k.vajutus('sin')
        self.k.sin()
        self.assertAlmostEqual(self.k.ekraan(), float(1), places = 7)
suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')