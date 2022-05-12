# Käyttöohje
Saat ladattua viimeisimmän julkaisun lähdekoodin [täältä]()

## Tallennus
Tietokantaa varten on hakemisto: *datafile*
Hakemistoon luodaan *tilastot.db* tiedosto, joka pitää yllä pelien määrää

## Ohjelman käynnistyksen komennot
Ennen käynnistystä asenna riippuvuudet:
> poetry install

Ennen ensimmäistä käynnistyskertaa luo *tietokanta*:
> poetry run invoke build

Ohjelman käynnistys:
> poetry run invoke start

## Peliruutu:
# Aloitusnäyttö:
Alkunäyttö antaa ohjeita painamaan kirjaimia, painamalla:
- R = alkaa *yksinpeli*
- G = alkaa *kaksinpeli*
- B = alkaa *kolminpeli*
- W = ohjataan *wikipedia-sivulle*
- Y = ruudulle ilmestyy *pelikerrat*
- P = peli *sulkeutuu*
![alkuruutu](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/alkuruutu.png)

Painamalla **R**, **G** tai **B** peli käynnistyy:
![alkunäkymä](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pelinalku.png)

Pelaaja painaa hiiren vasemmalla painikeella tyhjään ruutuun, jolloin ruudulle ilmestyy kuvia:
### Yksinpeli/Kaksinpeli:
![eteneminen](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/eteneminen.png)

### Kolminpeli:
![kolminpeli](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kolminpeli.png)

Jos pelaaja laittaa kolme kuvaa suoraan vaakaan/pystyyn/vinoon, niin pelaaja häviää:
![kolmensuora](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kolmensuora.png)

Ja tulee häviöruutu:
![havioruutu](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/havioruutu.png)

Tämän jälkeen peli palaa alkuruutuun. Painamalla **Y** pelaaja näkee pelikertojen määrät:
![pelikerrat](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/muutos.png?raw=true)

Painamalla **W** aukeaa wikipediasivusto ristinollasta:
![wikisivu](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/wikisivu.png)

Painamalla **P** peli sulkeutuu
