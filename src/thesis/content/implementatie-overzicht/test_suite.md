# Testsuite

De testsuite bestaat uit drie verschillende scenes.

* Spaceship Indoor
* Piper's Alley
* Ziggoerat Stad

Elk van deze scenes is gedefinieerd als een set van objecten, een camerapad,
en een set van lichtconfiguraties.

De scenes zijn zo geselecteerd dat zij representatief zijn voor mogelijke scenes
in games: een afgesloten ruimte, een openlucht straat, en een grote openlucht 
scene. Hierdoor is het mogelijk om de verschillende lichttoekenningsalgoritmes
te evalueren bij verschillende schalen en dieptes.

Elk van de scenes is gecree\"erd in Blender. De verschillende objecten zijn
ge\"exporteerd als `.obj` bestand. De lichtconfiguraties zijn gegenereerd aan
de hand van lichtgeneratievolumes. Een lichtgeneratievolume is een rechthoekig 
blok, die per lokale as beschrijft hoeveel lichten er relatief in gegenereerd
dienen te worden. Aan de hand van deze lichtgeneratievolumes worden lichten
met een gespecificeerde radius en een willekeurige tint gegenereerd. Deze 
lichten worden uniform over de ruimte verdeeld.

Elk van de scenes zal in de volgende secties verder worden toegelicht. Een
volledig overzicht van de scenes en gerelateerde data kan gevonden worden in
de data-repository [^data-repo]

[^data-repo]: de data-repository kan gevonden worden op github.com/BeardedPlatypus/thesis-data-suite/tree/master/scenes


## Indoor: Spaceship
\input{./img/tex/test-suite-spaceship-frame.tex}

De indoor-ruimteschip scene, weergegeven in figuur \ref{fig:test-suite-spaceship-frame}
is gebaseerd op de CG Lighting Challenge #18, gemodelleerd door Juan Carlos Silva.[^1] 
Deze scene staat model voor indoor-scenes. De scene bestaat uit een middenstuk 
en een omliggend gangenstelsel. De grootste bron van details is afkomstig van 
de panelen in de gangen. 

Het camerapad en de lichtgeneratievolumes zijn weergegeven in figuur 
\ref{fig:test-suite-spaceship-map}. De camera beweegt zich door de gangen en kruist hierbij 
twee maal het middenstuk, gedurende $519$ frames. De lichten in het middenstuk 
hebben een radius van $30.0$, de lichten in het gangenstelsel een radius van
$23.0$.

[^1]: Scene url: www.3drender.com/challenges/


## Straatzicht: Piper's Alley
\input{./img/tex/test-suite-pipers-alley-frame.tex}

De Piper's Alley scene, weergegeven in figuur \ref{fig:test-suite-pipers-alley-frame}
is gebaseerd op de CG Lighting Challenge #42, gemodelleerd door Clint Rodrigues.[^2]
De scene beschrijft een enkele straat met grote diepte, waar aan weerszijde
huizen zijn geplaatst. In de verre diepte zijn een kloktoren en triomfboog zichtbaar.
De gebouwen zijn de bron van de meeste details. 

Het camerapad en de lichtgeneratievolumes zijn weergegeven in figuur
\ref{fig:test-suite-pipers-alley-map}. De camera beweegt zich door het eerste deel
van de straat gedurende $551$ frames. Alle lichtconfiguraties zijn gegenereerd met een
radius van $180.0$.

[^2]: Lighting challenge url: forums.cgsociety.org/archive/index.php?t-1309021.html


## Stadsscene: Ziggoerat
\input{./img/tex/test-suite-ziggurat-frame.tex}
\input{./img/tex/test-suite-ziggurat-map.tex}

De ziggoerat scene is gemodelleerd als onderdeel van de open film Sintel[^3]. 
De scene bestaat uit een gedetailleerde tempelberg waaromheen, in lagere 
resolutie, huizen en een stadsmuur zijn geplaatst. Deze scene staat model voor
grote openlucht scenes.

Het camerapad en de lichtgeneratievolumes zijn weergegeven in figuur 
\ref{fig:test-suite-ziggurat-map}. De camera beweegt zich eerst langs de trap 
omhoog, om vervolgens om de tempelberg heen te vliegen. Het camerapad is $463$
frames lang. De lichten zijn onderverdeeld in twee sets. De lichten op de 
ziggoerat hebben een radius van $10.0$ en zijn met een grotere dichtheid 
geplaatst. De lichten in de stad hebben een radius van $50.0$, en zijn verspreid
over grotere volumes.

[^3]: Open film url: durian.blender.org

