## Raytracing

\input{./img/tex/rt-forward.tex}

Raytracing simuleert de werking van licht en het menselijk ook, en lost 
hiermee zowel het visibiliteitsprobleem als het perspectief op.
Er is reeds vastgesteld dat menselijke waarneming berust op het waarnemen
van licht dat valt op de lens en geprojecteerd wordt op de retina, 
de lichtsensor. In theorie is het mogelijk om beelden op een zelfde manier op
te bouwen, zoals dit gebeurd in het oog. In dit geval zouden vanuit lichten
willekeurige stralen geschoten kunnen worden. Hierbij is een straal gedefinieerd
als zijnde een vector met een beginpunt en een richting. Wanneer een dergelijke
straal door de canvas op het oogpunt valt, wordt deze meegeteld.  Dit is 
geillustreerd in figuur \ref{fig:rt-forward}. Deze techniek wordt forwaards 
tracen genoemedt. Echter vaak is het canvas van een camera velen malen kleiner 
dan de scene in kwestie. Dit zorgt ervoor dat de kans dat de canvas geraakt 
wordt, uitermate klein is. Hierdoor is een groot aantal lichtstralen nodig, 
voordat een geloofwaardige afbeelding wordt verkregen.  

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

\input{./img/tex/rt-raytracing.tex}

Waarbij `do_shading` gebruikt wordt om de kleur te bepalen van de specifieke
pixel. Dit is verder geillustreerd in figuur \ref{fig:rt-raytracing}

Dit concept is de basis voor alle raytracing algoritmes. Merk hierbij 
verder op, dat er geen expliciete perspectief projectie plaats vindt. 
Doordat stralen opgebouwd zijn beginnend in het oogpunt door
punt $\mathbf{p'}$, wordt het perspectief impliciet gedefineerd.

