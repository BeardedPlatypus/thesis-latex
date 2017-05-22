# Software

Om de verschillende lichttoekenningsalgoritmes op een consistente manier te 
vergelijken, is gekozen om elk van deze algoritmes te implementeren. Hiervoor is
het programma `nTiled` ontwikkeld. Naast de lichttoekkeningsalgoritmes bevat
dit programma alle functionaliteit die nodig is om de renderpijplijn uit te 
voeren, en relevante data te verzamelen.

## Organisatie

`nTiled` kan worden onderverdeeld in de volgende modules:

camera 
  ~ De camera implementeert het cameramodel zoals beschreven in sectie 
    \ref{sec:camera-model}.
    
gui
  ~ De gui bevat alle componenten die nodig zijn voor het gebruikersinterface.
  
log
  ~ De logmodule bevat de functies die gebruikt worden om relevante data te 
    verzamelen.
  
main
  ~ De main-module implementeert de controlefuncties die verantwoordelijk zijn 
    voor de uitvoering van het programma.
    
math
  ~ De math-module bevat alle extra wiskundige functies die gebruikt worden 
    binnen `nTiled`
    
pipeline
  ~ De pipeline-module is verantwoordelijk voor de gehele pijplijn en bevat
    de implementaties van de shaders en de datastructuren van de 
    lichttoekenningsalgoritmes.
    
state
  ~ De state-module bevat alle componenten gerelateerd aan de staat van een
    enkele uitvoering van `nTiled`. Het is hierbij verantwoordelijk voor het
    inlezen van de configuratiebestanden en het beheren van deze attributen.
  
world
  ~ De world-module is verantwoordelijk voor het inlezen en beheren van alle 
    geometrie en lichten.
    
Voor een compleet overzicht van de implementatie zie de documentatie[^docu] en 
repository[^repo] van `nTiled`.

[^docu]: de nTiled documentatie kan gevonden worden op ntiled.readthedocs.io/en/latest/index.html
[^repo]: de nTiled repository kan gevonden worden op github.com/BeardedPlatypus/nTiled


## Libraries

`nTiled` is gebouwd op de volgende libraries:

`openGL 4.4` en `GLAD`
  ~ `openGL` met behulp van `GLAD`[^glad] verzorgt voor de rendering pijplijn.
  
`glfw`
  ~ `glfw` is de window manager, verantwoordelijk voor het aanmaken van de 
    applicatie in het besturingssysteem en het managen van de gebruikersinput.[^glfw]
    
`assimp`
  ~ `assimp` is gebruikt om de geometrie-objecten in `nTiled` te laden. [^assimp]
  
`glm`
  ~ `glm` is de wiskundige library die de vector- en matrixberekeningen aan de 
     `C++` kant verzorgt. [^glm]
    
`rapidjson`
  ~ `rapidjson` is verantwoordelijk voor het inlezen van de `json` configuratie
    bestanden en het exporteren van de verzamelde data. [^rapidjson]

`dear, imgui`
  ~ `dear, imgui` verzorgt de GUI. [^imgui]
  
[^glad]: glad project pagina: github.com/Dav1dde/glad
[^glfw]: glfw website: www.glfw.org
[^assimp]: assimp project pagina: github.com/assimp/assimp
[^glm]: glm website: glm.g-truc.net/0.9.8/index.html
[^rapidjson]: rapidjson project pagina: github.com/miloyip/rapidjson
[^imgui]: dear, imgui project pagina: github.com/ocornut/imgui

De software is ontwikkeld en en gecompiled met behulp van `visual studio 2015`


## Renderpijplijn

De renderfunctionaliteit is ge\"implementeerd in de pipeline-module. De
pipeline-module kan worden onderverdeeld in de Forward- en Deferred-pijplijn,
die verder behandeld zullen worden in hoofdstuk \ref{ch:Forward en Deferred Shading},
en de lichttoekkeningsalgoritmes, die zullen worden behandeld in hoofdstuk 
\ref{ch:Tiled Shading} tot \ref{ch:Hashed Shading}. 

Voor elk lichttoekenningsalgoritme is zowel een Forward- als Deferred-shader
gedefinieerd. Dit leidt tot de volgende shaders:

Na\"ief
  ~ De shader zonder lichttoekenningsdatastructuur.

Tiled
  ~ De shader met de Tiled Shading-datastructuur.
  
Clustered
  ~ De shader met de Clustered Shading-datastructuur.
  
Hashed
  ~ De shader met de Hashed Shading-datastructuur.
  
Alle shading-berekeningen vinden plaats in de fragment-shader. Binnen de 
vertex-shaders worden slechts de relevante co\"ordinatenstelseltransformaties
op de positie en normaal uitgevoerd. Binnen de fragment-shaders wordt eerst
de relevante set van lichten bepaald aan de hand van het corresponderende 
lichttoekenningsalgoritme. Vervolgens wordt voor elk van deze lichting een
shading-berekening uitgevoerd, waarbij de resultaten gesommeerd worden.

\input{./lst/io-computeLight.tex}

De shading-berekening is een simpele directe-lichtbenadering van een wit
lambertiaansoppervlakte, zoals beschreven in sectie \ref{sec:shading}.
Deze functie is gedefinieerd in listing \ref{lst:io-computeLight} en komt
overeen met de functie:

$$
\mathit{L}(l_{i}, \mathbf{p}) = \mathit{c}_\mathbf{p} * \mathit{I_i} * \cos\theta * \mathit{f_\mathtt{att}}
$$

waar

$$
\mathit{f_\mathtt{att}} = ( 1 - \left.\frac{\mathit{d}}{\mathit{r_i}}\right|_{{0, 1}})
$$

en $\theta$ de invalshoek is. Dit alles leidt tot het materiaal zoals 
weergegeven in figuur \ref{fig:imp-lambert}, waar de oppervlakte verlicht is met
twaalf lichten met verschillende tinten.

\input{./img/tex/imp-lambert.tex}

## Meetmethode

De executietijdmetingen zijn verzameld metde `QueryPerformanceCounter`. Deze 
functionaliteit is aangeboden in `Windows.h`. Hierdoor is het mogelijk om 
waardes te rapporteren. Dit maakt het mogelijk om de executietijd tot op
$\mu s$ nauwkeurig te meten.

