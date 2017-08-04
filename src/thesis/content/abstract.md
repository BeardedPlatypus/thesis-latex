In deze thesis wordt een nieuw lichttoekenningsalgoritme ge\"introduceerd op
basis van de verbindingloze octree. Het doel hiervan is om een betere performantie te
verkrijgen dan de huidige lichttoekenningsalgoritmes Tiled en Clustered Shading,
door de opgestelde datastructuren tussen frames her te gebruiken. Hiervoor wordt 
de ruimte opgedeeld aan de hand van een een camera-onafhankelijke octree.
Veranderingen in de \mbox{sc\`ene} zullen relatief klein zijn tussen frames,
waardoor de kosten van het aanpassen van de datastructuur ook klein zijn.

Om de performantie van dit nieuwe algoritme te evalueren is gekeken naar de 
uitvoeringstijd en aantal lichtberekeningen per frame bij verschillende 
\mbox{sc\`enes}, resoluties en aantallen lichten. Eerst zijn de 
lichttoekenningsalgoritmes Tiled en Clustered Shading ge\"implementeerd. De 
resultaten van deze implementaties zijn vergeleken met de resultaten van
de implementatie van Hashed Shading.

De Hashed Shading implementatie is een factor twee sneller dan de Tiled Shading
implementatie en vereist de helft van het aantal lichtberekeningen. Het aantal
lichtberekeningen voor Hashed Shading met de kleinste knoopgroottes komt 
overeen met het aantal lichtberekeningen van Clustered Shading. 
Hashed Shading vereist daarnaast geen complete herberekening van de datastructuren
bij een verandering van het camerapunt. Op basis hiervan kan gesteld worden
dat het doel van deze thesis bereikt is.
Er zijn echter nog wel enkele problemen met de huidige implementatie van 
Hashed Shading. Op dit moment worden nog geen dynamische lichten ondersteund. 
Daarnaast gebruikt de huidige implementatie veel geheugen. Voor beide problemen
worden oplossingen voorgesteld.

