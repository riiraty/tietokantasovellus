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

### Kirjautuminen ja uuden tunnuksen luominen

### Keskusteluketjujen toiminnallisuudet

Uusi aloitus, uusi kommentti, muokkaustoiminto, poistotoiminto, ketjujen tarkastelu

### Hakutoiminnallisuudet