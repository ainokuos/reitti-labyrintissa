import datetime

class DeadEndFilling:
    """Luokka, joka hakee reitin labyrintissa Dead-end filling-algoritmilla"""
    def __init__(self, labyrintti):
        """Luokan konstruktori

            Args:
                labyrintti: matriisi ratkaistavasta labyrintista
        """
        self.labyrintti = labyrintti
        self.koko = len(labyrintti)

    def viereiset(self, x, y):
        """Hakee ruudun mahdolliset viereiset ruudut

            Args:
                x: ruudun rivikoordinaatti
                y: ruudun sarakekoordinaatti
            Returns:
                lista viereisistä ruuduista
        """
        viereiset = []
        if y-1 >= 0:
            yla = (x, y-1)
            if self.labyrintti[x][y-1] == '.':
                viereiset.append(yla)

        if y+1 <= self.koko-1:
            ala = (x, y+1)
            if self.labyrintti[x][y+1] == '.':
                viereiset.append(ala)

        if x+1 <= self.koko-1:
            oik = (x+1, y)
            if self.labyrintti[x+1][y] == '.':
                viereiset.append(oik)

        if x-1 >= 0:
            vas = (x-1, y)
            if self.labyrintti[x-1][y] == '.':
                viereiset.append(vas)
        return viereiset

    def umpikujat(self):
        """Metodi, joka etsii umpikujat labyrintista"""
        for i in range(1, self.koko-1):
            for j in range(1, self.koko-1):
                if self.labyrintti[i][j] == ".":
                    viereiset = self.viereiset(i, j)
                    if len(viereiset) == 1:
                        self.muuraa(i, j)

    def muuraa(self, x, y):
        """Metodi, joka muuraa umpikujat, kunnes vastaan tulee polku

            Args:
                x: ruudun rivikoordinaatti
                y: ruudun sarakekoordinaatti
        """
        viereiset = self.viereiset(x, y)
        if len(viereiset) == 1:
            self.labyrintti[x][y] = "#"
            self.muuraa(viereiset[0][0], viereiset[0][1])

    def palauta(self):
        """Palauttaa ratkaistun reitin ja suoritusajan"""
        for k in self.labyrintti:
            print(k)
        print('')

        alku = datetime.datetime.now()
        self.umpikujat()
        loppu = datetime.datetime.now()

        for k in self.labyrintti:
            print(k)
        print(f'Aikaa kului: {loppu-alku}')
