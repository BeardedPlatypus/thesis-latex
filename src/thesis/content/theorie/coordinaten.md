## Coordinaten Stelsels

Zoals reeds vermeld in sectie \ref{sec:mathematische-notatie} wordt een drie 
dimensionale ruimte $\mathbb{R}^3$ gebruikt om de scenes voor te stellen. 
Waarbij punten zich bevinden op positie $\mathbf{p}$. 
Voordat een dergelijk punt echter een betekenis heeft, dient een oorsprong en 
een set van drie onafhankelijke vectoren te worden gedefinieerd. Deze combinatie
van oorsprong en basis wordt een co\"ordinatenstelsel genoemd. Hiermee is het
mogelijk om punt $\mathbf{p}$ eenduidig vast te leggen in de Euclidische 
ruimte. De oorsprong beschrijft het nulpunt, waaraan alle punten relatief zijn.
De drie onafhankelijke vectoren, of assen, defini\"eren vervolgens hoe de 
positie van punt $\mathbf{p}$ relatief aan de oorsprong verkregen kan worden.

\input{./img/tex/coord-stelsel.tex}

Binnen de meeste 3D pakketten wordt een Carthesisch rechtshandig 
co\"ordinatenstelsel gebruikt. Een Carthesisch co\"ordinatenstelsel is 
gedefinieerd aan de hand van drie loodrechte vlakken, waarbij een punt de positie
op elke as beschrijft. Dit is weergegeven in figuur \ref{fig:coord-stelsel}
De orientatie van een co\"ordinatenstelsel is afhankelijk van de richting en 
volgorde van de assen. Binnen deze thesis wordt altijd gebruik gemaakt van
rechtshandige co\"ordinatenstelsels, zodanig dat de $y$-as omhoog wijst, en de
$x$-as naar rechts. De negatieve $z$-as wijst vervolgens voorwaards. Positieve 
rotaties zijn in dit geval tegen-de-klok-in.

Een belangrijke observatie is dat het mogelijk is om van co\"ordinatenstelsel 
te veranderen door transformatie en projectie matrices toe te passen op de basis
en oorsprong, en dus op alle objecten binnen een bepaalde ruimte. Hierdoor is het 
mogelijk om verschillende co\"ordinatenstelsels te defini\"eren. Om een scene 
op te stellen worden de volgende co\"ordinatenstelsels gebruikt.

\input{./img/tex/coord-ruimtes.tex}

Per mesh wordt gebruik gemaakt van een *modelruimte* om de posities van de 
vertices en daarmee dus de triangles te defini\"eren. Dit referentiekader is
onafhankelijk van andere meshes.

Zoals eerder vermeld in sectie \ref{sec:geometrische-def} is voor elk object een
aparte transformatiematrix opgesteld. Hiermee wordt de geasoccieerde mesh 
omgezet van *modelco\"ordinaten* naar *wereldco\"ordinaten*. Met \'e\'en scene is
\'e\'en *wereldruimte* geassocieerd. Dit co\"ordinatenstelsel beschrijft de 
onderlinge relatie tussen objecten, lichten, en cameras die zich bevinden in de
scene.

Om de wiskunde van het renderen te vergemakkelijken wordt tevens nog een 
cameraruimte opgesteld, waarbij de scene zodanig wordt getransformeerd dat 
de oorsprong overeenkomt met de positie van de camera. De negatieve $z$-as komt
overeen met de kijkrichting, en de $x$- en $y$-assen komen overeen met de 
viewport van de camera. Deze transformatie wordt bereikt met behulp van de
LookAt matrix, die verder zal worden toegelicht in de volgende secties.

In de laatste stap voordat het renderalgoritme plaatsvindt, dient de 
cameraruimte nog omgezet te worden naar Normalised Device Coordinates (NDC).
Dit is een twee dimensionaal co\"ordinatenstelsel die de afbeelding van de
scene op de viewport beschrijft in coordinaten van $-1$ tot $1$. Ook dit zal 
verder toegelicht worden in de volgende secties.

De onderlinge relatie van de verschillende ruimtes, en hoe deze in elkaar om te
zetten zijn, is weergegeven in figuur \ref{fig:coord-ruimtes}.

