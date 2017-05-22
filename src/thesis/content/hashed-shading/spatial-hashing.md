## Verbindingloze octree

Nu de lichtoctree opgesteld is, is het mogelijk om deze voor te stellen als
een verbindingloze octree. De structuur van de lichtoctree kan voorgesteld worden
zoals beschreven in sectie \ref{sec:theorie-verbindingloze-octree}.

Naast de structuur dient tevens, per gevulde bladknoop, bijgehouden te worden
welke lichten van invloed zijn op de corresponderende ruimte. Omdat de gevulde
bladknopen slechts een kleine subset van alle knopen zijn is er gekozen om deze
data op te slaan in aparte hashtabellen. Hierbij is gekozen voor een
vergelijkbare aanpak als in Tiled en Clustered shading. Er zijn drie verschillende
datastructuren gespecificeerd: 

* Een lijst van alle lichten in de scene.
* Een lijst van lichtindices
* De data-hashtabellen

De lijst van lichtindices bestaan uit integers die wijzen naar specifieke lichten
in de lichtlijst. De data-hashtabellen bevat vervolgen per volle bladknoop in een
laag een vector van twee integers. De eerste integer specificeert een beginpunt
in de lichtindexlijst. De tweede integer specificeert het aantal lichten behorende
bij de gevulde bladknoop. Op deze manier wordt een subset van de lichtindexlijst
gespecificeerd. Deze subset komt overeen met alle indices relevant voor de 
gevulde bladknoop. Deze datastructuren zijn ge\"illustreerd in figuur 
\ref{fig:hs-verbindingloze-octree-algoritme}

\input{./img/tex/hs-verbindingloze-octree-algoritme.tex}

Wanneer een laag bestaat uit slechts een klein aantal knopen, zal de voorstelling
als spatiale hashfunctie relatief veel geheugen gebruiken, door de overhead van 
de texturen. Om deze reden worden veelal de eerst $i$ lagen niet expliciet voorgesteld
maar samengenomen in de eerste voorgestelde laag.

Het algoritme om een lichtoctree om te zetten naar een verbindingloze octree kan
dan als volgt worden voorgesteld.

* Haal alle knopen uit de lichtoctree op behorende tot laag $j$, waarbij
  bladknopen in laag $j^\prime < j$ worden opgesplits in kleinere bladknopen.
  
* Voor elke knoop in laag $j$, bereken de octreetabelwaarde, gespecificeerd als:

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

* Indien een kind van een knoop in laag $j$
    * een takknoop is: Voeg deze toe aan de lijst van takknopen van laag $j+1$.
    * een gevulde bladknoop is: Voeg deze toe aan de lijst van bladknopen van laag $j$.
    
* Bouw de octreetabel voor alle octree knopen

* Voor alle bladknopen bepaal de datatabelwaarde gespecificeerd als:

  $$  \mathtt{data\_node} = (\mathtt{len}(\mathtt{light_indices}), \mathtt{len}(\mathtt{node.indices})) $$
  
  vervolgens worden de knoopindices toegevoegd aan de lijst van lichtindices.
  
* Bouw de datatabel voor alle data knopen

* Herhaal totdat de volgende laag geen takknopen meer bevat.

Na uitvoering zijn $n$ octreetabellen, $m\leq n$ datatabellen en een lichtindexlijst
opgesteld. Deze kunnen op de GPU geladen worden en gebruikt worden in de shaders.

