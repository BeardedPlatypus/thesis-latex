# Resultaten

In de volgende sectie zal de performantie van Hashed Shading ge\"evalueerd
worden. hiervoor zal gekeken worden naar de invloed van de seed,
minimale knoopgrootte, en begindiepte, op de constructietijd en 
geheugengebruik van de datastructuren, en op de uitvoeringstijd en
aantal lichtberekeningen.

## Seed-waarde

\input{./img/tex/hs-seed-combined.tex}
\input{./img/tex/hs-seed-memory.tex}

Hashed Shading maakt gebruik van willekeurige nummergeneratie om 
de offset-waardes voor de offset-tabel $\Phi$ te genereren, indien
geen naburige offset-waardes correct zijn. De hypothese is dat deze
seed-waarde geen invloed heeft op de performantie van de verbindingloze octree.

Indien de seed-waarde invloed zou hebben op de verbindingloze octree, zou het
niet de uitvoeringstijd en het aantal lichtberekeningen be\"invloeden. De seed-waarde
heeft slechts invloed op de grootte van de gegenereerde spatiale hashfuncties, en
dus op het geheugengebruik en de constructietijd. De uitvoeringstijd en het 
aantal lichtberekeningen worden niet be\"invloed door de grootte van de spatiale
hashfunctie. Om deze reden is slechts gekeken naar de constructietijd en 
het geheugenverbruik, bij verschillende seed-waardes. Hierbij zijn voor
de drie \mbox{sc\'enes}  de kleinste en grootste sets lichten ge\"evalueerd.
Dit is gedaan bij een knoopgrootte gelijk aan de helft van de lichtradius
van de lichten gebruikt in de \mbox{sc\`ene}, en een begindiepte van nul 
voor tien verschillende seed-waardes.

De resultaten voor de constructietijd zijn weergegeven in figuur \ref{fig:hs-seed-exec}.
De resultaten voor het geheugengebruik zijn weergegeven in figuur \ref{fig:hs-seed-memory}. 
Uit de grafieken blijkt dat het geheugen niet wordt be\"invloed door de seed-waarde.
Elk van de lagen verbruikt dezelfde hoeveelheid geheugen. Verder is er geen significante
invloed waar te nemen op de constructietijd van de verbindingloze octree. 
De variatie die zichtbaar is kan verklaard worden door het feit dat bij sommige
seed-waardes mogelijk meer incorrecte offset-waardes worden gegenereerd. Elk van deze 
offset-waardes dient gecontroleerd te worden, en er zullen offset-waardes gegenereerd 
worden totdat een correcte waarde wordt gevonden. Dit introduceert een kleine 
hoeveelheid extra werk. 

Omdat de seed-waarde geen invloed heeft, zal in de verdere testen steeds een
seed waarde van $23$ gebruikt worden.

## Knoopgrootte van de verbindingloze octree

\input{./img/tex/hs-nodesize-construction-time.tex}
\input{./img/tex/hs-nodesize-construction-per-function.tex}
\input{./img/tex/hs-nodesize-memory.tex}
\input{./img/tex/hs-ns-layered-mem.tex}

In figuur \ref{fig:hs-n-layers} is het aantal lagen dat de octree vereist om de
gehele lichtconfiguratie te bedekken, weergegeven als functie van de minimale 
knoopgrootte. In het rood zijn de waardes weergegeven die
verder ge\"evalueerd zullen worden. De \mbox{sc\`enes} zijn zodanig opgesteld dat
een groter aantal lichten niet leidt tot meer lagen.  Elke set lichten is 
verdeeld over hetzelfde volume ongeacht de grootte van de set van lichten.
Een kleinere  knoopgrootte leidt tot meer lagen en meer minimale knopen. Dit heeft tot 
gevolg dat de verbindingloze octree zowel in constructietijd als geheugengebruik
zal toenemen wanneer de knoopgrootte wordt gereduceerd.

De constructietijd als functie van de knoopgrootte voor de verschillende 
lichtconfiguraties is weergegeven in figuur \ref{fig:hs-ns-construction-time}. 
Hierbij zijn de lichtaantallen per \mbox{sc\`ene} weergegeven in de legenda. De
knoopgrootte is relatief aan de gebruikte radius voor de lichten in de \mbox{sc\`ene}:

* Spaceship Indoor: $23.0$
* Piper's Alley: $180.0$
* Ziggurat City: $10.0$

In figuur \ref{fig:hs-layered-exec} zijn de constructietijden per functie weergegeven
voor de kleinste en grootste set lichten voor elke \mbox{sc\`ene}.
In figuur \ref{fig:hs-ns-memory} is het geheugengebruik van de verbindingloze
octree als functie van de knoopgrootte relatief aan de lichtradius weergegeven. 
Hierbij is het aantal pixels in elke textuur van de verbindingloze octree gesommeerd.
Deze waarde is als indicatie gebruikt voor het geheugengebruik.
In figuur \ref{fig:hs-ns-light-indices} is de grootte van de lichtindexlijst als functie 
van de knoopgrootte weergegeven. Voor elke gevulde bladknoop wordt een set van relevante
lichtindices toegevoegd aan de lichtindexlijst. Als laatste zijn de groottes van de hash- en 
offset-tabellen voor de verschillende lagen van de verbindingloze octree
als functie van de knoopgrootte voor de grootste lichtconfiguraties per \mbox{sc\`ene}
weergegeven in figuur \ref{fig:hs-layered-mem}

Bij alle lichtconfiguraties is een sterke toename in geheugengebruik en 
constructietijd waar te nemen wanneer de knoopgrootte kleiner wordt dan \mbox{\'e\'enmaal de lichtradius}.
Dit is een direct gevolg van de toename van het aantal (minimale) knopen. 
Bij een kleinere knoopgrootte zal elk licht een groter aantal minimale 
knopen bedekken. De maximale grootte van het rooster bij een knoopgrootte van
$r$ voor een enkel licht kan gedefinieerd worden als:

$$ n = \left( \mathrm{max} \left(1, \frac{2 \mathbf{l}.\mathrm{radius}}{\mathit{r}} \right) + 1 \right)^3 $$

\noindent waar $n$ het totaal aantal knopen in het rooster is. Uitgaande van het volume
van een bol zal ongeveer $52\%$ van de lichtvolumes gevuld zijn:

$$ n_{\mathrm{licht}} \approx 0.52 \left( \mathrm{max} \left(1, \frac{2 \mathbf{l}.\mathrm{radius}}{r} \right) + 1 \right)^3 $$

\noindent Het aantal gevulde knopen in de diepste laag zal dus kubiek toenemen bij kleinere knoopgroottes.

### Geheugengebruik

De hi\"erarchische voorstelling van de lichtvolumes leidt ertoe dat de lege 
volumes effici\"ent kunnen worden opgeslagen. Echter door de gedeeltelijk
overlap van de lichten, bevindt een significant deel van de lichtinformatie zich
in de diepste lagen van de octree. Dit is duidelijk waar te nemen in de grootte
van de hashfuncties weergegeven in figuur \ref{fig:hs-layered-mem}.
Het merendeel van de data-elementen bevindt zich in de twee diepste lagen van de
octree. Doordat in de huidige implementatie met elke volle knoop een element in
de lichtindexlijst is geassocieerd, leidt dit er tevens toe dat deze kubiek toeneemt
bij waardes kleiner dan tweemaal de lichtradius.
Dit is waarneembaar in figuur \ref{fig:hs-ns-light-indices}.

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
licht, en dus de gehele constructietijd toe. Doordat het aantal
knopen in de diepste lagen kubiek toeneemt, neemt ook de constructietijd kubiek toe.
De constructietijd is primair afhankelijk van de opbouw van de spatiale hashfuncties, 
zoals terug te zien is in figuur \ref{hs:nodesize-construction-per-function}.


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
nauwkeurigheid waarmee de lichten in de \mbox{sc\`en} voorgesteld worden. Hierdoor 
bevatten de bladknopen minder lichten, doordat niet relevante lichten niet meer overlappen.
Deze lichten worden ook niet meer ge\"evalueerd in de berekening van pixels die in het
volume van een dergelijke bladknoop vallen.

Wanneer de knoopgrootte groter wordt dan de diameter van de lichten leidt een
grotere knoopgrootte niet noodzakelijk tot meer lichtberekeningen. Dit is een
gevolg van hoe de knopen de ruimte opdelen. Het is mogelijk dat door de 
plaatsing van de grotere knopen, bepaalde knopen met minder lichten overlappen
ondanks het groter volume dat wordt bestreken. Hierdoor neemt voor dergelijke
knoopgroottes het aantal lichtberekeningen af, zoals zichtbaar is in figuur
\ref{fig:hs-ns-frame-high:lc:alley}.

De relatie tussen uitvoeringstijd en aantal lichtberekeningen is duidelijk 
zichtbaar in de grafieken van de uitvoeringen met een hogere resolutie en een aantal lichten.
Het gedrag van de grafieken van het aantal lichtberekeningen
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
aantal lichten in de \mbox{sc\`ene}. Voor kleine hoeveelheden lichten is deze beperking
minimaal, terwijl de invloed het grootst is wanneer het aantal lichten het 
grootst is. Dit leidt ertoe dat voor een klein aantal lichten de uitvoeringstijd
zelfs afneemt, bij een grotere knoopgrootte. Hier valt uit af te leiden dat
de uitvoeringstijd die de extra textuuropvragingen vereisen, groter is dan de
winst die wordt verkregen met de reductie in het aantal lichtberekeningen.


## Begindiepte van de verbindingloze octree

\input{./img/tex/hs-sd-cons-mem.tex}
\input{./img/tex/hs-sd-li-exec.tex}

Zoals vermeld in sectie \ref{sec:theorie-verbindingloze-octree} is het mogelijk om naast de knoopgrootte de
begindiepte in te stellen voor de verbindingloze octree. Hierbij komt een 
begindiepte van nul overeen met een beschrijving van elke laag binnen
de verbindingloze octree, en een diepte van het aantal lagen minus 
\mbox{\'e\'en} met een verbindingloze octree bestaande uit slechts een enkele laag.

Het veranderen van deze waarde heeft geen invloed op het aantal 
lichtberekeningen dat wordt uitgevoerd, doordat ongeacht de begindiepte dezelfde
set van lichten wordt opgehaald binnen de renderstap. Het kan echter wel van 
invloed zijn op de uitvoeringstijd, doordat bij een grotere begindiepte 
minder textuuraanspraken worden uitgevoerd.

Daarnaast zal het van invloed zijn op het geheugengebruik en de constructietijd.
Het gebruik van kleine texturen, bijvoorbeeld van \mbox{\'e\'en} pixel voor de eerste laag 
van de verbindingloze octree, leidt veelal tot onnodig geheugengebruik, door de
overhead geassocieerd met het bijhouden van texturen. Hier staat tegenover dat een grotere begindiepte 
een toename van kleinere knopen vereist, die expliciet bijgehouden dienen te
worden. Dit leidt tot een toename in geheugengebruik. Daarnaast leidt een groter
aantal knopen tot een grotere constructietijd, doordat elk van deze knopen
toegekend dient te worden binnen de corresponderende spatiale hashfunctie.

Om deze aspecten te evalueren zijn de volgende figuren opgesteld. In figuur
\ref{fig:hs-sd-construction} is de constructietijd als functie van de knoopgrootte relatief aan de lichtradius weergegeven
bij verschillende begindieptes voor de grootste gedefinieerde set lichten
per \mbox{sc\`ene}. In figuur \ref{fig:hs-sd-memory} en \ref{fig:hs-sd-light-indices} zijn
respectievelijk het aantal pixels in de datastructuren en het aantal lichtindices 
als functie van de  knoopgrootte voor verschillende begindieptes gegeven. 
Als laatste is de rendertijd als functie van de knoopgrootte voor de verschillende begindieptes
weergegeven in figuur \ref{fig:hs-sd-exec}.

Uit alle figuren valt op te maken dat de ge\"evalueerde begindieptes geen 
significante invloed hebben op de constructietijd, geheugenverbruik, en 
uitvoeringstijd. De afwezigheid van een effect op de constructietijd en het geheugenverbruik kan verklaard worden
doordat een verandering van de begindiepte slechts invloed heeft op de eerste 
lagen van de verbindingloze octree. Uit de resultaten van het
geheugenverbruik per laag laag van de verbindingloze octree, fig. \ref{fig:hs-layered-mem} bleek dat
het merendeel van de knopen zich in de diepere lagen bevindt. Een samenvoeging
van de eerdere lagen zal geen invloed hebben op de set knopen in de diepste 
lagen. Hierdoor zal het merendeel van de constructietijd en het geheugenverbruik
niet veranderen.

De uitvoeringstijd voor grotere begindieptes is iets kleiner, wat een gevolg van
de reductie van het aantal textuuraanspraken is. Echter deze verschillen zijn
minimaal. Doordat de uitvoeringstijd primair afhankelijk is van het aantal 
lichtberekeningen heeft de begindiepte dus ook weinig invloed op de 
uitvoeringstijd.

Op basis hiervan kan geconcludeerd worden dat het voordelig is om de eerste
lagen van de verbindingloze octree samen te voegen, doordat het gebruikte 
aantal texturen hierdoor gereduceerd wordt, zonder dat dit een negatieve 
invloed heeft op het geheugen en de uitvoeringstijd. Door Choi et. al. 
\cite{choi2009linkless} wordt een begindiepte van drie aangehouden om de overhead
die elke textuur met zich meebrengt te reduceren. Uit deze resultaten blijkt dat 
een begindiepte van drie geen vergroting van geheugenverbruik of uitvoeringstijd
met zich meebrengt. Om deze reden zal een begindiepte van drie gebruikt worden 
in de vergelijking met Tiled en Clustered Shading.

## Vergelijking met Tiled en Clustered Shading

\input{./img/tex/hs-compare-frames.tex}
\input{./img/tex/hs-compare-frames-lc.tex}
\input{./img/tex/hs-compare-lights.tex}
\input{./img/tex/hs-compare-resolution.tex}
\input{./img/tex/hs-compare-lights-res-lc.tex}

In de voorgaande secties zijn de verschillende parameters van de verbindingloze
octree ge\"evalueerd. Als laatste zal nu gekeken worden naar de performantie van
Hashed Shading in verhouding tot Tiled en Clustered Shading. Hiervoor wordt de 
uitvoeringstijd van Hashed Shading met die van Tiled Shading voor zowel de 
Forward als Deferred pijplijnen vergeleken. Tevens wordt het aantal lichtberekeningen van 
Hashed Shading vergeleken met het aantal lichtberekeningen van zowel Tiled en
Clustered Shading voor de Deferred pijplijn. Om een duidelijk zicht op de 
performantie te verkrijgen, zijn de uitvoeringstijd en aantal lichtberekeningen voor gehele uitvoeringen
als ook als functie van het aantal lichten en de resolutie verzameld. Deze zullen in 
de volgende secties verder gepresenteerd worden.

Zowel de data van Tiled Shading als Clustered Shading zijn verzameld met een tegelgrootte
van $32 \times 32$ pixels. Voor Hashed Shading zijn knoopgroottes van $0.25$, 
$0.5$ en $1$ maal de radius van de lichten in de \mbox{sc\`ene} gebruikt. De verbindingloze
octree is bij elk van deze knoopgroottes ge\"initaliseerd met een begindiepte 
van $3$.

### Frames

In figuur \ref{fig:hs-compare-frames:forward} en \ref{fig:hs-compare-frames:deferred} zijn de uitvoeringstijden per frame weergegeven voor
respectievelijk de Forward en Deferred pijplijn. In figuur \ref{fig:hs-compare-frames:lc} is het aantal
lichtberekeningen per frame weergegeven.

Voor Forward Shading ligt de uitvoeringstijd van Hashed Shading onder de 
uitvoeringstijd van Tiled Shading. Dit verschil in uitvoeringstijd is 
verwaarloosbaar voor de Deferred pijplijn. Dit verschil is te verklaren aan de 
hand van de reductie van het aantal lichtberekeningen en de simpliciteit van de
lichtberekening. In het geval van Deferred Shading zal het verschil in aantal
lichtberekeningen tussen Tiled en Hashed Shading kleiner zijn dan in Forward
Shading, doordat bij Deferred Shading slechts \mbox{\'e\'en} fragment per
pixel gegenereerd wordt. De winst in uitvoeringstijd die behaald wordt door
de reductie van het aantal lichtberekeningen wordt in het geval van Deferred
Shading te niet gedaan door de extra complexiteit geassocieerd met het ophalen
van de relevante lichten bij Hashed Shading. Bij een complexere shader zal
Hashed Shading waarschijnlijk beter presteren dan Tiled Shading.
Doordat het aantal lichtberekeningen wordt beperkt per fragment, leidt dit 
ertoe dat de reductie in aantal lichtberekeningen wel een significante invloed
heeft op de uitvoeringstijd bij Forward Shading.

De reductie in aantal lichtberekeningen is duidelijk terug te zien in figuur
\ref{fig:hs-compare-frames:lc}. Clustered Shading presteert slechts minimaal beter dan Hashed Shading
met een kleine knoopgrootte. In figuur \ref{fig:hs-compare-frames:lc:alley} is tevens duidelijk waar te nemen
dat Hashed Shading, net als Clustered Shading de slechtst mogelijke situatie van
Tiled Shading oplost.


### Lichten

In figuur \ref{fig:hs-compare-lights:forward} en \ref{fig:hs-compare-lights:deferred} zijn de gemiddelde uitvoeringstijden per frame als 
functie van het aantal lichten weergegeven voor respectievelijk de Forward en 
Deferred pijplijn. In figuur \ref{fig:hs-compare-lights:lc} is het gemiddeld aantal lichtberekeningen 
per frame als functie van het aantal lichten weergegeven.

Hierin is duidelijk te zien dat Hashed Shading voor de gebruikte lichtberekening
een vergelijkbare uitvoeringstijd heeft als Tiled Shading voor de Deferred 
Pijplijn. Binnen Forward Shading leidt Hashed Shading tot een factor twee
verbetering. Wanneer gekeken wordt naar het aantal lichtberekeningen als
functie van het aantal lichten, is te zien dat Hashed Shading vergelijkbaar
presteert als Clustered Shading.

### Resolutie

In figuur \ref{fig:hs-compare-resolution:forward} en \ref{fig:hs-compare-resolution:deferred} zijn de gemiddelde uitvoeringstijden per frame als 
functie van de resolutie weergegeven voor respectievelijk de Forward en 
Deferred pijplijn. In figuur \ref{fig:hs-compare-resolution:lc} is het gemiddeld aantal lichtberekeningen 
per frame als functie van de resolutie weergegeven.

De uitvoeringstijd en aantal lichtberekeningen als functie van de resolutie 
tonen dezelfde trend als de uitvoeringstijd en aantal lichtberekeningen als
functie van het aantal lichten. In het geval van Deferred Shading is de 
uitvoeringstijd van Hashed Shading vergelijkbaar met die van Tiled Shading.
Binnen Forward Shading stijgt de uitvoeringstijd met ongeveer een factor
twee langzamer. Het aantal lichtberekeningen van Hashed Shading stijgt 
vergelijkbaar met dat van Clustered Shading.

Hierbij dient de opmerking geplaatst te worden dat het geheugengebruik van
Hashed Shading onafhankelijk van de resolutie is, waar dit voor zowel Tiled
als Clustered Shading direct gekoppeld is aan de resolutie door de keuze van
de tegelgrootte.

