# Clustered Shading

\input{./img/tex/cs-straat.tex}

Clustered Shading bouwt verder op de light toekenning geintroduceerd in tiled
shading. Tiled shading presteert slechter wanneer een hoop lichten achter elkaar
geplaatst zijn, die fragmenten in de diepte verlichten, zoals de straat scene
in figuur \ref{fig:cs-straat}. Zoals te zien is, zijn er vlakken die alle 
lichten bevatten, echter fragmenten binnen deze vlakken zullen niet verlicht
worden door elk van deze lichten. Clustered shading lost dit op door van vlakken
naar hogere dimensies clusters te gaan. In de eerste plek wordt de diepte 
meegenomen voor de bepaling van clusters, verder kunnen andere attributen zoals
bijvoorbeeld normalen gebruik worden om verder onderscheid tussen fragmenten te
maken.

## Algoritme

Het algoritme voor Clustered Shading bestaat uit de volgende stappen:

1. Render de scene naar de GBuffers.
2. Bereken de clusters.
3. Bepaal de unieke clusters.
4. Ken de lichten toe aan de clusters.
5. Voer de licht berekeningen uit voor shading.

In het geval van forward clustered shading wordt in de eerste stap de z-buffer
gevuld, en eventuele alternatatieve buffers die gebruikt worden binnen de 
clusters. Deze zullen dan vervolgens worden gebruikt voor de bepaling van de 
unieke clusters.  

### Cluster bepaling

Het doel van cluster bepaling is om een functie op te stellen die een fragment
afbeeldt op een integer, zodanig dat alle vergelijkbare fragmenten dezelfde
waarde toegekend krijgen. Binnen clustered shading wordt hiervoor de locatie van
een fragment gebruikt, en eventueel de normaal, echter andere attributen zijn 
ook mogelijk.  

Ideaal gezien bevat een cluster waartoe een fragment behoort slechts de lichten 
die invloed hebben op dat fragment. Hiervoor is het nodig dat de clusters
klein zijn en bestaan uit vergelijkbare fragmenten, zodanig dat er weinig
lichten toegekend hoeven te worden aan een cluster die geen invloed hebben op
een deel van de fragmenten. Hier staat tegenover dat het de efficientie van de 
cluster berekening, en de lichttoekenning, en het geheugengebruik ten goede komt 
als er zoveel mogelijk fragmenten binnen een zelfde cluster zitten.  

\input{./img/tex/cs-opdeling.tex}

Gezien vergelijkbare fragmenten veelal ruimtelijk dicht bij elkaar liggen, 
is het logisch om een ruimtelijk opdeling te maken. Binnen clustered shading
is gekozen voor een onderverdeling van de het zichtsfrustrum in kleinere 
sub frustrums. De uitgangsbasis hiervoor is het rooster opgesteld in tiled 
shading. Elk van de vlakken vormt een ruimte strekkend van de 
$z_{\mathtt{near}}$ tot de $z_{mathtt{far}}$. Deze worden opgedeeld om zo
subfrustrums binnen het zichtsfrustrum te krijgen. Om er voor te zorgen dat
de dimensies van de subfrustrums in elke richting vergelijkbaar zijn, is
er gekozen voor een exponentiele opdeling, zoals weergegevin in figuur 
\ref{fig:cs-opdeling}.  

De functie waarmee fragmenten afgebeeld worden op de sleutel van clusters kan nu
als volgt gegeven worden. We stellen dat de minimale sleutel van een cluster 
gedefinieerd wordt door de tuple van $(\mathit{i}, \mathit{j}, \mathit{k})$, 
waarmee de gediscretiseerde locatie in het zichtsfrustrum wordt vastgelegd. 
De $\mathit{x}$ en $\mathit{y}$ waardes komen respectievelijk overeen met
$\mathit{i}$ en $\mathit{j}$. Deze kunnen berekend worden vergelijkbaar hoe deze
berekend worden in tiled shading. Uitgaande dat een fragment zich bevindt op
de positie $\mathit{p_x}$ en $\mathit{p_y}$ in pixel coordinaten en de grote
van een rooster is gedefinieerd als $\mathbf{s}$, dan geldt:

$$ 
\begin{aligned}
i &= \lfloor \mathit{p_x} / \mathit{s_x} \rfloor \\
j &= \lfloor \mathit{p_y} / \mathit{s_y} \rfloor \\
\end{aligned}
$$

Uitgaande dat de waarde $f_z$ in camera coordinaten is, en de afstand van het
frustrum gegeven wordt door 
$(\mathit{z}_{\mathtt{near}}, \mathit{z}_{\mathtt{far}})$ dan kan de waarde voor
$\mathit{k}$ kan als volgt berekend worden:

$$ 
k = \lfloor \frac{\log(\frac{\mathit{f_z}}{\mathit{z}_{\mathtt{far}}})}{\log(1 + \frac{2 \tan\theta} * \mathit{h})} \rfloor 
$$

waarbij $\mathit{h}$ het percentage van de hoogte van een enkel vlak is
tenopzichte van de gehele hoogte.
Deze tuple kan vervolgens uitgebreid worden met andere attributen zoals de 
normaal. Elk cluster aanwezig in een frame is uniek gedefineerd door een
dergelijke tuple.

### Unieke cluster bepaling

\input{./img/tex/cs-sort-and-compact.tex}

Nadat voor elk fragment bepaald is tot welke cluster deze behoort, dienen alle
unieke clusters bepaald te worden. Gezien slechts clusters belicht dienen te 
worden, is het niet nodig om voor elk cluster de invloeden van lichten te 
berekenen, en deze bij te houden in het geheugen.  

Het vinden van unieke clusters kan gedaan worden door een sorteer en comprimeer
stap uit te voeren. Deze technieken zijn veelal beschikbaar in bibliotheken om
uitgevoerd te worden op grafische kaarten, en zijn tevens makkelijk te 
implementeren. Deze stappen zijn geillustreerd in figuur 
\ref{fig:cs-sort-and-compact}. Sorteren blijft echter een dure operatie. Een
optimilasie ten opzichte van het globaal sorteren van clusters, kan 
geimplementeerd worden door slechts lokaal te sorteren per vlak. Sorteren
over verschillende vlakken is onnodig, gezien deze per definitie van de tuples
verschillend zullen zijn.  

### Light toekenning

In de meeste tiled shading algoritmes wordt licht toegekend aan vlakken door
intersecties te vinden tussen vlakken en het lichtvolume. Dit is ook mogelijk
voor clustered shading indien kleine hoeveelheden licht en clusters gebruikt
worden. Echter indien de hoeveelheid lichten en clusters toeneemt, leidt dit
tot performantie problemen.  

Om een betere performantie te verkrijgen, worden lichten in de vorm van een
begrensings volume hierarchie (bounding volume hierachy) opgeslagen. Voor
elk cluster wordt deze BVH gebruikt om efficient te bepalen welke lichten
invloed hebben op het cluster.  

### Shading

De shading functie gebruikt in de fragment shader komt in grote mate overeen
met tiled shading. Door middel van de clusters is het opnieuw mogelijk om 
een fragment aan een bepaalde afstand en lengte binnen de licht index lijst
te verkrijgen. Echter, niet alle clusters zullen expliciet bijgehouden worden,
dit zou leiden tot onnodig geheugen verbruik. In dit geval bestaat er geen
directe koppeling tussen de cluster sleutel van een fragment, en de positie
binnen een lijst van clusters. Om te bepalen tot welk cluster een fragment
behoort zal niet tijdens de shading stap opnieuw de sleutel berekend worden,
maar zal een textuur opgesteld worden tijdens de sorteer en comprimeer stap,
bestaande uit de index van elk uniek cluster. Tijdens de shading stap zal 
deze worden uitgelezen en gebruikt worden om de relevante lichten te 
bepalen. Dit is weergegeven in figuur \ref{fig:cs-datastructuren}.

## Besluit

Clustered shading bouwt verder op tiled shading door de licht toekenning
binnen het zichtsfrustrum toe te passen. Hiervoor worden lichten toegekend
aan clusters die gedefinieerd worden door de posite van fragmenten, en eventuele
andere attributen. Per frame wordt een clustering opgesteld die gebruikt wordt
om shading functies uit te voeren.

