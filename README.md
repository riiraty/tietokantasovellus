# Tietokantasovellus
Tietojenkäsittelytieteen aineopintojen harjoitustyö, Helsingin yliopisto, kevät 2020

## Keskustelufoorumi
Harjoitustyö on yksinkertainen keskustelufoorumi.
Tarkempi kuvaus tietokantakaavioineen löytyy [täältä](https://github.com/riiraty/tietokantasovellus/blob/master/documentation/documentation.md).

### Sovellus Herokussa
Sovellus löytyy osoitteesta [https://afternoon-oasis-48455.herokuapp.com/](https://afternoon-oasis-48455.herokuapp.com/)

Sovellus käyttää Herokussa PostgreSQL-tietokantaa.

### Toteutetut toiminnallisuudet

#### Rekisteröityminen

* Käyttäjä voi rekisteröityä foorumille täyttämällä [lomakkeen](https://afternoon-oasis-48455.herokuapp.com/auth/signup/)
* Salasanat tallentuvat tietokantaan toistaiseksi selkokielisinä

#### Sisäänkirjautuminen

* Käyttäjä voi [kirjautua sisään](https://afternoon-oasis-48455.herokuapp.com/auth/login/) palveluun omilla tunnuksillaan
* Tieto kirjautumisesta tulee näkyviin navigointipalkkiin

#### Keskustelujen tarkastelu

* Käyttäjä näkee [listauksessa](https://afternoon-oasis-48455.herokuapp.com/posts/) 25 tuoreinta kommenttiketjua 
* Ketjun otsikko on linkki, josta voi avata ketjun näkyviin
* Yksittäisen ketjun näkymässä listataan ketjun postaukset

#### Käyttäjien tarkastelu

* Yksittäisen käyttäjän sivulla voi tarkastella tuoreimpia kommentteja ja postaushistoriaa
* Osa keskeneräistä hakutoimintoa

#### Uuden kommenttiketjun luominen

* Kirjautunut käyttäjä voi aloittaa uuden kommenttiketjun täyttämällä [lomakkeen](https://afternoon-oasis-48455.herokuapp.com/posts/threads/new/)
* Uusi ketju ja ensimmäinen postaus tallennetaan tietokantaan

#### Vanhan ketjun kommentoiminen

* Kirjautunut käyttäjä voi lisätä ketjuun kommentin täyttämällä lomakkeen
* Ketjuun päivittyy muokkausajankohdaksi uusimman postauksen luomisajankohta

#### Omien sisältöjen hallinnointi

* Kirjautunut käyttäjä näkee yksittäisen ketjun listauksessa omien kommenttiensa kohdalla napit postauksen muokkausta ja poistoa varten
* Kommentin muokkaaminen päivittää vastaavan rivin tietokannassa
* Kommentin poisto varmistetaan käyttäjältä, varmistus poistaa vastaavan rivin tietokannasta
* Ketjun aloittanut käyttäjä voi poistaa koko ketjun, ja kaikki siihen liittyvät kommentit
* Ketjun poisto varmistetaan käyttäjältä

#### Hakutoiminto

* Navigointipalkkiin on lisätty hakukenttä, mutta toiminnallisuus on vielä kesken

#### Muuta

* Sivun ylälaitaan on toteutettu navigointia varten valikko
* Lomakkeiden syötteillä on validointeja, virheviestit näytetään käyttäjälle
* Sovellukseen on lisätty Bootstrapin tyylejä
* Toiminnoista näytetään käyttäjälle flash-viestejä
