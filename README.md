# Pygame-2DPlatform-Starter
En enkel starter pakke for deg som har lyst til å lage et 2d-platfom spill. Pakken inkluderer:
* En spiller
* En type Platform 
* Enkel tyngdekraft
* Kollisjon mellom objekter

## Hvordan bruke pakken for første gang
### last ned pygame 
Hvis du ikke har pygame installert, må du skrive `pip install pygame` i terminalen. 

### Kjør programmet
Gå i en IDE og kjør `Index.py`. Dette vil lage et nytt vindu, som spillet kjøres i. Du beveger deg med `wasd` 

<img width="405" alt="Skjermbilde 2020-01-18 kl  16 51 09" src="https://user-images.githubusercontent.com/26656069/72666477-f5730680-3a12-11ea-8938-30837d26bdb4.png">

Hvis du bruker MacOS kan du oppleve problemer med å lukke det nye vinduet. Da må tvinge avslutning av python, og heller kjøre programmet fra terminalen.


## Pakke elementer forklart
### Collitions (kolisjoner)
Inneholder 2 lister som blir sjekket opp mot hverandre. Hvis et element i den ene listen koliderer med et element fra den andre listen, registreres dette. Dette fører til at disse elementene ikke kan gå gjennom hverandre. Vi kan sjekke hva som har kolidert i `collided` dictionarien.

### SimplePlatform 
Når du **lager** en platform trenger du å definere: 
* Bredde
* Høyde
* x posisjon
* y posisjon 
* Navn på platformen   _(Brukes til å sjekke kollisjoner)_

Når du **tegner** en platform må du definere:
* Hvor du skal tegne _(Ofte til sjermen `screen`)_
* Fargen


