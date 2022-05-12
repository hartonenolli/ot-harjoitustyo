# Sovelluksen arkkitehtuuri

## Rakenne

Hakemistot src, src/sprites ja database
![rakennekuva]()

## Sovelluslogiikka

Alustaa pelikentän, kun käyttöliittymä kutsuu pelikentän alustavaa kutsua. Kutsuu luokan perivää Spritet-luokkaa ja palautta kuvia:
- 0 = valkoinen
- 1 = nalle
- 2 = pupu
- 3 = pojanamongus

**Ristinolla -> GameLevel -> Spritet**

![kuvaus]()

Käyttöliittymä **ristinolla_kayttoliittyma.py** ja pelilogiikka **game_level.py** toimii keskenään tiiviisti. Pelin toimivuuden kannalta käyttöliittymä tarkastaa kolmen suorat ja käsittelee klikkauksen asettaen kuvan ruutuun.

![havainnol]()

## Käyttöliittymä

Sisältää pelikentät ja koordinaatit, jotka väliteetään pelin alkaessa pelilogiikalle. Näkymiä on:
- alotusnäyttö
  - annetaan ohjeita pelimuotojen, historian, wikipedian tai lopettamisen väliltä
- pelikenttä
  - 5x5 tai 7x5
- lopetusnäyttö

### Pelihistoriasta

Pelihistoria tulostetaan aloitusnäytölle. Käyttöliittymän luokka **Ristinolla** kutsuu tietokannan tiedostoa *database_ristinolla.py* luokkaa **Database**.

![Tietokantaa varten]()

## Tietokanta

Pelihistorian pysyväistallennusta varten on *database_ristinolla.py* ja *init_database.py*. Init_database.py käytetään vain tietokannan tekemiseen. Tietokanta tulee tehdä ennen ensimmäistä käynnistyskertaa komennolla: ***poetry run invoke build***
Komennon suoritettuaan tehdään *tilastot.db* hakemistoon *datafile*

![kuva tasta]()
