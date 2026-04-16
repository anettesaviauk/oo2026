import unittest

def pindala(a,b):
    pindala = a*b
    if pindala<0: pindala=-pindala
    return pindala



class TestMath(unittest.TestCase):
    def test_pindala(self):
        self.assertEqual(pindala(3,5) , 15)
        print('Addition test passed')
    def test_tyhi_pindala(self):
        self.assertEqual(pindala(0,5),0)
    def test_negatiivne_pindala(self):
        self.assertEqual(pindala(3,-5),15)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Tests run: {result.testsRun}')