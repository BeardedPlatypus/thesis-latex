## Overzicht van spatiale datastructuren

### Binaire-ruimte-partitionering

Binaire ruimte partitionering is een methode om een $d$-dimensionale ruimte onder
te verdelen. Hiervoor wordt aan de hand van hypervlakken de ruimte recursief
opgedeeld\cite{naylor1998tutorial}. Waarbij een hypervlak een $d$-dimensionaal 
vlak is. Deze recursieve opdeling wordt opgeslagen in een 
binaire-ruimte-partitioneringsboom. In het geval van een 1-dimensionale ruimte, 
zoals een lijst, komt dit overeen met een binaire zoekboom, waarbij de 
hypervlakken punten binnen de lijst zijn. In het geval van een drie dimensionale 
ruimte zullen de hypervlakken standaard vlakken zijn. De volgende datastructuren 
kunnen gedefinieerd worden als specifieke  implementaties van binaire-ruimte-partitionering.

### Rooster

Het rooster is de meest simpele spatiale datastructuur. De relevante ruimte 
wordt grofweg in cellen van een specifieke grootte onderverdeeld. Binnen elke cel wordt 
vervolgens een verwijzing naar de relevante data bijgehouden.

Een dergelijke datastructuur kan, indien de grootte van de cellen klein wordt
genomen, een hoge nauwkeurigheid van relevante lichten opleveren. Tevens zullen
cellen snel en eenvoudig toegankelijk zijn. Echter hier staat tegenover dat bij 
een na\"ive implementatie het geheugengebruik zeer snel toeneemt, gezien voor 
elke cel binnen het rooster de ruimte om een cel op te slaan gereserveerd dient
te worden, ongeacht of deze daadwerkelijke data bevat.

Clustered Shading maakt gebruik van een vorm van een rooster over het zichtfrustrum.
Hierbij wordt de data compacter voorgesteld door slechts cellen die zowel licht
als geometrie bevatten op te slaan.

Een rooster kan simpelweg gedefinieerd worden als een drie dimensionale lijst. 
Indien dit als binaire-ruimte-partitionering wordt weergegeven, wordt recursief 
in elke dimensie steeds \mbox{\'e\'en} cel gedefinieerd.

### Octree

\input{./img/tex/hs-octree.tex}

De octree is een boomdatastructuur waarbij met elke knoop een kubus is geassocieerd. 
Elke takknoop bezit precies acht kinderen De kinderen verdelen de ruimte geassocieerd 
met de takknoop op in acht equivalente nieuwe
kubussen\cite{meagher1982geometric}. Deze structuur is ge\"illustreerd in figuur
\ref{fig:hs-octree}. Data kan ofwel in elke knoop opgeslagen worden, ofwel alleen 
in de bladknopen. Indien een knoop een ruimte volledig beschrijft is het niet nodig 
om deze verder onder te verdelen. Deze hi\"erarchische structuur zorgt ervoor dat 
het mogelijk is  om de ruimte in hoge resolutie te beschrijven zorder tegen dezelfde
geheugenproblemen als het rooster aan te lopen, doordat grote homogene ruimtes 
met slechts \mbox{\`e\`en} enkele knoop voorgesteld kunnen worden.

De octree definieert een ruimtepartitionering door per takknoop drie hypervlakken
op te stellen. Deze zullen altijd het middelpunt van de octreeknoop snijden.

### kd-boom

Een kd-boom is een boomstructuur in $d$ dimensies, waarbij $k$ discriminatoren
zijn gedefinieerd\cite{bentley1975multidimensional}. De discriminator associeert
een specifieke ori\"entatie van een hypervlak met een punt. Alle knopen op een 
zelfde niveau delen dezelfde discriminator. 
Een takknoop definieert vervolgens de positie van het hypervlak met ori\"entatie 
$k_i$. Hierbij wordt de ruimte geassocieerd met de knoop opgedeeld in twee
delen.

Dit is een specifiek geval van binaire-ruimte-partitionering, op elk niveau 
wordt de ruimte in twee helften ingedeeld. Het verschil met generieke 
binaire-ruimte-partitionering is dat de set van hypervlakken slechts een subset is 
van alle mogelijke hypervlakken.

### R-boom

De R-boom is een $n$-dimensionale zelfbalancerende boom. Met elke knoop is een
$n$-dimensionaal vierkant geassocieerd. De data opgeslagen in de R-boom bevindt
zich in de bladknopen, waar de positie van elk datapunt binnen het vierkant 
geassocieerd met de bladknoop ligt\cite{guttman1984r}. De $n$-dimensionale 
vierkanten hebben verder de volgende eigenschappen

* De vierkanten overlappen minimaal
* Elk vierkant bevat slechts een minimale hoeveelheid lege ruimte.

Deze eigenschappen in combinatie met het feit dat de boom gebalanceerd is, 
zorgen ervoor dat de spatiale data effici\"ent opgehaald kan worden. 

## Keuze voor de datastructuur

Aan het begin van deze sectie is het doel van de lichttoekenningsdatastructuur
gesteld op het effici\"ent onderverdelen van de ruimte, zodanig dat voor een 
punt $\mathbf{p}$ in deze ruimte de set van relevante lichten opgehaald kan 
worden. Hiervoor dient de ruimte onderverdeeld te worden, waarna vervolgens
de lichten toegekend moeten worden aan de volumes van deze opdeling op basis 
van de corresponderende lichtvolumes. Nadat de datastructuur opgesteld is, dient 
het volume van de opdeling waar punt $\mathbf{p}$ in valt berekend te kunnen 
worden.

De R-boom is ontwikkeld met het op op zoekproblemen zoals het dichtste-buurprobleem.
Om deze reden is het minder geschikt als lichttoekenningsdatastructuur, waar het
doel is om een beschrijving rond het punt $\mathbf{p}$ te geven. 

De rooster-datastructuur vereist dat voor de gehele \mbox{sc\`ene} cellen worden
opgesteld met een uniforme grootte. Om een accurate voorstelling te verkrijgen dient
deze grootte zo klein mogelijk gekozen te worden. Dit leidt tot een groot 
geheugengebruik, gezien voor elk van deze cellen geheugen gereserveerd dient te worden.
Dit geheugenverbruik gaat in tegen de eis dat de datastructuur compact voor te stellen
moet zijn.

Zowel de kd-boom als de octree zijn hi\"erarchische datastructuren waardoor deze compacter
in het geheugen voorgesteld kunnen worden. Doordat de lichtvolumes niet als geheel aan
de volumes van de opdeling toegekend hoeven te worden kunnen de grenzen van de opdeling
arbitrair gekozen worden. In het geval van de kd-boom kunnen deze grenzen gekozen worden
op basis van de data opgeslagen in de kd-boom. Voor de octree liggen de mogelijke grenzen van 
de opdeling vast, ongeacht de data in de octree. Dit betekent dat voor een effici\"ente 
opdeling van de lichten binnen de kd-boom een heuristiek voor de plaatsing van de 
grenzen ontwikkeld dient te worden. Hierbij dient tevens rekening gehouden te worden
met het dynamische karakter van de lichten. 

De octree-implementatie vereist deze extra complexiteit niet. Daarnaast zou de uniformiteit
van de knopen per laag van de octree het ondersteunen van dynamische lichten moeten
vergemakkelijken. Verder is de set van relevante lichten voor een punt $\mathbf{p}$ 
effici\"ent op te halen door de octree te doorlopen. De hi\"erarchische structuur 
maakt het mogelijk om de octree compact in het geheugen voor te stellen.
Om deze redenen is de octree-datastructuur gekozen als basis voor het Hashed Shading 
algoritme.

