## Licht octree

\input{./img/tex/hs-licht-octree.tex}

De licht octree beschrijft de volledige set van lichten binnen een scene.
Hierbij wordt binnen een blad knoop bijgehouden met welke licht volumes 
de knoop gedeeltelijk overlapt. Dit is weergeven in figuur \ref{fig:hs-licht-octree}.
Vanuit de licht octree kan de verbindingloze octree worden opgesteld. 
Tevens kan met behulp van de licht octree en de set van enkele licht bomen, 
de invloed van veranderingen van dynamische lichten op het de verbindingloze
octree berekend worden.

Voor de constructie van een licht octree is de set $S$ van lichten nodig, 
en dient grootte $l_{\mathtt{node}}$ van de blad knopen gespecificeerd te worden.
Op basis van de set van lichten wordt de oorsprong van de octree berekend. 
Deze is gespecificeerd als de grootste waarde waarvoor geldt dat er geen licht volumes
bevinden op punten die kleiner zijn dan de oorsprong.

$$ 
\begin{split} 
\mathbf{p_o} := \mathbf{p} - b : ( \forall \mathbf{l} \in S & \mathbf{p}.x < \mathbf{l}.p.x - \mathbf{l}.r \land \\
                                                            & \mathbf{p}.y < \mathbf{l}.p.y - \mathbf{l}.r \land \\
                                                            & \mathbf{p}.z < \mathbf{l}.p.z - \mathbf{l}.r )\land \\
                            (\not \exists \mathbf{p^\prime} & ( \mathbf{p^\prime}.x > \mathbf{p}.x \lor \\ 
                                                            &   \mathbf{p^\prime}.y > \mathbf{p}.y \lor \\
                                                            &   \mathbf{p^\prime}.z > \mathbf{p}.z ) \land \\
                                 ( \forall \mathbf{l} \in S & \mathbf{p^\prime}.x < \mathbf{l}.p.x - \mathbf{l}.r \land \\
                                                            & \mathbf{p^\prime}.y < \mathbf{l}.p.y - \mathbf{l}.r \land \\
                                                            & \mathbf{p^\prime}.z < \mathbf{l}.p.z - \mathbf{l}.r )) 
\end{split}
$$

Het is nu mogelijk om voor elk licht een enkele lichtboom op te stellen. Deze
worden vervolgens iteratief toegevoegd aan een octree geinitialiseerd met eenkele
lege blad knoop.

Het toevoegen van de enkele lichtbomen vindt plaats in twee stappen. Eerst 
wordt afgedaald in de licht octree tot de begin knoop van de enkele lichtboom. 
Indien een blad knoop wordt tegen gekomen, wordt deze vervangen met een lege 
tak knoop. Wanneer vervolgens de begin knoop van de enkele lichtboom bereikt is wordt
de wortel knoop $\mathbf{l}$ recursief toegevoegd aan de huidige licht octree knoop 
$\mathbf{o}$. Hierbij zijn de volgende vijf situaties mogelijk.

* De enkele licht boom $\mathbf{l}$ is een lege blad knoop: het algoritme stopt.
* De enkele licht boom $\mathbf{l}$ is een niet lege blad knoop:
      * De knoop in de licht octree $\mathbf{o}$ is een blad knoop: het licht 
        van $\mathbf{o}$ wordt toegevoegd aan $\mathbf{o}$.
      * De knoop in de licht octree $\mathbf{o}$ is een tak knoop: $\mathbf{o}$
        wordt toegevoegd aan elk van de kinderen van $\mathbf{o}$. 
* De enkele licht boom $\mathbf{l}$ is een tak knoop:
      * De knoop in de licht octree $\mathbf{o}$ is een blad knoop: $\mathbf{o}$
        wordt vervangen met een tak knoop waarbij elk van de kinderen dezelfde 
        lichten als $\mathbf{o}$ bevat.
      * De knoop in de licht octree $\mathbf{o}$ is een tak knoop: De kinderen 
        van $\mathbf{l}$ worden aan de overeenkomstige kinderen van $\mathbf{o}$
        toegevoegd. 

Dit algoritme is weergegeven in lst \ref{lst:hs-octree-constructie}.


