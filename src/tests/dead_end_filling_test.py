import unittest
from dead_end_filling import DeadEndFilling

class TestDeadEndFilling(unittest.TestCase):
    def setUp(self):
        self.labyrintti =  [['#', '.', '#', '#', '#'],
                            ['#', '.', '#', '.', '#'],
                            ['#', '.', '#', '.', '#'],
                            ['#', '.', '.', '.', '#'],
                            ['#', '#', '#', '.', '#']]
        self.DEF = DeadEndFilling(self.labyrintti)

    def test_umpikujat(self):
        self.DEF.umpikujat()
        self.assertEqual(self.labyrintti[1][3], "#")

    def test_muuraa(self):
        self.DEF.muuraa(1, 3)
        self.assertEqual(self.labyrintti[2][3], "#")

    def test_palauta(self):
        self.DEF.palauta()
        self.assertEqual(self.labyrintti[3][3], ".")
        self.assertEqual(self.labyrintti[1][3], "#")
