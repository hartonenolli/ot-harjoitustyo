# Sovelluksen arkkitehtuuri

## Rakenne

Hakemistot src, src/sprites ja database

![rakennekuva](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/ark_arkkitehtuuri.jpg)

## Sovelluslogiikka

Alustaa pelikentän, kun käyttöliittymä kutsuu pelikentän alustavaa kutsua. Kutsuu luokan perivää Spritet-luokkaa ja palautta kuvia:
- 0 = valkoinen
- 1 = nalle
- 2 = pupu
- 3 = pojanamongus

**Ristinolla -> GameLevel -> Spritet**

![kuvaus](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/ark_kuvienhaku.jpg)

Käyttöliittymä **ristinolla_kayttoliittyma.py** ja pelilogiikka **game_level.py** toimii keskenään tiiviisti. Pelin toimivuuden kannalta käyttöliittymä tarkastaa kolmen suorat ja käsittelee klikkauksen asettaen kuvan ruutuun.

**Kuvassa peli käynnistetään, valitaan kaksinpeli, alustetaan pelikenttä, laitetaan ruutuun kuva ja tarkastetaan onko tullut kolmen suora**

![havainnol](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/ark_pelintoiminta.jpg)

## Käyttöliittymä

Sisältää pelikentät ja koordinaatit, jotka väliteetään pelin alkaessa pelilogiikalle. Näkymiä on:
- alotusnäyttö
  - annetaan ohjeita pelimuotojen, historian, wikipedian tai lopettamisen väliltä
- pelikenttä
  - 5x5 tai 7x5
- lopetusnäyttö

### Pelihistoriasta

Pelihistoria tulostetaan aloitusnäytölle. Käyttöliittymän luokka **Ristinolla** kutsuu tietokannan tiedostoa *database_ristinolla.py* luokkaa **Database**.



![Tietokantaa varten](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/ark_historia.jpg)

## Tietokanta

Pelihistorian pysyväistallennusta varten on *database_ristinolla.py* ja *init_database.py*. Init_database.py käytetään vain tietokannan tekemiseen. Tietokanta tulee tehdä ennen ensimmäistä käynnistyskertaa komennolla: ***poetry run invoke build***
Komennon suoritettuaan tehdään *tilastot.db* hakemistoon *datafile*

![kuva tasta](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/ark_database.jpg)

## Koko pelin toiminta

Kuvassa on pelin käynnistyksestä pelin loppuun asti vaiheet. Peli alustetaan ja klikkaukset tarkastetaan joka kerralla. Kun havaitaan kolmen suora, niin tulee loppuruutu näkymä ja lisätään pelimuotoon tietokannassa yksi pelikerta. Pelaaja lopettaa pelin painamalla P.

![kokokuva](https://github.com/hartonenolli/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/ark_kokopeli.jpg)
