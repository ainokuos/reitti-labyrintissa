from labyrintti2 import Labyrintti
from dead_end_filling import DeadEndFilling

def main():
    labyrintti = Labyrintti()
    DEF = DeadEndFilling(labyrintti.palauta())
    DEF.umpikujat()
    DEF.palauta()


if __name__=="__main__":
    main()
