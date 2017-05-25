# Conclusie

In alle ge\"evalueerde gevallen presteert Tiled Shading beter dan de na\"ieve
implementatie. Doordat het aantal lichtberekeningen per fragment beperkt wordt,
zijn de exeuctietijden per frame ook consistenter. Dit uit zich vooral in de
executietijden van Forward Tiled Shading.

De CPU projectie implementatie vormt geen knelpunt. Dit ondersteund de stelling
in Tiled Shading\cite{olsson2011tiled}, dat voor aantal lichten in de orde van 
honderden, deze operatie effici\"ent op de CPU ge\"implementeerd kan worden.

Tevens is waargenomen dat voor scenes waar significante overlap tussen 
lichtvolumes ten opzichte van de camera-$z$-as is, Tiled Shading slechter,
presteert. In dit geval bevatten de tegels significant meer lichten, waardoor
het tijdsgedrag dat van het na\"ive algoritme in grotere mate benaderd.

Een laatste interessante observatie is dat de tegelgrootte weinig tot geen 
invloed op de executietijd lijkt te hebben. Vermoedelijk hangt dit samen
met de keuze van de grootte van de lichten gebruikt in de scenes. Deze zijn
veelal groot ten opzichte van de tegelgrootte. Hierdoor zullen veel naburige
tegels een vergelijkbare set van lichten bevatten. In dit geval is de invloed
van de tegelgrootte van minder belang. Indien de scene meer kleine lichten
bevat, kan het lonen om een kleinere tegelgrootte te selecteren.

# Discussie

## Ondersteunen van transparantie

In sectie \ref{sec:fds-transparantie} is vermeld dat Deferred Shading een aparte
Forward pijplijn vereist om transparante geometrie te renderen. Tiled Shading
biedt geen directe ondersteuning voor transparantie. Echter doordat de 
lichtberekeningen van Forward Tiled Shading en Deferred Tiled Shading 
gelijkaardig zijn, kan de implementatie versimpeld worden. Zowel het 
lichtmanagement als het opgestelde rooster kan gedeeld worden tussen de 
pijplijnen. Dit versimpelt de implementatie en verbetert de effici\"ency.\cite{olsson2011tiled}

## Evaluatie van verschillende tegelgroottes.

Om een beter inzicht te verkrijgen in de invloed van de tegelgrootte op
de executietijd, zou de lichtgrootte als parameter ge\"evalueerd dienen te 
worden. Hierbij is de verwachting dat kleinere tegelgroottes effici\"enter zijn
bij kleinere lichtvolumes. Bij grotere lichtvolumes is deze effici\"ency winst,
minimaal, zoals gevonden is in de resultaten. In dit geval kan beter gekozen 
worden voor grotere tegelgroottes, om zo het geheugenverbruik te beperken.

