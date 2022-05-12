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

### Testien ulkopuolella

Pelilogiikkaa varten on tehty automaattisesti suoritettavia testejä. Muut on testattu manuaalisesti.
- ristinolla_kayttoliittyma.py
- database_ristinolla.py
- sprite_kuvat.py
- init_database.py

## Testikattavuus

Testien kattavuus on **99%**

![testikattavuuskuva](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage_report.jpg)

## Asennuksesta

Sovellusta on testattu linux-ympäristössä

## Toiminnallisuuksista

Toiminnallisuudet on pääosin testattu manuaalisesti, monet toiminnallisuudet eivät kuulu pelilogiikkaan.
Toiminnallisuuksien testauksessa on annettu esim samaa syötettä useasti.

## Korjaamattomia laatuvikoja

- Sovellus tulostaa terminaalille pelin suljettaessa:
  - pygame.error: video system not initialized
