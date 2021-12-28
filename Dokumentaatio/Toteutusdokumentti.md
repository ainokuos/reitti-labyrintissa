## Ohjelman toteutus

Ohjelma tuottaa labyrintteja satunnaistetulla Primin algoritmilla luokassa `Labyrintti`. Ohjelmassa on kaksi ratkaisualgoritmia luokissa `DeadEndFilling` ja `BreadthFirstSearch`, jotka molemmat saavat argumentikis ratkaistavan labyrintin. 

## Vertailu
Ohjelmassa vertaillaan ratkaisualgoritmien nopeuksia. Mahdollisilla testattavilla syötteillä voi jo huomata, että leveyshaun käyttämä aika ei kasva yhtä nopeasti kuin dead-end filling:lla. 

Leveyshaku käy labyrintin ja apumatriisin kerran läpi, joten sen aikavaativuus on O(n+m). Dead-end fillin käy labyrintin ensin läpi etsien sen umpikujat, joista se sitten muuraa kunnes löytää polun. Sen aikavaativuus on siis noin O(n).
## Parannuksia
Labyrinttien toteutus toimii rekursiivisesti ja suurin mahdollinen labyrintin koko on 42 x 42. Suuremmilla syötteillä mahdollinen rekusriosyvyys ylittyy. Tämän voisi todennäköisesti korjata tehostamalla luontiin kätettyä algoritmia,, mutta tapaa en vielä keksinyt.

Dead-end filling -algoritmi hidastuu selvästi, kun syötteet kasvavat, joten sen toteutuksessa on todennäköisesti vielä epähuomioituja turhia kohtia. 

## Lähteet
### Labyrintin luonti

[Maze generating algorithm, Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

### Ratkaisualgoritmit

[Maze solving algorithm, Wikipedia](https://en.wikipedia.org/wiki/Maze-solving_algorithm)

Tietorakenteet ja algoritmit -kirja, Antti Laaksonen
