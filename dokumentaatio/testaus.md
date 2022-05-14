# Testausdokumentti

Ohjelmaa on testattu automaattisin testen ja manuaalisella kokeilemisella. 
Testeissä on avustanut myös: Rico 7v ja Liselle 3v.

## Testit
### Sovelluslogiikka

Sovelluslogiikka: **game_level.py**-tiedostosta testataan *GameLevel*-luokkaa automaattisin testein. 
**game_level_test.py**-tiedostosta löytyy luokka *TestGameLevel*-luokka.
Testeillä testataan pelilogiikka. Näitä asioita ovat esim:
- Sijoitetaan kuva peliruudulle
- Tarkastetaan pelikenttää kolmen suoran varalta

### Tietokanta

Tietokantana toimii **database_ristinolla.py**-tiedosto, jossa on luokka *Database*. Luokkaa testataan automaattisin testein.
**database_test.py**-tiedostosta löytyy luokka *TestDatabase*

### Testien ulkopuolella

Pelilogiikkaa varten on tehty automaattisesti suoritettavia testejä. Muut on testattu manuaalisesti.
- ristinolla_kayttoliittyma.py
- sprite_kuvat.py
- init_database.py

## Testikattavuus

Testien rivikattavuus on:
- 99% **GameLevel**
- 100% **Database**

Haarautuvuuden kattavuus on:
- 100% **GameLevel**
- 75% **Database**

![testikattavuuskuva](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/new_coverage.jpg)

## Asennuksesta

Sovellusta on testattu linux-ympäristössä

## Toiminnallisuuksista

Toiminnallisuudet on pääosin testattu manuaalisesti, monet toiminnallisuudet eivät kuulu pelilogiikkaan.
Toiminnallisuuksien testauksessa on annettu esim samaa syötettä useasti.

## Korjaamattomia laatuvikoja

- Sovellus tulostaa terminaalille pelin suljettaessa:
  - pygame.error: video system not initialized
