# Fysische werkelijkheid {#sec:fysische-werkelijkheid}

De fysische wereld waarin de mens zich bevindt wordt gedicteerd door alle 
fysische wetten. De mens neemt deze wereld waar door middel van zintuigen. Voor 
de computergrafieken, waarneming is het belangrijkste zintuig. Door middel van 
waarneming wordt de drie dimensionale wereld om de mens heen ge\"interpeteerd. 
Deze interpretatie zal de fysische werkelijkheid genoemd worden binnen deze 
thesis. Zowel de fysische wereld als de manier waarop deze waargenomen wordt,
bepaalt dus de fysische werkelijkheid.  

## Waarneming

\input{./img/tex/fw-waarneming.tex}

De mens neemt de wereld waar door het oog. Het menselijk oog interpreteert de
drie dimensionale wereld door stralen van licht te focussen op een enkel punt, 
met behulp van een lens. Het enkele punt dat licht omzet naar neurosignalen 
wordt de retina genoemd\cite{wolfe2015sensation}. Een camera bootst het oog na, 
en projecteert licht op een elektronische fotosensor, die het signaal omzet naar een 
digitaal signaal. Dit is weergegeven in figuur \ref{fig:fw-waarneming}.  

Deze manier van projectie heeft twee belangrijke gevolgen:  

* Objecten worden als kleiner waargenomen naarmate ze verder van de waarnemer af
  staan.  
* Objecten worden waargenomen met \textit{foreshortening}, i.e. de dimensies van een 
  object parallel aan het gezichtsveld, worden als kleiner waargenomen dan 
  dimensies van hetzelfde object loodrecht aan het gezichtsveld.  
  
\noindent De mens verwacht dat deze eigenschappen aanwezig zijn, om beelden te 
interpreteren. 

## Licht

Het tweede belangrijke inzicht met betrekking tot waarneming is dat de wereld wordt 
waargenomen door middel van licht. Dit betekent dat bij afwezigheid van licht, het niet
mogelijk is om iets waar te nemen. Verder betekent dat ook dat het gedrag van
licht een grote invloed heeft op de manier hoe de wereld wordt waargenomen.  


Licht is een vorm van elektromagnetische straling. Dit betekent dat de fysische wetten
met betrekking tot elektromagnetische straling ook van invloed zijn op licht.
Voor de computergrafieken is met name de optica van belang. Hierin wordt licht,
en de interactie tussen licht en materie bestudeerd. Deze wetten vormen veelal de 
basis om licht te simuleren. Licht zal
onder normale omstandigheden, zich altijd in een rechte lijn zolang het binnen
hetzelfde medium blijft. Wanneer het licht in contact komt met een nieuw medium
zijn er verschillende fenomenen die kunnen plaatsvinden:

Absorptie

  ~  Het licht wordt geabsorbeerd door de atomen van het nieuwe medium, en 
     uitgestoten als warmte. Hierbij gaat het licht verloren.
  
Reflectie

  ~  Het licht wordt gereflecteerd op het oppervlakte van het nieuwe medium.
     Hierbij wordt het licht terug de \mbox{sc\`ene} ingestuurd. 
     De hoek van reflectie hangt af van het type medium. Indien het materiaal
     zich gedraagt als een spiegel zal het licht teruggekaatst worden 
     met dezelfde hoek gespiegeld aan de oppervlakte normaal.
     Indien het materiaal licht diffuus weerspiegelt betekent dat de hoek 
     van inval niet uitmaakt voor de reflectie en deze min of meer 
     willekeurig is. 
     
 Transmissie

  ~  Het licht plant zich verder voort door het nieuwe medium, opnieuw in een
     rechte lijn, met mogelijk een aangepaste richting op basis van de 
     brekingsindex van het nieuwe en het oude medium.
    

\input{./img/tex/fw-licht.tex}

Deze fenomenen zijn verder ge\"illustreerd in figuur \ref{fig:fw-licht}. Ze zijn 
niet exclusief aan elkaar. Een medium kan dus bijvoorbeeld een gedeelte van het
licht absorberen en een ander gedeelte reflecteren.  

Zoals eerder vermeld is, neemt het oog de wereld waar door licht op te vangen.
Het merendeel van het licht dat opgevangen wordt is gereflecteerd via een of 
meerdere oppervlaktes. Een belangrijke constatering is dat objecten slechts 
zichtbaar zijn als er binnen het medium geen (onderzichtige) andere media liggen 
tussen het object en de lens. Dit is een triviale constatering in de fysische
werkelijkheid. Echter dit zal niet triviale consequenties hebben binnen de 
computergrafieken zoals later zal worden beschreven.

Om de interactie van licht te simuleren is het van belang dat licht meetbaar is.
Er zijn hiervoor twee sets van eenheden, Radiometrie en Fotometrie\cite{suffern2007ray}. Binnen 
Radiometrie wordt de lichtkracht over alle golflengte gemeten. Bij 
Fotometrie wordt deze kracht gewogen, aan de hand van het gestandaardiseerde
model voor de perceptie van helderheid. Fotometrie is van belang binnen de Computer Grafieken 
omdat het inzicht geeft in de perceptie van de mens. Binnen 
deze thesis zal slechts kort ingegaan worden op Radiometrie.  

\input{./tbl/fw-eenheden.tex}

De belangrijkste termen van Radiometrie zijn opgesteld in tabel \ref{tbl:fw-eenheden}. 
De stralingsenergie Q is de basis eenheid van elektromagnetische straling. 
Deze energie bevindt zich in de fotonen. Flux $\Phi$ beschrijft de 
stralingsenergie dat zich verplaatst door een ruimte per seconde.
Binnen de computergrafieken is de belangrijkste eenheid 
radiantie L. Hiermee wordt de stralingsflux van fotonen die zich bewegen 
door een kegel. Wanneer de grootte van de basis van de kegel nul benaderd, 
bewegen de fotonen zich in een rechte lijn voort.
Radiantie heeft de volgende  eigenschappen die van belang zijn bij 
de simulatie van licht:

* Radiantie is constant binnen een straal die zich voortplant door vacu\"um. 
  Tevens is het gelijk in beide richtingen waarin een straal zich kan voortplanten
* Indien het punt van meting op een oppervlakte wordt genomen, maakt het niet 
  uit of de flux binnenkomt, of uitgaand is. Het maakt zelfs niet uit of de 
  flux geabsorbeerd, gereflecteerd, of doorgelaten wordt door het materiaal.

## Kleur

\input{./img/tex/fw-kleur.tex}

Een tweede belangrijk aspect van licht voor computergrafieken is het concept 
kleur. Het concept kleur is niet een fysisch verschijnsel, maar een gevolg
van hoe ogen licht interpeteren. De mens neemt slechts een gedeelte van al het 
licht waar. Dit wordt het zichtbare licht genoemd. Het menselijk oog 
interpreteert het licht door het zowel een intensiteit als een kleur toe te 
kennen. De kleur die waargenomen wordt van een lichtstraal is afhankelijk van 
het licht. Een gemiddeld persoon is in staat om 3 verschillende primaire kleuren 
waar te nemen, rood, blauw en groen. Elke zichtbare kleur kan voorgesteld worden
als een mix van deze primaire kleuren. De manier om deze kleuren te mengen
is afgebeeld in figuur \ref{fig:fw-kleur} Belangrijk om hierbij te vermelden is 
dat licht zich gedraagt als additieve kleurmenging. Dit houdt in dat indien 
verschillende kleuren licht op het zelfde punt worden afgebeeld, dit punt zal 
worden waargenomen als de kleur gelijk aan de optelling van deze lichten.  

Objecten kunnen tevens een kleur hebben. Reeds is besproken dat objecten worden
waargenomen door de reflectie van hun licht. De kleur van een object is dan ook
het gevolg van de gedeeltelijk absorptie van licht. In het geval dat een 
gekleurd object wordt verlicht met puur wit licht, zal slechts het licht dat 
overeenkomt in frequentie met de kleur van het object weerspiegelt worden. 
De frequenties tegenovergesteld aan de kleur van het object, zullen worden 
geabsorbeerd door het object.  

## Animatie

Beweging kan gesimuleerd worden door statische beelden snel genoeg na elkaar af 
te beelden. Deze illusie wordt *schijnbare beweging* genoemd. In de Computer Grafieken
wordt hier dankbaar gebruik van gemaakt om bewegende beelden te cre\"eren. 

Om de illusie van beweging te cre\"eren, dienen de beelden met een hoge framerate
weergegeven te worden. Veelal worden hier framerates tussen de 20 en 60 frames
per seconde voor gebruikt. Een hogere framerate leidt tot een vloeiendere 
beweging.

## Simulatie

Binnen de computergrafieken is het doel veelal om de waarneming van de fysische werkelijkheid te benaderen.
Echter hiervoor is het niet nodig om de volledige fysische werkelijkheid te 
benaderen. Het simuleren van de fysische werkelijkheid om een afbeelding te 
verkrijgen, het renderen, kan dus in grofweg in twee problemen worden ingedeeld:  

* Wat is zichtbaar binnen een \mbox{sc\`ene} vanuit het huidige gezichtspunt.  
* Hoe ziet datgene wat zichtbaar is er uit binnen de afbeelding.  

Wat afgebeeld wordt op een afbeelding, hangt af van twee aspecten, hoe wordt de 
drie dimensionale \mbox{sc\`ene} op het twee dimensionale beeld geprojecteerd. En wat van elk object dat geprojecteerd 
kan worden is daadwerkelijk zichtbaar op de uiteindelijk afbeelding. Het eerste
wordt perspectief projectie genoemd. Het tweede probleem wordt het 
visibiliteitsprobleem genoemd.  

Hoe hetgene wat afgebeeld wordt, er uiteindelijk uit ziet binnen onze 
afbeelding, wordt in de tweede stap bepaald. Deze stap wordt shading genoemd, 
en alle berekeningen gerelateerd aan kleur, absorptie, weerspiegeling etc., 
vallen hier onder.  

