# Algoritme

In deze sectie wordt het algoritme beschreven dat de basis vormt voor de 
implementatie binnen `nTiled`. De volledige set van datastructuren en 
algoritmes zal Hashed shading genoemd worden, naar de ruimtelijke hash-functies 
die de basis vormen van de octree implementatie, zoals eerder beschreven in de
theorie.

## Overzicht

\input{./img/tex/hs-overzicht.tex}

Het hashed shading algoritme vervangt de toekenning van clusters per pixel, 
met een verbindingsloze octree. De octree geeft een gevoxeliseerde beschrijving 
van de lichten binnen een scene. Elke blad knoop binnen bevat de lichten waarmee
de knoop overlapt. Deze lichten worden beschreven met een afstand en lengte binnen
de licht index lijst, zoals deze gespecificeerd is in tiled en clustered shading.
De grootte van de voxels kunnen door de gebruiker gespecificeerd worden.
Als de afstand en lengte binnen de licht indices lijst vast gesteld is, kan 
de licht berekening plaatsvinden zoals in tiled en clustered shading.

Bovenop de linkloze octree, en de lijsten van lichten en licht indices, 
wordt er aan de CPU kant een traditionele octree bijgehouden die alle
lichten bevat, en per licht een octree die het licht binnen de traditionele
octree beschrijft. Deze set van cotrees wordt gebruikt om de verbindingloze
octree op te stellen en aanpassingen aan de staat van de lichten efficient
up te daten.

Het hashed shading algoritme kan dus in drie componenten worden onderverdeeld;

* Opzoeken van licht informatie
* Constructie van de verschillende datastructuren
* Updaten van data binnen de lichtstructuur

Deze datastructuren en hoe deze samenhangen met deze componenten zijn geillustreed 
in figuur \ref{fig:hs-overzicht}. 

Binnen `nTiled` zijn de eerste twee componenten gerealiseerd. Een strategie
voor het updaten van de datastructuur zal besproken worden in de discussie. 

De constructie stap binnen hashed shading is een pre-process stap en kan worden
uitgevoerd voordat de daadwerkelijke rendering plaatsvindt. 
Deze constructie valt uit een in drie stappen. Eerst zal voor elk licht
een enkele licht boom berekend worden. Uit deze enkele lichtbomen wordt 
vervolgens de overkoepelende licht octree gebouwd worden. 
Nadat de licht octree opgesteld is, is het mogelijk om een verbindingloze 
octree op te stellen. De verbindingloze octree zal vervolgens gebruikt 
worden om de scenes mee te shaden.

In deze sectie zal de constructie van elk van de datastructuren worden
toegelicht. Tevens zal het algoritme voor het opzoeken van de licht informatie
worden toegelicht.

