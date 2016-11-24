## Geometrische definities

Voordat het mogelijk is om drie dimensionale omgevingen om te zetten naar
afbeeldingen is het nodig om een beschrijving van deze scenes te hebben. 
De basis render primitieven die gebruikt worden door de meeste grafische 
hardware zijn punten, lijnen en driehoeken. Een punt wordt beschreven met 
homogene coordinaten:  

$$ \mathbf{v} = \begin{pmatrix} \mathit{v_x} \\ \mathit{v_y} \\ \mathit{v_z} \\ \mathit{v_w} \end{pmatrix} $$

Indien gesproken wordt van primitieven zal, als niet anders is aangegeven, 
gedoeld worden op driehoeken. De notatie voor een driehoek is:  

$$ \bigtriangleup\mathbf{v_1}\mathbf{v_2}\mathbf{v_3} $$

\input{./img/tex/gd-object.tex}

Een *mesh* is een collectie van driehoeken die samen de vorm van een object 
vormen. Een *object* bevat zowel een *mesh* als een transformatie matrix die die
de locatie, schaal, en rotatie van het *object* vastlegt. De verschillende 
geometrische definities zijn geillustreerd in figuur \ref{fig:gd-object}. De 
volledige beschrijving van een virtuele omgeving zal een *scene* genoemd worden.
Deze bevat een set van objecten, de lichten, en eventuele definities van 
gezichtspunten.  

