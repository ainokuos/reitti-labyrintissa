import random

class Labyrintti:
    """Luokka tuottaa labyrintin nxn matriisina annetulla n

        attributes:
            n: luku, joka määrittää labyrintin koon
    """
    def __init__(self, n):
        """ Luokan konstruktori

            Args:
                n: labyrintin koko, joka muodostuu nxn
        """

        self.n = n
        self.ruudukko = []
        self.vierailtu = []
        self.edelliset = []

    def luo_ruudukko(self):
        """Metodi, joka luo ruudukon labyrinttia varten
        """

        self.ruudukko = [[]]*self.n
        self.vierailtu = [[]]*self.n

        for i in range(self.n):
            self.ruudukko[i] = ["#"]*self.n
            self.vierailtu[i] = [0]*self.n

        self.ruudukko[1][1] = "."


    def viereiset(self, x, y):
        """Metodi, joka tutkii tämän hetkisen solmun mahdolliset viereiset solmut

            Args:
                x: rivikoordinaatti
                y: sarakekoordinaatti

            Returns:
                Lista viereisistä solmuista, joissa ei ole vierailtu
        """
        viereiset = []

        if y-2 >= 0:
            yla = (x, y-1, x, y-2)
            if self.vierailtu[x][y-2] == 0:
                viereiset.append(yla)

        if y+2 < self.n-1:
            ala = (x, y+1, x, y+2)
            if self.vierailtu[x][y+1] == 0:
                viereiset.append(ala)

        if x+2 < self.n-1:
            oik = (x+1, y, x+2, y)
            if self.vierailtu[x+2][y] == 0:
                viereiset.append(oik)

        if x-2 >= 0:
            vas = (x-1, y, x-2, y)
            if self.vierailtu[x-2][y] == 0:
                viereiset.append(vas)
        return viereiset

    def luo_labyrintti(self, x, y):
        """Luo labyrintin ruudukkoon

            Args:
                x: rivikoordinaatti
                y: sarakekoordinaatti

        """
        if self.vierailtu[x][y] == 1:
            if len(self.edelliset) > 0:
                edellinen = self.edelliset.pop(-1)
                self.luo_labyrintti(edellinen[0], edellinen[1])
                return
        viereiset = self.viereiset(x, y)
        self.vierailtu[x][y] = 1

        if len(viereiset) == 0:
            if len(self.edelliset) == 0:
                return
            edellinen = self.edelliset.pop(-1)
            self.luo_labyrintti(edellinen[0], edellinen[1])

        if len(viereiset) > 1:
            self.edelliset.append((x, y))

        if len(viereiset) == 0:
            return
        reitti = random.choice(viereiset)

        self.ruudukko[reitti[0]][reitti[1]] = "."
        self.ruudukko[reitti[2]][reitti[3]] = "."

        self.luo_labyrintti(reitti[2], reitti[3])

    def piirra(self):
        """Metodi, joka piirtää labyrintin
        """
        print("Uusi:")
        self.luo_ruudukko()
        self.luo_labyrintti(1, 1)
        i = 0
        j = 1
        while i <= self.n:
            while j <=self.n:
                if self.vierailtu[i][j] == 0:
                    self.luo_labyrintti(i, j)
                    j +=2
            i += 1

        for k in self.ruudukko:
            print(k)
        #print(self.vierailtu)

labyrintti = Labyrintti(5)
labyrintti.piirra()