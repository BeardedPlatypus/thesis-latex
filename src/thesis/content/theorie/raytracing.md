# Raytracing

Zoals eerder vermeld, werkt raytracing door te kijken binnen een punt, wat het 
eerst zichtbare object is, wanneer een straal wordt getrokken vanaf het oogpunt
door $\mathbf{p'}$. Dit concept van stralen is geinspireerd door hoe de fysische
wereld werkt.  

Licht in de fysische wereld onder normale omstandigheden, zal zich als een 
rechte lijn voortplanten. Indien het een object raakt zal het gedeeltelijk
of in zijn geheel geabsorbeerd worden. Het deel van het licht dat niet 
geabsorbeerd wordt zal worden weerkaatst. De richting van de weerkaatsting 
hangt af van de lokale oppervlakte van het object waarop het licht weerkaatst.
Zowel ogen als cameras creeeren beelden, door over een bepaalde oppervlakte 
licht te bundelen op een vorm van een sensor, en dit te interpeteren.
In het geval van het oog, bundelt het hoornvlies licht op het netvlies. 
Binnen cameras wordt het licht doormiddel van een lens op een beeldsensor
geprojecteerd, waarna het wordt omgezet in een beeld.  

In theorie zou het mogelijk zijn om beelden op een zelfde manier op te bouwen,
zoals dit gebeurd in de fysische werkelijkheid. Hierbij zouden vanuit lichten
willekeurige stralen geschoten kunnen worden. Wanneer een dergelijke straal
door de canvas op het oogpunt valt, wordt deze meegeteld.  Dit is geillustreerd 
in figuur ... Deze techniek wordt forwaards tracen genoemedt. Echter vaak is de 
canvas van een camera velen malen kleiner dan de scene in kwestie. Dit zorgt 
ervoor dat de kans dat de canvasgeraakt wordt uitermate klein is. Hierdoor is 
een groot aantal lichtstralen nodig, voordat een geloofwaardige afbeelding 
wordt verkregen.  

Met de realisatie dat we uiteindelijk slechts de stralen nodig hebben, die 
door het canvas op het oogpunt vallen kunnen we de techniek omdraaien.
In plaats van willekeurige stralen te schieten vanuit lichten, schieten we,
per punt dat we willen weten op de canvas, een straal. 
Deze straal zal dus altijd het oogpunt raken, en door punt $\mathbf{p'}$ 
gaan. Vervolgens dient gekeken te worden welk object, als er een bestaat,
deze straal raakt. Hiermee wordt punt $\mathbf{p}$ gevonden. 
Vanaf $\mathbf{p}$ kunnen we bepalen welke lichten dit punt raken, en dus
hoe het punt $\mathbf{p'}$ gekleurd dient te worden. Dit zal verder 
besproken worden in de sectie over shading.  

Deze techniek, waarbij gestart wordt vanuit de camera wordt, achterwaardse 
tracing genoemd. Belangrijk om hierbij op te merken is dat ray tracing, dus voor
elk punt $\mathbf{p'}$ een punt $\mathbf{p}$ vindt. Wanneer gesteld wordt dat 
punt $\mathbf{p'}$ een (sub)pixel is, zou een algoritme dus bestaan uit twee 
loops. In de eerste plaats wordt per pixel een straal gegenereerd. Vervolgens 
wordt per straal gekeken over alle objecten welke object zowel door de straal 
geraakt wordt en het dichtstbij ligt. Doordat de buitenste loop over de pixels 
loopt, worden raytracing algoritmes dan ook wel beeldcentrische algoritmes 
genoemd.
De pseudo code zal er als volgt uitzien:  

```
for pixel in canvas:
    ray = construct_ray(eye, pixel)
    
    for object in scene:
        closest = None
        if (ray.hits(object) and 
           (closest == None or distance(object, eye) < distance(closest, eye))):
            closest = object
    
    do_shading(closest, ray)
```

Waarbij `do_shading` gebruikt wordt om de kleur te bepalen van de specifieke
pixel. Dit is verder geillustreerd in figuur ...

Dit concept is de basis voor alle raytracing algoritmes. Merk hierbij 
verder op, dat er geen expliciete perspectief projectie plaats vindt. 
Doordat stralen opgebouwd zijn beginnend in het oogpunt door
punt $\mathbf{p'}$, wordt het perspectief impliciet gedefineerd.

