# Määrittelydokumentti
Projektin tarkoituksena on vertailla kahta reitinhakualgoritmia labyrintissa. Labyrintit toteutetaan satunnaistetulla Primin algoritmilla, joka tallentaa solun viereisiä seiniä pinoon. Algoritmi tuottaa labyrintteja, joissa ei ole silmukoita, joten ratkaisualgoritmien tarkoitus on löytää ainut olemassa oleva reitti. Labyrintit toteutetaan matriisina, jonka molemmat ratkaisut kätvät läpi. Leveyshaku hakee ensin etäisyydet kaikista saavutettavissa olevista ruuduista taulukkoon, jonka perusteella piirtää ratkaisun labyrinttiin. Leveyshaun aikavaativuus tulisi olla O(n+m). Dead-end filling etsii ensin labyrintin umpikujat ja muuraa umpeen kunnes vastaan tulee polku. Se käy syötteen läpi vain kerran ja muuraa rekursiivisesti, joten sen aikavaativuus on luokkaa O(2n).


## Lähteet
[Wikipedia, Maze solving algorithm](https://en.wikipedia.org/wiki/Maze-solving_algorithm)

[Wikipedia, Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

Tietorakenteet ja algoritmit -kirja, Antti Laaksonen
