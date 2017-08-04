# Resultaten

\input{./img/tex/ts-frames-forward.tex}
\input{./img/tex/ts-frames-deferred.tex}
\input{./img/tex/ts-lc-frames-deferred.tex}
\input{./img/tex/ts-lc-frames-example.tex}
\input{./img/tex/ts-lights.tex}
\input{./img/tex/ts-lc-light.tex}
\input{./img/tex/ts-resolution.tex}
\input{./img/tex/ts-lc-resolution.tex}

De performantie van het Tiled Shading algoritme ge\"introduceerd in de vorige
sectie, is ge\"evalueerd aan de hand van de drie \mbox{testscenes}. Hiervoor zijn de
uitvoeringstijden van na\"ief Forward Shading en Forward Tiled Shading, en
na\"ief Deferred Shading en Deferred Tiled Shading vergeleken. Daarnaast zijn
het aantal lichtberekeningen per frame van na\"ief Deferred Shading en Deferred
Tiled Shading vergeleken.

Er zal eerst gekeken worden naar de uitvoeringstijd en aantal lichtberekeningen per frame 
gedurende een  enkele uitvoering. Vervolgens wordt gekeken naar de uitvoeringstijd en
aantel lichtberekeningen als functie van het aantal lichten en de resolutie.


## Frames

De uitvoeringstijden per frame voor Forward Shading zijn weergegeven in figuur
\ref{fig:ts-frames-forward}, en de uitvoeringstijden per frame voor Deferred
Shading in figuur \ref{fig:ts-frames-deferred}. Het aantal lichtberekeningen
per frame gedurende een volledige uitvoering zijn weergegeven in figuur 
\ref{fig:ts-lc-frames-deferred}.
In elk van deze figuren geven de grafieken links de uitvoeringen weer van een 
klein aantal lichten bij een resolutie van $320 \times 320$ pixels. De rechter 
grafieken geven de  uitvoeringen met een groot aantal lichten bij een resolutie
van $2560 \times 2560$ pixels weer. Het Tiled Shading algoritme is bij de 
uitvoeringstijdmetingen uitgevoerd met een tegelgrootte van $32 \times 32$
pixels. 

In zowel de lage als hoge resolutie uitvoeringen presteert Tiled Shading beter
dan de na\"ieve implementatie. De lage resolutie uitvoeringen worden tussen de
anderhalf en twee maal sneller uitgevoerd met Tiled Shading, ten opzichte van
de na\"ieve implementatie. Hierbij is geen significant verschil waar te nemen
tussen Forward en Deferred Shading. Dit komt overeen met de resultaten van het
vorige hoofdstuk. 
Bij deze lage resolutie en klein aantal lichten kost het opbouwen van het 
rooster praktisch geen tijd. Het reduceert echter wel significant het aantal
lichtberekeningen, zoals weergegeven in figuur \ref{fig:ts-lc-frames-deferred}.
De tegelgrootte heeft slechts een kleine invloed op het aantal lichtberekeningen
per frame. Waarbij kleinere tegels leiden tot minder lichtberekeningen.

Bij een hogere resolutie en een groter aantal lichten is de invloed van het
lichttoekenningsalgoritme significanter. Alle Tiled Shading uitvoeringen worden
ongeveer viermaal sneller uitgevoerd dan de na\"ieve tegenhanger.
Tevens zijn de uitvoeringstijden voor Forward Shading consistenter. Dit is vooral 
zichtbaar in de Spaceship Indoor \mbox{sc\`ene}, fig. 
\ref{fig:ts-frames-forward:indoor-high}, waar de schommelingen afhankelijk van
de camerapositie, minder hevig zijn. Dit duidt er op dat er minder 
lichtberekeningen per fragment worden uitgevoerd, in vergelijking tot de na\"ive
implementatie, waardoor de totale uitvoeringstijd minder toeneemt wanneer een
groot aantal fragmenten op \mbox{\'e\'en} pixel vallen. Dit komt overeen met de
reductie in het aantal lichtberekeningen die waargenomen wordt in 
figuur \ref{fig:ts-lc-frames-deferred:indoor-low} en \ref{fig:ts-lc-frames-deferred:indoor-high}.

Bij hogere resoluties en meer lichten is de opbouw van het rooster de tijdsbepalende
stap. Dit is een direct gevolg van het groter aantal lichten, en de relatief bruteforce
aanpak waarmee lichten worden toegekend aan tegels. Daarnaast neemt door de 
hogere resolutie het aantal tegels ook toe, waardoor een licht met meer tegels 
zal overlappen. Hierdoor zal tevens meer tijd nodig zijn om het licht aan alle
tegels toe te wijzen. Verder is de gebruikte shader erg simpel. Bij 
een complexere shader zal een groter percentage van de uitvoeringstijd besteed
worden aan de lichtevaluatie.

Voor alle Deferred Shading uitvoeringen reduceert het Tiled Shading algoritme
het aantal berekeningen per frame met ongeveer een factor vier. Hierbij 
valt tevens op te merken dat voor de hoge resolutie, de grootte van de tegels
geen significante invloed heeft op het aantal berekeningen.

Binnen de Ziggurat City \mbox{sc\`ene}, fig. \ref{fig:ts-frames-forward:city-high} en
\ref{fig:ts-frames-deferred:city-high}, is het verschil tussen de verschillende 
camerapunten minder nadrukkelijk aanwezig. In sectie \ref{sec:fds-frames} werd
al vastgesteld dat het verschil in uitvoeringstijd tussen de camerapunten in
grootte mate afhankelijk was van het percentage pixels zonder fragmenten.
Hierbij bevat het tweede camerapunt een lager percentage lege pixels. Dit 
verschil is duidelijk waar te nemen in het aantal lichtberekeningen, fig. 
\ref{fig:ts-lc-frames-deferred:city-high}.
De fragmenten die gegenereerd worden bij de tweede camerapositie, liggen veelal
in het deel van de Ziggurat City \mbox{sc\`ene} die verlicht wordt door enkele grote lichten,
fig. \ref{fig:test-suite-ziggurat-map}. Hierdoor zal de set van lichten 
geassocieerd met deze tegels kleiner zijn. Dit effect is duidelijk zichtbaar
in figuren \ref{fig:ts-lc-frames-deferred:city-low} en \ref{fig:ts-lc-frames-deferred:city-high} 
waar het verschil in aantal lichtberekeningen bijna een factor acht is.
Dit verschil leidt ertoe dat het verschil in uitvoeringstijd kleiner is.

Het verschil in effici\"entie is het kleinst in de Piper's Alley \mbox{sc\`ene}. Dit kan
verklaard worden aan de hand van de opbouw van de \mbox{sc\`ene}. De Piper's Alley \mbox{sc\`ene}
is \mbox{\'e\'en} diepe straat, waar de lichten achter elkaar zijn geplaatst, 
zie fig. \ref{fig:test-suite-pipers-alley-map}. Wanneer gekeken wordt naar de
onderverdeling van het zichtfrustum, fig. \ref{fig:ts-grid-intro:frustum} is te
zien dat dergelijke \mbox{sc\`enes}, met veel overlappende lichtvolumes in de diepte,
leidt tot de slechtst mogelijke situatie. De tegels zullen een groot aantal lichten bevatten
door deze overlap. Hierdoor zal voor elk van de pixels in deze tegels een groot aantal 
lichtberekeningen nodig zijn. Hierdoor zullen deze tegels het tijdsgedrag van de na\"ieve
implementatie benaderen. Een vergelijkbaar effect is niet zichtbaar in de Spaceship Indoor en
Ziggurat City \mbox{sc\`enes}.


## Lichten

In figuur \ref{fig:ts-lights} zijn de gemiddelde uitvoeringstijden per frame per 
uitvoering geplot, als functie van het aantal lichten in de \mbox{sc\`ene}, voor zowel
Forward Shading, links, en Deferred Shading, rechts. In figuur \ref{fig:ts-lc-lights}
zijn het gemiddeld aantal lichtberekening per frame als functie van het aantal 
lichten in de \mbox{sc\`ene} weergegeven voor Deferred Shading . Als laatste is de 
uitvoeringstijd voor het opbouwen van de lichtroosters weergegeven in figuur 
\ref{fig:ts-lights-grid}. Deze testen zijn uitgevoerd bij een resolutie van 
$2560 \times 2560$ pixels. 

Er is voor zowel de na\"ieve implementatie, als de Tiled implementatie een 
lineair verband waar te nemen in het aantal lichtberekeningen dat uitgevoerd wordt.
De keuze van de tegelgrootte heeft geen significante invloed op het aantal lichtberekeningen. 

Wanneer gekeken wordt naar de uitvoeringstijd van de verschillende Tiled Shading
varianten, valt op dat de tegelgrootte van $8 \times 8$ pixels, en in 
mindere mate de tegelgrootte van $16 \times 16$ pixels, slecht presteren. Dit
effect is toe te schrijven aan de tijd die nodig is om het lichtrooster op te stellen,
zoals weergegeven in figuur \ref{fig:ts-lights-grid}. 
Wanneer het rooster uit meer tegels bestaat, zal de opbouw meer uitvoeringstijd 
vereisen. Gezien de tegelgrootte geen significante invloed heeft op het aantal
lichtberekeningen, leidt dit ertoe dat kleinere tegelgroottes slechter presteren.


## Resolutie

De gemiddelde uitvoeringstijden per frame per uitvoering als functie van de 
resolutie zijn weergegeven in figuur \ref{fig:ts-resolution}. In figuur 
\ref{fig:ts-lc-resolution} zijn het aantal lichtberekeningen per frame als 
functie van de resolutie weergeven voor Deferred Shading. Als laatste is 
de uitvoeringstijd voor het opbouwen van het lichtrooster als functie van 
de resolutie weergegeven in figuur \ref{fig:ts-resolution-grid}.

Voor zowel de na\"eve implementatie als de Tiled Shading implementaties is een 
kwadratisch verband waar te nemen in het aantal lichtberekeningen. Dit komt
overeen met de kwadratische toename in pixels ten opzichte van de resolutie waarde. 
Ook bij een toename van de resolutie heeft de tegelgrootte 
geen significante invloed op het gemiddeld aantal lichtberekeningen per frame. 

Echter, zoals in figuur \ref{fig:ts-resolution} is te zien, presteert Tiled 
Shading met een tegelgrootte van $8 \times 8$ pixels slecht. Het aantal tegels
neemt tevens kwadratisch toe bij een hogere resolutie. Het opbouwen van
het rooster schaalt hierdoor dus ook kwadratisch. Zoals waar te nemen in figuur \ref{fig:ts-resolution-grid}

