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

Hvis du bruker MacOS kan du oppleve problemer med å lukke det nye vinduet. Da må tvinge avslutning av python, og heller kjøre programmet fra terminalen. 


## Pakke elementer forklart
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

### SimplePlayer 
Spilleren 

