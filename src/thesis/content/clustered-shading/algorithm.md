# Algoritme 

\input{./img/tex/cs-algorithm.tex}

Het Clustered Shading-algoritme\cite{olsson2012clustered} is weergegeven in 
figuur \ref{fig:cs-algorithm}. Het vertoont grote overeenkomst met het Tiled
Shading algoritme. Vergelijkbaar met Tiled Shading wordt per frame een set van
lichttoekenningsdatastructuren opgesteld die vervolgens tijdens de 
lichtberekening worden gebruikt om het aantal te evalueren lichten te reduceren.

In tegenstelling tot Tiled Shading kunnen deze clusters niet berekend worden 
voor de geometriestap. Dit komt, doordat de clusters afhankelijk zijn van de
diepte van fragmenten, en dus dient een dieptebuffer opgebouwd te zijn, voordat
de clusters bepaald kunnen worden\cite{olsson2012clustered}. Binnen Deferred Shading wordt de dieptebuffer
opgebouwd in de geometriestap. Binnen Forward Shading zonder extra 
uitbreidingen wordt de dieptebuffer slechts opgebouwd tijdens de renderstap. Voor
Tiled Shading en de na\"ieve implementatie is dit geen probleem. 
Echter voor Clustered Shading leidt het gebrek aan een dieptebuffer ertoe dat de clusters niet
opgesteld kunnen worden voor de renderstap.

Om de dieptebuffer toch beschikbaar te maken voordat de renderstap wordt 
uitgevoerd, dient een extra stap toegevoegd te worden, waarin de dieptebuffer
al wordt opgesteld. Deze stap wordt een z-prepass\cite{Clarberg:2013:SDS:2461912.2462022} genoemd. 
Tijdens de z-prepass wordt alle geometrie gerasteriseerd en gerenderd met een dummy fragmentshader. 
De enige taak van deze dummy shader is het wegschrijven van de diepte
naar de diepte buffer. Vervolgens kan de diepte gebruikt worden om de clusters
te berekenen, als ook om niet zichtbare fragmenten weg te gooien voordat de
lichtberekening wordt uitgevoerd. 
Hier staat echter wel tegenover dat alle geometrie twee maal per frame, 
gerasterised dient te worden. Afhankelijk van de complexiteit van de geometrie 
en eventuele tesselatie kan dit performantie verslechteren.

Nadat de dieptebuffer is berekend kunnen de clusters worden opgesteld. Hiervoor
worden eerst de unieke clusters en hun corresponderende sleutels, berekend. 
Vervolgens wordt aan elk van deze clusters de lichten toegevoegd waarmee deze
overlappen. 

Als laatste wordt de lichtberekeningsstap uitgevoerd. Hiervoor wordt voor 
elk fragment aan de hand van het cluster waartoe deze behoort, de set van 
relevante lichten opgehaald. Vervolgens wordt de lichtberekening met elk van
deze lichten uitgevoerd.


## Clustersleutels

De eerste stap in het opstellen van de clusters is de bepaling van de relevante
clusters. Omdat de clusters het zichtfrustum onderverdelen in een discrete set
van subfrusta, kan elk cluster worden aangeduid met een tupel van drie of meer
integers $\left(i, j, k, \dots \right)$\cite{olsson2012clustered}, zoals weergegeven in figuur \ref{fig:cs-opdeling:sleutel}.
Hierbij zijn $i$ en $j$ gelijk aan de co\"ordinaten voor tegels binnen Tiled
Shading. De integer $k$ specificeert de diepte-index. Een dergelijk tupel wordt
een clustersleutel genoemd. In sectie \ref{sec:cs-onderverdeling} is de diepte van vlak 
$\mathtt{near}_k$ gedefinieerd als:

$$ \mathtt{near}_k = \mathtt{near}_0 \left( 1 + \frac{2 \tan\theta}{S_y} \right)^k $$

\noindent Hieruit kan de waarde voor $k$ worden afgeleid als zijnde:

$$ k = \left\lfloor \frac{\log\left(\frac{-\mathit{z}}{\mathtt{near}}\right)}{\log\left( 1 + \frac{2 \tan\theta}{S_y}\right)}\right\rfloor $$

\noindent Indien deze berekening wordt uitgevoerd voor elk fragment in de dieptebuffer, 
wordt een $k$-buffer verkregen, die de $\mathbf{z}$-co\"ordinaat van elk 
subfrustum beschrijft. De $k$-buffer legt de clustersleutel geassocieerd met
elk fragment vast door de $k$ waarde en de positie binnen de buffer.

## Unieke clustersleutels

\input{./img/tex/cs-sort-and-compact.tex}

De unieke clusters kunnen afgeleid worden uit de opgestelde $k$-buffer. Een 
belangrijke observatie hier, is dat fragmenten slechts tot dezelfde cluster
kunnen behoren, als zij in dezelfde tegel liggen. Hierdoor beperkt het probleem
om alle unieke clustersleutels te vinden zich tot het vinden van alle unieke 
$k$-waardes per tegel. 

De unieke $k$-waardes per tegel kunnen bepaald worden door elke tegel eerst te
sorteren, en vervolgens een compact-operatie uit te voeren. De verschillende
stappen zijn weergegeven in figuur \ref{fig:cs-sort-and-compact}. Hierbij komt
elke verschillend gekleurde tegel overeen met \mbox{\'{e}\'{e}n} $k$-waarde.
Na het sorteren en de compact operatie, blijft per tegel een lijst van unieke
clusters over, waar de set van relevante lichten voor bepaald kan worden.

Om vervolgens per fragment effici\"ent het cluster waartoe het behoort op te
zoeken, wordt tijdens deze stap ook per fragment de index overeenkomend met 
de cluster geassocieerd. Dit wordt gedaan door bij de sorteerstap een referentie
naar het fragment toe te voegen aan de $k$-waarde. Vervolgens wordt tijdens
de compact stap deze referentie gebruikt om de index geassocieerd met de cluster
toe te voegen aan een textuur op de positie van het fragment\cite{olsson2012clustered}.

Deze stappen zijn binnen `nTiled` ge\"implementeerd in de vorm van een `openGL` 
compute-shader. Hierbij wordt per tegel een werkgroep gestart. De compute-shader
voert de sorteer- en compactstap uit. Hierbij wordt de sorteerstap uitgevoerd 
met behulp van een bottom-up merge-sort-algoritme\cite{Sedgewick:2011:ALG:2011916}.
Elke $k$-waarde wordt voorgesteld als een 16-bit integer. Bij de eerste stap van
het merge-sort-algoritme wordt de $k$-waarde verschoven over 16-bits. Vervolgens
wordt de gelineariseerde index van het fragment hierbij opgeteld.

$$ k^\prime = (k \ll 16) + p_x + p_y \times n_x $$

\noindent waar $p_x$ en $p_y$ respectievelijk de $\mathbf{x}$-as en de $\mathbf{y}$-as 
posities van het fragment binnen de tegel zijn en $n_x$ het totaal aantal pixels
in de $\mathbf{x}$-as van de tegel.

Nadat de $k^\prime$ waardes zijn gesorteerd, wordt een compact-operatie 
uitgevoerd. Hierbij worden alle waardes samengenomen waar de 16 meest 
significante bits gelijk zijn. De 16 minst significante bits worden vervolgens
gebruikt om de unieke clusterindex geassocieerd met cluster $k$ weg te schrijven
naar een clusterindextextuur op de positie geassocieerd met het fragment van
$k^\prime$.

Nadat deze stappen zijn uitgevoerd is er per tegel een lijst van unieke $k$-waardes
en een totaal aantal unieke $k$-waardes beschikbaar. Tevens is de clusterindex
voor alle fragmenten opgeslagen in de clusterindextextuur.

## Lichttoekenning

Om de grote aantallen lichten effici\"ent aan de unieke clusters toe te kennen, 
wordt een Bounding Volume Hierarchy (BVH) gebruikt\cite{olsson2012clustered}. Deze BVH wordt
per frame opgesteld. Hiervoor worden de lichten geordend met respect tot de 
$\mathbf{z}$-as. Vervolgens worden de lichten gegroepeerd per 32, en wordt voor
elke groep een Axis-Aligned Bounding Box (AABB) opgesteld. Deze groepen worden
opnieuw gegroepeerd per 32, totdat er slechts 1 wortelelement over is.

De BVH wordt vervolgens per cluster doorlopen. Hierbij wordt per niveau voor elk
van de elementen getest of de AABB van het element overlapt met het volume van
het cluster. Alleen van de elementen die overlappen met het cluster worden de 
kinderen ge\"evalueerd. De uiteindelijk overlappende lichten worden toegevoegd
aan het cluster.

Binnen `nTiled` is deze optimalisatie niet ge\"implementeerd. De clusters worden
in plaats hiervan opgesteld door middel van een bruteforce methode gelijkend op
de lichttoekenningsmethode van Tiled Shading. Eerst worden de lichten afgebeeld
op het zichtvenster en worden de tegels waarop elk licht invloed heeft bepaald, 
zoals in Tiled Shading. Vervolgens wordt voor deze tegels nagegaan of het 
lichtvolume overlapt met de unieke clusters binnen de tegel met respect tot de
$\mathbf{z}$-as. Indien dit het geval is wordt een referentie naar het licht
toegevoegd aan het unieke cluster.

## Datastructuren

\input{./img/tex/cs-datastructuren.tex}
\input{./lst/cs-lichttoekenning.tex}

De datastructuren in Clustered Shading gelijken in grote mate op die van 
Tiled Shading, \ref{sec:ts-datastructuren}. Echter binnen Clustered Shading kan
de clusterindex niet meer direct berekend worden uit de positie van het 
fragment. Deze associatie dient dus expliciet bijgehouden te worden. Om deze
reden is de clustermaptextuur ge\"introduceerd\cite{olsson2012clustered}. Hierin wordt per fragment 
de index van het overeenkomstige cluster bijgehouden. De clusterlijst vervangt
vervolgens de functie van het lichtrooster binnen Tiled Shading.

In `nTiled` wordt binnen de sorteer- en compactstap slechts de lokale 
clusterindex binnen de tegel opgeslagen. Om de verkregen clusterindexmap om te
zetten naar een textuur die de globale indices bevat, dient de offset van
eerdere tegels bij elke waarde opgeteld te worden. Om niet elke waarde in de 
clustermap textuur expliciet bij te werken na de sorteer- en compactstap, is
in plaats hiervan gekozen om een tweede textuur bij te houden. Deze bevat 
voor elke tegel \mbox{\'e\'en} waarde, die de offset voor alle fragmenten binnen
de tegel geeft. Vervolgens kan de cluster die geassocieerd is met een fragment
opgehaald worden door de lokale offset op te tellen bij de tegeloffsetwaarde.
Dit leidt tot de volgende datastructuren\cite{olsson2012clustered}, waarvan 
de relaties zijn weergegeven in Figuur \ref{fig:cs-datastructuren}.


Globale lichtlijst:
  ~ bevat alle lichten. Deze array is in dezelfde vorm aanwezig in de na\"ieve 
    shaders.
    
Lichtindexlijst:
  ~ bevat lichtindices die verwijzen naar lichten in de globale lichtlijst.
    Deze array is dus een lijst van alle referenties van alle clusters.
    
Clusterlijst:
  ~ bevat voor elke cluster een vector die de offset en aantal lichten binnen
    de lichtindexlijst specificeert. Deze lijst neemt de rol van het 
    lichtrooster binnen Tiled Shading over.
    
Tegeloffsettextuur:
  ~ Specificeert de globale offset binnen de clusterlijst voor alle fragmenten
    voor elke tegel.
    
Clustermaptextuur:
  ~ Specificeert de lokale offset binnen alle clusters van een tegel voor alle
    fragmenten.


## Lichtbepaling


Op basis van de voorstelling van de clusters op de GPU kan de lichtberekening 
per fragment worden opgesteld. Hiervoor dient eerst de set van lichten 
geassocieerd met het fragment opgehaald te worden. Hiervoor wordt het 
cluster behorende tot het fragment bepaald. De lokale clusterindexoffset wordt opgehaald uit de clustermap,
en de globale clusterindexoffset uit de tegeloffset. Vervolgens wordt met de 
verkregen clusterindex de offset en aantal lichten in de lichtindexlijst 
opgehaald uit de clusterlijst. De lichtberekening wordt dan uitgevoerd met 
de gespecificeerde set lichten. De code hiervoor is weergegeven in lst. \ref{lst:cs-lichttoekenning}

