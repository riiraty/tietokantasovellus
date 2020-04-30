# Sovelluksen rajoitteet ja puutteet palautushetkellä

### Tietoturvariskit ja ylläpitoa vaikeuttavat puutteet

* Salasanat on tallennettu tietokantaan selkokielisinä. 

* Sovellus ei käytä migraatiotyökalua tietokantamuutoksia varten.

* Testaus ja deployment ei automatisoitu, ei edes ole testejä.

* Login_managerin kirjautumiskehotteen jälkeisen redirectin url 'next' ei validointia.

* Ei toteutettu kunnon rooleja, moderointioikeudet käyttäjänimellä 'MODERATOR', pystyy poistamaan kommentteja ja ketjuja.

* Hakutuloksia ei ole sivutettu.

### Käytettävyys ja ulkoasu

* Kommentin lisäämisen jälkeen käyttäjä palaa ketjun ensimmäiselle sivulle, eikä tuoreimpien kommenttien sivulle

* Sivutukset pilkottu turhan pieniksi toimintojen havainnollistamiseksi, kunnes tarkastus ohi.

* Käyttäjäsivulla historia sivutettu, mutta käyttäjä ja viimeaikaiset ladataan joka sivulle uusiksi vs. historian voisi avata omalle sivulle profiilista. 

* Uuden postauksen tai kommentin _content_ ei säilytä käyttäjän formatointia.

* Aikavyöhykkeitä ei huomioitu, käyttäjälle näytetään UTC mukainen ajankohta tallennuksille.

* Poistotoimintojen vahvistusikkuna ei tyylitelty.

* Tooltipeissä ei Bootstrapin tyyli toimi.

### Toteuttamattomia toimintoja

* Salasanan vaihtaminen.

* Oman profiilin muokkaus, esim. esittelyteksti, kuva.

* Käyttäjätilin poistaminen.

* _Delete all_ -toiminto oman sisällön tyhjentämistä varten, käyttäjätilin poiston yhteydessä tai muuten vaan.

* Tagien lisääminen ketjuihin tai kommentteihin, niiden avulla hakeminen.

* Kommenteista tykkääminen.

* Toisten käyttäjien seuraaminen.