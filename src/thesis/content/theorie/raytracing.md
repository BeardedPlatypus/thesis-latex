## Raytracing

\input{./img/tex/rt-forward.tex}

Raytracing simuleert de werking van licht en het menselijk oog, en lost 
hiermee zowel het visibiliteitsprobleem als de perspectiefprojectie op.
Er is reeds vastgesteld dat menselijke waarneming berust op het waarnemen
van licht dat valt op de lens en geprojecteerd wordt op de retina, 
de lichtsensor. In theorie is het mogelijk om beelden op een zelfde manier op
te bouwen, zoals dit gebeurd in het oog. In dit geval zouden vanuit lichten
willekeurige stralen geschoten kunnen worden. Hierbij is een straal gedefinieerd
als zijnde een vector met een beginpunt in de oorsprong van een licht. 
Wanneer een dergelijke straal door de canvas op het oogpunt valt, wordt deze meegeteld.  Dit is 
ge\"illustreerd in figuur \ref{fig:rt-forward}. Deze techniek wordt forwaards 
tracen genoemdt. Vaak is het canvas van een camera velen malen kleiner 
dan de \mbox{sc\`ene} in kwestie. Dit zorgt ervoor dat de kans dat de canvas geraakt 
wordt, uitermate klein is. Hierdoor is een groot aantal lichtstralen nodig, 
voordat een geloofwaardige afbeelding wordt verkregen.  

Met de realisatie dat we uiteindelijk slechts de stralen nodig hebben, die 
door het canvas op het oogpunt vallen is in te zien dat de techniek ook omgedraaid kan worden.
In plaats van willekeurige stralen te schieten vanuit lichten, wordt er
door elk punt op de canvas een straal getrokken vanuit het zichtspunt.
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
lussen. In de eerste plaats wordt per pixel een straal gegenereerd. Vervolgens 
wordt per straal gekeken voor alle objecten, welke object zowel door de straal 
geraakt wordt en het dichtstbij ligt. Doordat de buitenste lus over de pixels 
loopt, worden raytracing-algoritmes dan ook wel beeldcentrische algoritmes 
genoemd. De pseudo code is weergegeven in listing \ref{lst:rt-alg}.

\input{./lst/rt-alg.tex}
\input{./img/tex/rt-raytracing.tex}

Waarbij `do_shading` gebruikt wordt om de kleur te bepalen van de specifieke
pixel. Dit is verder ge\"illustreerd in figuur \ref{fig:rt-raytracing}. 
Hierbij worden eerst de punten op de canvas opgesteld. Vervolgens wordt
door elk van deze punten een straal getrokken, en wordt gekeken of deze
snijden met een primitief. Vervolgens worden alle pixels gemarkeerd die
snijden.

Dit concept is de basis voor alle raytracing algoritmes. Merk hierbij 
verder op, dat er geen expliciete perspectief projectie plaats vindt. 
Doordat stralen opgebouwd zijn beginnend in het oogpunt door
punt $\mathbf{p'}$, wordt het perspectief impliciet gedefinieerd.

