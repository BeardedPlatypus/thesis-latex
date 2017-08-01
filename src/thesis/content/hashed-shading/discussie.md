# Conclusie

In dit hoofdstuk is Hashed shading ge\"introduceerd met als doel om tot een
lichttoekenningsalgoritme te komen waarvoor de datastructuren niet per frame
opgebouwd dienen te worden. Door het hergebruik van de datastructuren zou
het mogelijk moeten zijn om een performantiewinst te verkrijgen ten opzichte van
de lichttoekenningsalgoritmes, Tiled en Clustered 
Shading. Enerzijds dient het gepresenteerde algoritme (een gedeelte van) de 
opgestelde datastructuren her te gebruiken. Anderzijds dient het algoritme het
aantal lichtberekeningen en dus de performantie met minimaal een zelfde factor
te reduceren als Tiled en Clustered Shading.

Om de opgestelde datastructuren te kunnen hergebruiken tussen frames, dient de
ruimteopdeling camera-onafhankelijk te zijn. Tevens dienen de datastructuren
effici\"ent voorgesteld te kunnen worden in het geheugen van de grafische kaart.
Er is gekozen voor een verbindingloze octree datastructuur die de lichten in de 
\mbox{sc\`ene} beschrijft. Hiermee is het mogelijk om enerzijds de set van relevante
lichten te verkrijgen in slechts enkele textuuropvragen en anderzijds
niet elk minimale knoopvolume expliciet voor te stellen door het gebruik van een
hi\"erarchische structuur.

Er is aangetoond dat het mogelijk is om de lichten in een scene met behulp van
een dergelijke structuur voor te stellen en op deze manier het aantal 
lichtberekeningen te beperken. Het geheugengebruik en de constructietijd is hierbij
in de eerste plaats afhankelijk van de grootte van de kleinste knopen. Er is een
kubisch verband waar te nemen tussen het geheugengebruik en constructietijd, en 
de grootte van de ribben van de kleinste bladknopen wanneer deze kleiner is dan
de diameter van de gebruikte lichten. 
Het aantal lichtberekeningen en de uitvoeringstijd is lineair afhankelijk van de 
grootte van de ribben van de kleinste bladknopen.

In vergelijking tot Tiled en Clustered Shading blijkt dat Deferred Hashed Shading een 
vergelijkbare uitvoeringstijd heeft als Deferred Tiled Shading. Forward Hashed Shading
is ongeveer een factor twee sneller dan Forward Tiled Shading. Hashed Shading vereist
voor alle ge\"evalueerde knoopgroottes minder lichtberekeningen dan Tiled Shading.
Clustered Shading vereist in de huidige implementatie nog steeds minder lichtberekenigen,
echter het verschil tussen Clustered Shading en Hashed Shading met de kleinste ge\"evalueerde knoopgrootte is minimaal. 

Op basis hiervan kan gesteld worden dat het inderdaad mogelijk is om met behulp 
van Hashed Shading een vergelijkbare performantie als Tiled en Clustered Shading te 
verkrijgen, zonder dat hiervoor de datastructuren opnieuw opgebouwd dienen te worden.
De huidige implementatie is echter nog niet performanter dan Clustered Shading.
Daarnaast is het geheugenverbruik van Hashed Shading groot, en zijn dynamische lichten nog niet ondersteund.

# Discussie

## Performantie

Op dit moment is het geheugenverbruik een beperkende factor voor de keuze van de 
knoopgrootte. Door het kubisch gedrag neemt het geheugenverbruik significant toe
wanneer een hogere precisie wordt vereist. De verwachting is dat bij een hogere
precisie het aantal lichtberekeningen verder zal afnemen, doordat per pixel slechts
relevante lichten worden berekend. Om dezelfde performantie te verkrijgen als 
Clustered Shading is het dus nodig om het geheugenprobleem op te lossen om zo
een hogere precisie in de voorstelling van lichten in de \mbox{sc\`ene} te verkrijgen.

Een oplossing voor dit probleem zal niet worden ge\"implemnteerd binnen deze thesis.
Echter een voorstel voor een mogelijke oplossing zal gedaan worden in het volgende hoofdstuk,
als mogelijk verder onderzoek.

Hiernaast is nog significante optimalisatie mogelijk voor de constructietijd, door
de opbouw van de octree te verplaatsen naar de grafische kaart. De opbouw van de octreevoorstelling
van de enkele lichten kan triviaal worden geparallelliseerd door deze voor de 
verschillende lichten tegelijkertijd uit te voeren. Daarnaast kunnen de verschillende lagen van de verbindingloze
octree onafhankelijk van elkaar worden opgesteld.

## Dynamische Lichten

Doordat de datastructuren niet meer per frame worden opgesteld, worden dynamische lichten
niet meer triviaal ondersteund. Dit is wel het geval voor Tiled en Clustered Shading.
Voor elk van de lichten die een transformatie ondergaat dient te worden nagegaan of deze
zodanig veranderd is dat de knopen waarop het licht invloed heeft anders zijn dan voor
de transformatie. Is dit het geval dan dienen deze knopen aangepast te worden. Dit leidt
tot extra rekentijd, die niet meegenomen is in de huidige evaluatie. De ondersteuning voor
dynamische lichten zal niet verder ge\"implementeerd worden binnen deze thesis, echter
een theoretische beschrijving van de oplossing zal gegeven worden als voorstel voor 
verder onderzoek.

