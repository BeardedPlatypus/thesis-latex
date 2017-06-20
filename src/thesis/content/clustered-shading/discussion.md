# Conclusie

Op basis van het aantal lichtberekeningen presteert Clustered Shading beter dan
Tiled Shading. Doordat beter onderscheid gemaakt kan worden in de 
camera-$\mathbf{z}$-as bevatten clusters kleinere sets lichten. Dit leidt tot 
een reductie in het aantal lichtberekeningen ten opzichte van Tiled Shading. 
Tevens zorgt het voor een consistenter aantal lichtberekeningen tussen frames,
doordat lichtoverlap met respect tot de camera-$\mathbf{z}$-as geen significante
rol meer speelt. Het aantal lichtberekeningen binnen Clustered Shading blijft 
echter lineair afhankelijk van zowel het aantal pixels als het aantal lichten in
de scene.

Vergelijkbaar met Tiled Shading lijkt de tegelgrootte geen significante invloed
te hebben op het aantal lichtberekeningen voor de ge\"evalueerde scenes. Dit is
opnieuw toe te schrijven aan de grootte van de lichten binnen de scenes.
Doordat deze veelal overlappen met een groot aantal lichten zullen naburige 
clusters veelal dezelfde sets van lichten bevatten.

De uitvoeringstijden van een geheel frame, en om de set van clusters op te bouwen
zijn niet expliciet ge\"evalueerd. Hiervoor is gekozen omdat de uitvoeringstijd
van het opbouwen van de clusters grotendeels wordt bepaald door de `glGetTexImage`
functie. Daarnaast is de voorgestelde methode om lichten toe te kennen aan de 
clusters\cite{olsson2012clustered} niet ge\"implementeerd. Om deze redenen is 
het niet mogelijk om een accurate vergelijking te maken tussen Tiled en 
Clustered Shading met betrekking tot de uitvoeringstijd.

Forward Clustered Shading is niet expliciet ge\"evalueerd omdat de toevoeging
van de z-prepass een significante aanpassing aan de structuur van de shader 
vereist. Hierdoor wordt een vertekend beeld verkregen bij een directe 
vergelijking.


# Discussie

## Lichttoekenning op de GPU

In de originele implementatie van Clustered Shading wordt gebruik gemaakt van
een Bounding Volume Hierarchy\cite{olsson2012clustered} met een splitsingsfactor
van 32. Een dergelijke voorstelling maakt het mogelijk om effici\"enter lichten
toe te kennen aan de clusters dan met de bruteforce aanpak gebruikt in `nTiled`.
Hierdoor kunnen grotere aantallen lichten in een realtime setting gebruikt worden.

Deze aanpak is tevens te implementeren op de grafische kaart. Hierdoor kunnen 
deze lichttoekenningsoperaties parallel uitgevoerd worden, wat de constructie 
verder reduceert. Wanneer het opbouwen van de clusters op de grafische kaart
plaatsvindt, is er geen reden meer om de clustergegevens uit het videogeheugen
op te halen. Hierdoor dient de `glGetTexImage` functie niet meer uitgevoerd
te worden, wat de bottleneck in de Clustered Shading implementatie binnen
`nTiled` zou verhelpen.

Wanneer deze twee aanpassingen gedaan zouden worden, zou de uitvoeringstijd
van Clustered Shading kleiner dan de uitvoeringstijd van Tiled Shading en de
na\"ieve implementatie moeten zijn.

