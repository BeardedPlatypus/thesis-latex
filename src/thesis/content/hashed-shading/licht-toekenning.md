## Licht toekenning

Nu de verbindingloze octree is opgesteld kan deze gebruikt worden voor de
lichttoekenning. Het berekenen van de relevante lichten voor een fragment 
$\mathbf{p}$ komt neer op een afdaling in de verbindingloze octree. 
Voor elke stap in de afdaling dient eerste de octree beschrijving opgehaald
te worden uit de verbindingloze octree. Deze is gedefinieerd als

\begin{align*}
(\mathtt{is\_leaf}_i, \mathtt{is\_empty}_i) =& H_i\left[ \mathbf{k}_i  + \Phi_i\left[ \mathbf{k}_i \right] \mod \mathit{m}_i  \right] \\
\mathbf{k}_i =& \lfloor*{\mathbf{p^\prime} / \mathit{s}_i}\rfloor
\end{align*}

Hierbij is $\mathbf{k}_i$ de positie in laag $i$, $\mathbf{p^\prime}$ de positie
van fragment $\mathbf{p}$ ten opzichte van de octree oorsprong 
$\mathbf{O}_\mathtt{octree}$ en $\mathit{s}_i$ de grootte van een knoop in laag
$i$. De waardes $\mathtt{is\_leaf}$ en $\mathtt{is\_empty}$ beschrijven de 
structuur van de hashcluster behorende tot fragment $\mathbf{p}$ en de 
hashclusters die behoren tot dezelfde ouder. Om de relevante waarde voor fragment 
$\mathbf{p}$ te vinden dient eerst vastgesteld te worden tot welk kind
fragment $\mathbf{p}$ behoort. De positie binnen de ouder kan berekend worden 
als:

$$
\mathbf{k}_{\mathtt{local}} = \mathbf{k}_{i + 1} - 2 * \mathbf{k}_{i}
$$

waarbij de bit locatie van fragment $\mathbf{p}$ gesteld kan worden als

$$
\sum_{j=0}^{2} \mathbf{k}_{\mathtt{local}, j} * 2^j
$$

Als laatste kan de relevante bit met behulp van bitverschuivingen verkregen worden:

\begin{minted}{glsl}
# bit masking of k-th bit in n
int mask = 1 << k
int masked_n = n & mask
int bit = masked_n >> k
\end{minted}

Wanneer de waardes $\mathtt{is\_leaf}$ en $\mathtt{is\_empty}$ berekend zijn,
zijn er 3 mogelijkheden:

* De knoop in laag $i$ is een tak knoop, en de hashcluster wordt berekend 
  voor laag $i + 1$.
* De knoop is een niet lege bladknoop. De hashcluster geassocieerd met 
  fragment $\mathbf{p}$ wordt opgehaald uit de datahashtabel geassocieerd met
  laag $i$.
* De knoop is een lege bladknoop en het hashcluster $(0, 0)$ wordt 
  teruggegeven.
  
Wanneer het hash cluster gevonden is, kan de shading plaats vinden. Dit is exact
hetzelfde als bij Tiled en Clustered shading.
De pseudo code voor dit algoritme is weergegeven in lst \ref{lst:hs-lichttoekenning}.
Verder is een illustratie van de bepaling van het relevante hash cluster voor punt
$\mathbf{p}$ weergegeven in figuur \ref{fig:hs-light-assignment-algoritme-p}.

\input{./img/tex/hs-light-assignment-algoritme-p.tex}

In deze sectie is een compleet overzicht gegeven van het hashed shading algoritme
op basis van de verbindingloze octree. In de volgende sectie zal de effici\"entie
worden bepaald aan de hand van de test scenes.

\input{./lst/hs-lichttoekenning.tex}

