## Geometrische definities {#sec:geometrische-def}

\input{./img/tex/gd-object.tex}

Om een afbeelding te cre\"eren van een virtuele drie dimensionale omgeving,
is het in de eerste plaats nodig om een beschrijving te hebben van deze omgeving.
Om een omgeving voor te stellen wordt een set van primitieven gedefinieerd. 
Deze primitieven maken het mogelijk om een beschrijving te geven van elk object
binnen de \mbox{sc\`ene}. De basis renderprimitieven die gebruikt worden in grafische 
render-hardware zijn punten, lijnen en driehoeken. 
Een enkel punt kan beschreven worden in homogene co\"ordinaten als: 

$$ \mathbf{v} = \begin{pmatrix} \mathit{v_x} \\ \mathit{v_y} \\ \mathit{v_z} \\ \mathit{v_w} \end{pmatrix} $$

\noindent Door middel van twee en drie punten kunnen respectievelijk lijnen en driehoeken
voorgesteld worden. Een driehoek wordt genoteerd als: 

$$ \bigtriangleup\mathbf{v_1}\mathbf{v_2}\mathbf{v_3} $$

Wanneer gesproken wordt binnen deze thesis over primitieven, zal, indien niet 
anders aangegeven, gedoeld worden op driehoeken. Met behulp van driehoeken is 
het mogelijk om de geometrie van alle objecten in een \mbox{sc\`ene} te beschrijven.
Dit proces is weergegeven in figuur \ref{fig:gd-object}. Door een collectie van
verschillende driehoeken te nemen, wordt een *mesh* gevormd. Een *mesh* 
beschrijft het oppervlakte van een object. 
Vervolgens wordt een *object* gedefinieerd door middel
van een referentie naar een *mesh* en een transformatiematrix $\mathbf{A}$. 
Deze transformatiematrix beschrijft de locatie, schaal en rotatie van de *mesh*
van het *object* binnen de drie dimensionale wereld. Hierdoor is het mogelijk
om meerdere objecten op verschillende plekken in de wereld voor te stellen met
dezelfde *mesh* en een verschillende matrix. Een voorbeeld van een set van 
vier objecten met dezelfde mesh maar verschillende transformatiematrices is
weergegeven in figuur \ref{fig:gd-object}.

De volledige beschrijving van een omgeving zal een *\mbox{sc\`ene}* genoemd worden. Deze
bevat de definities van de verschillende objecten binnen de wereld, als ook 
de lichten en eventuele camera's en zichtspunten.

