# Tietokantasovellus
Tietojenkäsittelytieteen aineopintojen harjoitustyö, Helsingin yliopisto, kevät 2020

## Keskustelufoorumi
Harjoitustyö on yksinkertainen keskustelufoorumi.
Tarkempi kuvaus tietokantakaavioineen löytyy [täältä](https://github.com/riiraty/tietokantasovellus/blob/master/documentation/documentation.md).

### Sovellus Herokussa
Sovellus löytyy osoitteesta [https://afternoon-oasis-48455.herokuapp.com/](https://afternoon-oasis-48455.herokuapp.com/)

Sovellus käyttää Herokussa PostgreSQL-tietokantaa.

### Toteutettu toiminnallisuus: 
* Käyttäjä voi kirjautua sisään polulla [/auth/login/](https://afternoon-oasis-48455.herokuapp.com/auth/login/) ('hello', 'test')
* Sivun ylälaidassa on linkki kirjautumislomakkeelle, tai tieto kirjautuneesta käyttäjästä ja linkki uloskirjautumista varten
* Salasanat on toistaiseksi tallennettu tietokantaan selkokielisinä
* Kirjautunut käyttäjä voi lisätä foorumille uuden aloituksen täyttämällä lomakkeen polulla [/posts/new](https://afternoon-oasis-48455.herokuapp.com/posts/new)
* Aloituksen pituuden on oltava 3-280 merkkiä
* Lisätty aloitus tallentuu tietokantaan
* Aloituksen yhteyteen tallentuu tieto sen lisänneestä käyttäjästä
* Tehdyt aloitukset listautuvat polulla [/posts/](https://afternoon-oasis-48455.herokuapp.com/posts/) taulukkoon, jossa näkyy aloituksen sisältö, aloittajan käyttäjänimi ja luomisajankohta
* Sivun ylälaitaan on toteutettu navigointia varten valikko
