from labyrintti2 import Labyrintti

class WallFollower:
    def __init__(self, labyrintti):
        self.labyrintti = labyrintti
    
    def viereiset(self, x, y):
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

    def kulje(self, x, y):
        
    
    def palauta(self):
        for k in self.labyrintti:
            print(k)
WF = WallFollower(Labyrintti().palauta())
WF.palauta()
