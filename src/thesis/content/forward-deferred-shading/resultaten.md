# Resultaten 

De performantie van het deferred algoritme dat ge\"introduceerd werd in de 
vorige sectie, is ge\"evalueerd aan de hand van de drie test scenes. Eerst zal
het gedrag per frame gedurende een enkele uitvoering besproken worden.
Vervolgens wordt gekeken naar de gemiddelde executietijd per frame als functie 
van het aantal lichten, en de resolutie.

Binnen de testen refereert *forward* naar de `forward_attenuated` shader en
*deferred* naar de `deferred_attenuated` shader van `nTiled`.

## Frames {#sec:fds-frames}

\input{./img/tex/fds-test-frames-high.tex}

In figuur \ref{fig:fds-test-frames} zijn de gemiddelde executietijden per frame
gedurende een complete uitvoering weergegeven. Links zijn de waardes weergegeven 
van de uitvoeringen met het laagste aantal lichten per scene bij een resolutie 
van $160 \times 160$. Rechts zijn de waardes weergegeven van het hoogste aantal 
lichten per scene bij een resolutie van $2560 \times 2560$.  

Gelijk valt hierbij op dat bij een lage resolutie en een klein aantal lichten 
forward en deferred shading elkaar nauwelijks ontlopen. Het verschil in 
executietijd is echter significant bij een hoge resolutie en een groot aantal
lichten. Niet alleen is de executietijd kleiner bij deferred shading, het is 
tevens consistenter. Dit is belangrijk voor computerspellen en andere real-time
toepassingen waar een consistente framerate nodig is voor een overtuigende 
virtuele ervaring. 

De consistentie in executietijd kan verklaard worden doordat de tijdsbeperkende 
stappen niet afhankelijk zijn van het aantal fragmenten die zichtbaar zijn.
Het wegschrijven van fragmenten naar de GBuffer is een simpele operatie die 
geen berekeningen vereist. Een verschil in fragmenten zal hierdoor geen 
significant verschil in executietijd veroorzaken. Tevens zal de 
belichtingsberekening slechts uitgevoerd worden voor een enkel fragment, 
waardoor het aantal fragmenten ook geen invloed op de belichtingsstap heeft. 
Bij forward shading is de lichtberekening tijdsbepalend en deze is direct 
gekoppeld aan het aantal fragmenten dat gecree\"erd wordt. 

\input{./img/tex/fds-test-frames-example.tex}

Deze koppeling tussen visibiliteit en shadingcomplexiteit is dan ook direct 
terug te zien in het tijdsgedrag van forward shading. Zo is in de indoor
spaceship scene te zien dat de executietijd van forwardshading de executietijd
van deferred shading benaderd rond frame 170 en frame 430. Deze frames komen
overeen met een zicht op een enkele muur, zoals weergegeven in figuur 
\ref{fig:fds-test-frames-example:si:170} en \ref{fig:fds-test-frames-example:si:430}.
Hier benaderd het aantal fragmenten per pixel \mbox{\'e\'en}.

Verder is er binnen de ziggurat stadsscene, fig. \ref{fig:fds-test-frames:city-high}
nog een sprong in executie tijd te zien bij frame 100 en frame 167. Deze 
sprongen komen overeen met de verandering van camera, zoals te zien is in figuur
\ref{fig:fds-test-frames-example:zc}. Het verschil in executietijd is een gevolg
van het percentage lege ruimte in de drie camera standpunten. Waar het zicht 
tussen frame 100 en frame 167 voornamelijk bestaat uit geometrie, en in de 
frames voor 100 en na 167 ook een lege lucht waar te nemen is.

## Lichten

\input{./img/tex/fds-test-lights.tex}

In figuur \ref{fig:fds-test-lights} is de gemiddelde executietijd per frame
weergegeven als  functie van het aantal lichten in de scene bij een resolutie
van $2560 \times 2560$. Hierbij zijn alle executietijden per frame gemiddeld 
over alle frames in een uitvoering.

Er is een lineair verband waar te nemen bij zowel forward als deferred shading.
Dit komt overeen met de verwachting dat het aantal lichtberekeningen per fragment
lineair schaalt met het aantal lichten. Deferred shading schaalt met een kleinere
factor dan forward shading, doordat er slechts voor een enkel fragment de extra
lichten ge\"evalueerd dienen te worden.

## Resolutie

\input{./img/tex/fds-test-resolution.tex}

In figuur \ref{fig:fds-test-resolution} is de gemiddelde executietijd per frame
weergegeven als functie van de resolutie weergegeven bij het grootste aantal 
lichten per scene. Hierbij komt een resolutie van $n$ overeen met een gebruikte
resolutie van $n \times n$. De executietijden per frame zijn op een zelfde manier
gemiddeld als de executietijd per aantal lichten. 

In elk van de grafieken is een kwadratisch verband waarneembaar. Dit komt 
overeen met de kwadratische toename van pixels, en dus fragmenten.

