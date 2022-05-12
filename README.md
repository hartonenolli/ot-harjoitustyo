# Väärinpäin ristinolla

Sovellus on ristinolla, mutta ***väärinpäin***. Pelin voittaa se pelaaja,
joka ei joudu pakosta asettamaan kolmensuoraa.

## Dokumentaatio
- [Käyttöohje](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Muutokset](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Rakenne](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/rakenne.md)
- [Vaatimuusmäärittely ja toiminnallisuudet](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Sekvenssikaavio](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_2.jpg)

# Pelin ASENNUS
## Komentorivi:
### Poetry
- poetry install

## ENNEN ENSIMMÄISTÄ KÄYYNISTYSTÄ:
- poetry run ivoke build

### Ohjelma käynnistyy
- poetry run invoke start

### Ohjelman testaus
- poetry run invoke test

### Ohjelman testikattavuus
- poetry run invoke coverage-report

### Pylint
- poetry run invoke lint
