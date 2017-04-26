## Verbindingloze octree

Nu de licht octree opgesteld is, is het mogelijk om deze voor te stellen als
een verbindingloze octree. De structuur van de licht octree kan voorgesteld worden
volgens de standaard beschrijving zoals weergegeven in sectie /ref{sec:theorie-verbindingloze-octree} .
De constructie zal het constructie algoritme hier volgen.

Naast de structuur van de octree dient tevens de data gemodeleerd worden in deze
verbindingloze octree. Zoals eerder vermeld bevat elke gevulde blad knoop een
set van lichten die van invloed zijn op het volume dat de blad knoop beschrijft. 
Vergelijkbaar met tiled en clustered shading, kunnen de relevante lichten 
beschreven worden met een reeks licht indices die in een lijst worden bijgehouden.
De reeks kan gespecificeerd worden met een offset, en een lengte van de reeks
binnen deze licht index lijst. De data kan vervolgens, vergelijkbaar met de
tiled en clustered shading worden voorgesteld aan de hand van twee integers, 
die deze offset en lengte definieren.

Doordat het aantal knopen met data slechts een kleine subset van het totaal
aantal knopen is, is er gekozen om deze data los van de octree representatie
op te slaan. Dit leidt ertoe dat er per laag twee ruimtelijke hash functies
zijn gedefinieerd. De volledige representatie van de datastructuren is 
weergegeven in figuur \ref{fig:hs-verbindingloze-octree-algoritme}

\input{./img/tex/hs-verbindingloze-octree-algoritme.tex}

Belangrijk hierbij is dat het geheugen gebruik om een laag voor te stellen
veelal relatief groter is bij kleine lagen. Om deze reden worden de eerste
lagen veelal niet expliciet voorgesteld, maar worden de knopen pas vanaf
laag $i$ voorgesteld als eerste ruimtelijke hash functie. Dit leidt tot een
compactere voorstelling en verlaagd tevens het aantal iteraties dat uitgevoerd
dient te worden om een gehashed cluster te berekenen, doordat direct vanaf
laag $i$ gestart kan worden.

Het algoritme om elke laag weer te geven kan recursief worden opgesteld;
gegeven een set $S$ van knopen van de huidige laag van de licht octree, 
en een lijst van licht indices. 
Voor elke knoop wordt de verbindingloze octree voorstelling berekend,
deze is gedefinieerd als


\begin{align*}
\mathtt{octree\_node}_i \mathop{:=}& \left( \sum_{k=0}^7 \mathtt{is\_leaf}(\mathtt{sub\_node}_k) \times 2^k, \sum_{k=0}^7 \mathtt{is\_empty}(\mathtt{sub\_node}_k) \times 2^k \right) \\
\mathtt{is\_leaf}(\mathtt{node}) =&
\begin{cases}
  1 & : \mathtt{node} \text{ is een blad knoop.}\\
  0 & : \text{anders}
\end{cases}\\
\mathtt{is\_empty}(\mathtt{node}) =&
\begin{cases}
  1 & : \mathtt{node} \text{ is geen blad knoop, of bevat minimaal 1 relevant licht.} \\
  0 & : \text{anders}
\end{cases}
\end{align*}

Verder wordt indien een kind geen blad knoop is deze toegevoegd aan de lijst van
knopen voor de volgende laag. Indien een kind een niet lege blad knoop is, wordt
de hashed cluster berekend. Voor de huidige lengte van licht indices

```
hashed_cluster = (len(light_indices), len(node.indices))
```

vervolgends worden de indiices van deze knoop toegevoegd aan de lijst van licht
indices. Voor de set van octree structuur knopen en voor de set van hashed clusters
wordt elk een ruimtelijke hash functie berekend. 
Deze stappen worden herhaald voor de knopen van de volgende laag. Dit wordt gedaan
totdat de set van knopen van de volgende laag leeg is.
De pseudo code hiervan is gedefinieerd in lst. \ref{lst:licht_octree_constructie}.

