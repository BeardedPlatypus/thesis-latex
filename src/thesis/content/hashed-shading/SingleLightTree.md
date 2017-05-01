## Enkele Licht Boom

\input{./img/tex/hs-slt.tex}

De enkele licht boom (Single Light Tree) beschrijft de octree representatie van
een enkel licht binnen de gehele licht octree. Een voorbeeld hiervan is gegeven
in figuur \ref{fig:hs-slt}. Elke bladknoop beschrijft of het volume geassocieerd
met de bladknoop een gedeelte van het lichtvolume van de lichtbron bevat. De
verzameling van alle enkele lichtbomen wordt samengevoegd om de volledige licht
octree te verkrijgen. 

Om een enkele lichtboom op te stellen is de volgende informatie nodig:

* De lichtbron en zijn lichtvolume.
* Een grootte voor de ribben van de kleinst mogelijke bladknoop
* De oorsprong van de licht octree

Voor de licht octree oorsprong moet gelden dat deze kleiner is in elke dimensie
dan de oorsprong van het licht minus de radius:

$$ \forall d \in \lbrace x, y, z \rbrace :\quad p_d - r > o_d $$

Waar $p_d$ de oorsprong van de lichtbron is in dimensie $d$, r de radius van de
lichtbron en $o_d$ de oorsprong van de licht octree in dimensie $d$. 

De enkele lichtboom wordt opgebouwd in twee stappen. Eerst wordt een rooster 
opgesteld bestaande uit knopen van minimale lengte. Voor deze knopen wordt
vastgesteld of zij overlappen met het lichtvolume van de lichtbron. 
Vervolgens wordt dit rooster gebruikt om van bovenaf de enkele lichtboom op te
stellen. Beginnend vanaf de wortelknoop wordt bepaald of een knoop een tak- of
een bladknoop is.

Het rooster in de eerste stap wordt zodanig gekozen dat het bestaat uit het 
minimale aantal knopen dat het volledige lichtvolume omvat. Vervolgens dient per
knoop bepaald te worden of deze overlapt met het lichtvolume. Hiervoor wordt 
gekeken of het punt $\mathbf{v}$ binnen de knoop dat het dichtst bij de 
oorsprong van de lichtbron ligt binnen de radius van het licht valt. 
Dit punt kan gevonden worden door een klemoperatie toe te passen op de oorsprong
van de lichtbron. Voor elke dimensie wordt de positie van de lichtbron geklemd 
tussen de uiterste waarden van de knoop:

$$ \mathbf{v} = \begin{pmatrix} 
                  p_x |_{[k_x, k_x + l]} \\
                  p_y |_{[k_y, k_y + l]} \\
                  p_z |_{[k_z, k_z + l]}
                \end{pmatrix} $$

Waarbij $p_d$ de oorsprong van de lichtbron in dimensie $d$ is, $k_d$ oorsprong 
van de knoop in dimensie $d$ is, en $l$ de lengte van de ribben van de knoop.

Vervolgens wordt de afstand van dit punt tot de lichtbron vergeleken met de
radius van de lichtbron. Dit algoritme is weergegeven in de volgende pseudocode

```
def node_in_light(node, light):
    closest_point = vec3( clamp(node.x, light.orig.x, node.x + node.size)
                        , clamp(node.y, light.orig.y, node.y + node.size)
                        , clamp(node.z, light.orig.z, node.z + node.size)
                        )
    p = closest_point - light.orig
    return (p.x * p.x + p.y * p.y + p.z * p.z) > light.radius * light.radius
```

Het is niet nodig om deze berekening uit te voeren voor elke knoop in het 
rooster. In plaats hiervan kan een breedte eerst flood-fill algoritme gebruikt
worden. Er wordt in dit geval ofwel vanuit gegaan dat elke knoop in geen licht 
bevat waarna de nodes gevuld worden die wel overlappen. Of er wordt aangenomen
dat alle lichten overlappen, waarna alle knopen die niet overlappen worden 
leeggemaakt. 

In het geval van een puntlicht kan het volume worden gedefinieerd als dat van 
een bol:

$$ V = \frac{4}{3} \pi r^3 $$

gezien het volume van bol iets meer dan de helft van de omsluitende kubus bevat,
is voor het puntlicht gekozen om ervan uit te gaan dat alle knopen overlappen 
met het licht en vervolgens de niet overlappende knopen te markeren. Als 
beginpunten worden de hoeken van de kubus gebruikt. Dit gehele proces is 
weergegeven in figuur \ref{fig:hs-p1}

\input{./img/tex/hs-p1.tex}

In de tweede stap wordt van bovenaf de enkele lichtboom opgebouwd. Voor elke 
knoop wordt bepaald of dit een tak- of een bladknoop is. In het geval van een
takknoop, wordt tevens voor de kinderen van deze knoop bepaald, welke type
knoop zij zijn. Het type knoop wordt bepaald aan de hand van het rooster.
Er zijn initieel drie mogelijke situaties:

* De knoop overlapt niet met het rooster
* De knoop overlapt gedeeltelijk met het rooster
* De knoop valt binnen het rooster

In het eerste geval is de knoop altijd een lege bladknoop, gezien het onmogelijk
is dat er volle knopen van minimale lengte buiten het rooster liggen. 

In het tweede geval zijn er twee mogelijkheden ofwel er liggen volle 
roosterknopen binnen de enkele lichtboom knop, ofwel er liggen slechts lege 
roosterknopen in de enkele lichtboomknoop. Wanneer er slechts lege knopen binnen
de lichtboomknoop liggen, is deze knoop zelf ook leeg, anders is het een 
takknoop. 

Het punt binnen de lichtboomknoop dat het dichtstbij de lichtbronoorsprong ligt,
bevindt zich in de roosterknoop die overlapt met de lichtboomknoop en het 
dichtst bij de oorsprong van de lichtbron ligt. Indien deze roosterknoop leeg 
is, zijn alle andere roosterknopen tevens leeg. Dus om te bepalen of in het
tweede geval een enkele lichtboomknoop een takknoop of een lege bladknoop is,
dient slechtst gekeken te worden naar \'e\'en specifieke roosterknoop.

In het laatste geval zijn er drie mogelijkheden

* De enkele lichtboomknoop omvat alleen lege roosterknopen.
* De enkele lichtboomknoop omvat alleen volle roosterknopen.
* De enkele lichtboomknoop omvat zowel lege als volle roosterknopen.

De enkele lichtboomknoop is dan respectievelijk een volle bladknoop, lege 
bladknoop of takknoop. Indien de roosterknoop dichtstbij de lichtbronoorsprong
binnen de lichtboomknoop leeg is, dan is de enkele lichtboom knoop tevens leeg.
Dit volgt dezelfde redenering als in het geval van gedeeltelijke overlapping met
het rooster. Indien deze roosterknoop vol is, dan is het mogelijk dat er ofwel
slechts volle roosterknopen binnen de enkele lichtboomknoop vallen, ofwel dat
er zowel lege als volle knopen zijn. Hiervoor wordt gekeken naar de roosterknoop
binnen de lichtboomknoop die het verst weg van de lichtbron ligt. Indien deze
ook vol is, dan is de enkele lichtboomknoop tevens vol. Anders bevat de 
enkele lichtboomknoop zowel lege als volle knopen, en wordt deze gesteld op een
takknoop.

Op basis van dit algoritme is het mogelijk om een enkele lichtboom op te 
stellen. Deze zal gebruikt worden om de volledige lichtoctree te construeren in 
de volgende sectie.

