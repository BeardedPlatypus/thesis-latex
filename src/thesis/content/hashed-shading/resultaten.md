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

\input{./img/tex/hs-sd-cons-mem.tex}
\input{./img/tex/hs-sd-li-exec.tex}

Zoals vermeld in sectie \ref{sec:theorie-verbindingloze-octree} is het mogelijk om naast de knoopgrootte de
begindiepte in te stellen voor de verbindingloze octree. Hierbij komt een 
begindiepte van \mbox{\'e\'en} overeen met een beschrijving van elke laag binnen
de verbindingloze octree, en een diepte van het aantal lagen minus 
\mbox{\'e\'en} een verbindingloze octree bestaande uit slechts een enkele laag.

Het veranderen van deze waarde heeft geen invloed op het aantal 
lichtberekeningen dat wordt uitgevoerd, doordat ongeacht de begindiepte dezelfde
set van lichten wordt opgehaald binnen de renderstap. Het kan echter wel van 
invloed zijn op de uitvoeringstijd, doordat bij een grotere begindiepte minder 
maal het geheugen dient te worden aangesproken.

Daarnaast zal het van invloed zijn op het geheugengebruik en de constructietijd.
Het gebruik van kleine texturen, bijvoorbeeld van 1 pixel voor de eerste laag 
van de verbindingloze octree, leidt veelal tot onnodig geheugengebruik, door de
overhead geassocieerd met het bijhouden van texturen. Een grotere begindiepte 
leidt echter ook tot meer kleinere knopen die expliciet bijgehouden dienen te
worden. Dit leidt tot een groter geheugengebruik. Daarnaast leidt een groter
aantal knopen tot een grotere constructietijd, doordat elk van deze knopen
toegekend dient te worden binnen de corresponderende spatiale hashfunctie.

Om deze aspecten te evalueren zijn de volgende figuren opgesteld. In figuur
\ref{fig:hs-sd-construction} is de constructietijd als functie van de knoopgrootte weergegeven
bij verschillende begindieptes voor de grootste gedefinieerde set lichten
per scene. In figuur \ref{fig:hs-sd-memory} en \ref{fig:hs-sd-light-indices} zijn
respectievelijk het aantal pixels in de datastructuren en het aantal lichtindices 
als functie van de  knoopgrootte voor verschillende begindieptes gegeven. 
Als laatste is de rendertijd als functie van de knoopgrootte voor de verschillende begindieptes
weergegeven in figuur \ref{fig:hs-sd-exec}.

Uit alle figuren valt op te maken dat de ge\"evalueerde begindieptes geen 
significante invloed hebben op de constructietijd, geheugenverbruik, en 
uitvoeringstijd. De constructietijd en het geheugenverbruik kan verklaard worden
doordat een verandering van de begindiepte slechts invloed heeft op de eerste 
lagen van de verbindingloze octree. Zoals al bleek uit de resultaten van het
geheugenverbruik per laag laag van de verbindingloze octree, fig. \ref{fig:hs-layered-mem},
bevindt het merendeel van de knopen zich in de diepere lagen. Een samenvoeging
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
\cite{choi2009linkless} wordt een begindiepte van $3$ aangehouden om de overhead
die elke textuur met zich meebrengt te reduceren. Uit deze resultaten blijkt dat 
een begindiepte van $3$ geen vergroting van geheugenverbruik of uitvoeringstijd
met zich meebrengt. Om deze reden zal een begindiepte van 3 gebruikt worden 
in de vergelijking met Tiled en Clustered shading.

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
Forward als Deferred pijplijnen. Tevens wordt het aantal lichtberekeningen van 
Hashed Shading vergeleken met het aantal lichtberekeningen van zowel Tiled en
Clustered Shading voor de Deferred pijplijn. Om een duidelijk zicht op de 
performantie te verkrijgen zijn deze waardes verkregen voor gehele uitvoeringen
als ook als functie van het aantal lichten en de resolutie. Deze zullen in 
de volgende secties verder gepresenteerd worden.

Zowel Tiled Shading als Clustered Shading data zijn verkregen met een tegelgrootte
van $32 \times 32$ pixels. Voor Hashed Shading zijn knoopgroottes van $0.25$, 
$0.5$ en $1$ maal de radius van de gebruikte lichten gebruikt. De verbindingloze
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
Shading teniet gedaan door de extra complexiteit geassocieerd met het ophalen
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
per frame als functie van het resolutie weergegeven.

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

