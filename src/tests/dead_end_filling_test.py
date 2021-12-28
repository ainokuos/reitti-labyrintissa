import unittest
from dead_end_filling import DeadEndFilling

class TestDeadEndFilling(unittest.TestCase):
    def setUp(self):
        self.labyrintti =  [['#', '.', '#', '#', '#'],
                            ['#', '.', '#', '.', '#'],
                            ['#', '.', '#', '.', '#'],
                            ['#', '.', '.', '.', '.'],
                            ['#', '#', '#', '#', '#']]

        self.labyrintti2 = [['#', '.', '#', '#', '#', '#'],
                            ['#', '.', '#', '#', '.', '#'], 
                            ['#', '.', '.', '#', '.', '.'], 
                            ['#', '#', '.', '#', '.', '#'], 
                            ['#', '.', '.', '.', '.', '#'], 
                            ['#', '#', '#', '#', '#', '#']]

        self.DEF = DeadEndFilling(self.labyrintti)
        self.DEF2 = DeadEndFilling(self.labyrintti2)

    def test_umpikujat(self):
        self.DEF.umpikujat()
        self.assertEqual(self.labyrintti[1][3], "#")
    
    def test_toinen_labyrintti_umpikujat(self):
        self.DEF2.umpikujat()
        self.assertEqual(self.labyrintti[4][1], "#")
        self.assertEqual(self.labyrintti[1][4], "#")

    def test_muuraa(self):
        self.DEF.muuraa(1, 3)
        self.assertEqual(self.labyrintti[2][3], "#")

    def test_palauta(self):
        self.DEF.palauta()
        self.assertEqual(self.labyrintti[3][3], ".")
        self.assertEqual(self.labyrintti[1][3], "#")
    
    def test_palauta_toinen_labyrintti(self):
        self.DEF2.palauta()
        self.assertEqual(self.labyrintti2[2][4], ".")
        self.assertEqual(self.labyrintti2[1][4], "#")

    def test_oikea_vastaus(self):
        vastaus = [['#', '.', '#', '#', '#'],
                    ['#', '.', '#', '#', '#'],
                    ['#', '.', '#', '#', '#'],
                    ['#', '.', '.', '.', '.'],
                    ['#', '#', '#', '#', '#']]
        self.DEF.palauta()
        self.assertEqual(self.labyrintti, vastaus)