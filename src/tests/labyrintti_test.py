import unittest
from labyrintti import Labyrintti

class TestLabyrintti(unittest.TestCase):
    def setUp(self):
        self.labyrintti = Labyrintti(10)

    def test_luo_ruudukko(self):
        self.assertEqual(len(self.labyrintti.ruudukko), 10)

    def test_luo_labyrintti(self):
        self.labyrintti.luo(1, 1)
        self.assertEqual(len(self.labyrintti.ruudukko), 10)

    def test_aloitusruutu_oikein(self):
        self.labyrintti.luo(1, 1)
        self.assertEqual(self.labyrintti.ruudukko[0][1], ".")

    def test_palauta_labyrintti(self):
        self.labyrintti.palauta()
        self.assertEqual(self.labyrintti.ruudukko[1][1], ".")
