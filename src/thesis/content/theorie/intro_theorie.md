Grofweg kan het process van het renderen van 3d scenes ingedeeld worden in twee
 problemen:  

* Wat is zichtbaar binnen een scene vanuit het huidige viewpoint.
* Hoe ziet datgene wat zichtbaar is er uit binnen onze afbeelding.

Wat afgebeeld wordt op een afbeelding, hangt af van twee aspecten, hoe wordt de 
3d scene op het 2d beeld geprojecteerd. En wat van elk object dat geprojecteerd 
kan worden is daadwerkelijk zichtbaar op de uiteindelijk afbeelding. Het eerste
wordt perspectief projectie genoemd. Het tweede probleem wordt het 
visibiliteitsprobleem probleem genoemd.  

Hoe hetgene wat afgebeeld wordt, er uiteindelijk uit ziet binnen onze 
afbeelding, wordt in de tweede stap bepaald. Deze stap wordt shading genoemd, 
en alle berekeningen gerelateerd aan kleur, absorptie, weerspiegeling etc, 
vallen hier onder.  

In de volgende secties zal kort ingegaan worden op zowel het 
visibiliteitsprobleem als shading, en hoe deze opgelost kunnen worden. Dit zal 
de basis vormen voor de plaatsing van het onderzoek in deze thesis binnen het 
complete veld van computer graphics.  

Eerst zal perspectief projectie en het visibileitsprobleem worden behandeld. 
Hierbij zal kort ingegaan worden op zowel raytracing als rasterisatie als 
algoritmes die het visibileitsprobleem oplossen. Vervolgens zal shading 
conceptueel behandeld worden. Als laatste zal gekeken naar de moderne graphische
pijplijn. Hier wordt beschreven worden hoe in huidige hardware zowel het 
visibileitesprobleem als shading wordt opgelost.

