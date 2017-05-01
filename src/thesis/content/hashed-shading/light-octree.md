## Licht octree

\input{./img/tex/hs-licht-octree.tex}

De lichtoctree beschrijft de octree-representatie van de set van alle lichten
binnen de scene. Een illusttratie van een lichtoctree is te vinden in figuur
\ref{fig:hs-licht-octree}. Elke bladknoop bevat een lijst van lichten waarvan 
het lichtvolume (gedeeltelijk) overlapt met de bladknoop. Hierdoor is het 
mogelijk om de set van relevante lichten voor een punt $\mathbf{p}$ te beperken 
van de set van alle lichten binnen de scene, tot de set van lichten die 
opgeslagen is in de bladknoop waartoe punt $\mathbf{p}$ behoort. 

De lichtoctree volgt de standaard pointer implementatie zoals beschreven is in 
sectie \ref{sec:octree}. Voordat deze bruikbaar is binnen de grafische kaart, 
dient de lichtoctree eerst omgezet te worden naar een verbindinglozeoctree 
voorstelling.

Om de lichtoctree voor een scene te construeren is de volgende informatie nodig:

* De set van lichten die zich bevindt in de scene
* Een grootte voor de ribben van de kleinst mogelijke bladknoop

De oorsprong van de octree is gedefinieerd als het punt met de grootst mogelijke 
dimensies waarvoor geldt dat er geen lichtvolumes kleiner zijn dan dit punt.

$$ 
\begin{split} 
\mathbf{p_o} := \mathbf{p} - b : \quad ( \forall \mathbf{l} \in S & p.x < l.p.x - l.r \land \\
                                                            & p.y < l.p.y - l.r \land \\
                                                            & p.z < l.p.z - l.r )\land \\
                            (\not \exists \mathbf{p^\prime} & ( p^\prime.x > p.x \lor \\ 
                                                            &   p^\prime.y > p.y \lor \\
                                                            &   p^\prime.z > p.z ) \land \\
                                 ( \forall \mathbf{l} \in S & p^\prime.x < l.p.x - l.r \land \\
                                                            & p^\prime.y < l.p.y - \l.r \land \\
                                                            & p^\prime.z < l.p.z -  l.r )) 
\end{split}
$$

Waarbij $\mathbf{p_0}$ de oorsprong van de lichtoctree is $b$ een offset-waarde
is om afrondingsfouten te voorkomen.

Nadat de oorsprong is vastgesteld kan voor elk licht de corresponderende enkele
lichtboom worden opgesteld. Deze lichtbomen zullen vervolgens iteratief worden
toegevoegd aan aan een lichtoctree ge\"initialiseerd met een lege bladknoop.

Het toevoegen van een enkele lichtboom vindt plaats in twee stappen. Eerst wordt
afgedaald in de lichtoctree totdat de octreeknoop overeenkomend met de wortel 
van de enkele lichtboom is bereikt. Indien een bladknoop wordt tegengekomen
wordt deze vervangen met een takknoop waarvan de kinderen dezelfde lichten 
bevatten als de bladknoop die vervangen wordt. 
Vervolgens wordt de wortel van de enkele lichtboom toegevoegd aan de bereikte
octree knoop. Elke keer dat een lichtboomknoop wordt toegevoegd aan een 
octreeknoop zijn er vijf mogelijke situaties. Deze zijn weergegeven in tabel
\ref{tbl:hs-lichtoctree}. 

\input{./tbl/hs-lichtoctree.tex}


