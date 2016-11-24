## Rasterisatie

Rasterisatie algoritmes lossen perspectief projectie en het 
visibiliteitsprobleem op een verschillende volgorde op dan hoe het binnen 
raytracing algoritmes wordt opgelost. Waar raytracing uitgaat van het punt 
$\mathbf{p'}$ en kijkt welk object hier op valt, begint een rasterisatie 
algoritme met het afbeelden van alle objecten op de canvas, om vervolgens te 
bepalen op welke pixels deze objecten invloed hebben. In dit geval wordt 
uitgegaan van de punten $\mathbf{p}$ en worden de punten $\mathbf{p'}$
gevonden. Waar raytracing algoritmes dus beeld centrisch zijn, zijn rasterisatie
algoritmes object centrisch. Hierbij wordt in de buitenste loop over alle 
objecten gelopen. En daarna per object gekeken welke pixels door dit object 
worden beinvloedt. Dit leidt tot de volgende pseudo code:  

```
for object in canvas:
    projection = project(object, eye)
    
    for pixel in projection:
        do_shading(pixel, object)
```

\input{./img/tex/rs-rasterisatie.tex}

Dit is tevens afgebeeld in figuur \ref{fig:rs-rasterisatie}. 

Om een enkele primitief dus af te beelden op het canvas dient eerst, voor elke
hoek van dit primitief de perspectief deling uitgevoerd te worden. Hierna dient 
het resultaat omgezet te worden naar raster-ruimte, zodat de punten binnen 
pixels vallen. Vervolgens dienen de pixels overlopen te worden, om na te gaan 
of deze binnen of buiten het object valt of niet.  Dit leidt uiteindelijk tot 
een set van $\mathbf{p'}$, i.e. een set van pixels, die behoren tot het object. 
Om deze pixels efficient te overlopen, wordt meestal een bounding box in 
raster-ruimte gecreeerd. Slechts voor de pixels binnen deze bounding box wordt 
nagegaan of het object behoort tot hen of niet. Dit is weer gegeven in figuur 
...  

Hiermee is vastgesteld dat de oplossing voor de perspectief projectie bestaat
uit twee simpele stappen, die goedkoop uit te rekenen zijn. Echter, dit 
lost nog niet het visibiliteitsprobleem op, doordat het mogelijk is dat 
verschillende objecten op het punt $\mathbf{p'}$ worden afgebeeld.
Om het visibiliteitsprobleem op te lossen zijn verschillende algoritmes 
voorgesteld. In het volgende stuk zal het z-buffer algoritme besproken worden.
Dit is het algoritme waar grafische kaarten gebruik van maken, en is daarom 
van belang.  

Zoals opgemerkt bij de bespreking van het visibiliteitsprobleem, is dit 
intrinsiek een sorteer probleem, waarbij objecten geordend dienen te worden
ten opzichte van de kijkas, de $\mathbf{z}$-as. Om het zichtbare object binnen
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

