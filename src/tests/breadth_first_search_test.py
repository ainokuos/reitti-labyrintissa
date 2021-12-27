import unittest
from breadth_first_search import BreadthFirstSearch

class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.labyrintti = [['#', '.', '#', '#', '#'],
                            ['#', '.', '#', '.', '#'],
                            ['#', '.', '#', '.', '#'],
                            ['#', '.', '.', '.', '.'],
                            ['#', '#', '#', '#', '#']]
        self.BFS = BreadthFirstSearch(self.labyrintti)

    def test_palauta(self):
        self.BFS.palauta()
        self.assertEqual(self.labyrintti[3][1], "x")
