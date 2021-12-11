import random

class Labyrintti:
    """Luokka, joka luo labyrintin Primin algoritmilla"""
    def __init__(self, n):
        """Luokan konstruktori, joka luo ruudukon täynnä seiniä

            Arg:
                n: koko labyrintille, joka muodostetaan nxn
        """
        self.n = n
        self.ruudukko = [[]]*self.n
        self.vierailtu = [[]]*self.n

        for i in range(n):
            self.ruudukko[i] = ['#']*self.n
            self.vierailtu[i] = [0]*self.n

        self.ruudukko[0][1] = "."

        self.seinat = []

    def viereiset(self, x, y):
        """Metodi, joka etsii ruudun mahdolliset viereiset ruudut

            Args:
                x: ruudun rivikoordinaatti
                y: ruudun sarakekoordinaatti
            Returns:
                lista ruudun vierisistä ruuduista
        """
        viereiset = []
        if y-1 >= 1:
            yla = (x, y-1)
            if self.vierailtu[x][y-1] == 0:
                viereiset.append(yla)

        if y+1 < self.n-1:
            ala = (x, y+1)
            if self.vierailtu[x][y+1] == 0:
                viereiset.append(ala)

        if x+1 < self.n-1:
            oik = (x+1, y)
            if self.vierailtu[x+1][y] == 0:
                viereiset.append(oik)

        if x-1 >= 1:
            vas = (x-1, y)
            if self.vierailtu[x-1][y] == 0:
                viereiset.append(vas)
        return viereiset

    def luo(self, x, y):
        """Metodi, joka luo labyrintin

            Args:
                x: aloitusruudun rivikoordinaatti
                y: aloitusruudun sarakekoordinaatti
        """
        if self.vierailtu[x][y] == 1:
            return

        seina = self.viereiset(x, y)
        self.vierailtu[x][y] = 1
        self.ruudukko[x][y] = '.'

        for s in seina:
            if s in self.seinat:
                self.seinat.remove(s)
                self.vierailtu[s[0]][s[1]] = 1
            else:
                self.seinat.append(s)

        if len(self.seinat) > 0:
            seuraava = random.choice(self.seinat)
            self.seinat.remove(seuraava)
            self.luo(seuraava[0], seuraava[1])

    def maali(self):
        """Metodi, joka luo labyrintille päätepisteen"""
        for i in range(self.n-2, 1, -1):
            if self.ruudukko[i][self.n-2] == ".":
                self.ruudukko[i][self.n-1] = "."
                return

    def palauta(self):
        """Metodi, joka palauttaa labyrintin"""
        self.luo(1, 1)
        self.maali()
        return self.ruudukko
