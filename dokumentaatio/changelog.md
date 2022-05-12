## Viikko 3

- Alustettu pelin koodia
- Tehty luokkia: pelin käynnistys, alku-, ohje-, pelivalinta-ruutu.
- Lisätty testejä. Toistaiseksi aiheuttanut ongelmaa saada testit kattavasti toimimaan.
- Ongelmia aiheuttanut pelin käynnityst invoken avulla. (samoin testit)

## Viikko 4

- Sain pelin toimivaan muotoon 3x3 ruudukolla. Peliä voi pelata uudestaan ja pelaajat voivat antaa syötteenä pelaajien nimet.
- Testaus edelleen aiheutti ongelmia ja päädyin hakemaan apua pajatoiminnasta. Sain selville, että ohjelman koodin runko tekee automaattiesten testien suorittamisesta mahdotonta. Joudun aloittamaan projektin käytännössä uudestaan.
- Aloitettu projekti alusta ja saatu toimimaan osittain ominaisuuksia. Pelissä on 5x5 ruudukko ja nalleja ja pupuja asetetaan samalla idealla, kuin aikaisemmassa pelissä.

## Viikko 5

- Saatu peli toimimaan alkuruudusta loppuruutuun
- Testaukset ~89%, mikä on suuri parannus edelliseen
- Riippuvuudet laitettu kuntoon pyydetysti
- Lisätty aikaisemmassa pelissä olevia ominaisuuksia uuteen peliin. Voitu uusiokäyttää jotain
- Invokea täydennetty

## Viikko 6

- Eroteltu suuresti käyttöliittymää eri osiin
- Pelissä voi valita kolmen pelaajan vaihtoehdon
- Peliruutuja on kaksi 5x5 ja 7x5
- Lisätty kolmas kuva
- Peli kertoo kenen vuoro on pelata
- tasks.py tiedostossa korjattu coverage-report ja lisätty lint
- .coveragerc tiedosto oli lisätty jo viime viikolla
- Testikattavuus on 99%
- Clock ominaisuus main-funktiossa

## Viikko 7

- Lisätty yksinpeli mahdollisuus
- Yksinpelille tehty "tekoäly"
- Rakennetty tietokanta, joka pitää yllä pelikertoja
- Paranneltu pelin esteettistä ulkonäköä
- Luotu luokka Spritet korvaamaan aikaisemmin luokkia:
  - Nalle
  - Pupu
  - White
  - PojanAmongus
- Lisätty taskeihin: build. Tämä tekee tietokannan
