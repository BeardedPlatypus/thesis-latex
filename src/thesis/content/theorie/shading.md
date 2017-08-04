# Shading {#sec:shading}

In de voorgaande secties is besproken hoe visibiliteit opgelost kan worden. 
Echter dit is slechts de eerste stap in het genereren van beelden. Nu 
vastgesteld is hoe objecten in de \mbox{sc\`ene} weergegeven worden op het zichtvenster kan 
bepaald worden hoe deze objecten er daadwerkelijk uitzien.
Shading is het proces waarbij vergelijkingen worden
gebruikt om te bepalen welke kleur punten dienen te hebben. Hierbij wordt verder
gebouwd op de kennis van sectie \ref{sec:fysische-werkelijkheid} In deze sectie 
zal een mathematische beschrijving worden gegeven van shading.

## Mathematische modelering

De belangrijkste vergelijking binnen de computergrafieken is de rendervergelijking (rendering equation)\cite{Kajiya:1986:RE:15922.15902}:

$$ \mathit{L}(\mathbf{p}, \omega_{o}) = \mathit{L_{e}}(\mathbf{p}, \omega_{o}) + \int_{2\pi^{+}} \mathit{f_{r}}(\mathbf{p}, \omega_{i}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, \omega_{i})\cos\theta_{i}d\omega_{i} $$

\noindent Hier weergegeven in hemisfeervorm. Deze vergelijking toont de stabiele toestand
van de stralingsenergiebalans binnen een \mbox{sc\`ene}. Hierbij is 
$\mathit{L}(\mathbf{p}, \omega_{o})$ de radiantie uitgezonden vanuit punt
$\mathbf{p}$ over $\omega_{o}$. Deze radiantie kan gedefinieerd worden aan de 
hand van de som van gereflecteerde radiantie, en de radiantie die door het punt
$\mathbf{p}$ zelf wordt uitgestraald. De uitgestraalde radiantie is gedefinieerd als
$\mathit{L_{e}}(\mathbf{p}, \omega_{o})$. De reflectie van radiantie wordt 
beschreven door het tweede deel van de rendervergelijking:

$$  \mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \int_{2\pi^{+}} \mathit{f_{r}}(\mathbf{p}, \omega_{i}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, \omega_{i})\cos\theta_{i}d\omega_{i} $$

Dit wordt de reflectievergelijking genoemd\cite{akenine2016real}. Hierbij wordt ge\"integreerd over de
gehele hemisfeer om de volledige binnenkomende radiantie te berekenen. 
Vervolgens specificeert een zogenoemde bidirectionele reflectie distributie functie 
(bidirectional reflectance distribution function, BRDF)\cite{Nicodemus:65, suffern2007ray}, hoe de 
radiantie over een bepaalde ruimtehoek $\omega_{i}$ bijdraagt aan de uitgaande 
radiantie in punt $\mathbf{p}$ over ruimtehoek $\omega_{o}$. 
Hiermee kan precies worden vastgelegd wat de uitgaande radiantie is in punt
$\mathbf{p}$ over ruimtehoek $\omega_{o}$. 

De BRDF in essentie is de wiskundige functie die beschrijft hoe een materiaal
zich gedraagt ten opzichte van licht. Deze functies hebben een aantal 
eigenschappen die gebruikt kunnen worden bij de berekening van de kleur van 
een punt.  


Helmholtz reciprociteit
  ~ De waarde van een BRDF blijft gelijk indien $\omega_{i}$ en $\omega_{o}$ 
    worden omgedraaid\cite{suffern2007ray}. 
    
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
hand van de radiantie die berekend kan worden met de rendervergelijking.
Hierbij zijn de materialen van objecten beschreven met BRDFs.
Er is nog wel een groot probleem met deze voorstelling. De radiantie die uitgezonden
wordt vanuit $\mathbf{p}$ over $\omega_{o}$ is afhankelijk van alle 
radiantie binnenkomend over de gehele hemisfeer in punt $\mathbf{p}$. 
De binnenkomende radiantie is gelijk aan de radiantie uitgezonden vanuit
alle punten op de hemisfeer, volgens de Helmholtz reciprociteit. Dit heeft als gevolg
dat om de radiantie te berekenen, het nodig is om alle radiantie 
in de \mbox{sc\`ene} al van te voren te weten. Dit is niet mogelijk, en dus zullen
alle shading algoritmes pogen een benadering te geven van de daadwerkelijke
oplossing van de rendervergelijking. De kwaliteit van de benadering hangt
af van meerdere aspecten. Een grote beperkende factor binnen real-time computergrafieken
is de beschikbare rekentijd.

## Directe lichtbenadering

De meest simpele benadering van de reflectievergelijking is de directe-belichtingbenadering. 
Hierbij wordt voor elk punt slechts de lichtbijdrage van lichten die direct op een punt
schijnen berekend. Indirecte belichting, waarbij lichtstralen eerst andere oppervlaktes raken 
voordat deze door het punt in de camera worden gereflecteerd, worden buiten beschouwing gelaten.
Dit leidt tot een grote versimpeling van de reflectievergelijking. Deze kan 
nu opgesteld worden als een sommatie over de lichten in plaats van een integraal 
over de hemisfeer\cite{akenine2016real}:

$$ 
\mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \sum_{\mathit{k}=1}^{\mathit{n}} \mathit{f_{r}}(\mathbf{p}, l_{\mathit{k}}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, l_{\mathit{k}})\cos\theta_{i} 
$$

\noindent hierbij is licht $k$ gedefinieerd als $l_\mathit{k}$.

\noindent De directe-belichtingbenadering reduceert het aantal bewerken significant.
Om deze reden zal deze benadering verder gebruikt worden binnen deze thesis.

## Lambertiaanse Bidirectionele Reflectie Distributie Functie

\input{./img/tex/sh-lambert.tex}

Materialen kunnen gedefinieerd worden als set van BRDFs, die het gedrag van het
licht beschrijven indien het in contact komt met een object. De simpelste BRDF 
is de lambertiaanse BRDF\cite{suffern2007ray}. Deze BRDF beschrijft een puur diffuus oppervlakte, 
wat inhoudt dat de richting waarin een binnenkomende lichtstraal wordt
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

## Schaduw

Schaduw is een belangrijke visuele cue voor de plaatsing van objecten in de 
\mbox{sc\`ene}. De hersenen gebruiken schaduw om de onderlinge relatie van objecten
te bepalen. In de fysische werkelijkheid is een schaduw op een oppervlak het gevolg van
obstructie tussen deze oppervlakte en de lichtbron. Om schaduw te simuleren binnen
computergrafieken dient dus bepaald te worden of voor punten er objecten tussen het punt
en een lichtbron liggen. Dit betekent dat er extra werk uitgevoerd dient te worden om 
deze bepaling uit te voeren.

Zoals behandeld zal worden in de volgende sectie, zal de belichting binnen de moderne 
grafische pijplijn plaatsvinden per pixel. Bij deze berekening is er niet impliciet
een beschrijving van de \mbox{sc\`ene} beschikbaar. Deze dient expliciet in het geheugen
te worden bijgehouden. Dit leidt tot een toename in de complexiteit.
Om deze reden zijn schaduwen buiten beschouwing gelaten.

