# Theorie

In het algemeen kan gesteld worden dat lichttoekenning er om draait om de ruimte
zo effici\"ent mogelijk op te delen, zodat voor elk fragment slechts de lichten
die daadwerkelijk invloed hebben, snel opgehaald kunnen worden. 
De datastructuur die gebruikt wordt om de ruimte onder te verdelen dient dus de
volgende attributen te bezitten

* Voor elk punt in de ruimte dient de datastructuur effici\"ent de relevante 
  lichten met zo'n groot mogelijke precisie terug te geven
* De datastructuur dient compact van aard te zijn.
* De datastructuur moet dynamisch aan te passen zijn, indien lichten van positie
  of grootte veranderen.
* De datastructuur dient effici\"ent te construeren zijn.

Bij het renderen zal bij elke frame voor elk fragment de set van relevante 
lichten opgehaald dienen te worden. Dit is dus de operatie die het meest 
uitgevoerd zal worden. Tevens is het belangrijk dat de datastructuur compact is.
Het beschikbare geheugen op de grafische kaart is beperkt, en een compacte 
voorstelling verkleint de gebruikte geheugenbandbreedte. 

In veel moderne toepassingen zijn lichten dynamisch van aard. Denk hierbij aan
lichten die geassocieerd zijn met objecten binnen de scenes, zoals koplampen van
bewegende autos, als ook lokale lichten die veranderen in felheid door 
veranderingen in de scene, zoals uitdovende vuren, of explosies. Een 
datastructuur dient instaat te zijn om dergelijke effecten te modeleren, zonder
dat de renderingstijd negatief be\"invloed wordt. Het is mogelijk om de 
datastructuur volledig opnieuw op te bouwen per frame, echter in veel gevallen
zijn deze veranderingen tussen frames klein en lokaal van aard, waardoor het 
veelal effici\"enter is om de al opgestelde datastructuur (gedeeltelijk) her te
gebruiken.

Indien een datastructuur effici\"ent kan worden bijgewerkt gedurende de 
uitvoering, zal de effici\"encie het initieel opstellen van de datastructuur 
van minder groot belang zijn, gezien deze stap als een pre-process stap 
uitgevoerd kan worden. 

\input{./img/tex/hs-tiled-clustered-subd.tex}

Binnen tiled en clustered shading wordt de viewport ruimte onderverdeeld zoals
weergegeven in figuur \ref{fig:hs-tiled-clustered-subd}. Hierin wordt de
compactheid bereikt door slechts een klein deel van de ruimte te behandelen.
Het dynamisch karakter wordt in beide technieken behaald door per frame de
complete datastructuur opnieuw op te bouwen.

In de volgende secties zullen eerst enkele veel voorkomende spatiale 
datastructuren behandeld worden. Hierna zal toegelicht worden aan de hand van de 
bovengestelde eisen, waarom gekozen is voor de octree datastructuur. 
Vervolgens zal de achterliggende theorie van de octree datastructuur behandeld
worden en hoe deze voorgesteld kan worden op de GPU.

