\input{./img/tex/fds-scene.tex}

Binnen sectie \ref{sec:moderne-grafische-pipeline} is vastgesteld dat bij standaard
uitvoering, pas na uitvoering van de fragment shader wordt bepaald welke
fragmenten daadwerkelijk zichtbaar zijn. Dit betekent dat ook voor fragmenten
die geen enkele invloed zullen hebben op de scene, de shading berekening worden
uitgevoerd. De shading complexiteit is dus direct gekoppeld aan de scene
complexiteit. Voor simpele scenes is dit geen probleem, echter wanneer scenes
complexer worden kan dit leiden tot een grote mate van verspilde rekenkracht.
Een simpel voorbeeld van een dergelijke scene, waar belichtingsberekening
onnodig worden uitgevoerd is weergegeven in figuur \ref{fig:fds-scene}.  

Een logische stap om dit probleem op te lossen is het ontkoppelen van
visibiliteit en shading. Dit leidt tot twee discrete stappen, een 
visibiliteitsstap waar rasterisatie plaats vindt en de informatie van de
zichtbare fragmenten als uitvoer wordt gegeven.  

In de volgende secties zal eerst de theorie toegelicht worden, vervolgens
zal ingegaan worden op de implementatie binnen `nTiled` en de testen 
die zijn uitgevoerd.

