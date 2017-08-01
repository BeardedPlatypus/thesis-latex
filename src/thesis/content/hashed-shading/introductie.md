In de voorgaande hoofdstukken zijn Tiled en Clustered Shading ge\"introduceerd.
Het doel van deze lichttoekenningsalgoritmes is om voor elk fragment een set van
relevante lichten te bepalen, om zo het aantal lichtberekeningen terug te 
brengen. In dit hoofdstuk wordt Hashed Shading als alternatief 
lichttoekenningsalgoritme ge\"introduceerd. 

Zowel Tiled als Clustered Shading zijn camera-afhankelijk en  de geassocieerde 
datastructuren dienen om deze reden per frame opnieuw opgebouwd te worden. 
Hashed shading daarentegen gebruikt camera-onafhankelijke datastructuren, 
waardoor deze hergebruikt kunnen worden tussen frames. Tegelijkertijd behaald het 
nog steeds een vergelijkbare versnelling en wordt het geheugengebruik beperkt door 
gebruik te maken van een hi\"erarchische onderverdeling van de ruimte van de \mbox{sc\`ene}.

In de volgende secties zal eerst de achterliggende theorie besproken worden, 
waarbij ingegaan wordt op de keuze de spatiale datastructuur, en
hoe deze voorgesteld kan worden op de GPU. Vervolgens zal het het algoritme 
behandeld worden. Hierna zal de effici\"entie en het geheugengebruik aan de hand
van de \mbox{testsc\`enes} ge\"evalueerd worden. Als laatste zullen deze resultaten
vergeleken worden met de resultaten van Tiled en Clustered Shading.

