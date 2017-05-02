In de voorgaande hoofdstukken zijn Tiled en Clustered shading ge\"introduceerd
als lichttoekenningsalgoritmes om voor fragmenten de set van lichten die 
ge\"evalueerd dient te worden bij de shading berekening, te beperken.
In dit hoofdstuk wordt Hashed shading als als alternatief lichttoekenningsalgoritme
ge\"introduceerd. Zowel Tiled als Clustered shading zijn camera-afhankelijk en 
de geassocieerde datastructuren dienen om deze reden per frame opnieuw opgebouwd
te worden. Hashed shading daarentegen gebruikt camera-onafhankelijke datastructuren,
waardoor deze niet opnieuw opgesteld dienen te worden per frame. Tegelijkertijd 
behaald het nog steeds een vergelijkbare versnelling en wordt niet significant 
meer geheugen gebruikt. Dit wordt bereikt door de lichten binnen de scene te 
representeren als een octree. 

In de volgende secties zal eerst de achterliggende theorie besproken worden, 
waarbij ingegaan wordt op de keuze voor de octree als spatiale datastructuur, en
hoe deze voorgesteld kan worden op de GPU. Vervolgens zal het het algoritme 
behandeld worden. Hierna zal de effici\"ency en het geheugengebruik aan de hand
van de testscenes ge\"evalueerd worden. Als laatste zullen deze resultaten
vergeleken worden met Tiled en Clustered Shading.

