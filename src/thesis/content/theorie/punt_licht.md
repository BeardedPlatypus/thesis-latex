## Definitie van lichtbron

\input{./img/tex/pl-distance-attenuation.tex}

Zoals eerder benoemd, draait de kern van deze thesis om het optimaliseren van
het aantal lichtberekeningen in realtime toepassingen. Om deze reden is het 
belangrijk om het concept lichtbron zoals gebruikt in deze thesis te defini\"eren. 
Wanneer er gesproken wordt van een lichtbron zal binnen deze thesis
altijd worden gedoeld op een eindige omnipuntlichtbron die zich bevindt op punt $\mathbf{p}$ binnen
de \mbox{sc\`ene}.  

In de fysische wereld zijn lichtbronnen nooit eindig, echter de invloed die ze hebben
op de omringende wereld zal bij grotere afstand 0 benaderen. 
Dit is enerzijds het gevolg van absorptie door het medium waardoor de lichtbron zich 
beweegt. Binnen de fysica wordt deze relatie vastgelegd met de wet van 
Lambert-Beer\cite{bouguer1729essai} gedefinieerd voor 
uniforme demping als:

$$ T = e^{-\mu\mathit{d}} $$

\noindent waar $\mathit{d}$ de padlengte van de lichtstraal door het medium is en $\mu$ 
de dempingsco\"effici\"ent. Hierbij wordt de demping van het licht gerelateerd aan 
het medium waardoor het zich beweegt. Wanneer de demping als functie van de afstand $d$
wordt geplot, worden zogenoemde dempingscurves verkregen.
Anderzijds is het een direct gevolg van de geometrie. Voor een puntlichtbron zal de intensiteit
van een lichtbron kwadratisch afnemen met de afstand $d$ tot de oorsprong van de lichtbron.
De oppervlakte van een bol is gedefinieerd als 

$$ A = 4\pi r^2 $$

\noindent Dit betekent dat bij een toename van afstand $r$ tot de oorsprong, de 
oppervlakte kwadratisch zal toenemen. De energie die wordt uitgezonden door het
puntlichtbron zal bij een toename van een afstand $r$ op een kwadratisch groter oppervlak
worden afgebeeld. Dit betekent dat de waargenomen energie kwadratisch afneemt.
De demping ten gevolge van de afstand kan worden voorgesteld met een zogenoemde afstanddempingsfunctie $f$:

$$ \mathit{f}(\mathit{d}) = \frac{1}{1 + d^2} $$

Binnen de computergrafieken wordt veelal het medium waarin de \mbox{sc\`ene} zich 
bevindt niet expliciet voorgesteld, in plaats hiervan wordt aangenomen dat de wereld zich in vacu\"um bevindt. 
Uit performantie overwegingen worden binnen veel realtime renderingtoepassingen 
lichtbronnen verder voorgesteld door een eindige benadering. De invloed wordt beperkt tot een 
eindige ruimte. Buiten dit lichtvolume zal een lichtbron geen invloed hebben. 
Voor puntlichtbronnen komt dit neer op een bolvolume met een radius $r$.
Dit leidt tot een voorstelling als weergegeven in figuur \ref{fig:pl-licht}.


\input{./img/tex/pl-licht.tex}


Om de illusie te wekken dat de lichten fysiek accuraat zijn, dient tevens
een benadering gemaakt te worden van de afstanddempingsfuncties. 
Deze functies dienen te voldoen aan de eerder gestelde voorwaarde, waarbij 
de invloed \mbox{\'e\'en} is in de oorsprong, en nul op afstand $r$.
De fysieke afstanddempingsfunctie en enkele veel gebruikte benaderingen
zijn gegeven in figuur \ref{fig:pl-distance-attenuation} 
Binnen de thesis zelf is gekozen voor de benadering:

$$ \left(\left.\frac{\mathit{l}}{\mathit{r}}\right|_{[0,1]}\right)^2 $$

Als laatste dient de intensiteit van de lichtbron vastgelegd te worden. Zoals 
gebruikelijk binnen de computergrafieken, is hier gekozen voor een RGB voorstelling. 
Waarbij de waardes zich bevinden in het bereik van 0 tot en met 1.

Dit alles leidt ertoe dat een lichtbron gedefinieerd kan worden als de verzameling van de 
volgende eigenschappen:

* De positie $\mathbf{p}$ van het lichtbron ten opzichte van een co\"ordinatenstelsel met oorsprong $\mathcal{O}$.
* Een afstand $\mathit{r}$ die de invloed van de lichtbron bepaalt.
* Een afstanddempingsfunctie $f$ die het verval van invloed moduleert
* Een intensiteit $\mathbf{i}$ die de kleur en intensiteit van de lichtbron bepaalt.

