# Käyttötapaukset

## Keskusteluketjujen listaus

Käyttäjä voi tarkastella aiemmin aloitettuja keskusteluketjuja linkistä *Posts*. Sivulla näytetään 25 tuoreinta (viimeksi päivitettyä) ketjua. Listauksessa nähdään ketjun otsikko, kirjoittaja ja ajankohta ketjun luomiselle.

#### SQL-kysely:
```SQL
SELECT thread.id, thread.title, user.username, thread.modification_time
FROM thread
JOIN user ON user.id = thread.owner_id
ORDER BY thread.modification_time DESC
LIMIT 25;
```

## Yksittäisen ketjun tarkastelu

Käyttäjä voi avata keskusteluketjun omalle sivulleen klikkaamalla aloitusta keskustelujen listauksessa. Aloitukseen liittyvät kommentit listataan näkyviin.

#### SQL-kyselyt:
Haluttu ketju tietokannasta:
```SQL
SELECT * FROM thread WHERE id = ?;
```
Ketjuun kuuluvat postaukset:
```SQL
SELECT * FROM post
WHERE thread_id = ?
ORDER BY post_time;
```

## Käyttäjätilin luominen

Käyttäjä voi luoda itselleen käyttäjätilin linkistä *Sign up* täyttämällä lomakkeelle halutun uniikin käyttäjätunnuksen (3-26 merkkiä [a-zA-Z0-9_]) ja salasanan (7-256 merkkiä [0-9a-zA-Z@$!%*#?&] sisältäen numeron, kirjaimen ja erikoismerkin. 

#### SQL-kysely:
Onko tietokannassa haluttu käyttäjänimi käytössä:
```SQL
SELECT TOP 1 * FROM account
WHERE username = ?;
```
Jos ei, lisätään uusi käyttäjä:
```SQL
INSERT INTO account (username, password)
VALUES (?, ?);
```

## Käyttäjätilille kirjautuminen

Käyttäjä voi kirjautua tililleen linkistä *Login*. Kirjautumiseen vaaditaan käyttäjätunnus ja salasana. 

###### SQL-kysely:
Etsitään tietokannasta rivi, jossa syötetyt käyttäjätunnus ja salasa:
```SQL
SELECT TOP 1 * FROM account
WHERE username = ? AND password = ?;
```

## Uuden keskusteluketjun aloittaminen

Kirjautunut käyttäjä voi luoda uuden keskusteluketjun linkistä *Add new*. Lomakkeen kenttiin kirjoitetaan otsikko ja aloituksen sisältö. Otsinkon pituus voi olla 3-60 merkkiä, sisällön pituus voi olla 3-280 merkkiä, molemmissa on kielletty pelkkää whitespacea sisältävä syöte.

#### SQL-kyselyt:
Uuden ketjun luominen:
```SQL
INSERT INTO thread (title, owner_id)
VALUES (?, ?);
```
Uuden aloituksen luominen:
```SQL
INSERT INTO post (content, account_id, thread_id)
VALUES (?, ?, ?);
```

## Vanhan keskusteluketjun kommentoiminen

Kirjautunut käyttäjä voi kommentoida aiemmin tehtyä aloitusta tai kommenttia. 

#### SQL-kysely:
Kuten yllä ketjun aloitustekstin luominen

## Oman aloituksen tai kommentin muokkaaminen

Kirjautunut käyttäjä voi muokata aiemmin lisäämiään aloituksia tai kommentteja. Muut käyttäjät näkevät, että tekstiä on muokattu. Ketjun otsikkoa ei voi muokata.

#### SQL-kysely:
```SQL
UPDATE post
SET content = ?
WHERE id = ?;
```

## Oman aloituksen tai kommentin poistaminen

Kirjautunut käyttäjä voi poistaa aloittamansa keskusteluketjun tai oman kommentin.

Ketjun poistaminen:
```SQL
DELETE FROM thread
WHERE id = ?;
```
Mitä seuraa kommenttien poistaminen:
```SQL
DELETE FROM post
WHERE thread_id = ?;
```
Yksittäisen aloituksen tai kommentin poistaminen:
```SQL
DELETE FROM post
WHERE id = ?;
```

## Käyttäjän keskusteluhistorian tarkastelu

Käyttäjä voi tarkastella omalla tai toisen käyttäjän käyttäjäsivulla listausta keskusteluista, joihin tämä on osallistunut. Käyttäjäsivulle pääsee klikkaamalla käyttäjän nimeä tai hakutoiminnon kautta.

#### SQL-kyselyt:
Käyttäjä tietokannasta:
```SQL
SELECT FROM account
WHERE id = ?;
```
Kahdeksan viimeisintä aloitusta tai kommenttia (eri ketjuihin):
```SQL
SELECT FROM post
WHERE id IN (
  SELECT MAX(id) FROM post
  WHERE account_id = ?
  GROUP BY thread_id)
ORDER BY post_time DESC
LIMIT 8;
```
Kaikki käyttäjän aloittamat ketjut:
```SQL
SELECT FROM thread
WHERE owner_id =?;
```

## Hakutoiminto

Käyttäjä voi hakusanan avulla etsiä käyttäjiä, kommentteja ja ketjuja.

Käyttäjät:
```SQL
SELECT * FROM accont
WHERE username LIKE '%?%';
```
Kommentit:
```SQL
SELECT * FROM post
WHERE content LIKE '%?%';
```
Ketjut:
```SQL
SELECT FROM thread
WHERE title LIKE '%?%';
```
