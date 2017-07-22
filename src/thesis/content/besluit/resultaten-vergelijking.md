# Conclusie

De hypothese gesteld aan het begin van deze thesis, is dat het mogelijk moet
zijn om een lichttoekenninngsalgoritme te ontwerpen dat berekeningen van 
voorgaande frames hergebruikt om zo tot een betere performantie te komen dan
huidige lichttoekenningsalgoritmes. De moderne lichttoekenningsalgoritmes die
als referentie voor dit nieuwe lichttoekenningsalgoritme zijn genomen, zijn
Tiled Shading \cite{} en Clustered Shading \cite{}. 

Om te voldoen aan de gestelde hypothese dient het nieuw ontwikkelde 
lichttoekenningsalgoritme voor zowel Forward als Deferred pijplijnen een 
minimaal vergelijkbare versnelling te verkregen te worden als deze algoritmes 
opleveren. Om dit te evalueren is gekeken naar zowel de uitvoeringstijd per
frame, als het aantal lichtberekeningen dat per frame dient te worden 
uitgevoerd. Deze waardes zijn ge\"evalueerd binnen drie scenes, die samen
model staan voor de verschillend mogelijke scenes die voorkomen in moderne 
games. Deze waardes zijn verzameld met verschillende aantallen lichten en
bij verschillende resoluties.

Hashed Shading is het lichttoekenningsalgoritme ontwikkeld binnen deze thesis.
Er is voor gekozen om de onderverdeling van de ruimte camera-onafhankelijk te 
maken. Hierdoor is het mogelijk om de opgestelde onderverdeling her te 
gebruiken tussen frames, indien deze niet verandert. Deze onderverdeling 
is ge\"implementeerd in de vorm van een octree. Deze hi\"erarchische structuur
maakt het mogelijk om de onderverdeling van de ruimte waarin de lichten vallen,
effici\"ent en met hoge precisie voor te stellen. Om waardes effici\"ent op te 
kunnen vragen op de grafische kaart is gebruik gemaakt van de verbindingloze 
octree voorstelling \cite{}. De resultaten van dit nieuwe 
lichttoekenningsalgoritme zijn vergeleken met die van Tiled en Clustered Shading.

Ongeacht het lichttoekenningsalgoritme is zowel het aantal lichtberekeningen als
de uitvoeringstijd lineair afhankelijk van het aantal pixels, en het aantal 
lichten. De drie lichttoekenningsalgoritmes reduceren allen echter de factor van
deze lineaire afhankelijkheid. Doordat de factor gereduceerd wordt, wordt tevens
de variatie in uitvoeringstijd tussen frames gereduceerd. Hierdoor wordt een
constantere framerate verkregen.

In elk van de testen presteerde de Deferred pijplijn beter dan de Forward 
Pijplijn. Dit is een direct gevolg van de ontkoppeling van de geometrische
complexiteit van de shading complexiteit. Deze verbetering in uitvoeringstijd
is ten koste van het geheugengebruik. Voor Deferred Shading is het nodig om
GBuffers op te stellen. Hierin wordt voor elk van de verschillende attributen
die nodig zijn in de lichtberekening een textuur ter grootte van het zichtsveld
bijgehouden. Een tweede nadeel is dat Deferred Shading geen transparantie 
ondersteunt. Hiervoor dient een aparte Forward pijplijn opgesteld te worden. 
Een voordeel van elk van de ge\"evalueerde lichttoekenningsalgoritmes is dat de 
opgestelde datastructuren zowel voor de Deferred als deze Forward pijplijn gebruikt
kunnen worden, zonder dat deze opnieuw berekend dienen te worden.

Tiled Shading reduceert het aantal lichtberekeningen en de uitvoeringstijd ten
opzichte van de na\"ieve implementatie. Dit wordt bereikt door het zichtsveld in 
tegels onder te verdelen, en voor elk van deze tegels de lichten die overlappen 
met deze tegel bij te houden. Hierbij wordt ongeveer een factor drie tot vier
verbetering waargenomen in zowel de uitvoeringstijd als het aantal lichtberekeningen.
De tegelgrootte leek hierbij geen significante invloed te hebben.
In de situatie dat er een significante overlap van lichten in het zichtvenster was, 
presteert Tiled Shading significant slechter. Dit is het gevolg van een gbrek aan
opdeling in de camera-$\mathbf{z}$-as. Hierbij benadert het aantal lichtberekeningen
in deze tegels dat van de na\"ive implementatie.

Clustered Shading verlaagt het aantal lichtberekeningen door bovenop de onderverdeling
van het zichtvenster in tegels, ook deze tegels verder onder te verdelen in de 
camera-$\mathbf{z}$-as. Hiermee wordt het slechts mogelijke scenario van Tiled Shading
voorkomen, en een betere lichttoekenning in het algemeen bereikt. Ook binnen Clustered
Shading is geen significante invloed waar te nemen van de tegelgrootte op het aantal
lichtberekening.
Een bijkomende eis voor Clustered Shading is dat de dieptebuffers beschikbaar zijn op
het moment dat de clusters opgesteld worden. Dit is geen probleem binnen de Deferred
Shading pijplijn, maar vereist een extra pas om deze buffers te vullen binnen de 
Forward Shading pijplijn.

Hashed Shading benadert voor kleine knoopgroottes het aantal lichtberekeningen van 
Clustered Shading. Daarnaast is de Forward Shading pijplijn implementatie ongeveer
twee maal sneller dan de Forward Tiled Shading implementatie. De opgestelde 
datastructuren kunnen bij statische lichten direct hergebruikt worden zonder dat 
een herberekening vereist is. Er zijn echter nog wel twee grote problemen te
identificeren binnen de huidige implementatie van Hashed Shading. De eerste is 
het geheugengedrag van Hashed Shading. Bij kleinere knoopgroottes neemt het 
geheugengebruik kubiek toe. Hierdoor kan de huidige implementatie nog niet 
dezelfde precisie behalen als Clustered Shading. Het tweede probleem is het gebrek
aan ondersteuning voor dynamische lichten. Doordat de datastructuren hergebruikt 
worden zullen deze niet automatisch veranderingen in lichten reflecteren. Doordat
deze veranderingen expliciet moeten worden doorgevoerd, zal het ondersteunen van
dynamische lichten altijd tot een toename in uitvoeringstijd leiden.

Op basis van deze resultaten kan gesteld worden dat het mogelijk is om een camera-onafhankelijk
lichttoekenningsalgoritme op te stellen op basis van de verbindingloze octree \cite{}. 
Een dergelijke implementatie kan een vergelijkbare reductie van lichtberekeningen zorgen
als Clustered Shading. Hiermee is het doel van deze thesis gerealiseerd.
Echter de huidige implementatie van Hashed Shading is nog niet robuust genoeg om
Clustered Shading te vervangen. Hiervoor zal eerst het geheugengebruik van Hashed
Shading verlaagd moeten worden, en zullen dynamische lichten effici\"ent ondersteund
moeten worden. Hiervoor is verder onderzoek nodig. Enkele mogelijke oplossingen
voor deze problemen zijn in de volgende sectie uitgewerkt.

