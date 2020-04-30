# Tietokantasovellus
Aineopintojen harjoitustyö: Tietokantasovellus, Tietojenkäsittelytieteen osasto, Helsingin yliopisto, kevät 2020.

Intermediate Studies Project: Database Appliation, The Department of Computer Science, University of Helsinki, spring 2020.

## Keskustelufoorumi

[Dokumentaatio](https://github.com/riiraty/tietokantasovellus/blob/master/documentation/documentation.md).

[Käyttötapaukset ja tietokanta](https://github.com/riiraty/tietokantasovellus/blob/master/documentation/kayttotapaukset.md)

[Rajoitteet ja puutteet](https://github.com/riiraty/tietokantasovellus/blob/master/documentation/rajoitteet_ja_puutteet.md)

### Sovellus Herokussa
Sovellus löytyy osoitteesta [https://salty-meadow-68518.herokuapp.com/](https://salty-meadow-68518.herokuapp.com/)

Sovellus käyttää Herokussa PostgreSQL-tietokantaa.

[Asennus- ja käyttöohje](https://github.com/riiraty/tietokantasovellus/blob/master/documentation/asennus-_ja_kayttoohje.md)

### Toteutetut toiminnallisuudet

#### Rekisteröityminen

* Käyttäjä voi rekisteröityä foorumille täyttämällä lomakkeen
* Salasanat tallentuvat tietokantaan toistaiseksi selkokielisinä

#### Sisäänkirjautuminen

* Käyttäjä voi kirjautua sisään palveluun omilla tunnuksillaan
* Tieto kirjautumisesta tulee näkyviin navigointipalkkiin

#### Keskustelujen tarkastelu

* Käyttäjä näkee listauksena sivulla _Posts_ 25 tuoreinta kommenttiketjua 
* Ketjun otsikko on linkki, josta voi avata ketjun näkyviin
* Ketjun aloittajan käyttäjänimi on linkki käyttäjäsivulle
* Yksittäisen ketjun näkymässä listataan ketjun kommentit
* Ketjunäkymän sivutus näyttää kerrallaan seitsemän kommenttia, painikkeista voi navigoida sivujen välillä

#### Käyttäjien tarkastelu

* Yksittäisen käyttäjän sivulla voi tarkastella tuoreimpia kommentteja viiteen viimeaikaiseen ketjuun ja postaushistoriaa jossa näkyy viisi ketjua kerrallaan sivutettuna

#### Uuden kommenttiketjun luominen

* Kirjautunut käyttäjä voi aloittaa uuden kommenttiketjun navigointipalkin linkistä _New_
* Uusi ketju ja ensimmäinen postaus tallennetaan tietokantaan, käyttäjä tallennetaan ketjun omistajaksi

#### Vanhan ketjun kommentoiminen

* Kirjautunut käyttäjä voi lisätä ketjuun kommentin täyttämällä lomakkeen
* Ketjuun päivittyy muokkausajankohdaksi uusimman postauksen luomisajankohta

#### Omien sisältöjen hallinnointi

* Kirjautunut käyttäjä näkee yksittäisen ketjun listauksessa omien kommenttiensa kohdalla napit postauksen muokkausta ja poistoa varten
* Kommentin muokkaaminen päivittää vastaavan rivin tietokannassa
* Muut käyttäjät näkevät, että kommenttia on muokattu
* Kommentin poisto varmistetaan käyttäjältä, varmistus poistaa vastaavan rivin tietokannasta
* Ketjun aloittanut käyttäjä voi poistaa koko ketjun, ja kaikki siihen liittyvät kommentit
* Ketjun poisto varmistetaan käyttäjältä

#### Hakutoiminto

* Navigointipalkkin hakukentän syötteen perusteella etsitään käyttäjänimen, kommentin sisällän ja ketjun otsikon osalta tietokannasta osuvat rivit
* Hakutulokset esitetään kootusti omalla sivullaan

#### Arkistointitoiminto

* Kirjautunut käyttäjä voi tallentaa keskusteluketjuja ketjussa olevasta _archive_ napista
* Omaa arkistoa voi tarkastella sivulla _Archive_ ja siitä voi poistaa keskusteluketjuja

#### Muuta

* Sivun ylälaitaan on toteutettu navigointia varten valikko
* Lomakkeiden syötteillä on validointeja, virheviestit näytetään käyttäjälle
* Sovellukseen on lisätty Bootstrapin tyylejä
* Toiminnoista näytetään käyttäjälle flash-viestejä
* Alkeellinen moderointi 
