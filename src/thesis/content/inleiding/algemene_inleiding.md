\input{./img/tex/introduction-halo.tex}

# Situering

Realtime 3D grafische applicaties zijn niet meer weg te denken uit de moderne
maatschappij. De bekendste categorie van realtime 3D grafische applicaties zijn
games, maar ook buiten de entertainment industrie wordt er veelvuldig gebruik
gemaakt van dergelijke applicaties. Denk hierbij aan interactieve productvisualisaties, 
interactieve simulaties, en opkomende technologi\"en zoals Augmented en Virtual Reality. 

Onder realtime 3D grafische applicaties worden alle applicaties verstaan die in
realtime 3D data omzetten naar beelden. Om de illusie van bewegende beelden te
cre\"eren, worden deze beelden veelal met een framerate van 24 tot 60 frames per
seconde gegenereerd. Deze beelden worden niet van te voren berekend, waardoor de
applicatie in staat moet zijn om een beeld binnen 42 tot 17 milliseconden op te stellen. 
Dit maakt het mogelijk om interactief om te gaan met de 3D wereld die afgebeeld
wordt.

In onder andere games is het doel veelal om de 3D wereld met een vorm
van realisme weer te geven. Om de immersie te vergroten is er een constante vraag
om de wereld met een grotere grafische getrouwheid weer te geven: de wereld dient in een hogere resolutie
weergegeven te worden, complexere grafische fenomenen moeten gesimuleerd worden, en 
\mbox{Sc\`enes} dienen verlicht te worden met meer lichtbronnen. Dit alles leidt tot 
steeds complexere berekeningen, die meer middelen vereisen om in realtime
uitgevoerd te worden. Deze trend in grafische vooruitgang is duidelijk terug
te zien wanneer gekeken wordt naar games die de afgelopen jaren ontwikkeld zijn.
In Figuur \ref{fig:intro-halo} zijn screenshots van de games Halo 1 tot en met Halo 5 
en hun jaar van publicatie weergegeven.
Zowel de toename in complexiteit van de wereld als de belichting is duidelijk zichtbaar.
Het berekenen van dergelijke complexe \mbox{sc\`enes} in realtime wordt enerzijds
mogelijk gemaakt door de toename in beschikbare rekenkracht en geheugen. Anderzijds
worden algoritmes vereist die de hoeveelheid werk die verzet moet worden minimaliseren.

Om een afbeelding te generen van een 3D wereld dient per pixel de kleur berekend te 
worden. Dit kan gedaan worden door per lichtbron het effect op een pixel na te gaan.
Wanneer deze effecten gesommeerd worden, wordt de kleur van een pixel verkregen.
Om de hoeveelheid werk te beperken kan gekeken worden welke lichtbronnen een invloed hebben 
op een pixel. Lichtbronnen die geen invloed hebben hoeven vervolgens niet ge\"evalueerd te 
worden voor deze pixel. De klasse van algoritmes die nagaan
welke lichten relevant zijn voor pixels worden lichttoekenningsalgoritmes genoemd.
Twee veelgebruikte lichttoekenningsalgoritmes zijn Tiled Shading\cite{olsson2011tiled} en 
Clustered Shading\cite{olsson2012clustered}. Deze algoritmes bepalen per frame de relevante 
lichtbronnen per pixel.

# Doelstelling

Het doel van deze thesis is om te evalueren of het hergebruik van lichttoekenningsdatastructuren 
tussen frames uitgebuit kan worden om een performantieverbetering te verkrijgen ten opzichte
van Tiled en Clustered Shading. Hiervoor dient een nieuw lichttoekenningsalgoritme ontwikkeld
te worden, waarin de datastructuren hergebruikt worden. Dit algoritme dient minimaal een
vergelijkbare versnelling en reductie in aantal lichtberekeningen te realiseren als Tiled en
Clustered Shading.

# Methodologie

Om de performantie van het nieuwe lichttoekenningsalgoritme te evalueren zijn dit algoritme, 
en de Tiled en Clustered Shading algoritmes ge\"implementeerd in \mbox{\'e\'en} programma.
Zowel de uitvoeringstijd en het aantal lichtberekeningen van Hashed Shading zijn vergeleken
met die van Tiled en Clustered Shading, zodat een accuraat inzicht in de performantie wordt
verkregen.

# Contributie

Binnen deze thesis wordt een nieuw lichttoekenningsalgoritme voorgesteld op basis van de octree
datastructuur. Doordat deze octree onafhankelijk van het zichtfrustum is, is het mogelijk om de 
datastructuren te hergebruiken tussen frames, ongeacht of het camerastandpunt verandert.
Verder worden uitbreidingen voorgesteld om het geheugengebruik van dit nieuwe algoritme terug
te dringen.

# Overzicht

Hoofdstuk \ref{ch:Theorie}: Theorie
  ~ Binnen het theorie hoofdstuk wordt een algemene inleiding gegeven tot 3D computergrafieken.
    Hierbij wordt ingegaan op de visibiliteit, shading, en realtime computergrafieken. Tevens
    wordt de gebruikte terminologie en wiskunde behandeld. Als laatste zal aan de hand van de
    ge\"introduceerde concepten de probleemstelling en doel van de thesis in meer detail worden
    gedefinieerd.
    
Hoofdstuk \ref{ch:Methode-overzicht}: Methode-overzicht
  ~ Binnen het methode-overzicht wordt ingegaan op de gebruikte software en \mbox{testsc\`enes}.
    De implementatie van de ontwikkelde software wordt toegelicht. Als laatste zal ingegaan
    worden op de data-analyse.
    
Hoofdstuk \ref{ch:Forward en Deferred Shading}: Forward en Deferred Shading
  ~ Binnen Forward en Deferred Shading wordt een veelgebruikte methode ge\"introduceerd om de geometrische
    complexiteit te ontkoppelen van de shading berekening. 
    
Hoofdstuk \ref{ch:Tiled Shading}: Tiled Shading
  ~ Binnen Tiled Shading wordt het eerste veelgebruikte lichttoekenningsalgoritme ge\"introduceerd.
    De resultaten van dit lichttoekenningsalgoritme worden vergeleken met de resultaten van een
    implementatie zonder versnellingsstructuren.
    
Hoofdstuk \ref{ch:Clustered Shading}: Clustered Shading
  ~ Binnen Clustered Shading wordt het tweede veelgebruikte lichttoekenningsalgoritme ge\"introduceerd.
    De resultaten worden vergeleken met die van Tiled Shading en de na\"ieve implementatie.
    
Hoofdstuk \ref{ch:Hashed Shading}: Hashed Shading
  ~ Binnen het Hashed Shading hoofdstuk wordt het lichttoekenningsalgoritme ge\"introduceerd dat 
    binnen deze thesis is ontwikkeld. Hiervoor wordt eerst ingegaan op de achterliggende literatuur.
    Vervolgens worden het algoritme en de implementatie behandeld.
    Daarna worden de resultaten van Hashed Shading vergeleken met de resultaten van zowel Tiled en
    Clustered Shading als de na\"ieve implementatie.
    
Hoofdstuk \ref{ch:Besluit}: Besluit
  ~ In het besluit wordt ingegaan op de verschillende conclusies getrokken in de voorgaande hoofdstukken.
    Daarna wordt mogelijk verder onderzoek toegelicht.

