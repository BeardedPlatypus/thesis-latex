# Fysische werkelijkheid {#sec:fysische-werkelijkheid}

De fysische wereld waarin de mens zich bevindt, wordt gedicteerd door alle 
fysische wetten. De mens neemt deze wereld waar door middel van zintuigen. Voor 
de computergrafieken is waarneming het belangrijkste zintuig. Door middel van 
waarneming wordt de driedimensionale wereld om de mens heen ge\"interpeteerd. 
Deze interpretatie zal de fysische werkelijkheid genoemd worden binnen deze 
thesis. Zowel de fysische wereld als de manier waarop deze waargenomen wordt,
bepaalt dus de fysische werkelijkheid.  

## Waarneming

\input{./img/tex/fw-waarneming.tex}

De mens neemt de wereld waar door de ogen. Het menselijk oog interpreteert de
driedimensionale wereld door stralen van licht te focussen op een enkel punt, 
met behulp van een lens. Het enkele punt dat licht omzet naar neurosignalen 
wordt de retina genoemd\cite{wolfe2015sensation}. Een camera bootst het oog na, 
en projecteert licht op een elektronische fotosensor, die het licht omzet naar een 
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
basis om licht te simuleren. Licht zal zich onder normale omstandigheden altijd 
in een rechte lijn voortbewegen, zolang het binnen hetzelfde medium blijft. 
Wanneer het licht in contact komt met een nieuw medium
zijn er verschillende fenomenen die kunnen plaatsvinden:

Absorptie

  ~  Het licht wordt geabsorbeerd door de atomen van het nieuwe medium, en 
     uitgestoten als warmte. Hierbij gaat het licht verloren.
  
Reflectie

  ~  Het licht wordt gereflecteerd op het oppervlak van het nieuwe medium.
     Hierbij wordt het licht terug de \mbox{sc\`ene} ingestuurd. 
     De hoek van reflectie hangt af van het type medium. Indien het materiaal
     zich gedraagt als een ideale spiegel zal het licht teruggekaatst worden 
     met dezelfde hoek gespiegeld aan de oppervlakte normaal.
     Indien het materiaal licht diffuus weerspiegelt betekent dat de hoek 
     van inval niet uitmaakt voor de reflectie en deze min of meer 
     willekeurig is. 
     
 Transmissie

  ~  Het licht plant zich verder voort door het nieuwe medium, opnieuw in een
     rechte lijn, met mogelijk een aangepaste richting op basis van de 
     brekingsindex van het nieuwe en het oude medium.
    

\input{./img/tex/fw-licht.tex}

\noindent Deze fenomenen zijn ge\"illustreerd in figuur \ref{fig:fw-licht}. Ze zijn 
niet exclusief aan elkaar. Een medium kan dus bijvoorbeeld een gedeelte van het
licht absorberen en een ander gedeelte reflecteren.  

Zoals eerder vermeld is, neemt het oog de wereld waar door licht op te vangen.
Het merendeel van het licht dat opgevangen wordt is gereflecteerd via een of 
meerdere oppervlaktes. Een belangrijke constatering is dat een object slechts 
zichtbaar is als er geen occlusie van het object is. Dit is een triviale constatering in de fysische
werkelijkheid. Echter dit zal niet-triviale consequenties hebben binnen de 
computergrafieken zoals later zal worden beschreven.

Om de interactie van licht te simuleren is het van belang dat licht meetbaar is.
Er zijn hiervoor twee verzamelingen van eenheden, radiometrie en fotometrie\cite{suffern2007ray}. Binnen 
radiometrie wordt de lichtkracht over alle golflengte gemeten. Bij 
fotometrie wordt deze kracht gewogen, aan de hand van het gestandaardiseerde
model voor de perceptie van helderheid. Fotometrie is van belang binnen de computergrafieken 
omdat het inzicht geeft in de perceptie van de mens. Binnen 
deze thesis zal slechts kort ingegaan worden op radiometrie.  

\input{./tbl/fw-eenheden.tex}

De belangrijkste termen van Radiometrie zijn opgesteld in tabel \ref{tbl:fw-eenheden}. 
De stralingsenergie Q is de basiseenheid van elektromagnetische straling. 
Deze energie bevindt zich in de fotonen. Flux $\Phi$ beschrijft de 
stralingsenergie die zich door een ruimte per seconde heen verplaatst.
Binnen de computergrafieken is de belangrijkste eenheid radiantie L.
Dit is de stralingsflux van fotonen die zich beweegt door een kegel. 
Wanneer de grootte van de basis van de kegel nul benaderd, 
bewegen de fotonen zich in een rechte lijn voort.
Radiantie heeft de volgende  eigenschappen die van belang zijn bij 
de simulatie van licht:

* Radiantie is constant langs een straal die zich voortplant door vacu\"um. 
  Tevens is de binnenkomende straal gelijk aan de uitgaande straal.
* Indien het meetpunt op een oppervlak wordt genomen, maakt het niet 
  uit of de flux ingaand, of uitgaand is. Het maakt zelfs niet uit of de 
  flux geabsorbeerd, gereflecteerd, of doorgelaten wordt door het materiaal.
  
\noindent De radiantie kan dus gebruikt worden om de kleur van een oppervlakte te bepalen.

## Kleur

\input{./img/tex/fw-kleur.tex}

Een tweede belangrijk aspect van licht voor computergrafieken is het concept 
kleur. Kleur is niet een fysisch verschijnsel, maar een gevolg
van hoe ogen licht interpreteren. De mens neemt slechts een gedeelte van al het 
EM-spectrum waar. Dit wordt het zichtbare licht genoemd. Het menselijk oog 
interpreteert het licht door het zowel een intensiteit als een kleur toe te 
kennen. De kleur die waargenomen wordt van een lichtstraal is afhankelijk van 
het licht. Een gemiddeld persoon is in staat om 3 verschillende primaire kleuren 
waar te nemen, rood, blauw en groen. Elke zichtbare kleur kan voorgesteld worden
als een mix van deze primaire kleuren. De manier om deze kleuren te mengen
is afgebeeld in figuur \ref{fig:fw-kleur}. Indien verschillende lichten op 
hetzelfde punt worden afgebeeld, zal dit worden waargenomen als een licht 
gelijk aan de optelling van de individuele lichten.  

Objecten kunnen tevens een kleur hebben. Reeds is besproken dat objecten worden
waargenomen door de reflectie van licht op het oppervlak van het object. 
De kleur van een object is het gevolg van de gedeeltelijk absorptie van het licht
dat op het oppervlak valt. In het geval dat een 
gekleurd object wordt verlicht met puur wit licht, zal slechts het licht dat 
overeenkomt in frequentie met de kleur van het object weerspiegelt worden. 
De frequenties tegenovergesteld aan de kleur van het object, zullen worden 
geabsorbeerd door het object.  

## Animatie

Beweging kan gesimuleerd worden door statische beelden snel genoeg na elkaar af 
te beelden. Deze illusie wordt *schijnbare beweging* genoemd\cite{wolfe2015sensation}. In de computergrafieken
wordt hier dankbaar gebruik van gemaakt om bewegende beelden te cre\"eren. 

Om de illusie van beweging te cre\"eren, dienen de beelden met een hoge framerate
weergegeven te worden. Veelal worden hier framerates tussen de 20 en 60 frames
per seconde voor gebruikt. Een hogere framerate leidt tot een vloeiendere 
beweging.

## Simulatie

Binnen de computergrafieken is het doel veelal om de waarneming van de fysische werkelijkheid te benaderen.
Echter hiervoor is het niet nodig om de volledige fysische werkelijkheid te 
benaderen. Het simuleren van de fysische werkelijkheid om een afbeelding te 
verkrijgen, het renderen, kan dus in grofweg in twee problemen worden opgedeeld:  

* Wat is zichtbaar binnen een \mbox{sc\`ene} vanuit het huidige gezichtspunt.  
* Hoe ziet datgene wat zichtbaar is er uit binnen de afbeelding.  

\noindent Het eerste probleem kan worden opgelost met behulp van perspectief projectie.
Het tweede probleem wordt het visibiliteitsprobleem genoemd.  

Hoe hetgene wat afgebeeld wordt, er uiteindelijk uit ziet binnen onze 
afbeelding, wordt in de tweede stap bepaald. Deze stap wordt shading genoemd, 
en alle berekeningen gerelateerd aan kleur, absorptie, weerspiegeling etc., 
vallen hier onder.  

Voor een uitgebreidere beschrijving van de behandelde onderwerpen kan gerefereerd worden 
naar de volgende boeken:
Voor de psychologische grondslag van kleur en perceptie, kan gerefereerd worden 
naar Wolfe's Sensation and Perception\cite{wolfe2015sensation}. De fysica die ten grondslag ligt 
aan computergrafieken kan gevonden worden in Optics door Eugene Hecht 
\cite{hecht2016optics}.

# Virtuele voorstelling

Om een afbeelding te cre\"eren van een virtuele driedimensionale omgeving die
de fysische werkelijkheid benadert, is het in de eerste plaats nodig om een beschrijving 
te hebben van deze omgeving. Daarnaast is het nodig om een virtuele camera te defini\"eren
waarmee deze virtuele wereld wordt waargenomen.

## Voorstelling van de geometrie {#sec:geometrische-def}

\input{./img/tex/gd-object.tex}

Om een omgeving voor te stellen wordt een verzameling van primitieven gedefinieerd. 
Deze primitieven maken het mogelijk om een beschrijving te geven van elk object
binnen de \mbox{sc\`ene}. De basis renderprimitieven die gebruikt worden in grafische 
renderhardware zijn punten, lijnen en driehoeken. 

Wanneer gesproken wordt binnen deze thesis over primitieven, zal, indien niet 
anders aangegeven, gedoeld worden op driehoeken. Met behulp van driehoeken is 
het mogelijk om de geometrie van alle objecten in een \mbox{sc\`ene} te beschrijven.
Dit proces is weergegeven in figuur \ref{fig:gd-object}. Door een collectie van
verschillende driehoeken te nemen, wordt een *mesh* gevormd. Een *mesh* 
beschrijft het oppervlakte van een object. 
Vervolgens wordt een *object* gedefinieerd door middel
van een referentie naar een *mesh* en een transformatiematrix $\mathbf{A}$. 
Deze transformatiematrix beschrijft de locatie, schaal en rotatie van de *mesh*
van het *object* binnen de driedimensionale wereld. Hierdoor is het mogelijk
om meerdere objecten met verschillende transformaties binnen de wereld voor te stellen 
dezelfde *mesh*. Een voorbeeld van een verzameling van 
vier objecten met dezelfde mesh maar verschillende transformatiematrices is
weergegeven in figuur \ref{fig:gd-object}.

De volledige beschrijving van een omgeving zal een *\mbox{sc\`ene}* genoemd worden. Deze
bevat de definities van de verschillende objecten binnen de wereld, als ook 
de lichtbronnen en eventuele camera's en zichtspunten.

## Voorstelling van de camera {#sec:camera-model}

\input{./img/tex/cm-camera.tex}

Om een afbeelding van een \mbox{sc\`ene} te genereren moet het zichtpunt en 
ori\"entatie van het camerastandpunt gedefinieerd worden. Hiervoor wordt gebruik gemaakt
van een cameramodel\cite{CGF:CGF1181}. Dit cameramodel is een
beschrijving van een virtuele camera die zich bevindt binnen
de \mbox{sc\`ene}. Om deze camera te defini\"eren worden de 
volgende attributen opgesteld:


$\mathcal{O}_\mathtt{camera}$ 
  ~ De positie van de camera in de \mbox{sc\`ene}.
  
up
  ~ De lokale $\mathbf{y}$-as van de camera.
  
kijkrichting
  ~ De lokale $\mathbf{z}$-as van de camera, waarin de camera kijkt.
  
Z-near
  ~ De afstand van de oorsprong tot het zichtvenster.
  
Z-far
  ~ De maximale afstand tot waar objecten worden weergegeven.
  
gezichtsveld $\theta$
  ~ De hoek die bepaald hoeveel van de wereld zichtbaar is.
  
aspectratio
  ~ De ratio breedte $\mathit{w}$ tot hoogte $\mathit{h}$ van het zichtvenster.
  
\noindent Dit specificeert de volledige camera, zoals weergegeven in figuur \ref{fig:cm-camera}.
  
De *Z-near*, *Z-far*, oorsprong $\mathcal{O}_\mathtt{camera}$, gezichtsveld en
aspectratio defini\"eren het zogenoemde zichtfrustum. Dit frustum specificeert
de ruimte waarbinnen alle zichtbare objecten in de \mbox{sc\`ene} zich bevinden.

