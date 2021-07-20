import unittest
from vazifa import maxSon, katt_matn, juftSon

class TestVazifalar(unittest.TestCase):
    def test_maxSon(self):
        max1 = maxSon(23,  345, 567)
        self.assertAlmostEqual(max1, 567)
        
    def test_katta_matn(self):
        matn = katt_matn(['ali', 'vali', 'husan'])
        self.assertEqual(matn, ['Ali', "Vali", "Husan"])
        
    def test_juftSon(self):
        sonlar = juftSon([2132, 345, 56776, 789, 89])
        self.assertEqual(sonlar, [2132, 56776])
        
        
unittest.main()