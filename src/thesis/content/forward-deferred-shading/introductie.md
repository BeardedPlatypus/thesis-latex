\input{./img/tex/fds-scene.tex}

Binnen sectie \ref{sec:moderne-grafische-pipeline} is vastgesteld dat bij 
standaard uitvoering, pas na uitvoering van de fragment shader wordt bepaald 
welke fragmenten daadwerkelijk zichtbaar zijn. Dit betekent dat ook voor 
fragmenten die niet zichtbaar zijn in de gerenderde frame de belichtingsberekening 
wordt uitgevoerd. De shading complexiteit is dus direct gekoppeld
aan de geometrische complexiteit van de scene. Voor simpele scenes is dit geen 
probleem. Echter wanneer scenes complexer worden, leidt dit tot verspilde
rekenkracht. Een simpel voorbeeld van een dergelijke scene, waar  de
belichtingsberekening onnodig wordt uitgevoerd is weergegeven in figuur 
\ref{fig:fds-scene}. Elk van de bollen cree\"ert fragmenten die niet zichtbaar
zijn. Het aantal fragmenten dat per pixel gecree\"erd wordt, is visueel weergegeven 
in de warmtekaart, fig. \ref{fig:fds-scene:heatmap}.  

Een logische stap om dit probleem op te lossen, is het ontkoppelen van
visibiliteit en shading. Dit leidt tot twee discrete stappen, een 
visibiliteitsstap waar rasterisatie plaats vindt en de informatie van de
zichtbare fragmenten als uitvoer wordt gegeven en een renderstap, waar de 
informatie van de zichtbare fragmenten opnieuw wordt ingelezen, en de 
belichtingsberekening wordt uitgevoerd.  

In de volgende secties zal eerst de theorie toegelicht worden, vervolgens
zal ingegaan worden op het algoritme en de implementatie binnen `nTiled`.
Als laatste zal de effectiviteit behandeld worden aan de hand van uitgevoerde
testen.

