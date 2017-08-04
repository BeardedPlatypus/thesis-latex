## Rasterisatie

Rasterisatie algoritmes lossen de perspectiefprojectie en het 
visibiliteitsprobleem op in een omgekeerde volgorde ten opzichte van
de raytracingalgoritmes. Waar raytracing uitgaat van het punt 
$\mathbf{p'}$ op de canvas en kijkt welk object hier op valt, begint een rasterisatiealgoritme 
met het afbeelden van punten in de ruimte op de canvas, om vervolgens te 
bepalen op welke pixels deze objecten invloed hebben. In dit geval wordt 
uitgegaan van de punten $\mathbf{p}$ en worden de punten $\mathbf{p'}$
gevonden. Waar raytracing-algoritmes dus beeldcentrisch zijn, zijn rasterisatie-algoritmes 
objectcentrisch. Hierbij wordt in de buitenste lus over alle 
objecten gelopen. En daarna per object gekeken welke pixels door dit object 
worden be\"invloed. Dit leidt tot de volgende pseudocode:  

\begin{minted}[frame=single,framesep=12pt]{python}
for object in canvas:
    projection = project(object, eye)
    
    for pixel in projection:
        do_shading(pixel, object)
\end{minted}

\input{./img/tex/rs-rasterisatie.tex}

\noindent Dit is tevens afgebeeld in figuur \ref{fig:rs-rasterisatie}. 

Om een enkele primitief dus af te beelden op het canvas dient eerst, voor elke
hoek van dit primitief de perspectief deling uitgevoerd te worden. Hierna dient 
het resultaat omgezet te worden naar rasterruimte, zodat de punten binnen 
pixels vallen. Vervolgens dienen de pixels overlopen te worden, om na te gaan 
of deze binnen of buiten het object valt of niet.  Dit leidt uiteindelijk tot 
een set van $\mathbf{p'}$, i.e. een set van pixels, die behoren tot het object. 
Om deze pixels effici\"ent te overlopen, wordt meestal een omsluitend vierkant in 
rasterruimte gecre\"eerd. Slechts voor de pixels binnen dit vierkant wordt 
nagegaan of het object overlapt met de pixels of niet. Dit is weer gegeven in figuur \ref{fig:rs-rasterisatie:2}  

Hiermee is vastgesteld dat de oplossing voor de perspectiefprojectie bestaat
uit twee simpele stappen, die goedkoop uit te rekenen zijn. Echter, dit 
lost nog niet het visibiliteitsprobleem op, doordat het mogelijk is dat 
verschillende objecten op het punt $\mathbf{p'}$ worden afgebeeld.
Om het visibiliteitsprobleem op te lossen zijn verschillende algoritmes 
voorgesteld\cite{Sutherland:1974:CTH:356625.356626}. 

Het visibiliteitsprobleem wordt in grafische kaarten opgelost met behulp van een zogenoemd z-buffer algoritme
Zoals opgemerkt bij de bespreking van het visibiliteitsprobleem, is dit 
intrinsiek een sorteerprobleem, waarbij objecten geordend dienen te worden
ten opzichte van de kijk-as in cameraco\"ordinaten, de camera-$\mathbf{z}$-as. 
Om het zichtbare object binnen
een punt $\mathbf{p'}$ te bepalen, dient dus bepaald te worden welk object
de kleinste $\mathbf{z}$-as waarde heeft ten opzichte van het oogpunt.
De oplossing voor dit probleem is dan ook simpel. Voor elke pixel wordt de 
kleinste gevonden $\mathbf{z}$-as waarde bijgehouden in een corresponderende 
twee dimensionale array. Deze array wordt een z-buffer, of een diepte-buffer
(depth-buffer) genoemd. Wanneer een pixel gevonden wordt met een kleinere 
$\mathbf{z}$-waarde, wordt zowel het object in punt $\mathbf{p'}$ als de nieuwe 
diepte bijgewerkt. Wanneer alle objecten overlopen zijn zal er dus per pixel 
bekend zijn welke objecten gebruikt dienen te worden om de shading berekening 
uit te voeren.  

