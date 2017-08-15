# Algoritme {#sec:fds-algorithm}

\input{./img/tex/fds-gbuffer-ntiled.tex}

De voorgestelde opsplitsing van Forward Shading, weergegeven in listing \ref{lst:fds-algorithm:forward},
leidt tot het volgende algoritme.

* Rasteriseer de geometrie en schrijf de relevante attributen weg naar de GBuffer.
* Rasteriseer een vierkant vlak overeenkomend met het gezichtsveld.
* Per fragment van dit vlak, bereken de lichtbijdrage van elke lichtbron met dit fragment.
  
\noindent Hierbij wordt de renderpijplijn dus twee maal doorlopen. Eerst om de visibiliteit
te bepalen, vervolgens om de lichtberekening uit te voeren\cite{akenine2016real}.
  
Dit proces kan nog verder geoptimaliseerd worden door in te zien dat de lichtvolumes
tevens gerasteriseerd kunnen worden om zo de fragmenten te verkrijgen waarop zij mogelijk
invloed hebben\cite{lengyel2002mechanics}. Voor de fragmenten die geproduceerd worden met een lichtvolume wordt 
de lichtberekening uitgevoerd met de corresponderende lichtbron en de geometrie attributen
bepaald in de geometriestap. Deze bijdrages worden vervolgens gesommeerd in het geheugen
van de grafische kaart. Dit leidt tot het volledige deferred algoritme waarvan de pseudocode
is weergegeven in listing \ref{lst:fds-algorithm:deferred}.

Binnen `nTiled` is deze laatste optimalisatie niet ge\"implementeerd, en is gekozen om 
gebruik te maken van zichtveldoverdekkend vlak. De Forward en Deferred Shading algoritmes zonder
extra versnellingsstructuren worden binnen `nTiled` respectievelijk `Forward Attenuated`
en `Deferred Attenuated` genoemd. Voor de GBuffer binnen `nTiled` is gekozen voor drie
texturen waarin drie attributen worden opgeslagen: de diffuse kleur, de normaal en de diepte. 
Een voorbeeld van deze texturen van de GBuffer is weergegeven in Figuur \ref{fig:fds-gbuffer-nTiled}.

\input{./lst/fds-algorithm.tex}

