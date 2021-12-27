# Käyttöohje

### Asenna riippuvuudet komennolla
```
poetry install
```
### Käynnistä komennolla
```
poetry run invoke start
```
### Testit voi suorittaa komennolla
```
poetry run invoke test
```
### Testikattavuus on saatavilla komennolla
```
poetry run invoke coverage-report
```
### Pylint
```
poetry run invoke lint
```

### Käyttö
Sovellus kertoo miten voit testata joko dead-end filling -algoritmia tai leveyshakua tai molempia. Valinnan jälkeen ohjelma kysyy labyrintin kokoa muodossa n x n. Koon tulee olla minimissään 5 x 5 ja maksimissaan 42 x 42.
