## Overzicht van Spatiale Datastructuren

### Binaire ruimte partionering

\input{./img/tex/hs-datastructuur-bsp.tex}

Binaire ruimte partionering is een methode om een $d$ dimensionale ruimte onder
te verdelen. Hiervoor wordt aan de hand van hypervlakken de ruimte recursief
opgedeeld.\cite{naylor1998tutorial} Waarbij een hypervlak een $d$ dimensionaal 
vlak is. Deze recursieve opdeling wordt opgeslagen in een 
binaire-ruimte-partioneringsboom. In het geval van een 1-dimensionale ruimte, 
zoals een lijst, komt dit overeen met een binaire zoekboom, waarbij de 
hypervlakken een punt binnen de lijst is. In het geval van een 3-dimensionale 
ruimte zullen de hypervlakken standaard vlakken zijn, een illustratie voor een 
drie dimensionale ruimte is weergegeven in figuur \ref{fig:hs-datastructuur-bsp}. 
De volgende datastructuren kunnen gedefinieerd worden als specifieke 
implementaties van binaire ruimte partionering.

### Rooster

\input{./img/tex/hs-datastructuur-grid.tex}

Het rooster is de meest simpele spatiale datastructuur. De relevante ruimte 
wordt grofweg in cellen van een specifieke grootte onderverdeeld, zoals 
weergegeven in fig. \ref{fig:hs-datastructuur-grid}. Binnen elke cel wordt 
vervolgens een verwijzing naar de relevante data bijgehouden.

Een dergelijke datastructuur kan, indien de grootte van de cellen klein wordt
genomen, een hoge nauwkeurigheid van relevante lichten opleveren. Tevens zullen
cellen snel en eenvoudig toegankelijk zijn. Echter hier staat tegenover dat bij 
een na\"ive implementatie het geheugengebruik zeer snel toe neemt, gezien voor 
elke cel binnen het rooster deze verwijzing dient te worden opgeslagen. 

Clustered Shading maakt gebruik van een vorm van een rooster over de viewport.
Hierbij wordt de data compacter voorgesteld door slechts cellen die zowel licht
als geometrie bevatten, op te slaan.

\input{./img/tex/hs-datastructuur-grid-bsp.tex}

Een rooster kan simpelweg gedefinieerd worden als een drie dimensionale lijst. 
Indien dit als binaire ruimte partionering wordt weergegeven, wordt recursief 
in elke dimensie steeds \'e\'en cel gedefinieerd, zoals weergegeven in figuur 
\ref{fig:hs-datastructuur-grid-bsp}. 

### Octrees

\input{./img/tex/hs-octree.tex}

De octree is een boomdatastructuur waarbij elke takknoop precies acht kinderen
bezit. Elke knoop kan voorgesteld worden als een kubus. De kinderen van een tak
knoop verdelen de ruimte geassocieerd met de takknoop in acht equivalente 
kubussen.\cite{meagher1982geometric} Dit is weergegeven in fig 
\ref{fig:hs-octree}. 

Data kan ofwel in elke knoop opgeslagen worden, ofwel slechts in de bladknopen. 
Indien een knoop een ruimte volledig beschrijft is het niet nodig om deze verder 
onder te verdelen. Deze hierarchische structuur zorgt ervoor dat het mogelijk is 
om de ruimte in hoge resolutie te beschrijven, en tevens niet tegen de 
geheugenproblemen van het rooster aan te lopen, doordat grote homogene ruimtes 
door slechts een enkele knoop kunnen worden voorgesteld. 

\input{./img/tex/hs-datastructuur-octree-bsp.tex}

De octree definieert een ruimtepartionering door per takknoop drie hypervlakken
op te stellen. Deze zullen altijd het middelpunt van de octreeknoop snijden,
zoals weergegeven in figuur \ref{fig:hs-datastructuur-octree-bsp}.

### kd-boom

\input{./img/tex/hs-datastructuur-kd.tex}

Een kd-boom is een boomstructuur in $d$ dimensies, waarbij $k$ discriminatoren
zijn gedefinieerd.\cite{bentley1975multidimensional} De discriminator associeert
een specifieke orientatie van een hypervlak met een punt. Alle knopen op een 
zelfde niveau delen dezelfde discriminator. 
Een takknoop definieert vervolgens de positie van het hypervlak met orientatie 
$k_i$. Hierbij wordt de ruimte geassocieerd met de knoop opgedeeld in twee
delen. Dit is weergegeven in figuur \ref{fig:hs-datastructuur-kd}.

Dit is een specifiek geval van binaire ruimte partitionering, op elk niveau 
wordt de ruimte in twee helften ingedeeld. Het verschil met generieke 
binaire ruimte partionering is dat de set van hypervlakken slechts een subset is 
van alle mogelijke hypervlakken.

### R boom

\input{./img/tex/hs-datastructuur-r.tex}

De r-boom is een $n$-dimensionale zelf-balancerende boom. Elke knoop bevat een 
$n$-dimensionaal vierkant. In de bladknopen bevindt zich binnen dit vierkant de
data geassocieerd met deze knoop. In het geval van de takknoop bevinden alle
kinderen zich binnen het vierkant geassocieerd met de knoop. \cite{guttman1984r}
Hierbij hebben de vierkanten twee belangrijke eigenschappen:

* De vierkanten overlappen niet
* De vierkanten bevatten zo min mogelijk lege ruimte

In combinatie met het feit dat de boom gebalanceerd is, zorgt dit voor de 
mogelijkheid om spatiale data effici\"ent op te halen.

## Keuze voor de octree-datastructuur

Het doel van lichttoekenning is om de ruimte zodanig onder te verdelen dat 
de relevante lichten voor een punt in de wereld effici\"ent opgehaald kunnen
worden. De spatiale datastructuur die gebruikt wordt voor het ophalen van de
lichten dient te voldoen aan de eerder genoemde eisen. 

Een belangrijke observatie is dat dit geen dichtste-buur-probleem is. Onder 
perfecte omstandigheden zou de datastructuur alle lichten waarvan het punt in 
het lichtvolume valt, teruggeven, en geen enkel ander licht.
De punten zijn hierbij zijn de fragmenten die geprojecteerd zijn op de viewport.

Zowel de kd-boom als de R-boom zijn ontwikkeld met het dichtste-buur-probleem in
gedachte, waarbij de dataset bestaat uit een set van punten. Deze datastructuren 
zijn daarom minder geschikt voor lichttoekenning, waarbij de data geen punten 
maar volumes zijn. 

Zowel het rooster als de octree zijn geschikter voor lichttoekenning, omdat de
manier van opdeling bepaald wordt door het volume, en niet door de data. 
In het geval van het rooster levert dit uniforme kubussen op waarvoor voor
elk volume bepaald kan worden met welke lichtvolumen het overlapt. Dit betekent
dat ook voor grote uniforme ruimtes een groot aantal kubussen zijn gedefinieerd.
Hierdoor schaalt het rooster slecht met de grootte van de ruimte. De octree is
in staat om dergelijke uniforme ruimtes effici\"ent voor te stellen.
Om deze redenen is gekozen voor de octree-datastructuur als basis voor het
camera-onafhankelijke lichttoekenningsalgoritme.

