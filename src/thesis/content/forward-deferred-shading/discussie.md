# Conclusie

Uit alle grafieken blijkt dat de gemiddelde uitvoeringstijd kleiner is voor 
Deferred Shading dan voor Forward Shading. Echter beide technieken hebben een
zelfde tijdscomplexiteit ten opzichte van het aantal lichten. 

Deferred Shading heeft als bijkomend voordeel dat de uitvoeringstijd consistenter
is. Dit is een belangrijke eigenschap voor game-engines, waar een consistente
framerate belangrijk is voor de menselijke interpretatie, als ook voor het 
verdelen van de rekentijd over de verschillende subsystemen.

Tegenover de verbetering in de uitvoeringstijd staat wel dat een set van texturen
met een grootte gelijk aan het zichtvenster bijgehouden dient te worden. Dit betekent
dat Deferred Shading een grotere geheugenvoetafdruk heeft. Het aantal texturen
dat bijgehouden dient te worden is direct afhankelijk van de complexiteit
van de shader. Wanneer deze steunt op meer attributen dienen meer texturen
bijgehouden te worden.

Het gebruik van een GBuffer bij Deferred Shading maakt transparantie
onmogelijk, doordat per laag een aparte GBuiffer bijgehouden zou moeten worden.
Dit is door geheugengebruik van de GBuffer onmogelijk.
Deferred Shading is dus beperkt tot ondoorzichtige geometrie.

Het laatste minpunt is dat anti-aliasing niet meer triviaal ondersteund wordt.
Binnen de belichtingsstap is het niet mogelijk om arbitrair sub-pixels te bemonsteren, gezien
ook deze data expliciet opgeslagen moet worden in de geometriestap. Voor de ondersteuning
van anti-aliasing dient de GBuffer uitgebreid worden om subpixels op te slaan.


# Discussie

## Rasterisatie van lichtvolumes

Zoals vermeld in het sectie \ref{sec:fds-algorithm}, is het mogelijk om de 
lichtvolumes te rasteriseren, en vervolgens per licht slechts voor deze 
fragmenten de lichtberekening uit te voeren. Dit verlaagd het aantal
lichtberekeningen ten opzichte van de implementatie in `nTiled`. 
Het heeft echter als nadeel dat de geheugenbandbreedte significant vergroot wordt.
De texturen worden niet langer eenmalig per fragment bemonsterd, maar 
in het slechtste geval even vaak bemonsterd als er lichten in de \mbox{sc\`ene} zijn.

Doordat de geheugenbandbreedte binnen een grafische kaart beperkt is kan dit 
een knelpunt worden. Helemaal indien de shader complex is, en de GBuffer 
veel attributen dient op te slaan.
De effecten hiervan zijn niet ge\"evalueerd in deze thesis, er kan echter
aangenomen worden dat deze optimalisatie de uitvoeringstijd van Deferred Shading verlaagd zou hebben.

## Ondersteunen van transparantie {#sec:fds-transparantie}

Transparantie kan niet worden ondersteund met een standaard Deferred Shading
implementatie. Het is onrealistisch om per transparantie laag een extra 
GBuffer bij te houden, gezien elke GBuffer een vergelijkbare geheugenvoetafdruk
bezit. Binnen veel moderne game-engines wordt dit ondersteund door een aparte 
Forward Shading renderstap uit te voeren voor de transparante objecten, nadat
de kleuren van de ondoorzichtige objecten berekend zijn.

## Ondersteunen anti-aliasing

Het bemonsteren van subpixels binnen Forward Shading is triviaal. 
Binnen Deferred Shading is het echter niet mogelijk om subpixels arbitrair te bemonsteren
zonder dat de data hiervan opgeslagen moet worden in de GBuffer. 
Er zijn verschillende aanpakken voorgesteld om anti-aliasing mogelijk te maken
binnen Deferred Shading\cite{lauritzen2010deferred}.

## Alternatieven voor Deferred Shading

Er zijn verschillende alternatieven voorgesteld die elk op verschillende 
manieren de nadelen besproken in de conclusie proberen te verhelpen.
Lighting pre-pass\cite{engel2009light}, en vergelijkbare algoritmes
bouwen verder op deferred shading, met als belangrijkste doel het 
geheugenverbruik en de geheugenbandbreedte te verminderen.

In het volgende hoofdstuk zal ingegaan worden op Tiled shading, met als doel
om de geheugenbandbreedte te verlagen in vergelijking tot deferred shading 
waarbij de lichtvolumes gerasteriseerd worden.

