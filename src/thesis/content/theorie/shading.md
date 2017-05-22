# Shading {#sec:shading}

In de voorgaande secties is besproken hoe visibiliteit opgelost kan worden. 
Echter dit is slechts de eerste stap in het genereren van beelden. Nu 
vastgesteld is welke vorm objecten in de scene hebben, en welke delen van 
objecten daadwerkelijk zichtbaar zijn, is het tevens nodig om te bepalen hoe 
deze objecten er uit zien. Shading is het proces waarbij vergelijkingen worden
gebruikt om te bepalen welke kleur punten dienen te hebben. Hierbij wordt verder
gebouwd op de kennis van sectie \ref{sec:fysische-werkelijkheid} In deze sectie 
zal een mathematische beschrijving worden gegeven van shading.

## Mathematische modelering

\input{./img/tex/sh-rendering-equation.tex}

De belangrijkste vergelijking binnen computer graphics is de render 
vergelijking (rendering equation):

$$ \mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \mathit{L_{e}}(\mathbf{p}, \omega_{o}) + \int_{2\pi^{+}} \mathit{f_{r}}(\mathbf{p}, \omega_{i}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, \omega_{i})\cos\theta_{i}d\omega_{i}$$

Hier weergegeven in hemisfeer vorm. Deze vergelijking toont de stabiele toestand
van de stralingsenergie balans binnen een scene. Hierbij is 
$\mathit{L_{o}(\mathbf(p), \omega_{o}}$ de radiantie uitgezonden vanuit punt
$\mathbf{p}$ over $\omega_{o}$. Deze radiantie kan gedefinieerd worden aan de 
hand van de som van gereflecteerde radiantie, en de radiantie die door het punt
$\mathbf{p}$ zelf wordt uitgestraald. De uitgestraalde radiantie is 
$\mathit{L_{e}}(\mathbf{p}, \omega_{o})$. De reflectie van radiantie wordt 
beschreven door het tweede deel van de render vergelijking:

$$  \mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \int_{2\pi^{+}} \mathit{f_{r}}(\mathbf{p}, \omega_{i}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, \omega_{i})\cos\theta_{i}d\omega_{i} $$

Dit wordt de reflectie vergelijking genoemd. Hierbij wordt geintegreerd over de
gehele hemisfeer om de volledige binnenkomende radiantie te berekenen. 
Vervolgens specificeert een zogenoemde bidirectionele reflectie distributie 
functie  (bidirectional reflectance distribution function BRDF), hoe de 
radiantie over een bepaalde ruimtehoek $\omega_{i}$ bijdraagt aan de uitgaande 
radiantie in punt $\mathbf{p}$ over ruimtehoek $\omega_{o}$. 
Hiermee kan precies worden vastgelegd wat de uitgaande radiantie is in punt
$\mathbf{p}$ over ruimtehoek $\omega_{o}$. Dit is verder geillustreerd in fig.
\ref{fig:sh-rendering-equation}.

De BRDF in essentie is de wiskundige functie die beschrijft hoe een materiaal
zich gedraagd ten opzichte van licht. Deze functies hebben een aantal 
eigenschappen die gebruikt kunnen worden bij de berekening van de kleur van 
een punt.  


Helmholtz reciprociteit
  ~ De waarde van een BRDF blijft gelijk indien $\omega_{i}$ en $\omega_{o}$ 
    worden omgedraaid. 
    
$$ \mathit{f_r}(\mathbf{p}, \omega_{i}, \omega_{o}) = \mathit{f_r}(\mathbf{p}, \omega_{o}, \omega_{i}) $$  


Lineariteit
  ~ De totale gereflecteerde radiantie is gelijk aan de som van alle BRDFs 
    op dit specifieke punt. Hierdoor wordt het mogelijk om een materiaal voor te
    stellen met meerdere BRDFs in hetzelfde punt.  
    
Conservatie van energie
  ~ De totaal ingevallen radiantie is gelijk aan de som van het uitgezonden 
    licht, en het geabsorbeerde licht. Dit houdt in dat $\mathit{L_{o}}$ niet
    groter dan 1 kan zijn over alle $\omega_{o}$.
   
   
Het is nu mogelijk om een beschrijving van de kleur in elk punt te geven aan de
hand van de radiantie die berekend kan worden met de rendering vergelijking.
Hierbij zullen de materialen van objecten beschreven zijn met BRDFs.
Echter er is hier nog wel een groot probleem. De radiantie die uitgezonden
wordt vanuit $\mathbf{p}$ over $\omega_{o}$ is afhankelijk van alle 
radiantie binnenkomend over de gehele hemisfeer in punt $\mathbf{p}$. 
De binnenkomende radiantie is gelijk aan de radiantie uitgezonden vanuit
alle punten op de hemisfeer, volgens de Helmholtz reciprociteit. Als gevolg
heeft dit dat om de radiantie te berekenen, het nodig is om alle radiantie 
in de scene al van te voren te weten. Dit is niet mogelijk, en dus zullen
alle shading algoritmes pogen een benadering te geven van de daadwerkelijke
oplossing van de rendering vergelijking. De kwaliteit van de benadering hangt
af van meerdere aspecten, een grote beperkende factor binnen real-time graphics
is de beschikbare rekentijd.

## Lambertiaanse Bidirectionele Reflectie Distributie Functie

\input{./img/tex/sh-lambert.tex}

Materialen kunnen gedefinieerd worden als set van BRDFs, die het gedrag van het
licht beschrijven indien het in contact komt met een object. De simpelste BRDF 
is de lambertiaanse BRDF. Deze BRDF beschrijft een puur diffuus oppervlakte, 
wat inhoudt dat de richting waarin een binnenkomende straal licht wordt
gereflecteerd puur willekeurig is. Dit is weergegeven in fig. \ref{fig:sh-lambert}.
Deze BRDF heeft als uitkomst een constante waarde. Deze constante waarde wordt 
veelal gedefinieerd als de de *diffuse kleur* $\mathit{c}_{\mathtt{dif}}$ van 
dit object. Dit leidt tot de volgende functie:

$$ \mathit{f}(\omega_{i}, \omega_{o}) = \frac{\mathit{c}_{\mathtt{dif}}}{\pi} $$

Hierbij is de deling door $\pi$ een gevolg van de integratie van de cosinus
factor over de hemisfeer. 

De lambertiaanse BRDF is als standaard materiaal gebruikt binnen deze thesis. 
Indien niet anders vermeld zullen afbeeldingen en testen gegeneerd zijn met 
deze functie.

