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