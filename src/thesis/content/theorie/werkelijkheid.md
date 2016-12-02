# Fysische werkelijkheid

De fysische wereld waarin de mens zich bevindt wordt gedicteerd door alle 
fysische wetten. De mens neemt deze wereld door middel van zintuigen. Voor 
computer graphics, waarneming is het belangrijkste zintuig. Door middel van 
waarneming wordt de drie dimensionale wereld om de mens heen geinterpeteerd. 
Deze interpretatie zal de fysische werkelijkheid genoemd worden binnen deze 
thesis. Zowel de fysische wereld als de manier waarop deze waargenomen wordt
bepaald dus de fysische werkelijkheid.  

## Waarneming

\input{./img/tex/fw-waarneming.tex}

De mens neemt de wereld waar door het oog. Het menselijk oog interpreteert de
drie dimensionale wereld door stralen van licht te focussen op een enkel punt, 
doormiddel van een lens. Het enkele punt dat licht omzet naar neurosignalen 
wordt de retina genoemd. Een camera bootst het oog na, en projecteert 
licht op een electronische photosensor, die het signaal op zet naar een 
digitaal signaal. Dit is weergegeven in figuur \ref{fig:fw-waarneming}.  

Deze manier van projectie heeft twee belangrijke gevolgen:  

* Objecten worden als kleiner waargenomen naarmate ze verder van de waarnemer af
  staan.  
* Objecten worden waargenomen met Foreshortening, i.e. de dimensies van een 
  object parallel aan het gezichtsveld, worden als kleiner waargenomen dan 
  dimensies van hetzelfde object loodrecht aan het gezichtsveld.  
  
De mens verwacht dat deze eigenschappen aanwezig zijn, om beelden te 
interpeteren. 

## Licht

Het tweede belangrijke inzicht bij waarneming is dat de wereld wordt waargenomen
door middel van licht. Dit betekent dat bij afwezigheid van licht, het niet
mogelijk is om iets waar te nemen. Verder betekent dat ook dat het gedrag van
licht een grote invloed heeft op de manier hoe de wereld wordt waargenomen.  

\input{./tbl/fw-eenheden.tex}

Licht is electromagnetische straling. Voor Computer Graphics is met name de
optica van belang. Hierin wordt licht, en de interactie tussen licht en materie
bestudeerd. Deze wetten vormen veelal de basis om licht te simuleren. Licht zal
onder normale omstandingheden, zich altijd in een rechte lijn zolang het binnen
hetzelfde medium blijft. Indien het licht in contact komt met een nieuw medium
zijn er verschillende fenomen die kunnen gebeuren:

Absorptie

  ~  Het licht wordt geabsorbeerd door de atomen van het nieuwe medium, en 
     uitgestoten als warmte. Hierbij gaat het licht verloren.
  
Reflectie

  ~  Het licht wordt gereflecteerd op het oppervlakte van het nieuwe medium.
     Hierbij wordt het licht terug de scene ingestuurd. 
     De hoek van reflectie hangt af van het type medium. Indien het materiaal
     zich gedraagd als een spiegel, en zal het licht teruggekaatst worden 
     met dezelfde hoek gespiegeld om de normaal. 
     Indien het materiaal licht diffuus weerspiegelt betekent dat de hoek 
     van inval niet uitmaakt voor de reflectie en deze min of meer 
     willekeurig is. 
     
 Transmissie

  ~  Het licht plant zich verder voort door het nieuwe medium, opnieuw in een
     rechte lijn, met mogelijk een iets andere richting op basis van de 
     brekingsindex van het nieuwe en het oude medium.
    

\input{./img/tex/fw-licht.tex}

Deze fenomenen zijn verder geillustreerd in figuur \ref{fig:fw-licht}. Ze zijn 
niet exclusief aan elkaar. Een medium kan dus bijvoorbeeld een gedeelte van het
licht absorberen en een ander gedeelte reflecteren.  

Zoals eerder vermeld, neemt het oog de wereld waar door licht op te vangen.
Het merendeel van het licht dat opgevangen wordt is gereflecteerd via een of 
meerdere oppervlaktes. Een belangrijke constatering is dat objecten slechts 
zichtbaar zijn als er binnen het medium geen (onderzichtige) andere media liggen 
tussen het object en de lens. Dit is een triviale constatering in de fysische
werkelijkheid echter dit zal niet triviale consequenties hebben binnen de 
computer graphics zoals later zal worden beschreven.

Om de interactie van licht te simuleren is het van belang dat licht meetbaar is.
Er zijn hiervoor twee sets van eenheden, radiometrie en fotometrie. Binnen 
radiometrie wordt slechts de lichtkracht over alle golflengte gemeten. Bij 
fotometrie wordt deze kracht gewogen, aan de hand van het gestandardiseerde
model voor de perceptie van helderheid. Fotometrie is van belang voor computer 
graphics, omdat het inzicht geeft in de perceptie van de mens. Echter binnen 
deze thesis zal slechts kort ingegaan worden op radiometrie.  

De belangrijkste termen van Radiometrie zijn opgesteld in tabel 
\ref{tbl:fw-eenheden}. Binnen computer graphics is de belangrijkste eenheid 
radiantie. Dit is de  flux per eenheid geprojecteerde opperlakte per eenheid 
ruimtehoek. Radiantie meet de flux op een willekeurig punt in de ruimte, komende
van een specifieke hoek en gemeten over een oppervlakte eenheid op een 
denkbeeldige oppervlakte loodrecht op de hoek. Radiantie heeft de volgende 
eigenschappen die van belang zullen zijn indien deze berekend dient te worden 
gedurende de simulatie van licht:

* Radiantie is constant binnen een straal die zich voortplant door vacuum. 
  Tevens is het gelijk in beide richtingen die een straal zich voort kan planten
* Indien het punt van meting op een oppervlakte wordt genomen, maakt het niet 
  uit of de flux binnenkomt, of uitgaand is. Het maakt zelfs niet uit of de 
  flux geabsorbeerd, gereflecteerd, of doorgelaten wordt door het materiaal.

## Kleur

\input{./img/tex/fw-kleur.tex}

Een tweede belangrijk aspect van licht voor computer graphics is het concept 
kleur. Het concept kleur is niet een fysisch verschijnsel, maar een consequentie
van hoe ogen licht interpeteren. De mens neemt slechts een gedeelte van al het 
licht waar. Dit wordt het zichtbare licht genoemd. Het menselijk oog 
interpeteert het licht Door het zowel een intensiteit als een kleur toe te 
kennen. De kleur die waargenomen wordt van een lichtstraal is afhankelijk van 
het licht. Een gemiddeld persoon is in staat om 3 verschillende primaire kleuren 
waar te nemen, rood, blauw en groen. Elke zichtbare kleur kan voorgesteld worden
als een mix van deze primaire kleuren. De manier om deze kleuren te mengen
is afgebeeld in figuur \ref{fig:fw-kleur} Belangrijk om hierbij te vermelden is 
dat licht zich gedraagd als additieve kleurmenging. Dit houdt in dat indien 
verschillende kleuren licht op het zelfde punt worden afgebeeld, dit punt zal 
worden waargenomen als de kleur gelijk aan de optelling van deze lichten.  

Objecten kunnen tevens een kleur hebben. Reeds is besproken dat objecten worden
waargenomen door de reflectie van hun licht. De kleur van een object is dan ook
het gevolg van de gedeeltelijk absorptie van licht. In het geval dat een 
gekleurd object wordt verlicht met puur wit licht, zal slechts het licht dat 
overeenkomt in frequentie met de kleur van het object weerspiegelt worden. 
De frequenties tegenovergesteld aan de kleur van het object, zullen worden 
geabsorbeerd door het object.  

## Simulatie

Computer graphics heeft als doel om de fysische werkelijkheid te benaderen. 
Echter hiervoor is het niet nodig om de volledige fysische werkelijkheid te 
benaderen. Het simuleren van de fysische werkelijkheid om een afbeelding te 
verkrijgen, het renderen, kan dus in grofweg in twee problemen ingedeeld 
worden:  

* Wat is zichtbaar binnen een scene vanuit het huidige gezichtspunt.  
* Hoe ziet datgene wat zichtbaar is er uit binnen onze afbeelding.  

Wat afgebeeld wordt op een afbeelding, hangt af van twee aspecten, hoe wordt de 
3d scene op het 2d beeld geprojecteerd. En wat van elk object dat geprojecteerd 
kan worden is daadwerkelijk zichtbaar op de uiteindelijk afbeelding. Het eerste
wordt perspectief projectie genoemd. Het tweede probleem wordt het 
visibiliteitsprobleem probleem genoemd.  

Hoe hetgene wat afgebeeld wordt, er uiteindelijk uit ziet binnen onze 
afbeelding, wordt in de tweede stap bepaald. Deze stap wordt shading genoemd, 
en alle berekeningen gerelateerd aan kleur, absorptie, weerspiegeling etc, 
vallen hier onder.  

