# Algoritme {#sec:fds-algorithm}

\input{./img/tex/fds-gbuffer-ntiled.tex}

De voorgestelde opsplitsing van forward shading, weergegeven in listing \ref{lst:fds-algorithm:forward},
leidt tot het volgende algoritme.

* Rasteriseer de geometrie en schrijf de relevante attributen weg naar de GBuffer
* Rasteriseer een vierkant vlak overeenkomend met het gezichtsveld
* Per fragment van dit vlak, bereken de lichtbijdrage van elke licht met dit 
  fragment.
  
Hierbij wordt de renderingspijplijn dus twee maal doorlopen. Eerst om de visibiliteit
te bepalen. Vervolgens om de lichtberekening uit te voeren.
  
Dit proces kan nog verder geoptimaliseerd worden door in te zien dat de lichtvolumes
tevens gerasteriseerd kunnen worden om zo de fragmenten te verkrijgen waarop zij mogelijk
invloed hebben. Voor de fragmenten die geproduceerd worden met een lichtvolume wordt 
de belichtingsberekening uitgevoerd met het corresponderende licht en de geometrie attributen
bepaald in de geometrie stap. Deze bijdrages worden vervolgens gesommeerd in het geheugen
van de grafische kaart. Dit leidt tot het volledige deferred algoritme waarvan de pseudocode
is weergegeven in listing \ref{lst:fds-algorithm:deferred}.

Binnen `nTiled` is deze laatste optimalisatie niet ge\"implementeerd, en is gekozen om 
gebruik te maken van viewport-overdekkend vlak. De forward en deferred algoritmes zonder
extra versnellingsstructuren worden binnen `nTiled` respectievelijk `Forward Attenuated`
en `Deferred Attenuated` genoemd. Voor de GBuffer binnen `nTiled` is gekozen voor drie
texturen, positie, diffuse kleur en de normalen. Een voorbeeld van de diffuus en normaal 
texturen van de GBuffer is weergegeven in figuur \ref{fig:fds-gbuffer-nTiled}.

\input{./lst/fds-algorithm.tex}

