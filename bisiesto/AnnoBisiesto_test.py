
import unittest
import AnnoBisiesto

class AnnoBisiestoTest(unittest.TestCase):

    def test_symbols_bisiesto(self):
        self.assertEqual(AnnoBisiesto.Bisiesto(2004), True)
        self.assertEqual(AnnoBisiesto.Bisiesto(2008), True)
        self.assertEqual(AnnoBisiesto.Bisiesto(2100), False)
        self.assertEqual(AnnoBisiesto.Bisiesto(2200), False)
        self.assertEqual(AnnoBisiesto.Bisiesto(2000), True)
        self.assertEqual(AnnoBisiesto.Bisiesto(2400), True)

    def test_anno_no_numero(self):
        self.assertFalse(AnnoBisiesto.exception('dosmil'))
        self.assertTrue(AnnoBisiesto.exception('2000'))
        
if __name__ == '__main__':
    unittest.main()

