# Algoritme

\input{./img/tex/ts-algorithm.tex}

Het Tiled Shading-algoritme\cite{olsson2011tiled} voor zowel de Forward- als 
Deferred pijplijn is weergegeven in figuur \ref{fig:ts-algorithm}. Hierbij zijn
de pijplijn-specifieke stappen in het geel weergegeven, en de Tiled Shading 
stappen in het blauw. Het algoritme bevat grofweg twee extra stappen boven op
het na\"ieve algoritme, een initialisatiestap en een lichtbepalingsstap. Deze
stappen zijn in grote mate onafhankelijk van de gekozen pijplijn.

Tijdens de initialisatiestap wordt het rooster van tegels opgebouwd. Eerst 
worden lege tegels ge\"initialiseerd. Vervolgens wordt voor elk licht bepaald
met welke tegels deze overlapt.

Tijdens de belichtingsberekening wordt niet meer elk lichtvolume gerasteriseerd,
noch wordt elk licht ge\"evalueerd. In plaats hiervan wordt aan de hand van 
de fragmentpositie de tegel waartoe het fragment behoort, bepaald. Hierna wordt
de set van lichten geassocieerd met deze tegel opgehaald.


## Datastructuren {#sec:ts-datastructuren}

\input{./img/tex/ts-datastructuur.tex}

De gebruikte datastructuur dient een rooster van tegels bij te houden. Elke 
tegel dient een variabel aantal referenties naar lichten bij te houden. Dit
rooster dient effici\"ent opgebouwd te worden. Verder dient, wanneer de tegel
bepaald is, de set van lichteng geassocieerd met deze tegel effici\"ent op
te halen zijn. 

Om dit rooster voor te stellen wordt gebruik gemaakt van drie 
arrays\cite{olsson2011tiled}:

Globale lichtlijst:
  ~ bevat alle lichten. Deze array is in dezelfde vorm aanwezig in de na\"ieve 
    shaders.
    
Lichtindexlijst:
  ~ bevat lichtindices die verwijzen naar lichten in de globale lichtlijst.
    Deze array is dus een lijst van alle referenties van alle tegels.
    
Lichtrooster:
  ~ bevat voor elke tegel \mbox{\'e\'en} vector die een offset en aantal lichten
    geassocieerd met een tegel specificeert.
    

De relatie tussen de drie arrays is weergegeven in figuur \ref{fig:ts-datastructuur}.
Deze structuren zijn op de GPU voor te stellen met behulp van bufferobjecten of
texturen.


## Lichtbepaling

Nu de voorstelling van het rooster gedefinieerd is, is het mogelijk om de 
lichtberekening op te stellen. Hiervoor dient voor een fragment de set van 
relevante lichten bepaald te worden. Om dit te bereiken, wordt eerst 
de tegel waartoe het behoort bepaald:

$$ f: (\mathtt{frag.x}, \mathtt{frag.y}) \mapsto \left(\left\lfloor{\frac{\mathtt{frag.y}}{\mathit{n}}}\right\rfloor , \left\lfloor{\frac{\mathtt{frag.y}}{\mathit{n}}}\right\rfloor \right) $$
                                                  
waar $\mathtt{frag}$ de pixelco\"ordinaten van het fragment zijn, en $n$ de 
grootte van \mbox{\'e'en} tegel in pixels is. Op basis van deze indices kan de
offset en aantal lichten opgehaald worden uit het lichtrooster. 
Vervolgens wordt per lichtindex in de lichtindexlijst geassociceerd met deze 
tegel, de lichtberekening uitgevoerd met het corresponderende licht. 
de code hiervoor is gedefinieerd in listing \ref{lst:ts-lichttoekenning}

\input{./lst/ts-lichttoekenning.tex}

## Lichttoekenning

\input{./img/tex/ts-projectie.tex}

Om de datastructuren op te stellen in de roosterinitiialisatiestap dient voor 
elk licht bepaald te worden met welke tegels het lichtvolume overlapt. De set
van tegels komt overeen met het venster. Een simpele manier om de overlapping
te bepalen is door de corresponderende lichtvolumes af te beelden op het 
venster. Vervolgens kan bepaald worden welke tegels bedekt worden door het
geprojecteerde volume.~\cite{olsson2011tiled} 

Wanneer de grootte van de set van lichten in de honderden is, is het mogelijk
om deze berekeningen op de CPU uit te voeren. Wanneer er duizenden lichten zijn,
kan deze berekening te traag zijn op de CPU, en zal deze op de GPU 
ge\"implementeerd moeten worden. 

Er zijn verschillende algoritmes om deze projectie uit te voeren.~\cite{lengyel2002mechanics, sigg2006gpu}
Binnen `nTiled` is gekozen voor het algoritme voorgesteld door Mara en McGuire \cite{mara20122d}.
Hierbij wordt een compacte, omsluitende veelhoek opgesteld voor de geprojecteerde lichtvolumebollen. 

In `nTiled` is hier gekozen voor een omsluitend vierkant. Om dit vierkant op te stellen dienen de
uiterste waarden in de $x$- en $y$-as gevonden te worden. Deze uiterste waardes worden dan 
afgebeeld op het venster. De uiterste waardes kunnen als volgt gevonden worden.
Eerst wordt de bol geprojecteerd op het twee-dimensionale vlak parallel aan de as in kwestie.
Deze situatie is afgebeeld in figuur \ref{fig:ts-projectie}. Vervolgens is het doel
om de waardes $\mathit{t}_a$ en $\mathit{b}_a$ te vinden. Deze waardes zijn gedefinieerd als:

\begin{align*}
  t &= \sqrt{\mathit{c}^2 + \mathit{r}^2} \\
  \cos\theta &= \frac{\mathit{t}}{\mathit{c}} \\
  \sin\theta &= \frac{\mathit{r}}{\mathit{c}} \\
  \hat{\mathbf{\omega}}_{t_a} &=  \begin{pmatrix}\cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}\hat{\mathbf{c}}  \\
  \hat{\mathbf{\omega}}_{b_a} &=  \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\hat{\mathbf{c}}  \\
  t_a &= \mathbf{O} + \hat{\omega}_{t_a} t \\
  b_a &= \mathbf{O} + \hat{\omega}_{b_a} t \\
\end{align*}

vervolgens kunnen de punten $(t_x, t_y)$ en $(b_x, b_y)$ geprojecteerd worden op
het venster met behulp van de perspectiefmatrix van de camera om de uiterste
waarden $\mathbf{t}\prime$ en $\mathbf{b}\prime$ te verkrijgen. 

Om het rooster op te bouwen dient aan elke tegel die overlapt met het vlak 
gedefinieerd door $\mathbf{t}\prime$ en $\mathbf{b}\prime$ een referentie
naar het licht toegevoegd te worden.

Als extra optimalisatie worden lichten die buiten de diepte van het zichtfrustum
vallen niet meegenomen bij het opstellen van het rooster, gezien hier geen
fragmenten kunnen vallen. Indien de berekening uitgevoerd wordt op de GPU en een
dieptebuffer beschikbaar is, kunnen alle lichten die buiten de minimale en 
maximale diepte van fragmenten in de tegel vallen, tevens buiten beschouwing
gelaten worden.\cite{olsson2011tiled}

