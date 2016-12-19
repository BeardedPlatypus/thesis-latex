# Test suite

De test suite bestaat uit 3 verschillende scenes waarvoor, voor elke scene, 
geometrie, een camera pad, en verschillende lichtconfiguraties zijn 
gedefinieerd. Elk van de testen die volgt zijn uitgevoerd met deze scenes. 

De gedefinieerde scenes zijn:

* Ruimteschip: indoor scene
* Piper's Alley: straatzicht
* Ziggurat stad: stads scene

Deze zijn geselecteerd zodanig dat deze scenes representatief zijn voor de 
verschillende schalen die voor kunnen komen binnen games. Een afgesloten indoor
ruimte , een open lucht straat met details in de diepte, en een grote open lucht
scene. Door het gebruik van deze scenes is het mogelij om de performantie van de
verschillende rendertechnieken tevens te vergelijken op het niveau van verschillende
scenes.

Voor elk van de scenes zijn verschillende licht configuraties gedefinieerd. Elk
van de lichten zijn statisch, met een zelfde radius, indien niet anders 
aangegeven. De lichten zelf zijn uniform over de scenes verdeeld aan de hand van
licht volumes waarin een gespecificeerd aantal lichten worden geplaatst.

## Indoor: Spaceship
\input{./img/tex/test-suite-spaceship-images.tex}

Het indoor spaceship scene is gebaseerd op de CG lighting challenge #18, 
gemodeleerd door Juan Carlos Silva.[^1] Deze scene staat model voor indoor game scenes,
waarbij visibiliteit beperkt is. De scene bestaat uit ... tussen stukken verbonden
met hoekstukken en 1 centraal midden. De grootste bron van details komt uit de panelen
aan weerzijden van elk tussenstuk. De scene bestaat uit ... polygonen, de
verdeling van deze polygonen is gegeven in figuur \ref{fig:test-suite-spaceship:fragments}.
Het camera pad zoals weergegeven in figuur \ref{fig:test-suite-spaceship:camera}
bestaat uit ... frames. 
Voor elk component in de scene is een lichtvolume gedefinieerd waarin de lichten zijn
gegenereed. Dit si weergegeven in figuur \ref{fig:test-suite-spaceship:lights}.

[^1]: Scene url: \url{http://www.3drender.com/challenges/}

## Straatzicht: Piper's Alley
\input{./img/tex/test-suite-pipers-alley-images.tex}

De pipers alley scene is gebaseerd op de CG lighting challenge #42, gemodeleerd door
Clint Rodrigues.[^2] Deze scene beschrijft een enkele straat, met grote diepte, 
waar aan weerszijden huizen zijn geplaatst. Er zijn totaal ... polygonen binned de scene, 
de verdeling hier van is te zien in figuur \ref{fig:test-suite-pipers-alley:fragments}.
De camera beweegt over deze straat gedurende ... frames.
De lichtvolumes zijn geplaatst over de straat zoals weergegeven in figuur 
\ref{fig:test-suite-pipers-alley:lights}.

[^2]: Lighting challenge url: \url{http://forums.cgsociety.org/archive/index.php?t-1309021.html}

## Stadsscene: Ziggoerat
\input{./img/tex/test-suite-ziggurat-images.tex}

De ziggoerat stadsscene is gemodeleerd als onderdeel van de open film sintel.[^3] 
De scene bestaat uit een gedetailleerde ziggoerat, waarom heen in lagere resolutie
huizen en een stadsmuur liggen. De scene bestaat uit totaal 1,6 millioen polygonen, 
de distributie is te zien in figuur \ref{fig:test-suite-ziggurat:fragments}.
De camera beweegt eerst omhoog de ziggoerat, om vervolgens over de stad heen te pannen.
Dit gebeurt over 460 frames. Het pad is te zien in figuur \ref{fig:test-suite-ziggurat:camera}.
De lichten zijn onderverdeeld in twee sets, de lichten op de ziggoerat zijn kleiner en 
met een hogere dichtheid geplaatst, ten opzichte van de lichten die geplaatst zijn over de stad.
De lichtvolumes zijn weergegeven in figuur \ref{fig:test-suite-ziggurat:lights}.

[^3]: Open film url: \url{https://durian.blender.org}

