# Moderne Grafische Pijplijn {#sec:moderne-grafische-pipeline}

De voorgaande secties hebben een grof overzicht gegeven van zowel de problemen
als oplossingen binnen het renderen van afbeeldingen. Het onderzoek binnen deze
thesis richt zich op het real-time renderen. Het onderliggende gereedschap
verantwoordelijk voor het renderen van de afbeeldingen is de real-time grafische
pijplijn. In deze sectie zal eerst conceptueel de opbouw van de grafische 
pijplijn beschreven worden. Hiervoor wordt de beschrijving zoals gegeven in
Real-Time Rendering 3rd edition\cite{akenine2016real} aangehouden.
Hierna zal in meer detail de `openGL` implementatie 
besproken worden, waarop het onderzoek binnen deze thesis is gebouwd.  

## Conceptuele architectuur

In de fysieke wereld is een pijplijn een verzameling van stappen. Elke stap 
transformeert de uitkomst van de vorige stap in een volgende uitkomst. 
Elke stap bouwt dus verder op de voorgaande stap, echter elk van de stappen
kunnen wel in parallel uitgevoerd worden. Dit betekent dat de snelheid van de
pijplijn bepaald wordt door de stap met de langste bewerking.  
De grafische pijplijn is op een vergelijkbare manier opgebouwd en kan grofweg
onderverdeeld worden in drie conceptuele stappen.

* Applicatie-stap  
* Geometrie-stap  
* Rasterisatie-stap  

### Applicatie-stap

De applicatie-stap beschrijft alle berekeningen die plaatsvinden binnen de 
applicatie van de ontwikkelaar. Belangrijke aspecten hier zijn onder andere de 
verwerking van invoer van gebruikers, het opzetten van datastructuren en
collision detection. Aan het einde van de applicatie-stap dient een 
verzameling primitieven gestuurd te worden naar de geometrie-stap.  

### Geometrie-stap

\input{./img/tex/mgp-geometrie.tex}

De geometrie-stap is verantwoordelijk voor het merendeel van de per-polygon 
operaties. Deze stap kan verder onderverdeelt in de volgende sub-stappen: 

* Model- en zichtstransformaties
* Vertex shading
* Projectie
* Clipping
* Canvas afbeelding

\noindent Deze stappen zijn weergegeven in figuur \ref{fig:mgp-geometrie}. 
Belangrijk hierbij is dat de conceptuele beschrijving in sommige opzichten 
kan verschillen van daadwerkelijke implementaties.  

De geometrie-stap zorgt dat objecten geproduceerd door de applicatie-stap, 
omgezet worden naar een set van data die in de rasterisatie-stap omgezet 
kan worden in een daadwerkelijke afbeelding. 
Eerst worden objecten getransformeerd zodanig dat alle primitieven zich in 
hetzelfde co\"ordinatensysteem bevinden. 
Hierna vindt een eerste shadingstap plaats die wordt uitgevoerd voor alle
vertices van alle primitieven. Nadat de shading berekend is per vertex, wordt de 
perspectiefprojectie uitgevoerd en worden niet zichtbare objecten 
weggesneden uit het resultaat. Als laatste worden de primitieven die over zijn
omgezet naar canvas-co\"ordinaten. De set van primitieven in canvas-co\"ordinaten, 
en corresponderende shadingdata wordt vervolgens doorgestuurd naar de rasterisatie-stap.  

### Rasterisatie-stap

\input{./img/tex/mgp-rasterisatie.tex}

In de rasterisatie-stap worden de daadwerkelijke kleuren van de afbeelding
berekend. Hiervoor wordt een rasterisatie-algoritme uitgevoerd. 
Dit leidt tot de onderverdeling zoals weergegeven in figuur \ref{fig:mgp-rasterisatie}. 
De volgende sub-stappen kunnen onderscheden worden:

* Driehoekopzet
* Driehoekdoorkruizing
* Pixel-shading
* Samenvoeging

De eerste twee stappen komen \mbox{over\'e\'en} met het rasterisatie-algoritme. Hierbij 
wordt shadingdata uit de geometrie stap ge\"interpoleerd. Dit leidt tot een set
van fragmenten met geassocieerde ge\"interpoleerde shadingdata. 
Deze worden met behulp van pixel-shading verwerkt tot een specifieke kleur 
voor een specifieke pixel. Als laatste wordt door middel van het z-buffer 
algoritme en specificaties van de ontwikkelaar, elk van deze potentiele pixelwaardes 
samengevoegd tot een specifieke kleur waarde die weergegeven kan 
worden binnen de afbeelding.

## Moderne Grafische Pijplijn implementatie
  
\input{./img/tex/mgp-pipeline.tex}

De moderne grafische pijplijn is in grote mate programmeerbaar. Dit betekent
dat de ontwikkelaar in staat is om zelf algoritmes op de grafische pijplijn
te implementeren. Er zijn verschillende `APIs` beschikbaar waarmee
de ontwikkelaar deze algoritmes kan implementeren. De twee meest gebruikte 
industrie standaarden zijn `openGL` en `Direct3D`. `openGL` is een niet-platformspecifieke 
specificatie. Om deze reden is gekozen voor het gebruik van `openGL` binnen
deze thesis. `openGL` en `Direct3D` zijn vergelijkbaar, maar verschillen 
in nomenclatuur. In deze thesis zal gebruik gemaakt worden van de naamgeving
van `openGL`. 

Een overzicht van de verschillende stappen van de pijplijn voor respectievelijk
`openGL` en `Direct3D` zijn weergegeven in figuur \ref{fig:mgp-pipeline-opengl} en
\ref{fig:mgp-pipeline-direct3d}. De stappen die programmeerbaar zijn weergegeven
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
het rasterisatie algoritme, veelal komen deze overeen met pixels of subpixels.  

Terugkijkend op de conceptuele beschrijving van de grafische pijplijn, komen 
de stappen als volgt \mbox{over\'e\'en} met de conceptuele stappen. De applicatie-stap
is niet gedefinieerd binnen de `openGL` pijplijn. Deze wordt uitgevoerd voordat de 
`openGL` pijplijn wordt aangesproken. De applicatie stap eindigt met de vertex-specificatie. 
De applicatie specificeert hierbij een set van primitieven.
Vervolgens wordt deze verzameling van vertices verwerkt door een of meerdere 
vertexshaders. De ontwikkelaar heeft hier volledige controle over.
Veelal vinden hier de model- en zichttransformaties plaats. Ook is het 
mogelijk dat hier een eerste stap van de shading plaatsvindt, wat vervolgens 
ge\"interpoleerd zal worden in volgende stappen. De tesselatie en geometrie 
kunnen gebruikt worden om primitieven aan te passen, of zelfs volledige
nieuwe geometrie te produceren of juist weg te filteren. Deze stappen zijn 
optioneel. De vertex-post-processing, assemblage en rasterisatie zijn allemaal
fixed-function-operaties. Deze komen overeen met de stappen, clipping, canvas
afbeelding, driehoek opzet en driehoek doorkruizing. Hierin vindt op hardware
niveau de uitvoering van het rasterisatie-algoritme plaats. 
Aan het einde van deze stap wordt een set van fragmenten geproduceerd. Binnen de
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

Nadat de primitieven omgezet zijn naar een set van fragmenten, wordt op 
elk van de fragmenten de gespecificeerde fragmentshader toegepast. De 
rasterisatiestap produceert een set van data, waaronder de specifieke locatie van
fragmenten, en een interpolatie van berekende waardes binnen de vertexshader. Deze
kunnen vervolgens gebruikt worden door de fragmentshader, om de shading van
dat fragment te uit te voeren.  

De fragmentshader berekent de kleur voor alle fragmenten, voordat deze worden
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

Zoals eerder vermeld is een belangrijke observatie dat de fragmentshader wordt
uitgevoerd voor elk fragment, ongeacht of deze daadwerkelijk zichtbaar is. 
Dit kan leiden tot een grote mate van onnodige berekeningen, indien de scene
bestaat uit veel primitieven. Oplossingen hiervoor zullen verder besproken 
worden in volgende hoofdstukken.  

