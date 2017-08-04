# Testsuite

De testsuite bestaat uit drie verschillende \mbox{sc\`enes}.

* Spaceship Indoor
* Piper's Alley
* Ziggurat City 

Elk van deze \mbox{sc\`enes} is gedefinieerd als een set van objecten, een camerapad,
en een set van lichtconfiguraties.

De \mbox{sc\`enes} zijn zo geselecteerd dat zij representatief zijn voor mogelijke \mbox{sc\`enes}
in games: een afgesloten ruimte, een openlucht straat, en een grote openlucht 
\mbox{sc\`ene}. Hierdoor is het mogelijk om de verschillende lichttoekenningsalgoritmes
te evalueren bij verschillende schalen en dieptes.

Elk van de \mbox{sc\`enes} is gecre\"erd in Blender. De verschillende objecten zijn
ge\"exporteerd als `.obj` bestand. De lichtconfiguraties zijn gegenereerd aan
de hand van lichtgeneratievolumes. Een lichtgeneratievolume is een rechthoekig 
blok, dat per lokale as beschrijft hoeveel lichten er relatief in gegenereerd
dienen te worden. Aan de hand van deze lichtgeneratievolumes worden lichten
met een gespecificeerde radius en een willekeurige tint gegenereerd. Deze 
lichten worden uniform over de ruimte verdeeld.

Elk van de \mbox{sc\`enes} zal in de volgende secties verder worden toegelicht. Een
volledig overzicht van de \mbox{sc\`enes} en gerelateerde data kan gevonden worden in
de data-repository [^data-repo]

[^data-repo]: de scenes in de data-repository kunnen gevonden worden op \url{github.com/BeardedPlatypus/thesis-data-suite/tree/master/scenes}


## Indoor: Spaceship Indoor
\input{./img/tex/test-suite-spaceship-frame.tex}

De Spaceship Indoor \mbox{sc\`ene}, weergegeven in figuur \ref{fig:test-suite-spaceship-frame}
is gebaseerd op de CG Lighting Challenge #18, gemodelleerd door Juan Carlos Silva.[^1] 
Deze \mbox{sc\`ene} staat model voor \mbox{indoor-sc\`enes}. De \mbox{sc\`ene} bestaat uit een middenstuk 
en een omliggend gangenstelsel. De grootste bron van details is afkomstig van 
de panelen in de gangen. 

Het camerapad en de lichtgeneratievolumes zijn weergegeven in figuur 
\ref{fig:test-suite-spaceship-map}. De camera, weergegeven met de blauwe pijl,
beweegt zich door de gangen en kruist hierbij twee maal het middenstuk.
Het pad bestaat uit $519$ frames. De lichten in het middenstuk 
hebben een radius van $30.0$, de lichten in het gangenstelsel een radius van
$23.0$. De lichtgeneratievolumes voor deze lichten zijn respectievelijk weergegeven
met rode en gele blokken.

[^1]: Scene url: \url{www.3drender.com/challenges/}


## Straatzicht: Piper's Alley
\input{./img/tex/test-suite-pipers-alley-frame.tex}

De Piper's Alley \mbox{sc\`ene}, weergegeven in figuur \ref{fig:test-suite-pipers-alley-frame}
is gebaseerd op de CG Lighting Challenge #42, gemodelleerd door Clint Rodrigues.[^2]
De scene beschrijft een enkele straat met grote diepte, waar aan weerszijde
huizen zijn geplaatst. In de verre diepte zijn een kloktoren en triomfboog zichtbaar.
De gebouwen zijn de bron van de meeste details. 

Het camerapad en de lichtgeneratievolumes zijn weergegeven in figuur
\ref{fig:test-suite-pipers-alley-map}. De camera, weergegeven met een blauwe pijl,
beweegt zich door het eerste deel van de straat gedurende $551$ frames. Alle 
lichtconfiguraties zijn gegenereerd met een radius van $180.0$. 
De lichtgeneratievolumes zijn weergegeven met gele blokken.

[^2]: Lighting challenge url: \url{forums.cgsociety.org/archive/index.php?t-1309021.html}


## Stadsscene: Ziggurat City
\input{./img/tex/test-suite-ziggurat-frame.tex}

De Ziggurat City \mbox{sc\`ene} is een onderdeel van de open film Sintel[^3]. 
De \mbox{sc\`ene} bestaat uit een gedetailleerde tempelberg waaromheen, in lagere 
resolutie, huizen en een stadsmuur zijn geplaatst. Deze \mbox{sc\`ene} staat model voor
grote openlucht \mbox{sc\`enes}.

Het camerapad en de lichtgeneratievolumes zijn weergegeven in figuur 
\ref{fig:test-suite-ziggurat-map}. De camera, weergegeven met een blauwe pijl,
beweegt zich eerst langs de trap omhoog, om vervolgens om de tempelberg heen te
vliegen. Het camerapad is $463$ frames lang. De lichten zijn onderverdeeld in 
twee sets. De lichten op de ziggoerat hebben een radius van $10.0$ en zijn met
een grotere dichtheid geplaatst. De lichten in de stad hebben een radius van $50.0$, 
en zijn verspreid over grotere volumes. De lichtgeneratievolumes voor deze lichten
zijn respectievelijk weergegeven met gele en rode blokken.

[^3]: Open film url: \url{durian.blender.org}

