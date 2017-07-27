\input{./img/tex/introduction-halo.tex}

Real-time 3D grafische applicaties zijn niet meer weg te denken uit de moderne
maatschappij. De bekendste categorie van real-time 3D grafische applicaties zijn
games, maar ook buiten de entertainment industrie wordt er veelvuldig gebruik
gemaakt van dergelijke applicaties. Denk hierbij aan interactieve product 
visualisaties, interactieve simulaties, en binnen opkomende technologi\"en als 
Augmented en Virtual Reality. 

Onder real-time 3D grafische applicaties worden alle applicaties verstaan die in
real-time 3D data omzetten naar beelden. Om de illusie van bewegende beelden te
cre\"eren, worden deze beelden veelal met een framerate van 24 tot 60 frames per
seconde gegenereerd. Deze beelden worden niet van te voren berekend, waardoor de
applicatie in staat moet zijn om een beeld in milliseconden op te stellen. 
Hierdoor is het mogelijk om interactief om te gaan met de 3D wereld die afgebeeld
wordt.

In games, en andere toepassingen, is het doel veelal om de 3D wereld met een vorm
van realisme weer te geven. Om de immersie te vergroten is een constante vraag
om de wereld in meer detail voor te stellen. De wereld dient in een hogere resolutie
weergegeven te worden. Complexere grafische fenomenen moeten gesimuleerd worden. 
\mbox{Sc\`enes} dienen verlicht te worden met meer lichten. Dit alles leidt tot 
steeds complexere berekeningen, die meer middelen vereisen om in real-time
uitgevoerd te worden. Deze trend in grafische vooruitgang is duidelijk terug
te zien wanneer gekeken wordt naar games die de afgelopen jaren ontwikkeld zijn.
In figuur \ref{fig:intro-halo} zijn screenshots van de spellen Halo 1 tot en met Halo 5 weergegeven.
Zowel de toename in complexiteit van de wereld als de belichting is duidelijk zichtbaar.
Het berekenen van dergelijke complexe \mbox{\sc\`enes} in real-time wordt enerzijds
mogelijk gemaakt door de toename in beschikbare rekenkracht en geheugen. Anderzijds
vereist dit algoritmes die de hoeveelheid werk die verzet dient te worden minimaliseren.

Om een afbeelding te generen van een 3D wereld dient per pixel de kleur berekend te 
worden. Dit kan gedaan worden door per licht het effect op een pixel na te gaan.
Wanneer deze effecten gesommeerd worden, wordt de kleur van een pixel verkregen.
Om de hoeveelheid werk te beperken kan gekeken worden welke lichten daadwerkelijk
van invloed zijn op een pixel. Lichten die geen invloed hebben hoeven vervolgens
niet ge\"evalueerd te worden voor deze pixel. De klasse van algoritmes die nagaan
welke lichten relevant zijn voor pixels worden lichttoekenningsalgoritmes genoemd.
Twee veelgebruikte lichttoekenningsalgoritmes zijn Tiled Shading en Clustered Shading.
Deze algoritmes bepalen per frame de relevante lichten per pixel.
Het doel van deze thesis is om een lichttoekenningsalgoritme te ontwikkelen dat een
deel van de opgestelde datastructuren hergebruikt tussen frames, om zo tot een 
betere performantie te komen dan Tiled en Clustered Shading.

De thesis is als volgt onderverdeeld:

Hoofdstuk \ref{ch:Theorie}: Theorie
  ~ Binnen het theorie hoofdstuk wordt een algemene inleiding gegeven tot 3D computergrafieken.
    Hierbij wordt ingegaan op de visibiliteit, shading, en real-time computergrafieken. Tevens
    wordt de gebruikte terminologie en wiskunde behandeld. Als laatste zal aan de hand van de
    ge\"introduceerde concepten de probleemstelling en doel van de thesis in meer detail worden
    gedefinieerd.
    
Hoofdstuk \ref{ch:Methode-overzicht}: Methode-overzicht
  ~ Binnen het methode-overzicht wordt ingegaan op de gebruikte software en \mbox{testsc\`enes}.
    De implementatie van de ontwikkelde softwarde wordt toegelicht. Als laatste zal ingegaan
    worden op de data-analyse.
    
Hoofdstuk \ref{ch:Forward en Deferred Shading}: Forward en Deferred Shading
  ~ Binnen Deferred Shading wordt een veelgebruikte methode ge\"introduceerd om de geometrische
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
    Vervolgens worden de resultaten van Hashed Shading vergeleken met de resultaten van zowel Tiled en
    Clustered Shading als de na\"ieve implementatie.
    
Hoofdstuk \ref{ch:Besluit}: Besluit
  ~ In het besluit wordt ingegaan op de verschillende conclusie getrokken in de voorgaande hoofdstukken.
    Daarna wordt mogelijk verder onderzoek toegelicht.

