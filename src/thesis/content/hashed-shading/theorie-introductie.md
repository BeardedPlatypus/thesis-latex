# Theorie

In het algemeen kan gesteld worden dat het doel van lichttoekenning is om de 
ruimte zo effici\"ent mogelijk op te delen, opdat voor elk punt in de \mbox{sc\`ene} 
de verzameling van relevante lichtbronnen opgehaald kan worden. De relevante lichtbronnen zijn alle 
lichten die invloed hebben op het punt in kwestie, i.e. voor al deze lichten 
geldt dat het lichtvolume overlapt met dit punt. Een datastructuur dient deze
bevraging mogelijk te maken. Hiervoor dient de datastructuur de volgende attributen
te bezitten:

* Voor elk punt in de ruimte dient de datastructuur effici\"ent de relevante 
  lichten met zo'n groot mogelijke precisie terug te geven
* De datastructuur dient compact van aard te zijn, opdat het geheugengebruik minimaal is.
* De datastructuur moet dynamisch aan te passen zijn, indien lichten van positie
  of grootte veranderen.
* De datastructuur moet effici\"ent geconstrueerd kunnen worden.

Als laatste dient deze datastructuur verder camera-onafhankelijk te zijn,
opdat een verandering in het zichtvenster niet leidt tot een gehele heropbouw
van de datastructuren.

Tijdens het renderen zal per frame voor elk fragment de verzameling van relevante lichten 
opgehaald worden. Deze operatie zal dus het meest uitgevoerd worden. 
Tevens is het belangrijk dat de datastructuur compact is. Het beschikbare 
geheugen op de grafische kaart is beperkt, en een compacte voorstelling 
verkleint de gebruikte geheugenbandbreedte. 

In veel moderne toepassingen zijn lichten dynamisch van aard. Denk hierbij aan
lichten die geassocieerd zijn met objecten binnen de \mbox{sc\`enes}, zoals koplampen van
bewegende auto's, alsook lokale lichten die veranderen in intensiteit door 
veranderingen in de \mbox{sc\`ene}, zoals uitdovende vuren, of explosies. Een 
datastructuur dient instaat te zijn om dergelijke effecten te modelleren, zonder
dat de invloed op renderingstijd te groot wordt. Het is mogelijk om de datastructuur 
volledig opnieuw op te bouwen per frame, echter in veel gevallen
zijn deze veranderingen tussen frames klein en lokaal van aard, waardoor het 
effici\"enter kan zijn om de al opgestelde datastructuur (gedeeltelijk) te
hergebruiken.

Indien een datastructuur effici\"ent kan worden bijgewerkt gedurende de 
uitvoering, zal de effici\"entie van het initieel opstellen van de datastructuur 
van minder groot belang zijn, gezien deze stap eenmalig als een pre-processstap 
uitgevoerd kan worden. Vervolgens is het niet meer nodig om deze stap per frame
opnieuw uit te voeren.

\input{./img/tex/hs-tiled-clustered-subd.tex}

Binnen Tiled en Clustered Shading wordt de zichtvensterruimte onderverdeeld zoals
weergegeven in figuur \ref{fig:hs-tiled-clustered-subd}. In deze technieken wordt de
compactheid bereikt door slechts een klein deel van de ruimte te behandelen.
Het dynamisch karakter wordt in beide technieken behaald door per frame de
complete datastructuur opnieuw op te bouwen.

In de volgende secties zullen eerst enkele veel voorkomende spatiale 
datastructuren behandeld worden. Hierna zal toegelicht worden aan de hand van de 
bovengestelde eisen, waarom gekozen is voor de octree datastructuur. 
Vervolgens zal de achterliggende theorie behandeld worden om de octree datastructuur 
voor te stellen op de GPU.

