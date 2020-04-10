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
* Uusi käyttäjä voi rekisteröityä palveluun polulla [/auth/signup/](https://afternoon-oasis-48455.herokuapp.com/auth/signup/)
* Uusi käyttäjä tallennetaan tietokantaan
* Kirjautunut käyttäjä voi lisätä foorumille uuden aloituksen täyttämällä lomakkeen polulla [/posts/new](https://afternoon-oasis-48455.herokuapp.com/posts/new)
* Uusi aloitus tallennetaan tietokantaan
* Kirjautunut käyttäjä voi muokata omia aloituksiaan polulla /posts/<post.id>
* Muokattu teksti päivitetään tietokantaan
* Kirjautunut käyttäjä voi poistaa oman aloituksen polulla /posts/delete/<post.id>
* Poistettua aloitusta vastaava rivi poistetaan tietokannasta
* Lomakkeiden syötteille on validoinnit, virheviestit näytetään käyttäjälle
* Salasanat on toistaiseksi tallennettu tietokantaan selkokielisinä
* Aloituksen yhteyteen tallentuu tieto sen lisänneestä käyttäjästä
* Tehdyt aloitukset listautuvat polulla [/posts/](https://afternoon-oasis-48455.herokuapp.com/posts/) taulukkoon, jossa näkyy aloituksen sisältö, aloittajan käyttäjänimi ja luomisajankohta
* Kirjatuneen käyttäjän omien aloitusten yhteydessä on listauksessa linkki, josta pääsee muokkaamaan tekstiä
* Kirjautuneen käyttäjän omien aloitusten yhteydessä on varmituksella varustettu linkki, josta oman aloituksen voi poistaa
* Sivun ylälaidassa on linkit kirjautumis- ja rekisteröitymislomakkeille, tai tieto kirjautuneesta käyttäjästä ja linkki uloskirjautumista varten
* Sivun ylälaitaan on toteutettu navigointia varten valikko
