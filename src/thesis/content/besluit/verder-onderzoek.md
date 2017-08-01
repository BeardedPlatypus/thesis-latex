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

## Ondersteuning van dynamische lichten {#sec:ondersteuning-dynamische-lichten}

Het gebrek aan ondersteuning voor dynamische lichten is het tweede grote probleem
van de huidige implementatie van Hashed Shading. Doordat binnen Tiled en Clustered
Shading alle datastructuren per frame worden opgebouwd, worden veranderingen
impliciet meegenomen. Dit is niet het geval bij Hashed Shading, waar de 
datastructuren worden hergebruikt. Om deze reden is het nodig om de datastructuren
expliciet aan te passen, zodat deze de veranderingen van de lichten reflecteren.
In deze sectie zal een update-strategie uitgewerkt worden voor de puntlichten 
binnen Hashed Shading.

Voordat ingegaan wordt op deze update-strategie zal eerst herhaald worden hoe de 
datastructuren in de huidige implementatie worden opgebouwd. Om een verbindingloze
octree op te stellen worden de volgende stappen uitgevoerd:

1. Per licht wordt een octreevoorstelling opgesteld in de vorm van een enkele 
   lichtboom.
2. Alle enkele lichtbomen worden samengevoegd tot een lichtoctree.
3. Per laag van de lichtoctree worden de relevante knopen opgehaald. Voor deze
   knopen wordt een spatiale hashfunctie opgesteld.
4. De texturen geassocieerd met de spatiale hashfuncties worden in het 
   geheugen ingeladen.
   
Uit de resultaten van de opbouw van de verbindingloze octree, sectie \ref{},
kan afgeleid worden dat het grofweg opnieuw uitvoeren van deze stappen per
frame geen acceptabele framerate zal opleveren. Er is vastgesteld dat de 
tijdsbepalende stap in dit algoritme de (her)opbouw van de spatiale 
hashfuncties is. De leiddraad voor de de gepresenteerde update-strategie is 
dan ook om deze opbouw zoveel mogelijk te beperken.

De verwachting is dat een dergelijke herberekening niet nodig is voor elke frame.
Deze aanname is gemaakt op basis van de observatie dat transformaties van lichten
tussen frames veelal klein en lokaal van aard zijn. Hierdoor zullen de meeste 
transformaties niet een zodanige invloed hebben dat een volledige heropbouw nodig is.

Een spatiale hashfunctie, corresponderende met een laag, dient opnieuw opgebouwd
te worden wanneer een knoop moet worden toegevoegd die botst met een reeds 
opgeslagen knoop. Gegeven een reeds gedefinieerde spatiale hashfunctie $H$ en een
knoop $\mathbf{k}$, dan is dit het geval als

$$ H\left[ h_1(\mathbf{k}) + \Phi\left[ \mathbf{k} \right] \right] \neq \varnothing $$ 

De positie $h_1(\mathbf{k}) + \Phi\left[ \mathbf{k} \right]$ is in dit geval reeds 
gevuld. In alle andere gevallen kan de opgestelde spatiale hashfunctie gemodificeerd
worden door de geassocieerde textuur aan te passen.

\input{./tbl/dl-operaties.tex}

Met behulp van deze observatie kan elk mogelijke aanpassing van de octree gemodelleerd 
worden. Het toevoegen van elementen is weergegeven in tabel \ref{}. Het verwijderen van
elementen is weergegeven in tabel \ref{}. In deze tabellen zijn de volgende operaties
te onderscheiden.

Toevoegen van een knoop $\mathbf{k}$ in de data spatiale hashfunctie $H$ \mbox{\hfill}

  ~ Eerst dient gekeken te worden of geldt:
    $$ H \left[ h_1(\mathbf{k}) + \Phi\left[ h_2(\mathbf{k}) \right] \right] = \varnothing $$
    Indien dit het geval is kan de knoop $\mathbf{k}$ hier geplaatst, en dient
    de textuur geassocieerd met $H$ aangepast te worden. Is dit niet het geval 
    dan dient de data spatiale hashfunctie $H$ opnieuw opgesteld te worden.
    Daarnaast dienen de lichtindices geassocieerd met knoop $\mathbf{k}$ 
    toegevoegd te worden aan de lichtindexlijst.
   
   
Toevoegen van opgesplitste knopen in de octree spatiale hashfunctie $H$ \hfill

  ~ Opnieuw wordt gekeken of voor elke opgesplitste knoop $\mathbf{k}$ geldt:
    $$ H\left[ h_1(\mathbf{k}) + \Phi\left[h_2(\mathbf{k})\right] \right] $$
    Afhankelijk hiervan wordt de spatiale hashfunctie $H$ opnieuw opgesteld of
    aangepast. De waardes in deze nieuwe knopen beschrijven de nieuwe octreestructuur.
    
Aanpassingen van de data spatiale hashfunctie \hfill

  ~ Indien een lichtindex wordt toegevoegd aan een knoop dient deze te worden toegevoegd 
    aan de set van indices geassocieerd met deze knoop in de lichtindexlijst. In het 
    geval dat een lichtindex verwijderd wordt, dient deze uit de lichtindexlijst
    verwijderd te worden. Vervolgens dient de textuur zodanig aangepast te worden dat alle 
    clusters opnieuw wijzen naar de correcte subset van de lichtindexlijst.
    
Aanpassing van de octree spatiale hashfunctie \hfill

  ~ Indien de octreestructuur verandert, dienen alle relevante konpen aangepast te worden,
    zodanig dat de nieuwe situatie wordt beschreven. Dit kan gedaan worden door de 
    geassocieerde texturen aan te te passen
    
Verwijderen van knoop $\mathbf{k}$ uit de data spatiale hashfunctie $H$ \hfill

  ~ Gezien knoop $\mathbf{k}$ slechts opgehaald wordt als de corresponderende octreeknoop
    is gedefinieerd als vol, dient de dataknoop in het geheugen van de grafische kaart
    niet expliciet verwijderd te worden. Het volstaat om knoop $\mathbf{k}$ te markeren
    als leeg, $\varnothing$, zodat het geheugen hergebruikt kan worden tijdens het toevoegen
    van nieuwe knopen.
   
\input{./img/tex/dl-transformaties.tex}
   
Met behulp van deze operaties kan de verbindingloze octree aangepast worden wanneer de lichten
transformaties ondergaan. Voor puntlichten kunnen vijf transformaties ge\"identificeerd worden.

* Translatie van het puntlicht.
* Het groter schalen van de radius.
* Het kleiner schalen van de radius. 
* Het toevoegen van een puntlicht.
* Het verwijderen van een puntlicht.

Rotatie heeft geen invloed op puntlichten en kan daarom buiten beschouwing gelaten worden.
Elk van deze transformaties is ge\"illustreerd in figuur \ref{}. Hierbij is het toevoegen
van de index geassocieerd met het licht aan een knoop weergegeven in groen, en het verwijderen
van een index uit een knoop weergegeven in rood.

Om vervolgens de verbindingloze octree aan te passen dienen de volgende stappen uitgevoerd worden:

1. Voor alle dynamische lichten dienen de set van toevoegingen en verwijderingen opgesteld te worden.
2. Alle verwijderingen en toevoegingen per knoop dienen samengevoegd te worden.
3. De aanpassingen aan de verbindingloze octree dienen te worden opgesteld aan de 
   hand van de eerder opgestelde operaties. Hierbij dient, indien nodig, ook 
   ge\"evalueerd te worden of knopen samengevoegd kunnen worden.
4. De aanpassingen dienen doorgevoerd te worden in het grafisch geheugen.

Wanneer de transformaties vloeiend weergegeven worden bij een framerate van 30 tot 60 frames per 
seconde, zullen de transformaties klein en lokaal van aard zijn. Hierdoor zal
het aantal aanpassingen dat doorgevoerd dient te worden in de verbindingloze
octree ook klein zijn. Dit leidt ertoe dat enerzijds herberekeningen van de spatiale
octree schaars zullen zijn, en anderzijds de aanpassingen die gedaan dienen te
worden in redelijke tijd uitgevoerd kunnen worden.

Het aantal herberekeningen van de spatiale hashfuncties kan verder beperkt worden met het
inzicht dat extra lichtindices binnen een knoop niet tot lichtartefacten zullen leiden.
Dit houdt in dat het opsplitsen van bladknopen als gevolg van het toevoegen of verwijderen
van een lichtindex aan een subknoop niet noodzakelijk hoeft worden uitgevoerd.
In het geval dat een lichtindex wordt toegevoegd aan een subknoop van een bladknoop 
kan in plaats hiervan de lichtindex direct toegevoegd worden aan de bladknoop.
In het geval dat een lichtindex verwijderd kan worden van een subknoop van de 
bladknoop, kan deze operatie genegeerd worden. In beide gevallen wordt de structuur
van de octree behouden ten kosten van extra lichtberekeningen. Dit is voordelig 
wanneer de winst behaald met het reduceren van de lichtberekeningen niet opweegt
tegen de extra kosten die de aanpassingen aan de octree met zich meebrengen. 
In plaats hiervan kan gekozen worden om deze pas uit te voeren wanneer de behaalde
winst groter is, of wanneer de spatiale hashfunctie herberekend moet worden als 
gevolg van een andere operatie.

Een significant nadeel van de huidige implementatie van Hashed Shading is 
dat de gehele ruimte per laag beschreven wordt door een enkele spatiale 
hashfunctie. Hierdoor kunnen lokale aanpassingen leiden tot een globale 
herberekening. Er kan dus geen gebruik gemaakt worden van de lokaliteit van
de transformaties. Een oplossing hiervoor is reeds ge\"introduceerd in de vorige
sectie. Door de ruimte onder te verdelen in kleinere stukken, is het mogelijk om,
indien nodig, slechts de ruimte her te berekenen, waar de transformaties plaatsvinden.
Hierdoor zullen de kosten van herberekeningen kleiner zijn. Daarnaast kan door de 
keuze van de grootte van stukken, de uitvoeringstijd van een herberekening beter
beheerst worden.  Verder kan er bij een dergelijke implementatie er voor gekozen
worden om slechts de ingeladen stukken direct aan te passen. Voor niet zichtbare
stukken kunnen de aanpassingen opgeslagen worden, en slechts berekend worden wanneer
deze opnieuw ingeladen worden.

Ondanks al deze optimalisaties zal de ondersteuning voor dynamische lichten 
altijd extra kosten met zich meebrengen binnen Hashed Shading. het doel van
de voorgestelde strategie is om deze kosten zoveel mogelijk te beperken
waardoor lichtmanagement en de lichtberekeningen uitgevoerd kunnen worden binnen
een real-time applicatie.
    
## Andere onderzoeksrichtingen 

Naast oplossingen voor de twee ge\"identificeerde problemen zijn er nog andere richtingen
waarop verder onderzoek zich kan richten. De huidige implementatie ondersteunt geen schaduwen.
Er zou ge\"evalueerd kunnen worden hoe de datastructuur ge\"introduceerd in Hashed Shading 
gebruikt kan worden om schaduwen effici\"ent te berekenen. Voor Clustered Shading zijn
dergelijke algoritmes ontworpen, zie \cite{}, die mogelijk als leiddraad kunnen dienen.

Daarnaast worden slechts puntlichten gebruikt binnen de huidige implementatie van 
Hashed Shading. Moderne game-engines ondersteunen meer lichttypes dan alleen puntlichten
\cite{}. Voor de ondersteuning van andere lichtvolumes dient de octreevoorstelling
effici\"ent opgesteld te kunnen worden.

