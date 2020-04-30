# Sovelluksen asennus- ja käyttöohje

## Asennusohje

### Asentaminen paikallisesti

Kloonaa repositorio omalle koneellesi ja siirry juurikansioon.

Luo virtuaaliympäristö komennolla:

```python3 -m venv venv```

Ja ota se käyttöön komennolla:

```source venv/bin/activate```

Asenna riippuvuudet komennolla:

```pip install -r requirements.txt```

Käynnistä sovellus komennolla:

```python run.py```

Sovellus käynnistyy localhostin porttiin 5000, eli voit tarkastella sitä menemällä selaimella osoitteeseen <http://localhost:5000>

### Asentaminen Herokuun

Sinulla tulee olla käyttäjätili Herokussa.

Luo sovellukselle paikka Herokuun komennolla:

```heroku create oman-sovelluksen-nimi```

Jos jätät nimen pois komennosta, Heroku luo sovellukselle satunnaisen nimen.

Lisää paikalliseen versionhallintaan tieto Herokusta:

```git remote add heroku https://git.heroku.com/oman-sovelluksen-nimi.git```

Lähetä projekti Herokuun komennolla: 

```git add . git commit -m "initial commit" git push heroku master```

Lisää sovelluksen käyttöön tieto Herokusta komennolla:

```heroku config:set HEROKU=1```

Luo tietokanta Herokuun komennolla:

```heroku addons:add heroku-postgresql:hobby-dev```



## Käyttöohje

Forum on yksinkertainen keskustelufoorumi, missä rekisteröityneet käyttäjät voivat aloittaa uusia keskuteluja sekä kommentoida ja tallentaa vanhoja ketjuja. Ilman käyttäjätiliä on mahdollista tarkastella sisältöä osallistumatta. 

### Keskusteluketjujen ja käyttäjien tarkastelu

Voit tarkastella tuoreimpia keskusteluketjuja yläpalkin linkistä _Posts_. Ketjun otsikkoa klikkaamalla voit avata näkyviin keskustelun. Pitkät keskusteluketjut näytetään usealla sivulla, ketjun oikeasta alakulmasta voit navigoida sivujen välillä. Käyttäjänimen klikkaaminen avaa kyseisen käyttäjän oman sivun.

Käyttäjäsivulla näet ajankohdan, jolloin kyseinen käyttäjä liittyi Forumille. _Recent activity_ näyttää viisi viimeisintä keskustelua, joihin käyttäjä on osallistunut. _Post History_ listaa kaikki käyttäjän aloittamat keskustelut uusimmasta vanhimpaan, kerrallaan näytetään viisi keskustelua.


### Käyttäjätilin luominen ja kirjautuminen

Keskustelujen aloittaminen ja kommentoiminen vaatii käyttäjätunnukset. Voit luoda käyttäjätunnukset yläpalkin linkistä _Sign up_. Lomakkeelle tulee täyttää haluttu käyttäjänimi, jonka pituus voi olla 3-26 merkkiä, joiden on oltava numeroita, kirjaimia tai alaviivoja. Käyttäjänimen on oltava uniikki, eli toisella käyttäjällä ei voi olla samaa käyttäjänimeä. Lomakkeelle tulee täyttää myös haluttu salasana, jonka pituus on vähintään 7 merkkiä, joiden joukossa on oltava vähintään yksi kirjain, numero ja erikoismerkki (@$!%*#?&). Salasana tulee toistaa varmistuskenttään. Jos käyttäjätunnuksen luominen onnistuu, sinut kirjataan automaattisesti sisään.

Jos olet jo luonut käyttäjätunnuksen, voit valita yläpalkista linkin _Log in_. Anna käyttäjätunnuksesi ja kirjautu sisään painamalla nappia _login_. Voit peruuttaa kirjautumatta napista _cancel_ tai valitsemalla yläpalkista toisen sivun. 


### Keskusteluketjujen toiminnallisuudet
Kirjautuneena käyttäjänä voit pelkän keskustelujen tarkastelun sijaan tuottaa itse sisältöä ja tallentaa keskusteluja. Jos et ole kirjautunut, ja yrität käyttää kirjautumista vaativaa toimintoa, sinua pyydetään kirjautumaan sisään.

##### Uusi keskusteluketju
Voit aloittaa uuden keskustelun yläpalkin linkistä _New_. Otsikon pituuden on oltava 3-60 merkkiä, se ei voi koostua pelkistä välilyönneistä. Aloituksen sisällön on oltava 3-280 merkkiä, se ei voi koostua pelkistä välilyönneistä. Painamalla nappia _add a new post_, lomakkeelle syöttämäsi sisältö tallennetaan. Voit nyt nähdä uuden keskustelusi Most recent listauksessa. 

##### Ketjun kommentoiminen
Voit osallistua keskusteluun kommentoimalla. Painamalla keskusteluketjun otsikkoa saat näkyviin kommentit. Pitkät keskusteluketjut näytetään usealla sivulla, ketjun oikeasta alakulmasta voit navigoida sivujen välillä. Tuoreimman kommentin sisältävältä sivulta löydät alalaidasta napin _+ add a comment_, josta voit lisätä ketjun jatkoksi oman kommenttisi. Kommentin sisällön on oltava 3-280 merkkiä, se ei voi koostua pelkistä välilyönneistä.

##### Kommentin muokkaaminen ja poistaminen
Voit muokata ja poistaa omia kommenttejasi. Keskusteluketjussa omien kommenttien kohdalla näet valikot _edit_ ja _delete_. Painamalla _delete_ voi poistaa kommentin, valintasi vahvistetaan ennen lopullista poistoa. Painamalla _edit_ sinulle näytetään muokkauslomake.

Muokkauslomakkeella on vanha kommenttisi, voit muokata tai lisätä tekstiä. Voit tallentaa muokatun kommentin painamalla _save changes_. Jos et halua tallentaa muutoksia, paina _cancel_ tai siirry yläpalkin kautta jollekin muulle sivulle. Muut käyttäjät näkevät, jos kommenttiasi on muokattu. Jos haluat sittenkin muokkaamisen sijaan poistaa kommentin, paina _delete_ ja vahvista valintasi. Kommentin poistaminen on lopullista, et voi palauttaa poistamaasi kommenttia.

##### Kokonaisen keskusteluketjun poistaminen
Itse aloittamaasi keskusteluketjua tarkastellessa näet oikeassa yläkulmassa napin _delete the thread_. Tästä painamalla voit kerralla poistaa ketjun ja kaikki sen kommentit. Huomioi, että myös muiden käyttäjien tuottama sisältö poistuu lopullisesti. Jos poistat vain oman aloituksen ja kommentit, muut käyttäjät voivat jatkaa keskustelua. Ketju löytyy tällöin edelleen oman sivusi historiasta.

##### Keskustelun arkistoiminen
Voit tallentaa keskusteluketjun avaamalla sen ja painamalla nappia _archive_. Aiemmin tallentamasi keskustelut löytyvät yläpalkin linkistä _Archive_. Huomioithan, että jos keskustelun aloittanut käyttäjä poistaa ketjun, se poistuu myös arkistostasi. Voit itse poistaa ketjuja arkistosta painamalla nappia _remove_.

### Hakutoiminnallisuus
Yläpalkista löytyy hakukenttä, jonka avulla voit etsiä Forumilta käyttäjiä, kommentteja ja keskusteluketjuja.

##### Hakusanalla löytyvät:
* Käyttäjät, joiden käyttäjänimestä löytyy hakusana
* Kommentit, joiden sisällöstä löytyy hakusana
* Kommenttiketjut, joiden otsikosta löytyy hakusana

Hakusana voi koostua useasta sanasta. Tuloksissa näkyvät kaikki kohteet, joiden osana hakusana on, esim. hakusana _kahvi_ voi antaa tuloksia joissa on sanoja _kahvittelu_, _päiväkahvi_, _suklaakahvijäätelö_...
