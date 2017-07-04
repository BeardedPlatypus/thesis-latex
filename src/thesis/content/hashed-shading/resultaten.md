# Testen en resultaten

In de volgende sectie zal de effici\"entie van Hashed Shading ge\"evalueerd 
worden en vergeleken met Tiled Shading en Clustered Shading. Hiervoor zal eerst
naar de constructietijd en geheugengebruik van Hashed Shading gekeken worden, en
hoe deze be\"invloed wordt door de seed-waarde, minimale knoopgrootte en 
begindiepte van de verbindingloze octree. Vervolgens zal gekeken worden naar de
uitvoeringstijd en het aantal lichtberekeningen van Hashed Shading.


## Seed

\input{./img/tex/hs-seed-combined.tex}
\input{./img/tex/hs-seed-memory.tex}

Zoals beschreven in de theorie vereist de verbindingloze octree willekeurige
nummer generatie. Deze kan ge\"initialiseerd worden met verschillende 
seed-waardes. Hierbij is de hypothese dat de keuze voor een seed-waarde geen
significante invloed heeft op de performantie van de verbindingloze octree.

De willekeurige nummer generatie wordt gebruikt voor het genereren van de 
hash-offset-waardes, wanneer deze niet afgeleid kunnen worden op basis van
naastgelegen waardes. Indien geen geschikte waarde gevonden kan worden, wordt
de grootte van de hash-offset-tablel uitgebreidt. Indien de seed-waarde een
invloed zou hebben, is het dus slechts op de constructietijd en het 
geheugengebruik van de verbindingloze octree. De nummer generatie heeft geen
invloed op het aantal lichtberekeningen en dus de uitvoeringstijd van de 
lichtberekeningen, doordat de effici\"entie onafhankelijk is van de grootte
van de lagen van de verbindingloze octree.

Om de invloed van de willekeurige nummer generatie te evalueren is dus slechts
gekeken naar de constructietijd en het geheugengebruik bij 10 verschillende 
seed-waardes, waarbij de knoopgrootte op $0.5 \times$ de lichtgrootte is 
gehouden en een begindiepte van $0$ is gebruikt. Deze resultaten zijn 
weergegeven in de figuren \ref{fig:hs-seed-exec} en 
\ref{fig:hs-seed-memory}. 

Uit de grafieken blijkt dat het geheugengebruik niet be\"invloed wordt door de 
gebruikte seed-waarde. Elk van de lagen van de verbindingloze octree gebruikt 
een zelfde hoeveelheid geheugen. Verder is geen significante invloed 
waarneembaar op de constructietijd van de verbindingloze octree. De variatie
die zichtbaar is kan verklaard worden doordat voor sommige seed-waardes meer
hash-offset-waardes gegenereerd en gecontroleerd dienen te worden, in het
geval van botsingen in de hash-data-tabel. Hierdoor verschilt de 
constructietijd, echter niet zodanig dat gesproken kan worden van een invloed
op de performantie van de verbindingloze octree door de seed-waardes.
In verdere testen zal gebruikgemaakt worden van een seed-waarde van $23$.

## Knoopgrootte van de verbindingloze octree

\input{./img/tex/hs-nodesize-construction-time.tex}
\input{./img/tex/hs-nodesize-memory.tex}
\input{./img/tex/hs-ns-layered-mem.tex}

In figuur \ref{fig:hs-n-layers} is het aantal lagen dat de octree vereist om de
gehele lichtconfiguratie te bedekken, weergegeven als functie van de grootte van
de kleinste knopen van de octree. In het rood zijn de waardes weergegeven die
verder ge\"evalueerd zullen worden. De scenes zijn zodanig opgesteld dat dat 
een groter aantal lichten niet leidt tot meer lagen. Het groter aantal lichten
is verdeeld over hetzelfde volume als de kleinste set lichten. Een kleinere 
knoopgrootte leidt tot meer lagen en meer minimale knopen. Dit heeft tot 
gevolg dat de verbindingloze octree zowel in constructietijd als geheugengebruik
zal toenemen wanneer de knoopgrootte wordt gereduceerd.

De constructietijd als functie van de knoopgrootte voor de verschillende 
lichtconfiguraties is weergegeven in figuur \ref{fig:hs-ns-construction-time}. 
Hierbij zijn de lichtaantallen per scene weergegeven in de legenda. De
knoopgrootte is relatief aan de gebruikte radius voor de lichten in de scene:

* Spaceship indoor: $23.0$
* Piper's Alley: $180.0$
* Ziggurat City: $10.0$

In figuur \ref{fig:hs-ns-memory} is het geheugengebruik van de verbindingloze
octree als functie van de knoopgrootte weergegeven. Hierbij zijn het aantal 
pixels van de texturen gebruikt in elke laag van de verbindingloze octree 
gesommeerd en gebruikt als indicatie van dit geheugengebruik.
In figuur \ref{fig:hs-ns-light-indices} is het aantal lichtindices als
functie van de knoopgrootte weergegeven. Hierbij is met elke gevulde knoop
een lichtindex geassocieerd. Als laatste zijn de groottes van de hash en 
offset tabellen voor de verschillende lagen van de verbindingloze octree
als functie van de knoopgrootte voor de grootste lichtconfiguraties per scene
weergegeven in figuur \ref{fig:hs-layered-mem}

Bij alle lichtconfiguraties is een sterke toename in geheugengebruik en 
constructietijd waar te nemen wanneer de knoopgrootte kleiner wordt dan $1$.
Dit is een direct gevolg van de toename van het aantal (minimale) knopen. 
Bij een kleinere knoopgrootte zal elk licht een groter aantal minimale 
knopen bedekken. De maximale grootte van het rooster bij een knoopgrootte van
$k$ voor een enkel licht kan gedefinieerd worden als:

$$ n = \left( \mathrm{max} \left(1, \frac{2 l_{\mathrm{radius}}}{k} \right) + 1 \right)^3 $$

waar $n$ het totaal aantal knopen in het rooster is. Uitgaande van het volume
van een bol zal ongeveer $52\%$ van de lichtvolumes gevuld zijn:

$$ n_{\mathrm{licht}} \approx 0.52 \left( \mathrm{max} \left(1, \frac{2 l_{\mathrm{radius}}}{k} \right) + 1 \right)^3 $$

### Geheugengebruik

De hi\"erarchische voorstelling van de lichtvolumes leidt ertoe dat de lege 
volumes effici\"ent kunnen worden opgeslagen. Echter door de gedeeltelijk
overlap van de lichten, bevindt een significant deel van de lichtinformatie zich
in de diepste lagen van de octree. Dit is duidelijk waar te nemen in de grootte
van de datahashfuncties weergegeven in figuur \ref{fig:hs-layered-mem}.
Het merendeel van de data-elementen bevindt zich in de twee diepste lagen van de
octree. Doordat in de huidige implementatie met elke volle knoop een element in
de lichtindexlijst is geassocieerd, leidt dit tevens tot een kubisch verband
in het aantal lichtindices, waarneembaar in figuur \ref{fig:hs-ns-light-indices}.

Doordat de knoopgrootte voor een groter aantal lagen in de octree leidt, heeft 
de knoopgrootte tevens een invloed op het geheugengebruik van de 
octreevoorstellinghashfuncties van de verbindingloze octree. Dit is zichtbaar in
de grootte en het aantal lagen van de octreestructuur weergegeven in figuur 
\ref{fig:hs-layered-mem}.

### Constructietijd

Enerzijds is de constructietijd afhankelijk van het geheugengebruik doordat een
groter aantal knopen leidt tot meer berekeningen in het opstellen van de 
verbindingloze octree. Elke knoop per laag dient te worden gesorteerd. 
Vervolgens moet per groep botsende knopen een correcte offset-waarde gevonden 
worden.

Anderzijds leidt een kleinere knoopgrootte tot grotere roosters bij de 
constructie van de lichtoctree. Hierdoor neemt het aantal berekeningen per 
licht, en dus de gehele constructietijd toe. Hierdoor is ook in de 
constructietijd een kubisch verband waarneembaar

### Lichtberekeningen en uitvoeringstijd

\input{./img/tex/hs-ns-frame-low.tex}
\input{./img/tex/hs-ns-frame-high.tex}
\input{./img/tex/hs-ns-sum.tex}
\input{./img/tex/hs-ns-frames-render.tex}

In figuren \ref{fig:hs-ns-frame-low:exec}, \ref{fig:hs-ns-frame-low:lc} en
\ref{fig:hs-ns-frame-high:exec}, \ref{fig:hs-ns-frame-high:lc} zijn de 
uitvoeringstijd en aantal lichtberekeningen per frame voor respectievelijk een 
klein aantal lichten en een lage resolutie van $320 \times 320$ pixels, en een 
groot aantal lichten en een hoge resolutie van $2560 \times 2560$ pixels 
weergegeven. In figuren \ref{fig:hs-ns-sum:exec} en \ref{fig:hs-ns-sum:lc} zijn 
de gemiddelde uitvoeringstijd en het gemiddeld aantal lichtberekeningen per frame 
als functie van de minimale knoopgrootte weergegeven, bij een resolutie van 
$2560 \times 2560$ en een groot aantal lichten. Verder zijn de visualisaties
van het aantal lichten bij verschillende knoopgroottes weergegeven in figuur 
\ref{fig:hs-ns-frames-render}.

Zowel bij een lagere resolutie en een kleine set van lichten, als bij een hogere
resolutie en een grotere set van lichten leidt een kleinere minimale knoopgrootte
tot minder lichtberekeningen per frame. Dit is een direct gevolg van de hogere
nauwkeurigheid waarmee lichten benaderd worden. Hierdoor bevatten de bladknopen
minder lichten, doordat niet relevante lichten niet meer overlappen, waardoor
deze ook niet meer worden ge\"evalueerd in de berekening van pixels die tot een
dergelijke bladknoop behoren.

Wanneer de knoopgrootte groter wordt dan de diameter van de lichten leidt een
grotere knoopgrootte niet noodzakelijk tot meer lichtberekeningen. Dit is een
gevolg van hoe de knopen de ruimte opdelen. Het is mogelijk dat door de 
plaatsing van de grotere knopen, bepaalde knopen met minder lichten overlappen
ondanks het groter volume dat wordt bestreken. Hierdoor neemt voor dergelijke
knoopgroottes het aantal lichtberekeningen af.

De relatie tussen uitvoeringstijd en aantal lichtberekeningen is duidelijk 
zichtbaar in de grafieken van de hogere resolutie en grotere lichtset 
uitvoeringen. Het gedrag van de grafieken van het aantal lichtberekeningen
is, in minder uitgesproken vorm, terug te zien in de uitvoeringstijd.

De lichtberekeningen zijn een belangrijk component van de gehele rendertijd,
wat de gelijkenis in gedrag verklaard. Voordat de lichtberekening echter 
plaatsvindt, dient de lichtknoop waartoe een pixel behoort opgezocht te worden.
Een kleinere knoopgrootte leidt tot meer lagen in de octree. Met elke laag
die doorlopen dient te worden is een textuuropvraag geassocieerd. Dit leidt
tot een grotere uitvoeringstijd wanneer het aantal lagen van de octree toeneemt.
Hiermee wordt de winst die verkregen wordt met de reductie van het aantal 
lichtberekeningen beperkt. 

De invloed van het verschil in aantal lichtberekeningen op de uitvoeringstijd
bij een kleine set van lichten en een lage resolutie is minimaal. Hierdoor is 
dus ook de invloed van de knoopgrootte in dergelijke situaties, verwaarloosbaar.

Deze observaties zijn tevens terug te zien in figuur \ref{fig:hs-ns-sum:exec}
en \ref{fig:hs-ns-sum:lc}, waar de uitvoeringstijd en het gemiddeld aantal 
lichtberekeningen zijn uitgezet tegen de knoopgrootte voor verschillende 
aantallen lichten. Voor alle hoeveelheden lichten leidt een kleinere 
knoopgrootte tot minder lichtberekeningen. De invloed van de knoopgrootte
op de reductie van het aantal lichtberekeningen is afhankelijk van het
aantal lichten in de scene. Voor kleine hoeveelheden lichten is deze beperking
minimaal, terwijl de invloed het grootst is wanneer het aantal lichten het 
grootst is. Dit leidt ertoe dat voor een klein aantal lichten de uitvoeringstijd
zelfs afneemt, bij een grotere knoopgrootte. Hier valt uit af te leiden dat
de uitvoeringstijd die de extra textuuropvragingen vereisen, groter is dan de
winst die wordt verkregen met de reductie in het aantal lichtberekeningen.


## Begindiepte van de verbindingloze octree


## Frames

\input{./img/tex/hs-exec-frames-forward.tex}
\input{./img/tex/hs-exec-frames-deferred.tex}

## Lichten

\input{./img/tex/hs-exec-lights.tex}

## Resolutie

\input{./img/tex/hs-exec-resolution.tex}

