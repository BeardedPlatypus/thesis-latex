# Resultaten

De performantie van het Tiled Shading algoritme ge\"introduceerd in de vorige
sectie, is ge\"evalueerd aan de hand van de drie testscenes. Hierbij zijn de 
resultaten van na\"ief Forward Shading en Tiled Forward Shading, en na\"ief
Deferred Shading en Tiled Deferred Shading vergeleken. Opnieuw zal eerst gekeken
worden naar de executietijd per frame gedurende een enkele uitvoering. 
Vervolgens wordt gekeken naar de executietijd als functie van het aantal lichten
en de resolutie.

## Frames
\input{./img/tex/ts-frames-forward.tex}
\input{./img/tex/ts-frames-deferred.tex}

De executietijden per frame voor Forward Shading zijn weergegeven in figuur 
\ref{fig:ts-frames-forward}, en de executietijden per frame voor Deferred
Shading in figuur \ref{fig:ts-frames-deferred}. 
De grafieken links geven de uitvoeringen weer van een klein aantal lichten bij
een resolutie van $320 \times 320$. De rechter grafieken geven de uitvoeringen
met een groot aantal lichten bij een resolutie van $1920 \times 1920$. 
De Tiled Shading uitvoeringen zijn gedaan met een tegelgrootte van 
$32 \times 32$. 

Opnieuw kan geconstateerd worden dat voor een lage resolutie en een klein aantal
lichten executietijden vergelijkbaar zijn ongeacht methode. Zowel de na\"ieve 
Forward en Tiled Forward Shading, en de na\"ieve Deferred en Tiled Deferred 
algoritmes hebben vergelijkbare executietijden. Dit komt overeen met de 
resultaten van Forward en Deferred Shading.

Voor een hogere resolutie en een groot aantal lichten zijn de verschillen wel
significant. In alle gevallen is het Tiled Shading algoritme effici\"enter dan
de na\"ieve implementatie. Tevens zijn de executietijden voor Forward Shading
consistenter. Dit is vooral zichtbaar in de spaceship indoor scene, fig. 
\ref{fig:ts-frames-forward:indoor-high}, waar de schommeling afhankelijk van
de camerapositie, minder hevig zijn. Dit duidt er op dat er minder 
lichtberekeningen per fragment worden uitgevoerd, in vergelijking tot de na\"ive
implementatie. Hierdoor is de totale berekeningstijd per frame minder onderhevig
aan het aantal fragmenten in een frame. 

Binnen de ziggoerat scene, fig. \ref{fig:ts-frames-forward:city-high} en
\ref{fig:ts-frames-deferred:city-high}, is het verschil tussen de verschillende 
camerapunten minder nadrukkelijk aanwezig. In sectie \ref{sec:fds-frames} werd
al vastgesteld dat het verschil in berekeningstijd tussen de camerapunten in
grootte mate afhankelijk was van het percentage pixels zonder fragmenten.
Hierbij bevat het tweede camerapunt een lager percentage lege pixels. De 
fragmenten die gegenereerd worden bij de tweede camerapositie, liggen veelal
in het deel van de Ziggoerat scene die verlicht wordt door enkele grote lichten,
fig. \ref{fig:test-suite-ziggurat-map}. Hierdoor zullen de tegels op bij dit
camerapunt weinig lichten bevatten. Hierdoor neemt het aantal lichtberekeningen
af, en daarmee de executie tijd.

Het verschil in effici\"ency is het kleinst in de Piper's Alley scene. Dit kan
verklaard worden aan de hand van de opbouw van de scene. De Piper's Alley scene
is \mbox{\'e\'en} diepe straat, waar de lichten achter elkaar zijn geplaatst, 
zie fig. \ref{fig:test-suite-pipers-alley-map}. Wanneer gekeken wordt naar de
onderverdeling van het zichtfrustum, fig. \ref{fig:ts-grid-intro:frustum} is te
zien dat dergelijke scenes, met veel overlappende lichtvolumes in de diepte,
leidt tot het slechtst mogelijke situatie. Elk van de tegels zal een groot 
aantal lichten bevatten. Hierdoor zal het tijdsgedrag van de na\"ive
implementatie benaderd worden.

## Lichten

\input{./img/tex/ts-lights.tex}

In figuur \ref{fig:ts-lights} zijn de gemiddelde executietijden per frame per 
uitvoering geplot, als functie van het aantal lichten in de scene, voor zowel
Forward Shading, links, en Deferred Shading, rechts. Deze testen zijn uitgevoerd
bij een resolutie van $1920 \times 1920$ pixels. 

Voor Tiled Shading zijn verschillende tegelgroottes ge\"evalueerd. Hierbij is op
te merken dat er weinig verschil lijkt te zijn in uitvoeringstijd bij 
verschillende tegelgroottes. 

Er is voor zowel de na\"ieve implementatie, als de Tiled implementatie een 
lineair verband waar te nemen in alle grafieken. Hierbij schaalt de Tiled
Shading variant met een significant lagere factor in vergelijking tot de 
na\"ieve implementatie. In zowel de Spaceship indoor scene als de Ziggoerat
stadsscene is een factor van ongeveer zes waar te nemen. Bij de Piper's Alley
straatscene is dit slechts een factor vier. Dit verschil kan opnieuw verklaard
worden door de overlapping van lichtvolumes, waardoor het aantal lichten per
tegel gemiddelde toeneemt.

## Resolutie

\input{./img/tex/ts-resolution.tex}

De gemiddelde executietijden per frame per uitvoering als functie van de 
resolutie zijn weergegeven in figuur \ref{fig:ts-resolution}. Voor zowel de
na\"eve implementatie als de Tiled Shading implementaties is een kwadratisch
verband waar te nemen. Echter de factor voor Tiled Shading is zodanig klein dat
de schaling een lineair verband benaderd.
Ook voor de resolutie is geen grote invloed van de keuze voor tegelgrootte waar
te nemen.

