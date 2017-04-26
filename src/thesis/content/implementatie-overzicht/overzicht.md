# Overzicht

`nTiled` is de software geschreven om de verschillende lichtmethoden te testen.
Het is geschreven in `C++` en gebouwd op de volgende libraries.

`openGL 4.4`
  ~ `openGL` met behulp van `GLAD`[^glad] zorgt voor de rendering pijplijn.
  
`glfw`
  ~ `glfw` is de window manager, verantwoordelijk voor het aan maken van de 
    applicatie in het besturingssysteem. [^glfw]
    
`assimp`
  ~ `assimp` is gebruikt om de geometrie objecten in `nTiled` te laden. [^assimp]
  
`glm`
  ~ `glm` is een mathematische library gebruikt voor de vector en matrix
    berekeningen aan de `C++` kant. [^glm]
    
`rapidjson`
  ~ `rapidjson` wordt gebruikt om de `json` configuratie bestanden in te lezen. [^rapidjson]

`dear, imgui`
  ~ `dear, imgui` is de GUI libary. [^imgui]
  
[^glad]: glad project pagina: github.com/Dav1dde/glad
[^glfw]: glfw website: www.glfw.org
[^assimp]: assimp project pagina: github.com/assimp/assimp
[^glm]: glm website: glm.g-truc.net/0.9.8/index.html
[^rapidjson]: rapidjson project pagina: github.com/miloyip/rapidjson
[^imgui]: dear, imgui project pagina: github.com/ocornut/imgui

Het programma zelf kan grofweg worden ingedeeld in de render functionaliteit die
getest wordt binnen deze thesis, en zeven ondersteundende modules:

Camera 
  ~ De camera implementeert het camera model zoals beschreven in het theorie
    hoofdstuk. Hierbij is het mogelijk om data opgeslagen in `json` bestanden
    in te lezen.
    
GUI
  ~ De GUI implementeert de gebruikers interface met behulp van `dear, imgui`
  
log
  ~ De log module implementeert de logging capiciteiten.
  
main
  ~ Implementeert de functionaliteit gerelateerd aan het opstarten en sluiten
    van het programma.
    
math
  ~ In math zijn de extra wiskundige functies geimplementeerd die gebruikt worden 
    binnen `nTiled`.
    
state
  ~ State bevat de staat nodig voor een enkele uitvoering van `nTiled`. Tevens
    bevat het de functionaliteit om alle configuratie bestanden in te lezen.
    
world
  ~ Implementeert de functionaliteit om de geometrie en lichten in te lezen, 
    en te beheren binnen een uitvoering van `nTiled`
    
De pipeline module implementeert de rendering pipeline. Hierin wordt zowel de voorwaartse
als de deferred pijplijn geimplementeerd, in respectief de `forward` en `deferred` module. 
Tevens bevindt zich hierin de implementatie van de drie belichtings methodes in de module
`light-management`.

Voor beide types pijplijnen zijn de volgende shaders geimplementeerd:

Geattenueerd
  ~ De shaders zonder versnellingsstructuren.
  
Tiled
  ~ De shaders die de tiled versnellingsstructuur bevatten.
  
Clustered
  ~ De shaders die de clustered versnellingsstructuur bevatten.
  
Hashed
  ~ De shaders die de hashed versnellingsstructuur bevatten zoals voorgesteld in deze 
    thesis.
    
Elke shader bestaat uit een `C++` implementatie en corresponderende `glsl` bestanden.
Voor een compleet overzicht van de implementatie zie de documentatie [^docu] en repository van
`nTiled`.[^repo]

[^docu]: de nTiled documentatie kan gevonden worden op ntiled.readthedocs.io/en/latest/index.html
[^repo]: de nTiled repository kan gevonden worden op github.com/BeardedPlatypus/nTiled

