## Enkele Licht Boom

\input{./img/tex/hs-slt.tex}

De enkele licht boom (Single Light Tree) beschrijft voor een enkel licht de
octree representatie. Een voorbeeld hiervan is weergegeven in figuur 
\ref{fig:hs-slt}. Elke blad knoop geeft aan of een gedeelte van het volume
van de knoop overlapt met het licht volume. Uit deze licht bomen wordt de licht octree
afgeleidt. Tevens worden deze gebruikt bij het renderen om de invloed van 
veranderingen van  dynamische lichten binnen de licht octree te berekenen.

Om een een enkele licht boom te construeren is de volgende informatie nodig

* Een puntlicht met een geldige positie en radius
* Een afstand die de grootte van de kleinste cel in een enkele dimensie
  specificeert.
* Een geldige oorsprong van de octree waarin deze enkele lichtbron zich 
  bevindt.
  
Voor de oorsprong moet gelden dat deze kleiner is in elke dimensie dan de positie
van de lichtbron minus de radius:

$$ \forall d \in \lbrace x, y, z \rbrace \mathit{p_d} - \mathit{r} > \mathit{o_d}  $$

waar $\mathit{p_d}$ de oorsprong van de punt licht bron in dimensie $d$ is, 
$\mathit{r}$ de radius van de punt lichtbron, en $\mathit{o_d}$ de oorsprong van de 
octree in dimensie $d$.

De enkele lichtboom wordt opgebouwd met behulp van een bottom up algoritme.
Deze is in te delen in twee stappen. In de eerste stap wordt de onderste laag van
de enkele lichtboom berekend. Vervolgens worden knopen binnen elk rooster in elke
laag gecombineerd om te komen tot een octree representatie. 

\input{./img/tex/hs-knoop.tex}

In de eerste stap wordt berekend per knoop in het rooster, of deze knoop 
overlapt met het lichtvolume.
Dit kan eenvoudig gegaan worden door de afstand tot het dichtstbijzijnde punt van 
de cel tot de oorsprong te vergelijken met de radius van het licht. Indien 
de radius groter is, bevindt de cel zich (gedeeltelijk) binnen het lichtvolume.
Het dichtstbijzijnde punt in een dimensie kan simpelweg gevonden worden door,
de lichtpositie in die dimensie te klampen tussen de uiterste waarde van de cel
in die dimensie, zoals weergegeven in de volgende formule:

$$ \mathtt{clamp}(\mathit{c_d}, \mathit{p_d}, \mathit{c}_d + \mathit{c_l} ) $$

waarbij $\mathit{c_d}$ de oorsprong van de cel is in dimensie $d$, $\mathit{p_d}$
de positie van het licht in dimensie $d$, en $\mathit{c_l}$ de lengte van de cel
is. Dit is geillustreerd in figuur \ref{fig:hs-knoop}

Om te voorkomen dat deze berekening uitgevoerd dient te worden voor elke knoop
binnen het rooster, wordt gebruikt gemaakt van een breadth first flood fill 
algoritme. Er wordt ofwel vanuit gegaan dat elke knoop geen licht bevat, en 
vervolgens worden de nodes gevuld die wel overlappen. Of er wordt aangenomen
dat alle knopen overlappen met licht, en vervolgens wordt gekeken welke 
knopen niet overlappen. 

Het volume van een bol is gedefinieerd als 
$$ V = \frac{4}{3} \pi \mathit{r}^3 $$

Gezien een bol iets meer dan de helft van een omsluitende kubus bevat, is 
gekozen om uit te gaan dat elke knoop overlapt met het licht volume en 
vervolgens de hoeken van de kubus als seeds te gebruiken.

\input{./img/tex/hs-p1.tex}

Dit is weergegeven in figuur \ref{fig:hs-p1}

In de tweede stap wordt het rooster opgesteld in de eerste stap samengevoegd
totdat deze slechts uit een enkele knoop bestaat. Hierbij wordt iteratief
een nieuw rooster opgesteld van grote $\frac{n}{2}$. 
De waarde voor knoop $\mathbf{v}_{xyz}$ kan worden vastgesteld door te kijken
naar set $S$ van acht knopen die $\mathbf{v}_{xyz}$ omvat. Deze set is 
gedefinieerd als:

$$ S = \lbrace \mathbf{v^{\prime}}_{2x2y2z}, \mathbf{v^{\prime}}_{(2x+1)2y2z} \dots \mathbf{v^{\prime}}_{(2x+1)(2y+1)(2z+1)} \brace $$

Er zijn 3 mogelijke situaties

1. $\begin{aligned} &\forall \mathbf{v^{\prime}} \in S : \mathtt{is_empty} \end{aligned}$
   Knoop $\mathbf{v}$ wordt een lege node.
2. $\begin{aligned} &\forall \mathbf{v^{\prime}} \in S : \mathtt{is_full} \end{aligned}$
   Knoop $\mathbf{v}$ wordt een volle node.
3. $\begin{aligned} (\exists \mathbf{v^\prime} \in S : \mathtt{is_full} \land \exists \mathbf{v^\prime} \in S : \mathtt{is_empty(\mathbf{v^\prime})}) \lor \mathbf{v^\prime} \in S : \mathtt{is_partial}(\mathbf{v^\prime}) \end{aligned}$
   Knoop $\mathbf{v}$ bestaat uit een mix van verschillende nodes en wordt een 
   gedeeltelijke knoop.
   
Op basis van deze regels is het mogelijk om voor elk licht een enkele licht boom
op te stellen. De substitutie is tevens weergegeven in figuur 
\ref{fig:hs-substitutie}

\input{./img/tex/hs-substitutie.tex}

Deze zullen in de volgende sectie gebruikt worden om een volledige octree te 
construeren.

