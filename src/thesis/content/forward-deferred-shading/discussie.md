# Conclusie

Uit alle grafieken blijkt dat de gemiddelde executietijd kleiner is voor 
deferred shading dan voor forward shading. Echter beide technieken hebben een
zelfde tijdscomplexiteit ten opzichte van het aantal lichten. 

Deferred shading heeft als bijkomend voordeel dat de executietijd consistenter
is. Dit is een belangrijke eigenschap voor game-engines, waar een conistente
framerate belangrijk is voor de menselijke interpretatie, als ook voor het 
verdelen van de berekeningstijd over de verschillende subsystemen.

Tegenover de verbetering in de executietijd staat wel dat een set van texturen
met een grootte gelijk aan de viewport bijgehouden dient te worden. Dit betekent
dat deferred shading een grotere geheugenvoetafdruk heeft. Het aantal texturen
dat bijgehouden dient te worden is direct afhankelijk van de complexiteit
van de shader. 

Tevens maakt het gebruik van een GBuffer bij deferred shading transparantie
onmogelijk, doordat het niet mogelijk is om meerdere lagen geometrie op te
slaan. Deferred shading is dus beperkt tot slechts ondoorzichtige geometrie.

Het laatste minpunt is dat anti-aliasing niet meer triviaal ondersteun wordt.
Binnen de shading pass is het niet mogelijk om sub-pixels te bemonsteren, gezien
ook deze data expliciet opgeslagen moet worden.


# Discussie

## Rasterisatie van lichtvolumes

Zoals vermeld in het sectie \ref{sec:fds-algorithm}, is het mogelijk om de 
lichtvolumes te rasteriseren, en vervolgens per licht slechts voor deze 
fragmenten de lichtberekening uit te voeren. Dit verlaagd het aantal
lichtberekeningen ten opzichte van de implementatie in `nTiled`. 
Het heeft echter als nadeel dat dit de geheugenbandbreedte significant vergroot.
In plaats dat de texturen eenmalig per fragment bemonsterd worden, worden deze
dan in het slechtse geval even vaak bemonsterd als er lichten in de scene zijn.

Doordat de geheugenbandbreedte binnen een grafische kaart beperkt is kan dit 
een knelpunt worden. Helemaal indien de shader complex is, en de GBuffer 
veel attributen dient op te slaan.

De effecten hiervan zijn niet ge\"evalueerd in deze thesis, er kan echter
aangenomen worden dat dit de executietijd verlaagd zou hebben.

## Ondersteunen van transparantie

Transparantie kan niet worden ondersteund met een standaard deferred shading
implementatie. Het is onrealistisch om per transparantie laag, een extra 
GBuffer bij te houden, gezien elke GBuffer een vergelijkbare geheugenvoetafdruk
bezit. Binnen veel moderne engines wordt dit ondersteund door een aparte 
forwaardse renderingstap uit te voeren voor de transparante objecten, nadat
de ondoorzichtige objecten gerenderd zijn.

## Ondersteunen anti-aliasing

Het bemonsteren van subpixels binnen forward shading is triviaal. 
Binnen deferred shading is het echter niet meer mogelijk om subpixels te bemonsteren
zonder dat de data hiervan opgeslagen wordt in de GBuffer. 
Er zijn verschillende aanpakken voorgesteld die anti-aliasing mogelijk maken
binnen een deferred pijplijn.\cite{lauritzen2010deferred}

## Alternatieven voor deferred shading

Er zijn verschillende alternatieven voorgesteld die elk op verschillende 
manieren de nadelen besproken in de conclusie proberen te verhelpen.
Lighting pre-pass\cite{engel2009light}, en vergelijkbare algoritmes
bouwen verder op deferred shading, met als belangrijkste doel het 
geheugenverbruik en de geheugenbandbreedte te verminderen.

In het volgende hoofdstuk zal ingegaan worden op Tiled shading, met als doel
om de geheugenbandbreedte te verlagen in vergelijking tot deferred shading 
waarbij de lichtvolumes gerasteriseerd worden.

