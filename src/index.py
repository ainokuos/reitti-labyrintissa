import copy
from labyrintti import Labyrintti
from dead_end_filling import DeadEndFilling
from breadth_first_search import BreadthFirstSearch

def main():
    while True:
        print("1: Dead-end filling")
        print("2: Leveyshaku")
        print("3: Molemmat")
        print("0: Sulje")

        toiminto = int(input("Valitse toiminto: "))

        if toiminto == 1:
            koko = int(input("Anna labyrintin koko(n x n): "))
            labyrintti = Labyrintti(koko)
            DEF = DeadEndFilling(labyrintti.palauta())
            DEF.palauta()

        if toiminto == 2:
            koko = int(input("Anna labyrintin koko(n x n): "))
            labyrintti = Labyrintti(koko)
            BFS = BreadthFirstSearch(labyrintti.palauta())
            BFS.palauta()

        if toiminto == 3:
            koko = int(input("Anna labyrintin koko(n x n): "))
            labyrintti = Labyrintti(koko).palauta()
            labyrintti2 = copy.deepcopy(labyrintti)
            DEF = DeadEndFilling(labyrintti2).palauta()
            BFS = BreadthFirstSearch(labyrintti).palauta()


        if toiminto == 0:
            break

if __name__ == "__main__":
    main()
