# Perspectiefprojectie en het visibileitsprobleem

In sectie \ref{sec:fysische-werkelijkheid} zijn de twee problemen vastgesteld die opgelost dienen te 
worden om geloofwaardige afbeeldingen te generen. In deze sectie zal het eerste probleem
geadresseerd worden: wat is zichtbaar binnen een \mbox{sc\`ene} vanuit het huidige 
zichtspunt. Om te bepalen wat zichtbaar is dient zowel het perspectief 
gesimuleerd te worden, als bepaald te worden welk van de objecten in dit
perspectief als zichtbaar is.  

## Perspectiefprojectie

\input{./img/tex/vp-perspectief.tex}

Zoals eerder besproken zijn de twee eigenschappen van perspectief:

* Objecten worden als kleiner waargenomen naarmate ze verder van de waarnemer af
  staan.  
* Objecten worden waargenomen met *Foreshortening*, i.e.
  de dimensies van objecten parallel aan de vizierlijn worden als kleiner waargenomen
  dan de dimensies loodrecht op de vizier.

\noindent Deze effecten kunnen gesimuleerd worden door de drie dimensionale \mbox{sc\`ene} te projecteren naar het
oogpunt en af te beelden op het canvas\cite{suffern2007ray}. Zoals weergegeven in figuur 
\ref{fig:vp-perspectief}.  

Zoals eerder beschreven bestaan de objecten binnen de \mbox{sc\`enes} uit meshes van 
primitieven. Omdat elk van deze driehoeken gedefinieerd kan worden door zijn 
drie vertices, is het niet nodig om elke mogelijk punt binnen de driehoek af te 
beelden op de canvas, maar is het genoeg om slechts deze drie vertices te
projecteren.  

\input{./img/tex/vp-projectie-punt.tex}

In figuur \ref{fig:vp-projectie-punt} is de projectie $\mathbf{p'}$ van een 
enkel punt $\mathbf{p}$ op een enkele dimensie van de canvas weergegeven. 
De hoek $\theta$ is zowel de hoek van $\mathcal{O}\mathbf{p}\mathbf{b}$
als $\mathcal{O}\mathbf{p^\prime}\mathbf{b^\prime}$. Dit betekent 
dat het punt $\mathbf{p^\prime}$ berekend kan worden met behulp van
de verhouding:

$$ \frac{\lVert\mathbf{p} - \mathbf{b}\rVert}{\lVert\mathbf{b}\rVert} = \frac{\lVert\mathbf{p^\prime} - \mathbf{b^\prime}\rVert}{\lVert\mathbf{b^\prime}\rVert} $$

\noindent De afstand van het oogpunt tot de canvas $d$ is gelijk aan de afstand van $\mathbf{b^\prime}$
tot de oorsprong:

$$ d = \lVert \mathbf{b^\prime}\rVert $$

\noindent Hiermee kan vervolgens de positie van het geprojecteerde punt gemakkelijk berekend worden:

$$ \mathit{p'_{x}} = d \frac{\mathit{p_x}}{\mathit{p_z}} $$
$$ \mathit{p'_{y}} = d \frac{\mathit{p_y}}{\mathit{p_z}} $$
$$ \mathit{p'_{z}} = d $$
$$ \mathit{p'_{w}} = 1 $$

\noindent Binnen de computergrafieken wordt deze stap de perspectiefdeling genoemd. 
We kunnen deze berekeningen samenvoegen tot een enkele matrix $\mathbf{P}$ 
die een punt in een specifiek co\"ordinatenstelsel omzet naar een punt 
geprojecteerd op de canvas. Hiermee wordt de perspectiefprojectie van punten mogelijk:  

$$ \mathbf{P} \mathbf{p} = \mathbf{p'} $$

\noindent Of deze projectie expliciet nodig is, is afhankelijk van de gekozen 
renderingtechniek. Binnen rasterisatie is het nodig om deze stap expliciet
uit te voeren. Raytracing neemt de perspectiefprojectie impliciet mee.  

## Visibiliteitsprobleem

\input{./img/tex/vp-visibiliteit.tex}

Er is nu vastgesteld hoe objecten in perspectief afgebeeld kunnen worden op de canvas. 
Echter, hiermee is nog niet volledig vastgesteld wat daadwerkelijk 
zichtbaar gaat zijn op het canvas. Hiervoor is het tevens nodig om te bepalen
welke delen van objecten zichtbaar zijn, en welke verborgen zijn achter andere 
objecten. Dit probleem is weergegeven in figuur \ref{fig:vp-visibiliteit}.
Door alleen de objecten af te beelden kan niet worden bepaald welk van de twee
afbeeldingen van de kubus en de bol correct is. Dit probleem wordt onder andere 
het visibiliteitsprobleem genoemd, en was een van de eerste grote problemen binnen
de computergrafieken\cite{Sutherland:1974:CTH:356625.356626}.  

De oplossing van het visibiliteitsprobleem kan gevonden worden met behulp van de realisatie
dat de bepaling van de zichtbare ruimte op een canvas, neerkomt op een sorteerprobleem.
Stel voor een punt $\mathbf{p}$ dient bepaald te worden welk primitief zichtbaar is.
Met behulp van de perspectiefprojectie kan de set $S$ van van objecten die afgebeeld
worden op het punt $\mathbf{p}$ bepaald worden. Het object dat vervolgens zichtbaar is, 
zal het object zijn dat het dichtst bij het punt $\mathbf{p}$ en dus het zichtpunt van
de camera ligt. Indien de objecten in $S$ gesorteerd worden op basis van hun 
afstand tot de camera zal het eerste object het dichtst bij de camera liggen en dus
zichtbaar zijn. Gezien de afstand tot de camera overeenkomt met de $\mathbf{z}$-afstand
in cameraco\"ordinaten, dient dus het object met de kleinste $\mathbf{z}$-waarde gevonden 
worden. De algoritmes die dit probleem oplossen worden verborgen-oppervlaktebepalingsalgoritmes
genoemd (hidden surface detection algorithms).

De algoritmes die zowel de perspectiefprojectie en de visibiliteit oplossen kunnen grofweg 
worden ingedeeld in twee categorie\"en, raytracing-algoritmes en rasterisation-algoritmes.
Het resultaat van deze algoritmes zou in theorie hetzelfde moeten zijn, gezien beide
hetzelfde doel hebben.

Raytracing werkt op basis van het trekken van zogenoemde stralen uit het zichtpunt door
de pixels in de canvas. Vervolgens wordt gekeken of deze stralen snijden met primitieven.
Rasterisation beeldt de vertices van primitieven af op de canvas met behulp van de 
perspectiefprojectie. Vervolgens wordt bepaald welke pixels overlappen met het primitief.
In de volgende secties zal ingegaan worden op beide algoritmes.

