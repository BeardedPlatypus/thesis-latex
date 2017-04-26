In het voorgaande hoofdstuk zijn zowel Tiled als Clustered shading 
geintroduceerd. Deze technieken reduceren het aantal licht berekeningen dat 
gedaan moet worden. Hier staat tegenover dat deze technieken volledig 
afhankelijk zijn van de viewport. Hierdoor moet per frame opnieuw de tiles, en
clusters herberekend worden. In dit hoofdstuk wordt Hashed Shading 
geintroduceerd. De datastructuur die gebruikt wordt om een 3d coordinaat af te 
beelden op de set van relevante lichten, wordt volledig verplaatst naar het
geheugen van de grafische kaart. 

Deze datastructuur moet de volgende attributen bevatten:  

* De datastructureer moet het efficient op zoeken van relevante lichten bij een
  3d coordinaat faciliteren.  
* De datastructureer moet het mogelijk maken om veranderingen in lichten 
  efficient door te voeren.  
* De datastructuur dient efficient geconstruceerd te worden.  

Deze attributen zijn geordend op basis van belangrijkheid. Bij het renderen zal
op de eerste plaats voor elk fragment de relevante lichten opgezocht worden. 
Dit is de meest voorkomende operatie binnen het renderen van een scene.
Op de tweede plaats moet het mogelijk zijn om licht locatie en grootte aan te 
passen. Dit wordt triviaal ondersteund binnen zowel Clustered als Tiled shading.
Omdat er binnen Hashed shading niet per frame opnieuw een datastructuur wordt 
opgebouwd, is het van belang dat aanpassingen aan de datastructuur mogelijk zijn.
Onder normale omstandig heden zullen bestaande lichten niet in grootte mate 
verschillen tussen frames. Hierdoor zal het veelal niet nodig zijn om elke
frame updates uit te voeren. 
Het opbouwen van de datastructuur zal veelal slechts enkelmalig plaatsvinden
als pre-process stap, en kan, bij niet dynamische scenes, van te voren berekend
en vervolgens ingelezen kunnen worden. 
De laatste eigenschap waar aan voldaan moet worden, is dat de datastructuur,
efficient op de grafische kaart gebruikt dient te kunnen worden. 

In de volgende secties zal eerst een overzicht gegeven worden van de verschillende
datastructuren die voldoen aan de gestelde eisen. Vervolgens zal dieper ingegaan
worden op de theorie achter de gekozen datastructuur. 
Een overzicht van het opgestelde algoritme en de implementatie binnen `nTiled`, 
zal vervolgens gegeven worden. De effeciencie van de implementatie zal geevalueerd 
worden aan de hand van testen met de drie test scenes.  

