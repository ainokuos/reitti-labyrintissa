from collections import deque
import datetime

class BreadthFirstSearch:
    """ Luokka, joka ratkaisee labyrintin leveyshaulla"""
    def __init__(self, labyrintti):
        """Luokan konstruktori
        
            Args:
                labyrintti: matriisi ratkaistavasta labyrintista
        """
        self.labyrintti = labyrintti
        self.koko = len(self.labyrintti)
        self.loppu = ""

        self.vierailtu = [[]]*self.koko
        self.etaisyys = [[]]*self.koko

        for i in range (self.koko):
            self.vierailtu[i] = [0]*self.koko
            self.etaisyys[i] = [0]*self.koko

    def viereiset(self, x, y):
        """Hakee ruudun mahdolliset viereiset ruudut
        
            Args:
                x: rivikoordinaatti
                y: sarakekoordinaatti
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


    def haku(self):
        """Metodi joka suorittaa leveyshaun eli hakee saavutettavissa
            olevien ruutujen etäisyydet lähtöpisteestä
        """
        jono = deque([])
        jono.append((0, 1))
        self.vierailtu[0][1] = 1
        self.etaisyys[0][1] = 0

        while len(jono) > 0:
            solmu = jono.popleft()
            viereiset = self.viereiset(solmu[0], solmu[1])
            for viereinen in viereiset:
                if self.vierailtu[viereinen[0]][viereinen[1]]:
                    continue
                jono.append(viereinen)
                self.vierailtu[viereinen[0]][viereinen[1]] = 1
                self.etaisyys[viereinen[0]][viereinen[1]] = self.etaisyys[solmu[0]][solmu[1]] +1
                if viereinen[1] == self.koko-1:
                    self.loppu = (viereinen[0], viereinen[1])
                    return

    def reitti(self, x, y):
        """Metodi, joka merkkaa ruudukkoon löydetyn reitin rekursiivisesti
        
            Args:
                x: ruudun rivikoordinaatti
                y: ruudun sarakekoordinaatti
        """
        self.labyrintti[x][y] = "x"
        viereiset = self.viereiset(x, y)
        if len(viereiset) == 0:
            return
        seuraava = self.loppu
        for i in viereiset:
            if i == (0, 1):
                return
            if self.etaisyys[i[0]][i[1]] < self.etaisyys[seuraava[0]][seuraava[1]] and self.etaisyys[i[0]][i[1]] > 0:
                seuraava = (i[0], i[1])
        self.reitti(seuraava[0], seuraava[1])


    def palauta(self):
        """Metodi, joka palauttaa ratkaistu labyrintin"""
        alku = datetime.datetime.now()
        self.haku()
        self.reitti(self.loppu[0], self.loppu[1])
        self.labyrintti[0][1] = "x"
        loppu = datetime.datetime.now()
        for k in self.labyrintti:
            print(k)
        print(f"Aikaa kului BFS: {loppu-alku}")
