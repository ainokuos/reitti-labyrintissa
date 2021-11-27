
class DeadEndFilling:
    """ Luokka, joka etsii reitin dead-end filling algoritmilla

        attribute: 
            labyrintti: ruudukko, joka sisältää labyrintin
    """
    def __init__(self, labyrintti):
        """Luokan konstruktori
            Args:
                labyrintti: labyrintti ruudukkona
        """
        self.labyrintti = labyrintti

    def viereiset(self, x, y):
        """Metodi, joka hakee annetun ruudun mahdolliset viereiset ruudut
        
            Args:
                x: ruudun rivikoordinaatti
                y: ruudun sarakekoordinaatti
            
            Returns:
                Lista mahdollisista viereisistä ruuduista
        """
        viereiset = []
        if y-1 >= 0:
            if self.labyrintti[x][y-1] == ".":
                viereiset.append((x, y-1))
        if y+1 < 19:
            if self.labyrintti[x][y+1] == ".":
                viereiset.append((x, y+1))
        if x-1 >= 0:
            if self.labyrintti[x-1][y] == ".":
                viereiset.append((x-1, y))
        if x+1 < 19:
            if self.labyrintti[x+1][y] == ".":
                viereiset.append((x+1, y))
    
        return viereiset
    
    def umpikujat(self):
        """Metodi, joka käy läpi labyrintin ja etsii mahdolliset umpikujat"""
        for i in range(1, 19):
            for j in range(1, 19):
                if self.labyrintti[i][j] == ".":
                    viereiset = self.viereiset(i, j)
                    if len(viereiset) == 1:
                        self.muuraa(i, j)
    
    def muuraa(self, x, y):
        """Metodi, joka muuraa umpeen umpikujat
        
            Args:
                x:ruudun rivikoordinaatti
                y: ruudun sarakekoordinaatti
        """
        self.labyrintti[x][y] = "#"
        viereiset = self.viereiset(x, y)
        viereiset2 = self.viereiset(viereiset[0][0], viereiset[0][1])
        if len(viereiset2) == 1:
            self.muuraa(viereiset2[0][0], viereiset2[0][1])
    
    def palauta(self):
        """Metodi, joka tulostaa labyrintin"""
        for k in self.labyrintti:
            print(k)



    
    def __str__(self):
        return f'{self.labyrintti}'

