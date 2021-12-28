import unittest
from breadth_first_search import BreadthFirstSearch

class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.labyrintti = [['#', '.', '#', '#', '#'],
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

        self.BFS = BreadthFirstSearch(self.labyrintti)
        self.BFS2 = BreadthFirstSearch(self.labyrintti2)

    def test_palauta(self):
        self.BFS.palauta()
        self.assertEqual(self.labyrintti[3][1], "x")
    
    def test_toinen_labyrintti(self):
        self.BFS2.palauta()
        self.assertEqual(self.labyrintti2[1][1], "x")
    
    def test_oikea_reitti(self):
        self.BFS.palauta()
        self.assertEqual(self.labyrintti[1][3], ".")
        self.assertEqual(self.labyrintti[3][4], "x")
    
    def test_haku(self):
        self.BFS.haku()
        self.assertEqual(self.BFS.etaisyys[3][4], 6)
    
    def test_oikea_vastaus(self):
        vastaus = [['#', 'x', '#', '#', '#'],
                    ['#', 'x', '#', '.', '#'],
                    ['#', 'x', '#', '.', '#'],
                    ['#', 'x', 'x', 'x', 'x'],
                    ['#', '#', '#', '#', '#']]
        self.BFS.palauta()
        self.assertEqual(self.labyrintti, vastaus)
