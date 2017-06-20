# Conclusie

In alle uitvoeringen verlaagt Tiled Shading het aantal lichtberekeningen ten
opzichte van de na\"ieve implementatie. Voor tegelgroottes van $16 \times 16$,
$32 \times 32$, en $64 \times 64$ resulteert dit in een verlaging van de 
uitvoeringstijd per frame. Voor $8 \times 8$ pixels is de constructietijd van
het lichtrooster groter dan de tijdswinst per frame tijdens het shaden.

Er is geen significant verschil in aantal lichtberekeningen waar te nemen bij
verschillende tegelgroottes. Dit kan een gevolg zijn van de grootte van de 
gebruikte lichten. Deze zijn zodanig groot dat het merendeel overlapt met 
meerdere tegels. Hierdoor zullen veel al vier $32 \times 32$ tegels dezelfde 
set lichten bevatten, als \mbox{\'e\'en} $64 \times 64$ tegel. Hierdoor wordt
dus relatief weinig winst behaald met kleinere tegels. Indien een scene veel 
kleine lichten zou bevatten, zal de lichttoekenning bij kleinere tegels 
verbeteren. Dit leidt tot kleinere sets van lichten, waardoor het aantal 
lichtberekeningen dan wel zou afnemen.

Bij het gebruik van een computationeel zwaardere shaders zal Tiled Shading 
relatief beter presteren De opbouw van het lichtrooster is onafhankelijk van de
complexiteit van de shader. De constructietijd, bij een bruteforce aanpak, is
slechts lineair afhankelijk van het aantal lichten in de scene en het aantal 
tegels in het lichtrooster. Wanneer een complexere shader wordt gebruikt, neemt
relatief de tijdswinst door de reductie van het aantal lichten toe. Voor
de gebruikte belichtingsberekening is nu al waar te nemen dat de uitvoeringstijd
van de Tiled Shading implementaties voor het overgrote deel afhankelijk zijn van
de constructietijd van het rooster. Deze tijd zal niet veranderen bij het 
gebruik van een andere shader.

Tiled Shading presteert slechter in situaties waar een groot aantal lichten
overlapt in de camera $\mathbf{z}$-as, zoals in de Piper's Alley scene.
In dit geval bevatten de tegels die snijden met deze overlappende lichten
significant meer lichten. Hierdoor zal voor deze tegels het na\"ieve tijdsgedrag
benaderd worden.


# Discussie

## Ondersteunen van transparantie

In sectie \ref{sec:fds-transparantie} is vermeld dat Deferred Shading een aparte
Forward pijplijn vereist om transparante geometrie te renderen. Tiled Shading
biedt geen directe ondersteuning voor transparantie. Echter doordat de 
lichtberekeningen van Forward Tiled Shading en Deferred Tiled Shading 
gelijkaardig zijn, kan de implementatie versimpeld worden. Zowel het 
lichtmanagement als het opgestelde rooster kan gedeeld worden tussen de
pijplijnen. Dit versimpelt de implementatie en verbetert de effici\"entie.\cite{olsson2011tiled}


## Optimalisatie met behulp van de diepte

De geteste implementatie deelt het zichtfrustum op zoals voorgesteld in figuur
\ref{fig:ts-grid-intro:frustum}. Echter het is mogelijk dat een tegelvolume 
slechts fragmenten tussen de dieptes $\mathit{z_{min}}$ en $\mathit{z_{max}}$
bevat, waar $\mathit{z_{min}}$ en $\mathit{z_{max}}$ tussen de uiterste waarde
van het zichtfrustum liggen. Deze waardes kunnen vervolgens gebruikt worden om
het volume geassocieerd met een tegel verder te reduceren.\cite{olsson2011tiled}
Hierdoor is het mogelijk om de set van relevante lichten te verkleinen, doordat 
lichten die buiten de dieptes $\mathit{z_{min}}$ en $\mathit{z_{max}}$ vallen, 
tevens uitgesloten kunnen worden. Om een dergelijke optimalisatie te implementeren,
dient de diepte van het frame voor de opbouw van het lichtrooster bekend te zijn.

Deze optimalisatie werkt goed indien een scene weinig diepte discontinu\"iteiten bevat.
Wanneer een scene wel deze fragmenten met uiteenlopende dieptes bevat, is het nog steeds
mogelijk dat het slechts mogelijke scenario zich voordoet.


## Evaluatie van verschillende tegelgroottes.

Om een beter inzicht te verkrijgen in de invloed van de tegelgrootte op
de uitvoeringstijd, zou de lichtgrootte als parameter ge\"evalueerd dienen te 
worden. Hierbij is de verwachting dat kleinere tegelgroottes effici\"enter zijn
bij kleinere lichtvolumes. Bij grotere lichtvolumes is deze effici\"entie winst
minimaal, zoals gevonden is in de resultaten. In dit geval kan beter gekozen 
worden voor grotere tegelgroottes, om zo het geheugenverbruik en de lichtroosterconstructietijd 
te beperken.

