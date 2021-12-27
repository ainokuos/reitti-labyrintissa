![Screenshot from 2021-12-27 23-09-01](https://user-images.githubusercontent.com/80783887/147507425-c082cbdf-c5be-4109-821a-57e94292e9c1.png)

Ohjelma hakee labyrintista reitin dead-end filling -algoritmilla ja laveyshaulla. Koska labyrintit tuotetaan satunnaistetulla Primin algoritmilla ne ovat ns. täydellisiä labyrintteja eli niissä ei ole silmukoita. Molemmat ratkaisualgoritmit löytävät siis saman reitin, joka on ainut olemassa oleva ratkaisu. Molemmista on testattu, että ne löytävät saman ja oikean polun.

## Algoritmien aikoja:
| Labyrintin koko | Dead-end filling |Leveyshaku|
|:----:|:----:|:----:|
|5 x 5|0.000097|0.000111|
|10 x 10|0.00021|0.000965|
|15 x 15|0.000978|0.000965|
|20 x 20|0.001805|0.00061|
|25 x 25|0.001062|0.000765|
|30 x 30|0.001665|0.001057|
|35 x 35|0.002107|0.001498|
|40 x 40|0.002525|0.001656|
|42 x 42|0.006836|0.002173|


![Screenshot from 2021-12-27 23-00-06](https://user-images.githubusercontent.com/80783887/147506924-da130463-8387-48ae-89a4-3cddbd56c9bc.png)

Sininen: Dead-end filling

Punainen: Leveyshaku
