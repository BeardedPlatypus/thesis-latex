# Box projectie

Om lichten toe te kunnen kennen aan tiles, is het nodig om de bollen waarin een
puntlicht effect heeft, te projecteren op de view plane. Hiervoor is de techniek
gepresenteerd in ... gebruikt. 

[comment]: # 2D polyhedral bounds of a clipped perspective-projected 3d sphere

De versimpelde versie is geimplementeerd in `nTiled`. Hier zal kort toegelicht 
worden hoe deze techniek werkt. 

## Aanpak

In figuur ... is de situatie geschetst die opgelost dient te worden. We willen
een box tekenen om de geprojecteerde bol. Hiervoor dienen de uiterste waardes in
de x, en y-as berekend te worden. We kunnen dit probleem versimpelen door het 
niet in de 3d wereld op te lossen, maar in de xz en yz vlakken. Dit is mogelijk
doordat de uiterste x-waardes niet afhangen van de y-waardes en omgekeerd. 

Wanneer we de bol projecteren op het xz vlak, ontstaat het volgende figuur, 
waarin we de volgende waardes herkennen.

$O$ 
  ~ $(0, 0)$ ortographische projectie van de oorsprong op het $xz$-vlak

$\mathfrak{C}
  ~ $(x_\mathfrak{C} , y_\mathfrak{C} , z_\mathfrak{C} )$ Centrum van de bol in
  camera space

$C$
  ~ $ (x_\mathfrak{C}, z_\mathfrak{C} )$ ortographische projectie van het 
  centrum  van de bol op het $xz$-vlak.
  
$\vec{c}$
  ~ $C - O$ Vector van de oorsprong naar het centrum van de bol in het $xz$-vlak
  
$r$
  ~ Radius van de bol
  
Verder definieren we de volgende waardes. 

$\theta$
  ~ De hoek tussen $C$ en $T$

$T$
  ~ Bovenste begrensende punt

$B$
  ~ Onderste begrensende punt
  
$T'$
  ~ Projectie van $T$ op de viewplane
  
$t$
  ~ De afstand tot $T'$
  
$B'$
  ~ Projectie van $B$ op de viewplane
  
We kunnen nu de vector $\hat{\omega}$ definieren. Deze vector is gelijk aan 
$\vec{c} / ||c||$ geroteerd over $\theta$. Verder definieren we $t$ als de 
afstand tussen $O$ en $T$. 

$t = \sqrt{||c||^2 - r^2}$
$ \cos \theta = \frac{t}{c}$
$ \sin \theta = \frac{r}{c}$

We kunnen $T$ dan berekenen door.
$\hat{\omega} = \begin{bmatrix}\cos\theta & \sin\theta \\-\sin\theta &\cos\theta\end{bmatrix} $
$T = O + \hat{\omega}t$

$B$ kan vergelijkbaar berekend worden wanneer $\theta$ vervangen wordt door
$-\theta$.

Als laatste dient nu nog clipping meegenomen worden. 

Het Y waardes worden analoog berekend.

## Algoritme

Dit leidt vervolgens tot het volgende algoritme



