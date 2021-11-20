import unittest
from labyrintti import Labyrintti

class TestLabyrintti(unittest.TestCase):
    def setUp(self):
        self.labyrintti = Labyrintti(10)
    
    def test_luo_ruudukko(self):
        self.labyrintti.luo_ruudukko()

        self.assertEqual(len(self.labyrintti.ruudukko), 10)
    
    def test_luo_labyrintti(self):
        self.labyrintti.luo_ruudukko()
        self.labyrintti.luo_labyrintti(1, 1)

        self.assertEqual(len(self.labyrintti.ruudukko), 10)

