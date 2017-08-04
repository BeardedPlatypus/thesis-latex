# Resultaten

De performantie van de Clustered Shading implementatie binnen `nTiled` is 
ge\"evalueerd met behulp van de drie \mbox{testsc\`enes}. Hierbij is slechts gekeken naar
de Deferred Shading implementatie. De Forward Clustered Shading implementatie
vereist een z-prepass, zoals besproken in de vorige secties. Een dergelijke
aanpassing aan de Forward Shader heeft invloed op de algemene performantie. 
Hierdoor wordt een eerlijke vergelijking tussen de verschillende technieken
bemoeilijkt. Deferred Clustered Shading vereist geen aanpassing aan de 
structuur. Om deze reden kan deze variant wel accuraat vergeleken worden.

Voor de evaluatie van Clustered Shading zal eerst naar de individuele uitvoeringen gekeken worden, en 
vervolgens naar de invloed van lichten en resolutie op de Clustered Shading
implementatie. Hiervoor zal Deferred Clustered Shading vergeleken worden
met na\"ieve Deferred Shading en de Deferred Tiled Shading implementatie 
gebruikmakend van $32 \times 32$ pixels tegels. Er is gekozen voor de
$32 \times 32$ pixels variant omdat het verschil in aantal lichtberekeningen
tussen de verschillende tegelgroottes minimaal is en deze waarde het best presteerde.

## Frames
\input{./img/tex/cs-frames-stacked.tex}

In figuur \ref{fig:cs-frames-stacked} is de gesommeerde uitvoeringstijd van de
verschillende functies van Clustered Shading weergegeven. Hierin valt gelijk op
dat een meerderheid van de uitvoeringstijd gespendeerd wordt aan de functie 
`sortAndCompactKeys`. Dit is het gevolg van het gebruik van de `openGL` functie
`glGetTexImage`\footnote{Documentatie van $\mathtt{glGetTexImage}$: `\url{https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml}}
Deze functie wordt gebruikt om de berekende clusters uit het videogeheugen op te
halen. Dit is een trage operatie, waarvan de tijd direct afhankelijk is van de
grootte van de texturen die opgehaald dienen te worden. In het geval van deze
Clustered Shading implementatie wordt een textuur ter grootte van het zichtveld
en een textuur ter grootte van het aantal tegels opgehaald. Dit leidt tot een
erg trage implementatie. Hierdoor is de tijdscomplexiteit van de 
Clustered Shading implementatie hoofdzakelijk afhankelijk van de trage 
implementatie van `sortAndCompactKeys`. Dit maakt de uitvoeringstijd een
weinigzeggende indicator voor de performantie van het algoritme.
Om deze reden zal verder niet de  uitvoeringstijd vergeleken worden met de andere lichttoekenningsalgoritmen. 
Omdat de sorteer en compact stap een belangrijke en computationele zwaardere 
stap is binnen het Clustered Shading algoritme, zou een vergelijking waar 
`sortAndCompactKeys` buiten beschouwing gelaten worden ook tot een vertekend
beeld leiden. De verdere vergelijkingen kijken slechts naar het 
aantal lichtberekeningen.

\input{./img/tex/cs-lc-frames-deferred.tex}
\input{./img/tex/cs-lc-frames-example.tex}

Het aantal lichtberekeningen per frame gedurende een complete uitvoering van 
Clustered Shading zijn weergegeven in figuur \ref{fig:cs-lc-frames-deferred}.
In deze grafieken is tevens het aantal lichtberekeningen voor de na\"ieve 
implementatie en voor Tiled Shading gegeven. Alle varianten van Clustered
Shading vereisen minder lichtberekeningen dan zowel de na\"ieve implementatie 
als de Tiled Shading implementatie. Opnieuw lijkt de tegelgrootte geen grote
invloed te hebben op het aantal lichtberekeningen. Dit is vergelijkbaar met
de resultaten gevonden bij Tiled Shading. Ook hier zal gelden dat, bij de
gekozen grootte van lichten, nabijgelegen clusters veelal dezelfde set van
lichten zullen bevatten. Hierdoor is er geen significant verschil tussen de 
clusters met een tegelgrootte van $32 \times 32$ en de clusters met tegelgrootte
$8 \times 8$. Indien de \mbox{sc\`enes} meer kleinere lichten zou bevatten,
zouden, net als bij Tiled Shading, de kleinere tegelgroottes waarschijnlijk wel
beter presteren.

Het aantal lichtberekeningen per frame is consistenter dan bij Tiled Shading. 
Doordat het aantal lichten per cluster in grote mate is geminimaliseerd, is het
verschil tussen pixels zonder fragmenten en pixels met fragmenten kleiner. 
Hierdoor is het verschil in aantal lichtberekeningen tussen de verschillende
camerapunten in de Ziggurat City \mbox{sc\`ene} verwaarloosbaar. Dit is goed waar te nemen
in figuur \ref{fig:cs-test-frames-example}, waar te zien is dat het 
verschil in aantal lichtberekeningen tussen pixels zonder en met fragmenten
klein is.

Ook in de Spaceship Indoor \mbox{sc\`ene} is een consistenter aantal lichtberekeningen
waar te nemen. Binnen de Tiled Shading implementatie is deze variatie een
gevolg van de overlap van lichten. Wanneer de camera zich aan het begin van 
een corridor bevindt zal elk van de lichten in de corridor overlappen. Naarmate
de camera zich door de corridor heen beweegt zullen de lampen achter de camera
buitenbeschouwing worden gelaten, totdat uiteindelijk slechts een klein aantal lichten
nog invloed heeft op de geometrie. 
Binnen Clustered Shading zorgt de opdeling in de
camera $\mathbf{z}$-as ervoor dat elk cluster slechts lichten bevat die ook
in de $\mathbf{z}$-as relevant zijn. Dit leidt ertoe dat voor alle fragmenten
slechts een kleinere set lichten ge\"evalueerd dient te worden, die 
vergelijkbaar is met de set lichten in het minimale geval van Tiled Shading.
Dit heeft een lagere en consistentere hoeveelheid lichtberekeningen per frame
tot gevolg.

Het grootste verschil in aantal lichtberekeningen is waar te nemen in de Piper's
Alley \mbox{sc\`ene}. Dit is een direct gevolg van het oplossen van het slechtst mogelijke
scenario van Tiled Shading. Binnen de Piper's Alley \mbox{sc\`ene} was de overlap van 
lichten het extreemst. Nu de tegelvolumes opgesplitst zijn in de camera 
$\mathbf{z}$-as, worden niet alle overlappende lichten toegekend aan elk cluster.
Dit is duidelijk zichtbaar in figuur \ref{fig:cs-test-frames-example}.
De Tiled Shading implementatie vertoont een grote hoeveelheid lichtberekeningen
voor de tegels in het midden van de afbeelding. De Clustered Shading implementatie
bevat geen clusters met een dergelijk grote hoeveelheid lichten. Relatief aan alle clusters 
bevatten slechts de verste clusters een groter aantal lichten. Dit is een gevolg van de opdeling van
Clustered Shading, waar met clusters verder van de camera, grotere volumes 
geassocieerd zijn.


## Lichten

\input{./img/tex/cs-lc-light.tex}

In figuur \ref{fig:cs-lc-lights} is het gemiddeld aantal lichtberekeningen per
frame als functie van het aantal lichten bij een resolutie van $2560 \times 2560$
pixels, weergegeven. Clustered Shading is lineair afhankelijk van het aantal 
lichten, zoals ook de na\"ieve en de Tiled implementaties. Echter de factor 
waarmee het aantal lichtberekeningen schaalt is bijna een factor twee kleiner
voor alle scenes. 
De clustergrootte lijkt geen significante invloed te hebben op het aantal 
lichtberekeningen, wanneer de hoeveelheid lichten wordt gevarieerd.


##  Resolutie

In figuur \ref{fig:cs-lc-resolution} is het gemiddeld aantal lichtberekeningen
per frame als functie van de resolutie weergegeven. In deze grafieken is een
kwadratisch verband zichtbaar, wat duidt op een lineaire afhankelijkheid van het
aantal pixels. Vergelijkbaar met de variatie van aantal lichten, presteert 
Clustered Shading ook bij verschillende resoluties beter dan zowel de na\"ieve
als de Tiled Shading implementaties.
Ook bij de vari\"erende resolutie is geen significante invloed waar te nemen voor de
verschillende cluster grootten.


