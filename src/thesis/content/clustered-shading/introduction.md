Tiled Shading, zoals ge\"introduceerd in het vorige hoofdstuk, is een eerste
stap om effici\"entere lichttoekenning mogelijk te maken. Het doel hierbij is
om de effici\"entie van Deferred Shading met stencil-optimalisatie te benaderen
zonder dat dezelfde geheugenbandbreedte wordt gebruikt. Binnen Tiled Shading
wordt dit bereikt door een set van tegels te cre\"eren die het zichtveld 
bedekken. Voor elk van de tegels wordt bepaald, welke lichten invloed kunnen
hebben op de fragmenten binnen de tegel. Bij een effici\"ente implementatie
worden hierbij slechts de lichten bijgehouden die overlappen met het volume 
waarin de fragmenten van het tegel liggen. Dit volume wordt dus beperkt
door de fragmenten die het dichtst en het verst van de camera liggen.
Wanneer alle fragmenten in een tegel dicht bij elkaar liggen levert dit een
effici\"ente voorstelling op. Echter wanneer er zich binnen een tegel grote diepte
discontinu\"iteiten bevinden, leidt dit tot grote volumes bestaande uit grote
geometrisch lege ruimtes. Hierin liggen mogelijk veel lichten die geen invloed
hebben op de fragmenten in de tegel, wat leidt tot overbodige berekeningen.

Clustered Shading\cite{olsson2012clustered} is ge\"introduceerd om dit slechtste
scenario tegen te gaan, en tevens een effici\"entere en consistentere 
lichttoekenning mogelijk te maken. Hiervoor wordt het concept van tegels 
uitgebreid naar hogere dimensies. Deze hogere dimensie tegels worden clusters
genoemd. De meest voor de handliggende volgende dimensie is de diepte met 
respect tot de $\mathbf{z}$-as van de camera. Door de diepte expliciet op te
delen, heeft elke cluster een maximaal volume, onafhankelijk van het zicht.
Dit verhelpt het slechtste scenario van Tiled Shading, waarbij volumes 
geassocieerd met de tegels groter worden indien fragmenten verder uit elkaar
liggen. Tegelijkertijd verkleind het de volumes van de clusters, waardoor de
lichttoekenning specifieker, en dus effici\"enter wordt. Naast diepte, kunnen ook
andere attributen zoals de normaalinformatie van fragmenten meegenomen worden
om clusters op te stellen.

In dit hoofdstuk wordt het Clustered Shading algoritme behandeld. Hiervoor zal
eerst ingegaan worden op de theorie en het algoritme. Vervolgens zal de 
effici\"entie ge\"evalueerd worden aan de hand van de drie \mbox{testsc\`enes}.

