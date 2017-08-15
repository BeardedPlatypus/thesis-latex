# Probleemstelling

In de introductie wordt het doel van deze thesis gesteld op het ontwikkelen 
van een lichttoekenningsalgoritme dat de opgestelde datastructuren hergebruikt 
tussen frames om zo tot een performantiewinst te komen ten opzichte van 
lichttoekenningsalgoritmes die datastructuren per frame opbouwen. Met de 
kennis van dit hoofdstuk kan dit doel onderbouwt worden.

Voor het renderen van een afbeelding met behulp van de directe-lichtbenadering
van de rendervergelijking dient per pixel het geprojecteerde punt bepaald 
te worden. Voor elk punt dient vervolgens de fragmentshader uitgevoerd te 
worden, waar voor elke lichtbron in de \mbox{sc\`ene} de lichtbijdrage wordt 
berekend. Dit komt neer op het uitrekenen van de interactie tussen het 
materiaal van het punt en het lichtbron. Dit leidt tot een groot aantal 
berekeningen. 

Door de optimalisatie om lichtbronnen te benaderen met een eindige
voorstelling, zal niet langer elk punt be\"invloed worden door elke lichtbron.
Algoritmes die voor een punt de verzameling van lichtbronnen in de \mbox{sc\`ene} 
beperken tot de deelverzameling van lichtbronnen die een bijdrage leveren aan de 
belichting van een punt, worden lichttoekenningsalgoritmes genoemd. 
Deze algoritmes reduceren het aantal lichtberekeningen in de fragmentshader.

De lichttoekenningsalgoritmes Tiled\cite{olsson2011tiled} en Clustered 
Shading\cite{olsson2012clustered} bouwen de datastructuren
die de lichttoekenning mogelijk maken, per frame op. Bij een hoge framerate
zal er weinig verschil zijn tussen opeenvolgende afbeeldingen. Het doel van deze
thesis is om tot een lichttoekenningsalgoritme te komen dat deze datastructuren
hergebruikt tussen frames om zo tot een betere performantie te komen dan 
huidige lichttoekenningsalgoritmes. Hiervoor zullen Tiled en Clustered Shading
geanalyseerd worden in volgende hoofdstukken. Daarna zal een nieuw lichttoekenningsalgoritme
ge\"introduceerd worden. Dit algoritme is camera-onafhankelijk waardoor de 
datastructuren niet per frame opgebouwd dienen te worden, maar hergebruikt
kunnen worden bij veranderingen in het zichtpunt.

# Besluit

In dit hoofdstuk is een introductie gegeven tot realtime computergrafieken.
De perceptie en fysische eigenschappen van licht vormen de onderliggende basis
voor computergrafieken. Hierbij dienen de eigenschappen van licht en perceptie
gesimuleerd te worden om geloofwaardige afbeeldingen te cre\"eren. 

Om de fysische werkelijkheid te benaderen dient de visibiliteit van objecten bepaald
te worden door perspectiefprojectie en het oplossen van het visibiliteitsprobleem. 
Vervolgens wordt door middel van het benaderen van de rendervergelijking 
een afbeelding gegenereerd.
Binnen realtime computergrafieken wordt dit alles gerealiseerd
met behulp van van de moderne grafische pijplijn. Om deze pijplijn te gebruiken 
wordt binnen deze thesis gebruik gemaakt `openGL`.  

