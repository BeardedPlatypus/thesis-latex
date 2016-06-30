# Definitie van Licht

---
# Leiddraad
## Definitie Licht
## Beperking tot lichten met een eindige invloed (plaatje)
## Conclusie / eigenschappen
...

Zoals eerder benoemd, draait de kern van deze thesis om het optimaliseren van
het aantal lichtberekeningen in real-time toepassingen. Om deze reden is het 
belangrijk om het concept licht zoals gebruikt in deze thesis te definieren. 
Wanneer er gesproken wordt van een licht, of een lichtbron zal altijd gedoeld 
worden op een eindige puntlichtbron.

In de fysische wereld zijn lichten niet eindig maar zullen met grotere afstand 
een invloed van 0 benaderen. In veel real time toepassingen wordt afgestapt van
deze fysische werkelijkheid. Op een afstand groter dan $r$ wordt aangenomen
dat een licht geen invloed meer zal uitoefenen. 
Dit leidt tot een voorstelling als weergegeven in figuur ...
Hierbij is de invloed in de oorsprong gelijk aan $1$ en de invloed op een 
afstand groter dan $r$ gelijk aan 0. Hoe de invloed van 1 naar 0 vervalt 
wordt gemodeleerd met afstands attenuatie functies. 
In figuur ...
is de werkelijke afstands attenuatie functie weergeven en twee veel gebruikte 
afstandsattenuatie functies binnen real-time toepassingen. 

Dit alles leidt ertoe dat we een lichtbron kunnen definieren als de set van de 
volgende eigenschappen:

* De positie in $xyz$ ten opzichte van een coordinatenstelsel met oorsprong $O$
* Een afstand $r$ die de invloed van de lichtbron bepaald
* Een intensiteit die de kleur en kracht van de lichtbron bepaald
* Een afstandsattenuatiefunctie die het verval van invloed moduleert

