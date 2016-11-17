# Definitie van licht

---
# Leiddraad
# - Definitie Licht
# - Beperking tot lichten met een eindige invloed (plaatje)
# - Conclusie / eigenschappen
---

Zoals eerder benoemd, draait de kern van deze thesis om het optimaliseren van
het aantal lichtberekeningen in real-time toepassingen. Om deze reden is het 
belangrijk om het concept licht zoals gebruikt in deze thesis te definieren. 
Wanneer er gesproken wordt van een licht, of een lichtbron zal altijd gedoeld 
worden op een eindige puntlichtbron die zich bevindt op punt $\mathbf{p}$ binnen
de scene.  

In de fysische wereld zijn lichten nooit eindig, echter de invloed die ze hebben
op de omringende wereld zal bij grotere afstand 0 benaderen. Binnen de fysische 
wereld is dit een gevolg van absorptie door het medium waardoor het licht zich 
beweegt. Dit proces wordt afstands demping genoemd. Binnen de physica wordt 
deze relatie vastgelegd met de wet van Lambert-Beer gedefinieerd voor 
uniforme demping als.  

$$ T = e^{-\mu\mathit{l}} $$

waar $\mathit{l}$ de padlengte van de straal licht door het medium is en $\mu$ 
de dempingscoefficient is.

Hierbij wordt de demping van het licht gerelateerd aan het medium waardor het 
zich beweegt. Dit leidt tot afstandsdempings (distance attenuation) curves zoals 
weergegeven in figuur ...  

Binnen veel real-time rendering toepassingen wordt afgestapt van dit fysische 
model. Er wordt gebruikt gemaakt van een eindige benaderingen van deze 
lichtbronnen. Waarbij wordt gesteld dat het licht geen invloed meer heeft na
afstand r. 

Dit leidt tot een voorstelling als weergegeven in figuur ...  
Hierbij is de invloed in de oorsprong gelijk aan $1$, en op afstand r en groter
0. 

Echter om de illusie te wekken dat de lichten fysiek accuraat zijn, dient tevens
een benadering gemaakt te worden van de afstandsdempings functies. 
Deze functies dienen te voldoen aan de eerder gestelde voorwaarde, waarbij 
de invloed een is in de oorsprong, en nul op afstand r.
Enkele veel gebruikte benaderingen als wel de daadwerkelijke afstandsdemping 
zijn gegeven in figuur ...

Binnen de thesis zelf is gekozen voor de benadering:

$$ (\left.\frac{\mathit{l}}{\mathit{r}}\right|_{[0,1]})^2 $$

Als laatste dienen we intensiteit van de lichtbron vast te leggen. Zoals 
gebruikelijk binnen computer graphics, is hier gekozen voor een rgb voorstelling. 
Waarbij de waardes zich bevinden in het bereik van 0 tot en met 1.

Dit alles leidt ertoe dat we een lichtbron kunnen definieren als de set van de 
volgende eigenschappen:

* De positie $\mathbf{p}$ van het licht ten opzichte van een coordinatenstelsel met oorsprong $O$
* Een afstand $\mathit{r}$ die de invloed van de lichtbron bepaald
* Een afstandsdempingsfunctie $f$ die het verval van invloed moduleert
* Een intensiteit $\mathbf{i}$ die de kleur en kracht van de lichtbron bepaald

