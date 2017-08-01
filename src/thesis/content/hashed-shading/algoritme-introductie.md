# Algoritme

In deze sectie wordt het Hashed Shading algoritme toegelicht. Hiervoor zal
eerst ingegaan worden op het achterliggende idee, en zal een overzicht
worden gegeven van de gebruikte datastructuren. Hiernazal ingegaan worden
op de constructie en het gebruik van Hashed Shading binnen de fragmentshader.

## Overzicht

\input{./img/tex/hs-datastructuren-overzicht.tex}

Het doel van Hashed Shading is om de datastructuren gebruikt voor de 
lichttoekenning gedeeltelijk her te gebruiken tussen frames. Dit wordt bereikt
door een camera-onafhankelijke verbindingloze octree te gebruiken om de ruimte
van de \mbox{sc\`ene} onder te verdelen. Voor elk volume geassocieerd met een 
bladknoop wordt bijgehouden welke lichten overlappen. Hiervoor zal vergelijkbaar
met Tiled en Clustered Shading een lichtindexlijst en een globale lichtlijst
bijgehouden worden. De verbindingloze octree vervangt dan het lichtrooster van
Tiled Shading, of de clusters van Clustered Shading. Dit leidt tot de 
datastructuren weergegeven in figuur \ref{fig:hs-datastructuren-overzicht}.

Er zijn drie componenten die uitgewerkt dienen te worden om Hashed Shading te 
gebruiken in grafische applicaties:

* De constructie van de datastructuren.
* Het opvragen van de lichtinformatie voor een punt $\mathbf{p}$.
* Het bijwerken van de datstructuren wanneer lichten aangepast worden.

\noindent Binnen `nTiled` zijn de eerste twee componenten ge\"implementeerd. 
Een strategie voor het bijwerken van de datastructuren zal besproken worden
in sectie \ref{sec:ondersteuning-dynamische-lichten}. 

Er zal eerst ingegaan worden op de constructie van de datastructuren. Vervolgens
zal ingegaan worden op het opvragen van de lichtinformatie, zoals deze plaatsvindt
op de grafische kaart.

## Octree-opdeling van de \mbox{sc\`ene}

\input{./img/tex/hs-opdeling-scene.tex}

Om de benodigde datastructuren op te bouwen dient de \mbox{sc\`ene} voorgesteld te worden
als een octree. dit betekent dat eerst de opdeling van de ruimte opgesteld moet worden. 
Daarna wordt aan deze opdeling de lichten toegekend. Voor deze opdeling wordt een
nieuwe set co\"ordinaten ge\"introduceerd, de octree-co\"ordinaten. Hierbij zijn de 
wereldco\"ordinaten getransleerd, zodanig dat de oorsprong van het octree-co\"ordinatenstelsel
overeen komt met de oorsprong van de octree. Hierdoor zullen alle relevante punten positief zijn.

De octree dient zodanig gekozen te worden dat alle lichten in de \mbox{sc\`ene} er binnen vallen.
Hiervoor wordt de oorsprong van de octree genomen als het grootste punt $\mathbf{p}_\text{min}$ dat 
kleiner is dan  alle lichtevolumes minus een offset $\mathbf{c}$. Indien $L$ de set van lichten is, 
kan dit gedefinieerd worden als:

$$ 
\begin{split} 
\mathbf{p_o} := \mathbf{p}_\text{min} - \mathbf{c} : \quad ( \forall \mathbf{l} \in S & p.x < l.p.x - l.r \land \\
                                                            & p.y < l.p.y - l.r \land \\
                                                            & p.z < l.p.z - l.r )\land \\
                            (\not \exists \mathbf{p^\prime} & ( p^\prime.x > p.x \lor \\ 
                                                            &   p^\prime.y > p.y \lor \\
                                                            &   p^\prime.z > p.z ) \land \\
                                 ( \forall \mathbf{l} \in S & p^\prime.x < l.p.x - l.r \land \\
                                                            & p^\prime.y < l.p.y - \l.r \land \\
                                                            & p^\prime.z < l.p.z -  l.r )) 
\end{split}
$$

\noindent De offset-waarde $\mathbf{c}$ is meegenomen om te voorkomen dat door afrondingsfouten lichtvolumes
buiten de octree zouden vallen. 

Nadat de oorsprong van de octree is berekend, dient de grootte van de octree bepaald te worden.
Op een vergelijkbare manier als de oorsprong, kan het maximule punt $\mathbf{p}_\text{max}$ bepaald worden.
Dit punt $\mathbf{p}_\text{max}$ is gedefinieerd als het kleinste punt dat groter is dan alle lichtvolumes. 
De octree wordt voorgesteld als een kubus, dus dient de lengte van deze kubus minimaal gelijk te zijn 
aan de grootste dimensie tussen de oorsprong $\mathbf{p}_o$ en het maximale punt $\mathbf{p}_\text{max}$ plus
de offset-waarde $\mathbf{c}$:

$$ \operatorname{max}\left(\mathbf{p}_\text{max} - \mathbf{p}_text{min} + 2 mathbf{c}\right) $$

De gebruiker stelt de grootte van de knopen in de diepste laag in. Dit wordt de 
minimale knoopgroote $\mathit{d}$ genoemd. De grootte van de octree kan vervolgens bepaald worden
aan de hand van de minimale lengte en de minimale knoopgrootte. Hierbij dient de integer $\mathit{l}$
zo klein mogelijk gekozen te worden zodanig dat geldt:

$$ 2^\mathit{l} * \mathit{d} \geq \operatorname{max}\left(\mathbf{p}_\text{max} - \mathbf{p}_text{min} + 2 mathbf{c}\right) $$ 

\noindent De waarde $\mathit{l}$ komt overeen met het aantal lagen dat de octree bezit.

Hiermee liggen alle mogelijke opdelingen van de \mbox{sc\`ene} vast. Dit is ge\"illustreerd in figuur \ref{fig:hs-opdeling-scene}.

## Voorstelling van enkele lichten

\input{./img/tex/hs-light-grid.tex}
\input{./lst/hs-node_in_light.tex}

Wanneer de grootte en oorsprong van de octree berekend zijn, ligt de positie van alle mogelijke konpen vast.
De volgende stap is om de lichten in de \mbox{sc\`ene} toe te kennen aan de opdeling. 
Hiervoor zal eerst voor elk van de lichten bepaald worden met welke bladknopen uit de diepste laag van de 
octree deze overlappen. Op basis van het lichtvolume kan het kleinst-mogelijke rooster van knopen van 
minimale grootte waarbinnen het licht $\mathbf{l}$ valt, berekend worden. Hiervoor wordt bepaald
in welke knopen het kleinste en grootste punt van de omsluitende kubus van het lichtvolume vallen:

\begin{align*}
\mathbf{p}_{\mathbf{l}, \text{min}} &= \left\lfloor \frac{\mathbf{l}.\text{positie} - \mathbf{l}.\text{radius}}{\mathit{d}}\right\rfloor \\
\mathbf{p}_{\mathbf{l}, \text{max}} &= \left\lfloor \frac{\mathbf{l}.\text{positie} + \mathbf{l}.\text{radius}}{\mathit{d}}\right\rfloor 
\end{align*}

\noindent waarbij de punten $\mathbf{p}_{\mathbf{l}, \text{min}}$ en $\mathbf{p}_{\mathbf{l}, \text{max}}$ 
zich bevinden in octreeco\"ordinaten. De waarde $\mathit{d}$ is de minimale knoopgrootte. De grootte van het rooster is vervolgens gedefinieerd als:

$$ \operatorname{max}\left(\mathbf{p}_{\mathbf{l}, \text{max}} - \mathbf{p}_{\mathbf{l}, text{min}}\right) + 1 $$

\noindent De oorsprong van het rooster in wereldco\"ordinaten is vervolgens:

$$ \mathbf{p}_{\mathbf{l}, \text{min}} * \mathit{r} + \mathbf{p}_o $$

Vervolgens dient per knoop bepaald te worden of deze overlapt met het lichtvolume. Hiervoor wordt gekeken
of het punt $\mathbf{v}$ dat binnen het knoopvolume valt en het dichtstbij de oorsprong van de lichtbron ligt, 
op een afstand kleiner dan de radius van het licht ligt. Is dit het geval dan overlapt de knoop met het lichtvolume. 
Dit is weergeven in figuur \ref{fig:hs-light-grid}. Om het punt $\mathbf{v}$ dat binnen het knoopvolume ligt en zich op de kleinste afstand 
van de oorsprong van het licht $\mathbf{l}$ bevindt, te vinden, wordt de oorsprong van het licht per dimensie 
geklemd tussen de uiterste waardes van het knoopvolume:

$$ \mathbf{v} = 
\begin{pmatrix}
  \mathbf{l}.\text{position}_x \vert_{\mathbf{k}_{x,i}, \mathbf{k}_{x,i} + \mathit{d}} \\
  \mathbf{l}.\text{position}_y \vert_{\mathbf{k}_{y,i}, \mathbf{k}_{y,i} + \mathit{d}} \\
  \mathbf{l}.\text{position}_z \vert_{\mathbf{k}_{z,i}, \mathbf{k}_{z,i} + \mathit{d}} 
\end{pmatrix} $$

\noindent waar $\mathbf{k}_i$ de oorsprong van het knoopvolume is, en $\mathit{d}$ de minimale knoopgrootte.
Dit resulteert in de code weergegeven in listing \ref{lst:hs-node-in-light}.

\input{./img/tex/hs-p1.tex}

Het is niet nodig om deze berekening voor elke knoop in het rooster uit te voeren. 
De lichtvolumes zullen altijd uniform zijn. Dit betekent dat een flood-fill algoritme
gebruikt kan worden om ofwel de lege of volle knopen in het rooster te vullen.
Het volume van een puntlicht is een bol ter grootte van:

$$ V = \frac{4}{3}\pi r^3 $$

\noindent Het volume van een bol omvat iets meer dan de helft van het volume van de 
omsluitene kubus, om deze reden is er voor gekozen om er van uit te gaan 
dat alle knopen overlappen met het licht. Vervolgens worden de niet overlappende 
knopen als zodanig gemarkeerd. Hiervoor wordt begonnen in elk van de hoekpunten van
het rooster. Dit gehele proces is weergeven in figuur \ref{fig:hs-p1}.

\input{./img/tex/hs-licht-octree.tex}

Nu vastgesteld is welke knopen van minimale grootte overlappen met een lichtvolume,
zijn er drie mogelijke vervolgstappen:

* De gevulde knopen kunnen direct worden samengevoegd. Op basis van deze set
  knopen kan dan bottom-up de octree worden opgebouwd.
* De roosters per licht kunnen worden opgeslagen. Hierna wordt de informatie in
  deze roosters samengevoegd tot \mbox{\'e\'enzelfde} set van knopen als
  in de eerste mogelijkheid.
* De roosters kunnen per licht omgezet worden naar een octreestructuur, die
  vervolgens wordt opgeslagen. Deze octrees kunnen vervolgens worden samengevoegd
  om zo tot een enkele octree te komen die de gehele \mbox{sc\`ene} beschrijft.
  
\noindent Indien slechts statische lichten worden gebruikt, is er geen reden
om lichten los bij te houden, dus zal de eerste optie in dit geval de meest
effici\"ente keuze zijn. Indien lichten dynamisch van aard zijn, kan het 
nodig zijn dat de knopen waarop een licht invloed heeft, veranderen. Om
effici\"ent de verandering in knopen te berekenen kan de oude set knopen
vergeleken worden met de set van knopen die de nieuwe situatie beschrijft.
Om onnodig rekenwerk te voorkomen kan vervolgens de set van knopen waarop
een licht invloed heeft in de huidige frame bijgehouden worden.
Wanneer slechts het rooster per licht wordt bijgehouden, optie twee, is het
nodig om elke knoop in het rooster met \mbox{\'e\'en} bit voor te stellen.
Indien de knoopgrootte groot is, of de lichtvolumes klein kan dit 
effici\"ent bijgehouden worden. Echter deze  set knopen wordt
kubiek groter bij kleinere knoopgroottes. Wanneer de knoopgrootte klein is
zal een octreevoorstelling leiden tot minder geheugengebruik per licht,
waardoor optie drie effici\"enter zal zijn.
De voorstelling van een licht als octree is ge\"illustreerd in figuur \ref{fig:hs-licht-octree}.

Binnen `nTiled` is er voor gekozen om de lichten op te slaan in de octreevoorstelling.
Dit is gedaan met het oog op de uitbreiding om dynamische lichten te ondersteunen.

De octreevoorstelling van een enkel licht wordt top-down opgebouwd met behulp van
het opgestelde rooster. Hierbij wordt de octreeknoop die het gehele rooster omvat
genomen als de wortelknoop voor de octreevoorstelling van het enkele licht. 
Beginnend van deze knoop wordt bepaald of een knoop een takknoop of bladknoop is.
In het geval dat een knoop een takknoop is, worden ook de kindknopen van deze
knoop ge\"evalueerd. 

\input{./img/tex/hs-licht-octree-dt.tex}

Voor knoop $\mathbf{k}$ zijn er initieel drie mogelijke situaties:

* Het volume van knoop $\mathbf{k}$ overlapt niet met het rooster.
* Het volume van knoop $\mathbf{k}$ overlapt gedeeltelijk met het rooster.
* Het volume van knoop $\mathbf{k}$ valt in zijn geheel binnen het rooster.

In het eerste geval zal de knoop $\mathbf{k}$ altijd een lege bladknoop zijn,
gezien er geen gevulde knopen buiten het rooster vallen. 

In het tweede geval zijn er twee mogelijkheden, of wel er liggen volle roosterknopen
binnen knoop $\mathbf{k}$, of knoop $\mathbf{k}$ bestaat slechts uit lege roosterknopen.
Indien de roosterknoop het dichtst bij de oorsprong van het licht leeg is, zullen
de andere roosterknopen tevens leeg zijn. Dit is een gevolg van het feit dat het lichtvolume
bolvormig is. Er zullen geen knopen verder dan de ge\"evalueerde roosterknoop wel gevuld zijn
als de ge\"evalueerde knoop leeg is. In dit geval is knoop $\mathbf{k}$ een
lege bladknoop. Is de dichtstbijzijnde roosterknoop gevuld, dan bevat knoop $\mathbf{k}$
zowel lege als gevulde knopen, en is het een takknoop.

In het laatste geval zijn er drie mogelijke situaties:

* Knoop $\mathbf{k}$ omvat slechts lege roosterknopen.
* Knoop $\mathbf{k}$ omvat slechts gevulde roosterknopen.
* Knoop $\mathbf{k}$ omvat zowel lege als gevulde roosterknopen.

\noindent Knoop $\mathbf{k}$ is in deze situaties respectievelijk een lege bladknoop, 
een volle bladknoop, en een takknoop.
Indien de roosterknoop het dichtst bij de oorsprong van het licht leeg is, dan omvat knoop 
$\mathbf{k}$ slechts lege roosterknopen. Indien deze roosterknoop gevuld is, en de 
roosterknoop het verst van de oorsprong van het licht is tevens gevuld, dan omvat
knoop $\mathbf{k}$ slechts gevulde knopen. Anders bevat knoop $\mathbf{k}$ zowel een
lege als een gevulde knoop, en zal deze dus een takknoop zijn. 
De beslissingsboom voor dit algoritme is weergeven in figuur \ref{fig:hs-licht-octree-dt}. 
Hiermee kan elk licht als octree worden voorgesteld.


## Voorstelling van de \mbox{sc\`ene}

Nadat vastgesteld is hoe elk licht individueel wordt toegekend aan de opdeling, dient de octree 
voor de gehele \mbox{sc\`ene} opgesteld te worden. Deze \mbox{sc\`ene-octree} bevat per
bladknoop een set referenties naar de relevante lichten.

Indien de individuele lichten met een rooster voorgesteld zijn, kunnen de roosterknopen 
samengevoegd worden zodat een set van bladknopen ontstaat. Deze kunnen vervolgens bottom-up
samengevoegd worden, om zo tot een octree te komen.

Indien de individuele lichten voorgesteld zijn met een octree, kunnen elk van deze 
lichtoctrees top-down worden samengevoegd tot een \mbox{sc\`ene-octree}. Hiervoor
worden de lichtoctrees iteratief toegevoegd aan een \mbox{sc\`ene-octree} 
ge\"initialiseerd met een enkele lege bladknoop. Eerst wordt afgedaald tot de 
knoop die correspondeert met de wortel van de lichtoctree. Indien een bladknoop
$\mathbf{k}$ wordt tegengekomen, wordt deze opgedeeld door deze te vervangen met
een takknoop met kinderen gelijk aan bladknoop $\mathbf{k}$. Vervolgens 
wordt de wortelknoop toegevoegd aan de corresponderende \mbox{sc\`ene-knoop}. 
Hierbij zijn er vijf mogelijke situaties die beschreven zijn in tabel \ref{tbl:hs-licht-octree}.

\input{./tbl/hs-lichtoctree.tex}

## Verbindingloze octree

\input{./img/tex/hs-algoritme-beschrijving.tex}

Nu de \mbox{sc\`ene-octree} is opgesteld kan de set van datastructuren die gebruikt wordt in
de lichttoekenning geconstrueerd worden. Hiervoor dient de \mbox{sc\`ene-octree} voorgesteld
te worden als een verbindingloze octree. Tevens moet de lichtindexlijst opgesteld worden.

Omdat de set van relevante lichten slechts gedefinieerd is voor de gevulde bladknopen, is er
voor gekozen om de octreestructuur en lichtinformatie gescheiden op te slaan. Per laag $l$ 
worden dus twee spatiale hashfuncties opgesteld, \mbox{\'e\'en} die de octreebeschrijving 
bevat, en \mbox{\'e\'en} die de lichtinformatie voor alle gevulde knopen in laag $l$ bevat.

De lichtinformatie wordt vergelijkbaar voorgesteld als in Tiled en Clustered Shading. 
Elke gevulde bladknoop krijgt twee integers toegewezen die een subset van de lichtindexlijst
specificeren.

Het algoritme voor het opstellen van de datastructuren is weergeven in figuur \ref{fig:hs-algoritme-beschrijving}.
Na de uitvoering is een lichtindexlijst en twee sets van spatiale hashfuncties opgesteld. Deze kunnen vervolgens 
in het geheugen geladen en gebruikt door de shaders worden.

## Lichttoekenning

Het tweede component van Hashed Shading is het ophalen van de relevante lichtinformatie
voor punt $\mathbf{p}$ binnen de fragmentshader. Dit komt neer op het doorlopen 
van de verbindingloze octree, totdat een bladknoop wordt bereikt. In het geval
dat deze niet leeg is, kan de corresponderende lichtinformatie worden opgehaald uit
de datahashtabel. 

De afdaling komt neer op per laag het berekenen van de octreeknoop beschrijving waarin 
punt $\mathbf{p}$ valt:

$$ (\mathtt{is_leaf}, \mathtt{is_filled}) = H_l\left[ \mathit{h}_0\left(\left\lfloor \frac{\mathbf{p}}{\mathit{d}_l} \right\rfloor\right) + \Phi\left[ \mathit{h}_1\left(\left\lfloor \frac{\mathbf{p}}{\mathit{d}_l} \right\rfloor\right) \right] \right] $$

\noindent waarbij $\mathit{d}_l$ de knoopgrootte van de laag $l$ is.

$\mathtt{is_leaf}$ en $\mathtt{is_filled}$ beschrijven alle acht kinderen van de takknoop $\mathbf{k}$ in laag $l$.
De bits die overeenkomen met de kindknoop $\mathbf{k^\prime}$ van takknoop $\mathbf{p}$ waarin punt $\mathbf{p}$ valt, 
bevinden zich op positie:

$$ \mathit{k}^prime_\mathtt{bit} = \mathit{k}_x^\prime + 2 \cdot\mathit{k}_y^\prime + 4\cdot\mathit{k}_z^\prime $$

\noindent Door bitverschuivingen toe te passen, kan de bit op positie $\mathit{k}^prime_\mathtt{bit}$ achterhaald
worden.

Er zijn drie mogelijke situaties:

* kindknoop $\mathbf{k}^\prime$ is een takknoop, en er wordt verder afgedaald in de octree
* kindknoop $\mathbf{k}^\prime$ is een lege bladknoop, en een nulvector wordt teruggegeven.
* kindknoop $\mathbf{k}^\prime$ is een gevulde bladknoop, en de lichtinformatie wordt opgehaald uit de tweede spatiale hashfunctie
  geassocieerd met laag $l$.
  
\noindent Vervolgens kan op een vergelijkbare manier als in Tiled en Clustered Shading de set van
relevante lichten worden overlopen om de uiteindelijke kleur van punt $\mathbf{p}$ te berekenen. 
De `GLSL`-code voor dit algoritme is gegeven in listing \ref{lst:hs-lichttoekenning}

\input{./lst/hs-lichttoekenning.tex}
