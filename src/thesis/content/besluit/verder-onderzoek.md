# Verder onderzoek

I n de discussie van Hashed Shading zijn twee significante problemen 
ge\"identificeerd, die zich voordoen in het Hashed Shading algoritme. Enerzijds
is er de beperkende factor van het geheugenverbruik bij kleine knoopgroottes, 
die kubisch toeneemt voor kleinere knoopgroottes. Anderzijds is er de ondersteuning
voor dynamische lichten, iets dat triviaal ondersteund wordt in Tiled en Clustered
shading, maar extra werk vereist binnen Hashed Shading. Binnen deze sectie zullen 
eerst twee mogelijke verbeteringen ten opzichte van het geheugenverbruik voorgesteld
worden, wat in verder onderzoek uitgewerkt en ge\"implementeerd zou kunnen worden. 
Hierna zal gekeken worden hoe dynamische lichten ondersteund kunnen worden binnen
Hashed Shading. Als laatste zullen nog enkele andere richtingen gegeven worden waar
verder onderzoek naar gedaan kan worden.


## Reduceren van geheugenverbruik doormiddel van geometrie

\input{./img/tex/vo-geometrie.tex}

In de huidige implementatie van Hashed Shading wordt het volume van de gehele 
scene voorgesteld, zodat elk punt binnen deze scene opgevraagd kan worden. Een
belangrijk inzicht van Clustered Shading is dat slechts punten opgevraagd zullen 
worden van geometrie. In Clustered Shading wordt dit gebruikt om slechts de 
zichtbare clusters voor te stellen en zo het geheugenverbruik te beperken.
Hetzelfde inzicht kan gebruikt worden om het aantal knopen in de verbindingloze
octree te reduceren. Alleen knopen die geometrie bevatten hoeven voorgesteld te 
worden binnen de verbindingloze octree. 

Om het geheugenverbruik op de grafische kaart te reduceren, dient een zelfde
octree voorstelling gemaakt te worden van de geometrie zoals gedaan is voor de
lichten. Vervolgens kunnen alle lichtoctreeknopen die niet tevens geometrie 
bevatten buiten beschouwing gelaten worden, gezien deze nooit opgevraagd zullen
worden. Dit is ge\"illustreerd in figuur \ref{fig:vo-geometrie} voor een simpele
scene bestaande uit twee objecten en een enkel licht.

Een bijkomend voordeel van een dergelijke implementatie is dat een kleinere 
knoopgrootte niet alleen leidt tot een reductie in het aantal lichtberekeningen
gedurende de uitvoering. Tevens leidt een kleinere knoopgrootte er toe dat
de geometrie met een hogere nauwkeurigheid benaderd wordt. Hierdoor kan meer
lege ruimte verwaarloosd worden tijdens het opstellen van de verbindingloze 
octree.

Als laatste optimalisatie is het mogelijk om de hi\"erarchische structuur van 
de octree uit te buiten, om zo het aantal knopen verder te reduceren.
Gezien volumes die geen geometrie data bevatten nooit opgevraagd zullen worden,
maakt de set lichten geassocieerd met een dergelijke knoop niet uit. Dit betekent
dat voor de opbouw van de verbindingloze octree gesteld kan worden dat de set van
lichten geassocieerd met een dergelijke knoop gelijk is aan de omliggende knopen,
zonder dat dit visuele artefacten introduceert. Op basis van dit inzicht kan de 
eis voor het samennemen van acht bladknopen tot een enkele bladknoop in een hoger
liggende laag versoepelt worden. In de huidige implementatie geldt dat alle acht
knopen exact dezelfde set van lichten dienen te hebben, voordat deze samengenomen
kunnen worden. In de voorgestelde implementatie kan dit worden versoepeld tot de 
eis dat de subset van de acht knopen die geometrie bevat, de zelfde set van 
lichten bevat. In dit geval zullen meer knopen samengenomen kunnen worden, dan dat
het geval is voor de huidige implementatie. Dit leidt ertoe dat er in totaal
minder knopen bijgehouden dienen te worden.

Deze combinatie van optimalisaties zou tot een sterke reductie in knopen moeten
leiden, waardoor de constructietijd en het geheugenverbruik afneemt. Deze reductie
in geheugenverbruik kan gebruikt worden om kleinere knoopgroottes te gebruiken, 
waardoor de performantie van Hashed Shading, die van Clustered Shading nog beter 
zou moeten benaderen.

## Reduceren van geheugengebruik doormiddel van opdeling van de scene-ruimte

\input{./img/tex/vo-subsets.tex}

Een tweede inzicht waar Clustered Shading gebruik van maakt is dat fragmenten
slechts gegenereerd worden binnen het zichtfrustum. Hierdoor hoeft slechts de
beschrijving van de relevante lichten voor deze subset van de ruimte aanwezig te
zijn in het geheugen van de grafische kaart. Binnen Clustered Shading wordt 
slechts een beschrijving van het zichtfrustum gemaakt. Dit introduceert echter
de camera-afhankelijkheid die Hashed Shading verhelpt.

Om toch het geheugenverbruik te reduceren kan de scene-ruimte in stukken worden 
onderverdeeld, zodanig dat slechts een kleine set van stukken aanwezig hoeft te
zijn in het geheugen. Indien deze set een kleiner volume beschrijft dan de 
gehele scene, leidt dit tot een afname van geheugenverbruik. 

In de meest simpele implementatie zijn hier $2^3$ stukken nodig, indien de lengte 
van de stukken zodanig wordt gekozen dat de as-uitgelijnde omvattende doos (AABB) 
van het zichtfrustum  binnen het volume van de 8 stukken valt, zoals weergegeven
in figuur \ref{fig:vo-subsets:2}. In veel applicaties zullen rotaties van de camera
veel voorkomen. Dit zal er toe leiden dat de camerarotaties verantwoordelijk zullen
zijn voor de meeste uitwisseling van texturen. Indien een set van $3^3$ stukken
gebruikt wordt, zoals weergegeven in figuur \ref{fig:vo-subsets:3}, zullen slechts
translaties van het camerapunt leiden tot veranderingen in de texturen. Hiermee
kan de geheugenbandbreedte verlaagd worden ten koste van het geheugenverbruik.
Als laatste kan de uitwisseling van texturen beperkt worden door de punten van inladen
uit te spreiden. Hierdoor zullen geen punten binnen de scene zijn waar een kleine 
transformatie constant tot herladen van texturen leidt, zoals weergegeven in figuur
\ref{fig:vo-subsets:point}.

\input{./img/tex/vo-textures.tex}

Indien elk van deze stukken wordt voorgesteld als een aparte verbindingloze octree
leidt dit tot een groot aantal, veelal kleine, texturen. Dit is niet ideaal, gezien
de geheugenoverhead die geassocieerd is met elke textuur, en door de vaak beperkte
hoeveelheid beschikbare texturen. Door terug te kijken naar het geheugenverbruik
van Hashed Shading kan hier een oplossing voor gevonden worden. Uit het 
geheugenverbruik blijkt dat de eerste lagen relatief klein zijn, en dus weinig 
geheugen verbruiken, en dat het merendeel van het geheugen wordt verbruikt door
de diepste lagen van de verbindingloze octree. Gezien alle knopen in een laag
expliciet in dezelfde textuur worden opgeslagen, is er geen horde om slechts
de diepste lagen onder te verdelen en apart in te laden. Hierdoor hoeft de huidige
implementatie slechts minimaal aangepast te worden, en blijft het textuurverbruik
kleiner. Deze oplossing is visueel weergegeven in figuur \ref{fig:vo-textures}.
Om een dergelijke structuur mogelijk te maken dient voor deze diepste knopen
een extra referentie bijgehouden te worden, zodat, wanneer de opsplitsing 
van lagen in verschillende stukken wordt bereikt, er nagegaan kan worden, in 
welke textuur de uiteindelijk knoopinformatie gevonden kan worden.

Een laatste optimalisatie die op basis van de onderverdeling van de scene-ruimte
kan worden toegevoegd is het gebruik van detailniveaus. Onder normale 
omstandigheden zal het merendeel van de pixels geometrie beschrijven die dicht
bij de camera ligt. Dit is een gevolg van perspectief, waar objecten dicht bij 
de camera groter zijn, en dus veelal meer ruimte op het zichtvenster zullen 
innemen. Indien de gehele ruimte met dezelfde precisie wordt beschreven betekent
dit dat de ruimte ver van de camera meer geheugengebruikt relatief aan de 
performantie die hier mee gewonnen wordt. Om deze reden is het voordelig
om punten dichtbij de camera met een hogere resolutie te beschrijven, dan punten
ver van de camera. Dergelijke technieken maken dan dus gebruik van zogenoemde
detailniveaus (Level of Detail) \cite{}. Octree datastructuren kunnen dergelijke
detailniveaus op een natuurlijke manier ondersteunen, door gebruik te maken van
de hierarchische structuur. Indien een scene wordt opgedeed, kunnen stukken verder
van de camera voorgesteld worden met een kleinere diepte, en stukken dichtbij de
camera met een hogere diepte. Hierdoor wordt de resolutie gevarieerd, waardoor
het geheugenverbruik afneemt en tegelijkertijd, indien het merendeel van het
zichtvenster objecten dichtbij de camera weergeeft, het totaal aantal
lichtberekening verder wordt gereduceerd.

De verbindingloze octree leent zich zeer goed voor een dergelijke strategie. 
Doordat alle knopen in een laag indezelfde textuur worden opgeslagen, kunnen
voor bepaalde dieptes meerdere texturen gedefinieerd worden. Hierbij beschrijft
\mbox{\`e\`en} textuur dan de geassocieerde ruimte met bladknopen, alsof het de 
maximale diepte is, en een andere textuur de ruimte met zowel bladknopen als
takknopen, zodanig dat er nog diepere lagen bestaan. Afhankelijk van de afstand 
dat een stuk van de camera ligt kan gekozen worden om de maximale diepte kleiner
of groter te maken, zonder dat dit leidt tot het bijhouden van meerdere 
verbindingloze octrees.

Deze combinatie van optimalisaties zou, vooral voor grote scenes, tot een afname
in geheugenverbruik moeten leiden. Dit gaat echter ten koste van een toename in
geheugenbandbreedte en berekeningstijd.

## Ondersteuning van dynamische lichten

Naast het geheugenverbruik is het tweede probleem van de huidige implementatie
van Hashed Shading, het gebrek aan ondersteuning voor dynamische lichten. Doordat
Tiled en Clustered Shading per frame alle datastructuren opnieuw opbouwen, worden 
veranderingen van lichten tussen frames impliciet meegenomen. Dit is niet het
geval bij Hashed Shading, dus zullen de datastructuren expliciet aangepast moeten
worden om dergelijke veranderingen te reflecteren. In deze sectie zal een 
update-strategie uitgewerkt worden voor puntlichten binnen Hashed Shading.

Voordat echter ingegaan zal worden op deze update-strategie zal eerst gekeken
worden hoe dynamische lichten binnen Hashed Shading ondersteund kunnen worden door
de datastracturen per frame opnieuw op te bouwen. Ervan uitgaande dat een 
onderscheid gemaakt kan worden tussen dynamische en statische lichten, dan dient 
voor elk dynamische licht opnieuw een octree voorstelling gemaakt te worden die 
de transformatie reflecteert. Uit de octreevoorstellingen van de dynamische en statische 
lichten kan vervolgens een lichtoctree worden opgesteld, die gebruikt kan worden
om een nieuwe verbindingloze octree op te stellen. Als laatste stap dienen dan
de texturen geassocieerd met de verbindingloze octree in het GPU geheugen geladen
te worden. Dit komt neer op dezelfde stappen als bij het voor de eerste keer opbouwen 
van de verbindingloze octree, weergegeven in figuur \ref{}.

Uit de resultaten van de opbouw van de verbindingloze octree kan afgeleid worden 
dat een dergelijke aanpak niet effeci\"ent genoeg gaat zijn om een acceptabele
framerate te verkrijgen. De tijdsbepalende stap binnen dit algoritme is de 
(her)opbouw van de verbindingloze octree. De leiddraad voor de gepresenteerde
update-strategie is dan ook om deze heropbouw zoveel mogelijk te beperken.
De verwachting is dat een dergelijke opbouw niet nodig is per frame, waardoor
een update-strategie effici\"enter is. Deze aanname is gemaakt op basis van de 
observatie dat veranderingen van lichten tussen frames voornamelijk klein en lokaal 
zijn. Hierdoor zal een transformatie van een licht slechts invloed hebben op een klein 
deel van de scene, en dus de datastructuren.

Een spatiale hashfunctie, corresponderend met een laag, dient opnieuw opgebouwd
te worden wanneer een knoop die toegevoegd dient te worden, botst met een reeds 
opgeslagen knoop. Dit is het geval wanneer voor een knoop $\mathbf{p}$ geldt
dat het element $\mathbf{e} = h_1(\mathbf{p}) + Phi[\mathbf{p}]$ binnen de 
spatiale hashfunctie reeds in gebruik is. In alle andere gevallen kan een
transformatie doorgevoerd worden door de textuur geassocieerd met de spatiale
hashfunctie aan te passen. 

Uitgaande van deze observatie kan opgesteld worden hoe elke mogelijke aanpassing
aan de octree gemodelleerd wordt. Dit is voor het toevoegen van lichtindices
weergegeven in tabel \ref{}, en voor het verwijderen van licht indices weergegeven
in tabel \ref{}.

De volgende operaties zijn hierbij te onderscheiden:

* Toevoegen van een knoop in de data spatiale hashfunctie
  Eerst zal gekeken worden of het element $\mathbf{e} = h_1(\mathbf{p}) + Phi[\mathbf{p}]$
  actief gebruikt wordt. Is dit niet het geval, dan hoeft slechts dit punt
  aangepast te worden. Dit kan gedaan worden met behulp van een aanpassing
  aan de textuur. Is deze wel in gebruik, dan dient de spatiale hashfunctie
  opnieuw opgesteld te worden.
  Tevens dienen de corresponderende lichtindices toegevoegd te worden
  aan de lichtindexlijst. De data opgeslagen in de knoop komt overeen met deze lichtindices.
  
* Toevoegen van opgesplitste knopen in een lagere laag van een octree spatiale hashfunctie:
  Opnieuw zal gekeken worden of in deze laag de corresponderende elementen in gebruik zijn.
  Afhankelijk hiervan wordt de textuur aangepast of opnieuw berekend. De waardes in deze nieuwe
  knopen beschrijft de nieuwe structuur van de octree.
  
* Aanpassing van de data spatiale hashfunctie
  Indien een licht wordt toegevoegd aan een dataknoop zal eerst deze index toegevoegd worden
  aan de lichtindexlijst. Vervolgens zal deze verandering beschreven moeten worden in 
  alle dataknopen, zodat deze nog steeds de correcte set van lichten beschrijven.
  Dit kan gedaan worden door de relevante texturen aan te passen zodat zij deze nieuwe
  situatie beschrijven
  
* Aanpassing van de de octree spatiale hashfunctie.
  Indien de octree structuur veranderd, dient deze aanpassing weergegeven te worden
  in de verbindingloze octree. Hiervoor dienen alle relevante knopen aangepast te worden.
  Dit kan tevens gedaan worden met behulp van een aanpassing aan de relevante texturen.
  
* Verwijderen van een knoop uit de data spatiale hashfunctie:
  Gezien de dataknoop slechts wordt opgehaald als de corresponderende octreeknoop 
  als gevuld is gedefinieerd, volstaat het om de knoop te markeren als ongebruikt,
  zodat deze knoop kan worden hergebruikt tijdens het toevoegen van nieuwe knopen.
  Er is geen verdere actie nodig, gezien het algoritme niet meer deze knoop zal opvragen.

Met behulp van deze operaties kan de verbindingloze octree aangepast worden.

Nu vastgesteld is welke operaties opgesteld moeten worden om de octree aan te passen, 
kunnen de transformaties van lichten gedefinieerd worden met behulp van deze operaties.
Voor puntlichten kunnen vier verschillende transformaties ge\"identificeerd worden:

* Translatie van het puntlicht
* Schaling van de radius
* Toevoegen van een puntlicht
* Verwijderen van een puntlicht

Rotatie heeft geen invloed op puntlichten en kan doorom buiten beschouwing gelaten worden.
Elk van deze transformaties is weergegeven in figuur \ref{}. Deze figuren illustreren 
de observatie dat transformaties van lichten, translatie en schaling, klein en lokaal
van aard zij. Indien ervan uitgegaan wordt dat transformaties vloeiend weergegeven worden
bij een framerate van 30 tot 60 frames per seconde, zal de verandering tussen frames
erg klein zijn. Hierdoor zal het aantal operaties kleiner zijn dan een volledige heropbouw.

Om alle transformaties op te stellen kan een volgende strategie gehanteerd worden:

1. Stel de set van toevoegingen en verwijderingen op voor elke knoop die be\"invloed wordt
2. Bepaal of knopen samengevoegd kunnen worden na transformatie
3. Herbereken lagen die herberekend dienen te worden, voor de andere lagen bepaal de nieuwe
   textuur zonder dat deze opnieuw berekend worden.
4. Laad nieuwe texturen in het geheugen.

De transformaties weergegeven in figuur \ref{} kunnen worden gedefinieerd aan de hand 
van de toevoegingen, weergegeven in groen, en verwijderingen, weergegeven in rood.
De aanpassingen aan de octree worden vervolgens uitgevoerd volgens de eerder
opgestelde operaties, tabel \ref{}. 

Het aantal herberekeningen kan verder beperkt worden door de observatie dat extra lichtindices
binnen knopen niet leiden tot lichtartefacten. Slechts het ontbreken van relevante lichtindices
leidt tot lichtartefacten. Stel de situatie dat een knoop op diepte $\mathit{n}$ een bladknoop
is. Aan de subknoop, op diepte $n + 1$, van deze bladknoop wordt vervolgens ofwel een licht
toegevoegd, of een licht verwijderd. Dit heeft tot gevolg dat de bladknoop onderverdeeld dient
te worden in acht subknopen, die toegevoegd moeten worden aan de laag op diepte $n + 1$.
Dit kan een herberekening tot gevolg hebben. Deze opdeling kan voorkomen worden door 
in het geval van het verwijderen van een licht, deze niet uit te voeren, en in 
het geval van het toevoegen deze toe te voegen aan de bladknoop op diepte $n$.
In beide gevallen leidt dit ertoe dat er extra lichtberekeningen uitgevoerd worden voor een
deel van de ruimte, echter geen herberekening is nodig. Dit is voordelig indien de winst
die behaald wordt met de reductie in lichtberekeningen niet opweegt tegen de extra kosten
die een dergelijke herberekening met zich meebrengt. In dit geval kan er voor gekozen worden
om deze aanpassingen uit te voeren wanneer de behaalde winst groter is, of wanneer de laag
opnieuw herberekend dient te worden.

Een significant nadeel van de huidige implementatie van de verbindingloze octree
is dat de gehele ruimte globaal afhankelijk van elkaar is. Doordat elke laag de 
gehele ruimte beschrijft, is het niet mogelijk om lokaal aanpassingen te maken zonder
dat mogelijk de gehele ruimte dient te worden herberekend. Een oplossing hiervoor
is reeds ge\"introduceerd in de vorige sectie. Door de ruimte onder te verdelen
in kleinere stukken, kan gebruik gemaakt worden van het lokale gedrag van de 
transformaties van de lichten. Hierdoor zal slechts een kleiner percentage van
de gehele ruimte opnieuw opgebouwd worden. Daarnaast kan de grootte van de spatiale
hashfunctie zodanig gekozen worden dat deze effici\"ent en parrallel opgebouwd 
kunnen worden. Als laatste hoeft bij een dergelijke implementatie slechts de zichtbare stukken
direct aangepast worden. De aanpassingen aan niet zichtbare stukken kunnen 
worden opgeslagen totdat deze ingeladen moeten worden in het grafisch geheugen.

Ondanks al deze optimalisaties zal de ondersteuning voor dynamische lichten altijd een
extra kost met zich meebrengen binnen Hashed Shading. Het doel van de voorgestelde 
strategie hier is om deze kosten zoveel mogelijk te beperken, zodat het lichtmanagement
en de lichtberekening van Hashed Shading nog steeds uitgevoerd kan worden binnen real-time
applicaties. 

