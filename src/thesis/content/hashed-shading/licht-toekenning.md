## Licht toekenning

Nu de verbindingloze octree is opgesteld kan deze gebruikt worden binnen de
licht toekenning. Het berekenen van de relevante lichten voor een fragment 
$\mathbf{p}$ komt neer op een afdaling in de verbindingloze octree. De 
beschrijving van het algoritme zal plaatsvinden aan de hand van de situatie
weergegeven in figuur \ref{fig:hs-licht-toekenning:scene}
Binnen deze scene bevindt zich een fragment $\mathbf{p}$ behorende tot de
kubus in de scene. Verder bevinden drie lampen zich binnen de scene, 
$\lbrace \mathbf{l}_1, \mathbf{l}_2, \mathbf{l}_3 \rbrace$. Voor de set van
lichten is een licht octree opgesteld, gegeven in figuur 
\ref{fig:hs-licht-toekenning:licht-octree}.

\input{./img/tex/hs-licht-toekenning.tex}

Voor elke stap in de afdaling dient eerste de octree beschrijving opgehaald
te worden uit de verbindingloze octree. Deze is gedefinieerd als

\begin{align*}
(\mathtt{is\_leaf}_i, \mathtt{is\_empty}_i) =& H_i\left[ \mathbf{k}_i  + \Phi_i\left[ \mathbf{k}_i \right] \mod \mathit{m}_i  \right] \\
\mathbf{k}_i =& \lfloor*{\mathbf{p^\prime} / \mathit{s}_i}
\end{align*}

Hierbij is $\mathbf{k}_i$ de positie in laag $i$, $\mathbf{p^\prime}$ de positie
van fragment $\mathbf{p}$ ten opzichte van de octree oorsprong 
$\mathbf{O}_\mathtt{octree}$ en $\mathit{s}_i$ de grootte van een knoop in laag
$i$. De waardes $\mathtt{is\_leaf}$ en $\mathtt{is\_empty}$ beschrijven de 
structuur van de hashcluster behorende tot fragment $\mathbf{p}$ en de hash 
clusters die behoren tot dezelfde ouder. Om de relevante waarde voor fragment 
$\mathbf{p}$ te vinden dient eerst vast gesteld te worden tot welk kind
fragment $\mathbf{p}$ behoort. De positie binnen de ouder kan berekend worden 
als:

$$
\mathbf{k}_{\mathtt{local}} = \mathbf{k}_{i + 1} - 2 * \mathbf{k}_{i}
$$

waarbij de bit locatie van fragment $\mathbf{p}$ gesteld kan worden als

$$
\sum_{j=0}^{2} \mathbf{k}_{\mathtt{local}, j} * 2^j
$$

Als laatste kan de relevante bit met behulp van bit schuiven verkregen worden:

```
# bit masking of k-th bit in n
int mask = 1 << k
int masked_n = n & mask
int bit = masked_n >> k
```

Wanneer de waardes $\mathtt{is\_leaf}$ en $\mathtt{is\_empty}$ berekend zijn,
zijn er 3 mogelijkheden:

* De knoop is in laag $i$ een tak knoop, en het hash cluster wordt berekend 
  voor laag $i + 1$.
* De knoop is een niet lege blad knoop. De hash cluster geassocieerd met 
  fragment $\mathbf{p}$ wordt opgehaald uit de data hash tabel geassocieerd met
  laag $i$.
* De knoop is een lege blaad knoop en het hash cluster $(0, 0)$ wordt 
  teruggegeven.
  
Wanneer het hash cluster gevonden is, kan de shading plaats vinden. Dit is exact
hetzelfde als bij tiled en clustered shading.
De pseudo code voor dit algoritme is weergegeven in lst \ref{lst:hs-light-assignment}.
Verder is een illustratie van de bepaling van het relevante hash cluster voor punt
$\mathbf{p}$ weergegeven in figuur \ref{fig:hs-light-assignment-algoritme-p}.

\input{./img/tex/hs-light-assignment-algoritme-p.tex}

In deze sectie is een compleet overzicht gegeven van het hashed shading algoritme
op basis van de verbindingloze octree. In de volgende sectie zal de specifieke 
implementatie in `nTiled` toegelicht worden, waarna de efficientie worden
bepaald aan de hand van de test scenes.

