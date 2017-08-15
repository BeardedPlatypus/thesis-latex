In deze thesis wordt een nieuw lichttoekenningsalgoritme ge\"introduceerd in de
context van realtime rendering op basis van de verbindingloze octree. Het doel 
hiervan is om een betere performantie te
verkrijgen dan de huidige lichttoekenningsalgoritmes Tiled en Clustered Shading,
door de opgestelde datastructuren tussen frames te hergebruiken. Hiervoor wordt 
de ruimte opgedeeld aan de hand van een een camera-onafhankelijke octree.
Veranderingen in de \mbox{sc\`ene} zijn relatief klein tussen frames, 
waardoor de kost van het aanpassen van de datastructuur ook klein is.

Om de performantie van dit nieuwe algoritme te evalueren is gekeken naar de 
uitvoeringstijd en het aantal lichtberekeningen per frame bij verschillende 
\mbox{sc\`enes}, resoluties en aantallen lichtbronnen. Ter referentie zijn 
ook de lichttoekenningsalgoritmes Tiled en Clustered Shading ge\"implementeerd 
binnen hetzelfde programma. De  resultaten van deze implementaties zijn vergeleken.

De Hashed Shading implementatie vereist de helft van het aantal lichtberekeningen per
frame ten opzichte van Tiled Shading. Hierdoor is de Forward Hashed Shading implementatie
een factor twee sneller dan Forward Tiled Shading.
De beperking in het aantal lichtberekeningen met Hashed Shading met de kleinst
ge\"evalueerde knopen komt overeen met de reductie van het aantal lichtberekeningen
behaald binnen Clustered Shading. Daarnaast schaalt Hashed Shading in kleine mate
beter met de resoluties, doordat opdeling hier niet direct afhankelijk van is.

Daarnaast vereist Hashed Shading geen complete herberekening van de datastructuren
bij een verandering van het camerastandpunt, waardoor de kost ten opzichte van
Tiled en Clustered Shading afneemt. Op basis hiervan kan gesteld worden dat het doel van 
deze thesis bereikt is. Er zijn echter nog wel enkele beperkingen in de huidige implementatie 
van Hashed Shading. Op dit moment is slechts gekeken naar statische lichten. 
Het ondersteunen van dynamische lichten vereist wel dat de datastructuren van Hashed 
Shading bijgewerkt worden. Dit zal een extra kost met zich mee brengen. Echter doordat 
de verschillen tussen twee opeenvolgende frames klein zullen zijn, zal deze kost beperkt 
blijven. Daarnaast schaalt het geheugengebruik slecht met de knoopgrootte, waardoor
veel geheugen gebruikt wordt bij kleine knoopgroottes. Voor beide beperkingen worden oplossingen voorgesteld.

