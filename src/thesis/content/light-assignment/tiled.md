# Tiled Shading

\input{./img/tex/ts-onderverdeling.tex}

Een eerste stap in de optimalisatie van de lichttoekenning binnen beide render 
pijplijnen is Tiled Shading. Tiled shading beperkt het aantal lichtberekeningen 
per fragment door het canvas in te delen in een rooster. Voor elk vlak wordt 
berekend welke lichten daadwerkelijk invloed hebben binnen dit vlak. Vervolgens 
worden niet meer alle lichten binnen de scene overlopen, maar wordt slechts 
gekeken naar de lichten binnen een vlak waarin een fragment valt. Dit leidt tot 
een onderverdeling van het gezichtsfrustum, zoals weergegeven in 
figuur \ref{fig:ts-onderverdeling}.  

Binnen deferred tiled shading lost deze aanpak tevens het bandbreedte probleem
op zoals deze geintroduceerd is binnen de sectie \ref{deferred-shading}. 
Binnen het oorspronkelijke algoritme werden lichten een voor een behandeld, door
het licht volume van elk licht te rasteriseren, en vervolgens data op te halen
uit de G-buffer. Binnen tiled deferred shading loopt de binneste loop over de
pixels, en kan per fragment direct opgehaald worden welke lichten invloed hebben
op het fragment in kwestie.  

De techniek zelf is al langere tijd in gebruik binnen de game industrie
(\cite{balestra2008technology}, \cite{swoboda2009deferred}). Een
formelere beschrijving en evaluatie van de resultaten kan gevonden worden in
\cite{olsson2011tiled}.  

De techniek heeft verder als voordelen voor beide renderpijplijnen dat:

* Gemeenschappelijk termen in de rendering vergelijking kunnen buiten de 
  vergelijking gehaald worden.
* Licht berekening vindt plaats op register niveau.
* Dezelfe shading functies kunnen gebruikt worden.

Verder zijn er nog enkele specifieke voorden voor zowel forwaards als deferred.
In het geval van deferred rendering:

* G-Buffers worden slechts een enkele keer per fragment gelezen
* De framebuffer wordt slechts een enkele keer naar weggeschreven.
* Fragmenten binnen dezelfde tile ondergaan dezelfde berekening.

Voor forwaards renderen:

* Lichtmanagement is losgekoppeld van de geometrie. 
* Licht data hoeft slechts een enkele keer naar de GPU worden geladen per
  scene.
* FSAA werkt zoals verwacht.

## Algoritme beschrijving

Het algoritme bestaat uit de volgende stappen:

1. Bepaal het canvas rooster dat over de gehele frame buffer valt op basis van
   een vaste vlak grootte $t = (x,y)$ bijvoorbeeld, $32 \times 32$
2. Voor elk licht, bepaal de vlakken waar het licht invloed heeft, en voeg aan
   deze vlakken de identifier van het licht toe.
3. Voer de standaard render stap uit, tot aan de fragment shader.
4. Voor elk fragment, bepaal het vlak waartoe deze behoort. Op basis van dit
   vlak bepaal de lichten die invloed hebben op dit fragment, en verzamel de
   licht contributie op basis van deze lichten.
  

### Opbouwen van het rooster

De vlakgrootte $\mathbf{s}$ is een variable waar de ontwikkelaar verantwoordelijk voor 
is. De keuze is een afweging tussen geheugen en rekentijd. Een kleiner waarde 
$s$ heeft als gevolg dat er meer geheugen nodig is voor het opslaan van het 
rooster, gezien bij een vergelijkbare grootte van canvas er meer vlakken in het
rooster bijgehouden dienen te worden. Bij het opstellen van het rooster zal 
tevens een iets grotere berekeningstijd nodig zijn, doordat elk licht aan
meer roosters toegevoegd dient te worden. Echter gezien dit een triviale stap 
is, zal de invloed op de berekeningstijd van de applicatie minimaal zijn. 
Wanneer de fragment shader bereikt is zal minder berekeningstijd nodig zijn, 
doordat er minder lichten aan elk vlak toegekend zijn, kleinere vlakken zullen
een betere benadering van lichten geven. Binnen deze thesis zal, als niet anders
vermeld is, een vlakgrootte $\mathbf{s}$ van $32 \times 32$ gebruikt zijn.  

### Licht projectie

Met de grootte van vlakken vastgesteld is het nodig om te bepalen welke lichten
invloed hebben op welke vlakken. Dit kan gedaan worden door de lichtbollen te
projecteren op de canvas, en te bepalen welke vlakken overlappen met de 
projectie.  

### Datastructuren

\input{./img/tex/ts-datastructuur.tex}

De shaders moeten instaat zijn om op te zoeken welke lichten invloed hebben op
specifieke fragmenten. Om dit instaat te stellen, wordt gebruik gemaakt van
drie lijsten:

Globale Lichtlijst
  ~ De globale lichtlijst is een simpele lijst die elk van de lichten bevat,
    met de relevante data om een licht berekening uit te voeren.
    
Vlak-licht-index-lijst
  ~ De vlak-licht-index lijst is een opeenvolging van indices die referen naar 
    lichten binnen de globale lichtlijst, om zo het gebruikte geheugen te 
    beperken. Deze is zodanig opgesteld dat elk vlak in het rooster refereert
    naar een subset van deze index-lijst doormiddel van een bepaalde afstand van
    het begin en een lengte van lichten die behoort tot dit vlak.
  
Lichtrooster
  ~ Het lichtrooster definieert de afstand en lengte van elk vlak binnen de 
    vlak-licht-index-lijst. Elk vlak heeft een unieke positie binnen het 
    lichtrooster, dat gebruik kan worden om de licht indices in de index-lijst
    op te zoeken.
    
Deze datastructuren en hun onderlinge afhankelijkheid is geillustreerd in figuur
\ref{fig:ts-datastructuur}.  

