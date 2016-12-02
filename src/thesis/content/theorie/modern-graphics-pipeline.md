# Moderne Grafische Pijplijn

De voorgaande secties hebben een grof overzicht gegeven van zowel de problemen
als oplossingen binnen het renderen van afbeeldingen. Het onderzoek binnen deze
thesis richt zich op het real-time renderen. Het onderliggende gereedschap, 
verantwoordelijk voor het renderen van de afbeeldingen is de real-time grafische
pijplijn. In deze sectie zal eerst conceptueel de opbouw van de grafische 
pijplijn beschreven worden, waarna in meer detail de `openGL` implementatie 
besproken wordt, waarmee het onderzoek binnen deze thesis is gebouwd.  

## Conceptuele architectuur

In de fysieke wereld is een pijplijn een verzameling van stappen. Elke stap 
transformeert de uitkomst van de vorige stap in een volgende uitkomst. 
Elke stap bouwt dus verder op de voorgaande stap, echter elk van de stappen
kunnen wel in parallel uitgevoerd worden. Dit betekent dat de snelheid van de
pijplijn bepaald wordt door de stap met de langste bewerking.  

\input{./img/tex/mgp-conceptueel.tex}

De grafische pijplijn is op een vergelijkbare manier opgebouwd en kan grofweg
onderverdeeld worden in 3 conceptuele stappen.

* Applicatie stap  
* Geometrie stap  
* Rasteriser stap  

Deze zijn tevens weergegeven in figuur \ref{mgp-conceptueel}.  

### Applicatie stap

De applicatie stap beschrijft alle berekeningen die plaatsvinden binnen de 
applicatie van de ontwikkelaar. Belangrijke aspecten hier zijn onder de 
verwerking van invoer van gebruikers, het opzetten van datastructuren, 
collision detection, etc. Aan het einde van de applicatie stap dient een 
verzameling primitieven gestuurd te worden naar de geometrie stap.  

### Geometrie stap

\input{./img/tex/mgp-conceptueel.tex}

De geometrie stap is verantwoordelijk voor het merendeel van per-polygon 
operaties. Deze stap kan verder onderverdeelt worden zoals weergegeven 
in figuur \ref{mgp-geometrie}.
De volgende sub-stappen kunnen onderscheden worden:

* Model- en zichtstransformaties
* Vertex shading
* Projectie
* Clipping
* Canvas afbeelding

Belangrijk hierbij is dat de conceptuele beschrijving in sommige opzichten 
kan verschillen van daadwerkelijke implementaties.  

De geometrie stap zorgt dat objecten geproduceerd door de applicatie stap, 
omgezet worden naar een set van data die in de rasterisatie stap omgezet 
kan worden in een daadwerkelijke afbeelding. 
Eerst worden objecten getransformeerd zodanig dat alle primitieven zich in 
hetzelfde coordinaten systeem bevinden.
Hierna vindt een eerste shading stap plaats die wordt uitgevoerd voor alle
vertices van alle primitieven. Dit is een eerste stap in het oplossen van
het shading probleem. Nadat de shading berekend is per vertex, wordt de 
perspectief projectie uitgevoerd en worden niet zichtbare objecten 
weggesneden uit het resultaat. Als laatste worden de primitieven die over zijn
omgezet naar canvas coordinaten. De set van primitieven in canvas coordinaten, 
en corresponderende shading data wordt vervolgens doorgestuurd naar de laatste
stap.  

### Rasterisatie stap

\input{./img/tex/mgp-rasterisatie.tex}

In de rasterisatie stap wordt de daadwerkelijke kleuren van de afbeelding
berekend. Hiervoor wordt een rasterisatie algoritme uitgevoerd als beschreven
in . Dit leidt tot de onderverdeling zoals weergegeven in figuur 
\ref{mgp-rasterisatie}. 
De volgende sub-stappen kunnen onderscheden worden:

* Driehoek opzet
* Driehoek doorkruizing
* Pixel shading
* Samenvoeging

De eerste twee stappen komen overeen met het rasterisatie algoritme. Hierbij 
wordt shading data uit de geometrie stap geinterpoleerd. Dit leidt tot een set
van fragmenten met geassocieerde geinterpoleerde shading data. 
Deze worden met behulp van pixel shading verwerkt tot een specifieke kleur 
voor een specifieke pixel. Als laatste wordt doormiddel van het z-buffer 
algoritme en specificaties van de ontwikkelaar, elk van deze potentiele pixel
waardes samengevoegd tot een specifieke kleur waarde die weergegeven kan 
worden binnen de afbeelding.

## Moderne Grafische Pijplijn implementatie
   
De moderne grafische pijplijn wordt gedefinieerd als een programmeerbare 
pijplijn. Dit houdt in dat de ontwikkelaar in staat is om zelf algoritmes
te implementeren. Er zijn verschillende `APIs` beschikbaar waarmee een 
ontwikkelaar de grafische pijplijn kan gebruiken. De twee meest gebruikte 
industrie standaarden zijn `openGL` en `Direct3D`. `openGL` is een niet platform
specifieke specificatie. Om deze reden is gekozen voor het gebruik van `openGL`
binnen deze thesis. `openGL` en `Direct3D` zijn in grote mate vergelijkbaar, 
echter verschillen in nomenclatuur. In deze uitleg zal gebruik gemaakt worden
van de naamgeving zoals geintroduceerd in `openGL`. Indien een nieuwe term 
geintroduceerd wordt zal waar nodig ook de `Direct3D` equivalent worden 
gespecificeerd.  

\input{./img/tex/mgp-pipeline.tex}

De moderne grafische pijplijn is een grote mate programmeerbaar, echter in 
is wegens efficientie redenen slechts configureerbaar. 
Een overzicht van de verschillende stappen van de pijplijn voor respectievelijk
`openGL` en `Direct3D` zijn gegeven in figuur \ref{mgp-pipeline-opengl} en
\ref{mgp-pipeline-direct3d}. Door middel van kleuren is de mate van 
programmeerbaarheid, aangegeven. Tevens zijn optionele stappen aangegeven door 
een stippellijn. In beide `APIs` zijn 9 stappen terug te vinden. 

* Vertex Specificatie
* Vertex Shader
* Tesselatie
* Geometrie shader
* Vertex Post-Processing
* Primitieven assemblage
* Rasterisatie
* Fragment Shader
* Per-Sample operaties

De programmeerbaarheid van de pijplijn volgt uit de programmeerbare shaders, 
de *vertex shader*, *geometrie shader*, en *fragment shader*. Deze hebben 
respectievelijk invloed op vertices, primitieven en fragmenten. Fragmenten 
zijn de punten die worden teruggegeven nadat de primitieven zijn verwerkt door
het rasterisatie algoritme, veelal komen deze overeen met pixels of subpixels.  

Terugkijkend op de conceptuele beschrijving van de grafische pijplijn, komen 
de stappen als volgt overeen met de conceptuele stages. De applicatie stage
is niet gedefinieerd binnen de `openGL` pijplijn, deze bevindt zich voordat de 
`openGL` pijplijn wordt aan gesproken. De applicatie stap eindigt met de vertex 
specificatie. De applicatie specificeert hierbij een set van primitieven.
Vervolgens wordt deze verzameling van vertices verwerkt door een of meerdere 
vertex shaders. De ontwikkelaar heeft hier volledige controle over, echter 
veelal vinden hier de model en gezichts transformaties plaats. Ook is het 
mogelijk dat hier een eerste stap in shading plaatsvindt, wat vervolgens 
geinterpoleerd zal worden in volgende stappen. De tesselatie en geometrie 
kunnen gebruikt worden om primitieven aan te passen, of zelfs volledige
nieuwe geometrie te produceren of juist weg te filteren. Deze stappen zijn 
optioneel. De vertex post-processing, assemblage en rasterisatie zijn allemaal
fixed function operaties. Deze komen overeen met de stappen, clipping, canvas
afbeelding, driehoek opzet en driehoek doorkruizing. Hierin vindt op hardware
niveau de uitvoering van het rasterisatie algoritme plaats, en wordt een set 
van fragmenten geproduceerd. Binnen de fragmentshader worden deze fragmenten
gebruikt om per-pixel shading uit te voeren, waarmee een specifieke kleur
wordt gegenereerd voor elk fragment. Als laatste vind dan de samenvoeging
van fragmenten plaats in de per-sample operaties. Belangrijk hierbij is dat
hier tevens het z-buffer algoritme wordt uitgevoerd. Dit betekent dat 
per-pixel shading wordt uitgevoerd voor alle pixels, en dus tevens voor pixels
die uiteindelijk helemaal geen invloed hebben op de uiteindelijke afbeelding.  

Als laatste zal kort ingegaan worden op de vertex en fragment shaders, en de 
per-sample operaties.

### Vertex Shader

De vertex shader behandelt exclusief de punten, vertices, die gespecifieerd 
worden door de applicatie. De shaders zelf heeft geen kennis hoe elk van de 
vertices zich verhoudt tot primitieven. Veelal is de vertex shader 
verantwoordelijk voor het omzetten van de coordinaten van model naar camera
of wereld ruimte, afhankelijk van de specificatie van de fragment shader.
Tevens dient hier de locatie gezet te worden van de specifieke geprojecteerde
locatie.  

### Fragment Shader 

Nadat de primitieven omgezet zijn naar een set van fragmenten, wordt op 
elk van de fragmenten de gespecificeerde fragment shader uitgevoerd. De 
rasterisatie stap produceert een set van data, waaronder specifieke locatie van
fragmenten, en interpolatie van berekende waardes binnen de vertex shader. Deze
kunnen vervolgens gebruikt worden door de fragment shader, om de shading van
dat fragment te berekenen.  

De fragmentshader berekent de kleur voor elk fragment, voordat deze wordt 
samengevoegd in de per-sample operaties stap. Dit is veelal de stap binnen de
grafische pijplijn die de meeste berekeningsmiddelen vereist. In moderne 
applicaties wordt hier veelal de benadering van de renderingsvergelijking
berekend. Tevens is het mogelijk voor de fragmentshader, om resultaten naar
meerdere verschillende renderdoelen (*multiple render targets*) weg te 
schrijven.  

### Per-Sample Operaties

De laatste stap van een enkele uitvoering van de renderpijplijn bestaat uit
de per-sample operaties. Hierin worden de verschillende fragmenten samengevoegd
en weggeschreven naar de framebuffer, door middel van het z-buffer algoritme.
Verder kunnen hier stappen plaatsvinden zoals compositie en het mixen van 
kleuren, wat belangrijk is voor de ondersteuning van transparantie.  

Zoals eerder vermeld is een belangrijke observatie dat de fragmentshader wordt
uitgevoerd voor elk fragment, ongeacht of deze daadwerkelijk zichtbaar is. 
Dit kan leiden tot een grote mate van onnodige berekeningen, indien de scene
bestaat uit veel primitieven. Oplossingen hiervoor zullen verder besproken 
worden in volgende hoofdstukken.  

