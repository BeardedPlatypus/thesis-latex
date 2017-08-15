# Moderne Grafische Pijplijn {#sec:moderne-grafische-pipeline}

De voorgaande secties hebben een grof overzicht gegeven van zowel de problemen
als oplossingen binnen het renderen van afbeeldingen. Het onderzoek binnen deze
thesis richt zich op het realtime renderen. Het onderliggende gereedschap
verantwoordelijk voor het renderen van de afbeeldingen is de realtime grafische
pijplijn. In deze sectie zal eerst conceptueel de opbouw van de grafische 
pijplijn beschreven worden, zoals gegeven in Real-Time Rendering (3rd edition)\cite{akenine2016real}.
Hierna zal in meer detail de `openGL` implementatie 
besproken worden, waarop het onderzoek binnen deze thesis is gebouwd.  

## Conceptuele architectuur

In de fysieke wereld is een pijplijn een verzameling van stappen die in 
parallel uitgevoerd kunnen worden. Elke stap transformeert de uitkomst van de 
vorige stap in een volgende uitkomst. Voor een individuele uitkomst zal dus
elke stap in de pijplijn uitgevoerd moeten worden, echter doordat alle stappen
per uitvoering in parallel worden uitgevoerd zal een uitkomst gegenereerd
worden per uitvoering. Deze parallellisatie van stappen verhoogt dus de doorvoersnelheid.
De tijd om alle stappen eenmaal uit te voeren, zal dan ook gelijk zijn aan
de traagste stap.
De grafische pijplijn is op een vergelijkbare manier opgebouwd en kan grofweg
onderverdeeld worden in drie conceptuele stappen.

* Applicatiestap  
* Geometriestap  
* Rasterisatiestap  

### Applicatiestap

De applicatiestap beschrijft alle berekeningen die plaatsvinden binnen de 
applicatie van de ontwikkelaar. Belangrijke aspecten hier zijn onder andere de 
verwerking van invoer van gebruikers, het opzetten van datastructuren en
botsingdetectie. Aan het einde van de applicatiestap dient een 
verzameling primitieven gestuurd te worden naar de geometriestap.  

### Geometriestap

De geometriestap is verantwoordelijk voor het merendeel van de per-polygon 
operaties. Deze stap kan verder onderverdeeld worden in de volgende sub-stappen: 

* Model- en zichtstransformaties
* Vertex shading
* Projectie
* Clipping
* Canvas afbeelding

\noindent Belangrijk hierbij is dat de conceptuele beschrijving in sommige opzichten 
kan verschillen van daadwerkelijke implementaties als `openGL` en `Direct3D`.  

De geometriestap zorgt dat objecten geproduceerd door de applicatiestap, 
omgezet worden naar een verzameling van data die in de rasterisatiestap omgezet 
kan worden in een daadwerkelijke afbeelding. 
Eerst worden objecten getransformeerd opdat dat alle primitieven zich in 
hetzelfde co\"ordinatensysteem bevinden. 
Hierna vindt een eerste shadingstap plaats die wordt uitgevoerd voor alle
vertices van alle primitieven. Nadat de shading berekend is per vertex, wordt de 
perspectiefprojectie uitgevoerd en worden niet zichtbare objecten 
weggesneden uit het resultaat. Als laatste worden de primitieven die over zijn
omgezet naar canvas-co\"ordinaten. De verzameling van primitieven in canvas-co\"ordinaten, 
en corresponderende shadingdata wordt vervolgens doorgestuurd naar de rasterisatiestap.  

### Rasterisatiestap

In de rasterisatiestap worden de daadwerkelijke kleuren van de afbeelding
berekend. Hiervoor wordt een rasterisatiealgoritme uitgevoerd. 
De volgende sub-stappen kunnen onderscheden worden:

* Driehoekopzet
* Driehoekdoorkruizing
* Pixel-shading
* Samenvoeging

\noindent De eerste twee stappen komen \mbox{over\'e\'en} met het rasterisatie-algoritme. Hierbij 
wordt shadingdata uit de geometrie stap ge\"interpoleerd. Dit leidt tot een verzameling
van fragmenten met geassocieerde ge\"interpoleerde shadingdata. 
Deze worden met behulp van pixel-shading verwerkt tot een specifieke kleur 
voor een specifieke pixel. Als laatste wordt door middel van het z-buffer 
algoritme en specificaties van de ontwikkelaar, elk van deze potentiele pixelwaardes 
samengevoegd tot een specifieke kleurwaarde die weergegeven kan 
worden binnen de afbeelding.

## Moderne Grafische Pijplijn implementatie
  
\input{./img/tex/mgp-pipeline.tex}

De moderne grafische pijplijn is in grote mate programmeerbaar. Dit betekent
dat de ontwikkelaar in staat is om zelf algoritmes op de grafische pijplijn
te implementeren. Er zijn verschillende `APIs` beschikbaar waarmee
de ontwikkelaar deze algoritmes kan implementeren. De twee meest gebruikte 
industriestandaarden zijn `openGL` en `Direct3D`. `openGL` is een niet-platformspecifieke 
specificatie, terwijl `Direct3D` gebonden is aan Microsoft Windows. 
Om deze reden is gekozen voor het gebruik van `openGL` binnen
deze thesis. `openGL` en `Direct3D` zijn vergelijkbaar, maar verschillen 
in nomenclatuur. In deze thesis zal gebruik gemaakt worden van de naamgeving
van `openGL`. 

Een overzicht van de verschillende stappen van de pijplijn voor respectievelijk
`openGL` en `Direct3D` zijn weergegeven in figuur \ref{fig:mgp-pipeline-opengl} en
\ref{fig:mgp-pipeline-direct3d}. De stappen die programmeerbaar zijn, zijn weergegeven
in blauw. De andere stappen zijn om redenen van effici\"entie slechts configureerbaar.
De optionele stappen zijn weergegeven met ronde hoeken. In beide `APIs` zijn negen
stappen terug te vinden:

* Vertex Specificatie
* Vertex Shader
* Tesselatie
* Geometrie shader
* Vertex Post-Processing
* Primitieven assemblage
* Rasterisatie
* Fragment Shader
* Per-Sample operaties

\noindent De programmeerbaarheid van de pijplijn volgt uit zogenoemde programmeerbare shaders, 
de *vertex shader*, *geometrie shader*, en *fragment shader*. Deze hebben 
respectievelijk invloed op de vertices, primitieven en fragmenten. Fragmenten 
zijn de punten die worden teruggegeven nadat de primitieven zijn verwerkt door
het rasterisatie algoritme, veelal komen deze overeen met pixels.  

Terugkijkend op de conceptuele beschrijving van de grafische pijplijn, komen 
de stappen als volgt \mbox{over\'e\'en} met de conceptuele stappen. De applicatie-stap
is niet gedefinieerd binnen de `openGL` pijplijn. Deze wordt uitgevoerd voordat de 
`openGL` pijplijn wordt aangesproken. De applicatie stap eindigt met de vertex-specificatie. 
De applicatie specificeert hierbij een verzameling van primitieven.
Vervolgens wordt deze verzameling van vertices verwerkt door een of meerdere 
vertexshaders. De ontwikkelaar heeft hier volledige controle over.
Veelal vinden hier de model- en zichttransformaties plaats. Ook is het 
mogelijk dat hier een eerste stap van de shading plaatsvindt, wat vervolgens 
ge\"interpoleerd zal worden in volgende stappen. De tesselatie en geometrie 
kunnen gebruikt worden om primitieven aan te passen, of zelfs volledige
nieuwe geometrie te produceren of juist weg te filteren. Deze stappen zijn 
optioneel, en zullen niet gebruikt worden binnen deze thesis. De vertex-post-processing, 
assemblage en rasterisatie zijn allemaal
fixed-function-operaties. Deze komen overeen met de stappen, clipping, canvas
afbeelding, driehoek opzet en driehoek doorkruizing. Hierin vindt op hardware
niveau de uitvoering van het rasterisatie-algoritme plaats. 
Aan het einde van deze stap wordt een verzameling van fragmenten geproduceerd. Binnen de
fragmentshader worden deze fragmenten
gebruikt om per-pixel-shading uit te voeren, waarmee een specifieke kleur
wordt gegenereerd voor elk fragment. Als laatste vindt dan de samenvoeging
van fragmenten plaats in de per-sample-operaties.
Hier wordt tevens het z-buffer algoritme uitgevoerd. Dit betekent dat 
per-pixel-shading wordt uitgevoerd voor alle pixels, en dus ook voor pixels
die uiteindelijk helemaal geen invloed hebben op de afbeelding.
In de volgende secties zal nog ingegaan worden op de drie stappen die het meest relevant zijn
deze thesis.

### Vertexshader

De vertexshader behandelt exclusief de punten, vertices, die gespecificeerd 
worden door de applicatie. De shader zelf heeft geen kennis hoe elk van de 
vertices zich verhoudt tot de primitieven. Veelal is de vertexshader 
verantwoordelijk voor het omzetten van de co\"ordinaten van model- naar camera- of wereldruimte,
afhankelijk van de specificatie van de fragmentshader.
Tevens dient hier de locatie van de vertex in de canvas gezet te worden.

### Fragmentshader 

Nadat de primitieven omgezet zijn naar een verzameling van fragmenten, wordt op 
elk van de fragmenten de gespecificeerde fragmentshader toegepast. De 
rasterisatiestap produceert een verzameling van data, waaronder de specifieke locatie van
fragmenten, en een interpolatie van berekende waardes binnen de vertexshader. Deze
kunnen vervolgens gebruikt worden door de fragmentshader, om de shading van
dat fragment te uit te voeren.  

De fragmentshader berekent de kleur voor alle fragmenten, voor dat deze worden
samengevoegd tijdens de per-sample-operaties. De berekening van de kleur is veelal de stap binnen de
grafische pijplijn die de meeste berekeningsmiddelen vereist. In moderne 
applicaties wordt hier veelal de benadering van de rendervergelijking
berekend. Hierbij is de fragmentshader niet beperkt om slechts naar \mbox{\'e\'en} canvas 
data weg te schrijven. Het is mogelijk om meerdere canvassen aan te spreken met 
behulp van meerdere renderdoelen (*multiple render targets*).

### Per-sample-operaties

De laatste stap van een enkele uitvoering van de renderpijplijn bestaat uit
de per-sample operaties. Hierin worden de verschillende fragmenten samengevoegd
en weggeschreven naar de framebuffer, met behulp van het z-buffer algoritme.
Verder kunnen hier stappen plaatsvinden zoals compositie en het mixen van 
kleuren, wat belangrijk is voor de ondersteuning van transparantie. Deze 
stap zijn configureerbaar.

Zoals eerder vermeld is een belangrijke observatie dat voor de meeste implementaties 
van grafische pijplijnen, de fragmentshader wordt uitgevoerd voor elk fragment, ongeacht of 
deze daadwerkelijk zichtbaar is. 
Dit kan leiden tot een grote mate van onnodige berekeningen, indien de \mbox{sc\`ene}
bestaat uit veel primitieven. Oplossingen hiervoor zullen verder besproken 
worden in volgende hoofdstukken.  

Voor verdere informatie over realtime rendering en de moderne grafische pijplijn
wordt gerefereerd naar Real-Time Rendering\cite{akenine2016real}
Meer informatie over `Direct3D` en `openGL` kan
gevonden worden op hun respectievelijke documentatiewebsites.  
