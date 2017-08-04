# Theorie

Zoals vermeld in hoofdstuk \ref{ch:Forward en Deferred Shading}, vereist Deferred
Shading met een stencil-optimalisatie een hoge geheugenbandbreedte, doordat voor
elk licht opnieuw de relevante data uit de GBuffer opgehaald moet worden.
In het geval van Forward Shading, of als er geen stencil-optimalisatie is 
ge\"implementeerd in de Deferred pijplijn, dient voor elk fragment de 
lichtberekening ge\"evalueerd worden voor alle lichten in de scene. Beide 
aanpakken hebben dus significante nadelen.

Tiled Shading is ge\"introduceerd om beide problemen te verlichten\cite{olsson2011tiled}. Binnen Tiled
Shading wordt het zichtveld onderverdeeld in een set van tegels, zoals 
weergegeven in figuur \ref{fig:ts-grid-intro:frame}. Hierdoor wordt het 
zichtfrustum opgedeeld zoals weergegeven in figuur \ref{fig:ts-grid-intro:frustum}.
Voor elk van de tegels wordt vervolgens bepaald welke lichten overlappen met de
tegel. Deze set van lichten kan dan opgehaald worden tijdens de 
belichtingsberekening, en zo het aantal te evalueren lichten beperken.

Doordat het mogelijk is om per fragment direct een set van relevante lichten op
te halen, kan gebruik gemaakt worden van Deferred Shading zonder 
stencil-optimalisatie. Hierdoor hoeft per fragment slechts eenmaal de GBuffer
uitgelezen te worden. Tegelijkertijd blijft het aantal lichten dat ge\"evalueerd
dient te worden tijdens de lichtberekening beperkt. Dit verlaagt de 
geheugenbandbreedte significant. Deze opdeling kan zowel toegepast worden in 
Deferred Shading als Forward Shading. Op deze manier kan dus ook de uitvoeringstijd van
in Forward Shading beperkt worden.

Deze omzetting leidt tot een verschil in lus-structuur tussen Tiled Shading en
Deferred Shading met stencil-optimalisatie. Deferred Shading met stencil 
optimalisatie cree\"ert per licht fragmenten, waardoor de binnenste lus
over pixels loopt. Hierdoor zal per licht de data uit de GBuffer opgehaald 
worden. Tiled Shading en de na\"ive implementaties van Forward en 
Deferred Shading daarentegen cree\"ren eerst de fragmenten, en overlopen
dan de lichten. Hierdoor zal elk fragment slechts eenmalig overlopen worden.
Dus wordt het de GBuffer ook maar \mbox{\'e\'en} keer per fragment aangesproken.
Dit verschil lost het geheugenbandbreedte-probleem op.

Het principe om het zichtveld op te delen, om zo de complexiteit in een sub-veld
te verlagen is geen nieuw idee ge\"introduceerd met Tiled Shading. Zo 
maakte de Pixel-planes 5 computer een vergelijkbaar concept om de geometrie op 
te delen, om zo per sub-vlak het aantal te evalueren polygonen te verlagen\cite{fuchs1989pixel}.
Verschillende Tiled Shading implementaties zijn gebruikt in games\cite{balestra2008technology,andersson2009parallel,swoboda2009deferred}.

