# Perspectief projectie en het visibileitsprobleem

In de sectie ... zijn de twee problemen vastgesteld die opgelost dienen te 
worden om geloofwaardige afbeeldingen te generen. In deze sectie zal de eerste 
geadresseerd worden, wat is zichtbaar binnen een scene vanuit het huidige 
gezichtspunt. Om te bepalen wat zichtbaar is dient zowel het perspectief 
gesimuleerd te worden, als bepaald te worden welk van de objecten in 
perspectief als eerste zichtbaar is.  

## Perspectief projectie

\input{./img/tex/vp-perspectief.tex}

Zoals eerder besproken zijn de twee eigenschappen van perspectief:

* Objecten worden als kleiner waargenomen naarmate ze verder van de waarnemer af
  staan.  
* Objecten worden waargenomen met Foreshortening, i.e. de dimensies van een 
  object parallel aan het gezichtsveld, worden als kleiner waargenomen dan 
  dimensies van hetzelfde object loodrecht aan het gezichtsveld.  

Deze effecten kunnen gesimuleerd worden door de 3d scene te projecteren naar het
oogpunt en af te beelden op het canvas. Zoals weergegeven in figuur 
\ref{fig:vp-perspectief}.  

Zoals eerder beschreven bestaan de objecten binnen de scenes uit meshes van 
primitieven. Omdat elk van deze driehoeken gedefinieeerd kan worden door zijn 
drie vertices, is het niet nodig om elke mogelijk punt binnen de driehoek af te 
beelden op de canvas, maar is het genoeg om slechts deze drie vertices te
projecteren.  

\input{./img/tex/vp-projectie-punt.tex}

In figuur \ref{fig:vp-projectie-punt} is de projectie $\mathbf{p'}$ van een 
enkel punt $\mathbf{p}$ op een enkele dimensie van de canvas weergegeven. 
De hoek $\angle \mathbf{a}\mathbf{b}\mathbf{c}$
Hier is te zien dat de hoek tussen C en AB'C' gelijk is. Dit betekent 
dat we het punt C' kunnen bereken doordat de verhouding geldt  

$$ \frac{BC}{AB} = \frac{B'C'}{AB'} $$

Verder is de afstand van het oogpunt tot de canvas, AB', bekend. Wat ertoe 
leidt dat we het geprojecteerde punt gemakkelijk kunnen berekenen. 


$$ \mathit{p'_{x}} = d \frac{\mathit{p_x}}{\mathit{p_z}} $$
$$ \mathit{p'_{y}} = d \frac{\mathit{p_y}}{\mathit{p_z}} $$
$$ \mathit{p'_{z}} = d $$
$$ \mathit{p'_{w}} = 1 $$

waar d de afstand van het oogpunt tot de canvas is. 
Binnen computer graphics wordt deze stap de perspectief deling genoemd. 
We kunnen deze berekeningen samenvoegen tot een enkele matrix $\mathbf{P}$ 
die een punt in een specifiek coordinaten stelsel omzet naar een punt 
geprojecteerd op de canvas. Wat leidt tot de perspectief projectie van punten.  

$$ \mathbf{P} \mathbf{p} = \mathbf{p'} $$

Of deze projectie daadwerkelijk nodig is, is afhankelijk van de gekozen 
rendering techniek. Binnen rasterisatie is het nodig om deze stap expliciet
uit te voeren. Raytracing neemt de perspectief projectie impliciet mee.  

## Visibiliteitsprobleem

\input{./img/tex/vp-visibiliteit.tex}

Er is nu vastgesteld hoe objecten in perspectief afgebeeld op de canvas kunnen 
worden. Echter, hiermee is nog niet volledig vastgesteld wat daadwerkelijk 
zichtbaar gaat zijn op het canvas, zoals weergegeven in figuur 
\ref{fig:vp-visibiliteit}. Hiervoor is het tevens nodig om te bepalen
welke delen van objecten zichtbaar zijn, en welke verborgen zijn achter andere 
objecten. Dit probleem wordt onder andere het visibiliteitsprobleem genoemd, 
en was een van de eerstegrote problemen binnen computer graphics.  

De oplossing voor dit probleem is de realisatie dat het visibiliteitsprobleem
intrinsiek een sorteerprobleem is. Stel er bestaat een minimale oppervlakte 
$\mathit{O}$ op het canvas, waarvoor gekeken wordt welk deel zichtbaar is. 
Door middel van perspectief projectie is het mogelijk om te bepalen welke 
objecten op $\mathit{O}$ worden afgebeeld. Er van uitgaande dat er een object 
$\mathit{A}$ bestaat die afgebeeld wordt op $\mathit{O}$. Dan is dit object
daadwerkelijk zichtbaar in $\mathit{O}$ als er geen andere objecten op
$\mathit{O}$ worden geprojecteerd die dichterbij het oogpunt liggen dan
object $\mathit{A}$. Wanneer alle objecten gesorteerd zijn is het per
punt of het canvas mogelijk om het dichtstbijzijnde object te selecteren,
en deze weer te geven op het scherm.  

De algoritmes om dit efficient te doen worden verborgen oppervlakte 
bepalings (hidden surface determination) algoritmes genoemd. Deze kunnen 
grofweg ingedeeld worden in twee categorien, raytracing en rasterisatie. 
Hierbij zou, in theorie, geen verschil in resultaat hoeven zijn. Beide klasses 
van algoritmes hetzelfde doel hebben, het produceren van realistische beelden 
op basis van een 3d scene.  

Raytracing werkt op basis van het trekken van zogenoemde stralen door 
$\mathbf{p'}$ waarbij de eerste $\mathbf{p}$ wordt bepaald.
Rasterisation daarentegen, bepaald alle mogelijke $\mathbf{p'}$ op basis van 
alle mogelijke $\mathbf{p}$ die geprojecteerd worden op $\mathbf{p}$.
Vervolgens wordt bepaald welke $\mathbf{p'}$ daadwerkelijk zichtbaar is.  

In de volgende secties zal er kort ingegaan worden op beide technieken.

