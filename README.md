# Väärinpäin ristinolla

Sovellus on ristinolla, mutta ***väärinpäin***. Pelin voittaa se pelaaja,
joka ei joudu pakosta asettamaan kolmensuoraa.

Pelissä on eri pelimuotoja:
- yksin
- kaksin
- kolmin
Peli tallettaa pelihistoriaa
Peli ohjaa wikipediasivulle

## Dokumentaatio
- [Käyttöohje](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Muutokset](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/rakenne.md)
- [Vaatimuusmäärittely ja toiminnallisuudet](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Testaus](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

# Pelin ASENNUS
## Komentorivi:
### Poetry
- poetry install

## ENNEN ENSIMMÄISTÄ KÄYYNISTYSTÄ:
- poetry run invoke build

### Ohjelma käynnistyy
- poetry run invoke start

### Ohjelman testaus
- poetry run invoke test

### Ohjelman testikattavuus
- poetry run invoke coverage-report

### Pylint
- poetry run invoke lint
