import random

def labyrintti():
    """Luo satunnaisen labyrintin"""
    ruudukko = [[]]*10
    vierailtu = [[]]*10
    for i in range (10):
        ruudukko[i]=["0"]*10
        vierailtu[i]=[0]*10
    
    def luo(x, y):
        """Luo rekursiivisesti labyrintin ruudukkoon"""
        if y<0 or x<0 or y>=10 or x>=10:
            return
        if vierailtu[x][y] == 1:
            return 
        vierailtu[x][y] = 1
        if ruudukko[x][y] == "#":
            return

        viereiset = []
        if y-1 >= 0:
            yla = (x, y-1)
            if vierailtu[x][y-1] == 0:
                viereiset.append(yla)
        if y+1 < 10:
            ala = (x, y+1)
            if vierailtu[x][y+1] == 0:
                viereiset.append(ala)
        if x+1 < 10:
            oik = (x+1, y)
            viereiset.append(oik)
        if x-1 >= 0:
            vas = (x-1, y)
            viereiset.append(vas)

        reitti = random.choice(viereiset)
        ruudukko[reitti[0]][reitti[1]] = "."
        for k in viereiset:
            if k != reitti:
                ruudukko[k[0]][k[1]] = "#"
        luo(reitti[0], reitti[1])


    
    luo(0, 0)
    for k in ruudukko:
        print(k)

labyrintti()