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
![]()
