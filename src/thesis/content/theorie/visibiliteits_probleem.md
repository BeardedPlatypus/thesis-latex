# Perspectiefprojectie en het visibileitsprobleem

In sectie \ref{sec:fysische-werkelijkheid} zijn de twee problemen vastgesteld die opgelost dienen te 
worden om geloofwaardige afbeeldingen te generen. In deze sectie zal het eerste probleem
geadresseerd worden: wat is zichtbaar binnen een \mbox{sc\`ene} vanuit het huidige 
zichtpunt. Om te bepalen wat zichtbaar is dient zowel het perspectief 
gesimuleerd te worden, als bepaald te worden welk van de objecten in dit
perspectief als zichtbaar is.  

## Perspectiefprojectie

\input{./img/tex/vp-perspectief.tex}

De twee effecten van perspectief kunnen gesimuleerd worden door de driedimensionale 
\mbox{sc\`ene} te projecteren naar een oogpunt om deze zo af te beelden op een 
tweedimensionaal canvas\cite{suffern2007ray}. 
Dit is weergegeven in Figuur \ref{fig:vp-perspectief}. Het cameramodel gedefinieerd in de vorige sectie
wordt gebruikt om deze projectie mogelijk te maken. Dit leidt ertoe dat alle geometrie binnen
het zichtfrustum geprojecteerd zal worden op de oorsprong om zo het perspectief te 
simuleren\cite{suffern2007ray, akenine2016real}.

## Visibiliteitsprobleem

\input{./img/tex/vp-visibiliteit.tex}

Er is nu vastgesteld hoe objecten in perspectief afgebeeld kunnen worden op het canvas. 
Echter, hiermee is nog niet volledig vastgesteld wat daadwerkelijk 
zichtbaar gaat zijn op het tweedimensionale canvas. Hiervoor is het tevens nodig om te bepalen
welke delen van objecten zichtbaar zijn, en welke verborgen zijn achter andere 
objecten. Dit probleem is weergegeven in figuur \ref{fig:vp-visibiliteit}.
Door alleen de objecten af te beelden kan niet worden bepaald welk van de twee
afbeeldingen van de kubus en de bol correct is. Dit probleem wordt onder andere 
het visibiliteitsprobleem genoemd, en was een van de eerste grote problemen binnen
de computergrafieken\cite{Sutherland:1974:CTH:356625.356626}.  

De oplossing van het visibiliteitsprobleem kan gevonden worden in de realisatie
dat de bepaling van de zichtbare ruimte op een tweedimensionaal canvas, neerkomt op een sorteerprobleem.
Indien in een punt $\mathbf{p}$ bepaald moet worden welk primitief zichtbaar is, kan
met behulp van perspectiefprojectie de verzameling $S$ van objecten die afgebeeld worden op dit punt, 
opgesteld worden. Het object dat vervolgens zichtbaar is, 
zal het object in de verzameling $S$ zijn dat het dichtst bij het punt $\mathbf{p}$ en dus het zichtpunt van
de camera ligt. Indien de objecten in $S$ gesorteerd worden op basis van hun 
afstand tot de camera zal het eerste object het dichtst bij de camera liggen en dus
zichtbaar zijn. Gezien de afstand tot de camera overeenkomt met de $\mathbf{z}$-afstand
in cameraco\"ordinaten, dient dus het object met de kleinste $\mathbf{z}$-waarde gevonden 
worden. De algoritmes die dit probleem oplossen worden verborgen-oppervlaktebepalingsalgoritmes
genoemd\cite{warnock1969hidden, Sutherland:1974:CTH:356625.356626}.

De algoritmes die zowel de perspectiefprojectie als de visibiliteit oplossen kunnen grofweg 
worden ingedeeld in twee categorie\"en, raytracing-algoritmes en rasterisatie-algoritmes.
Het resultaat met betrekking tot het bepalen van de zichtbare geometrie van deze algoritmes 
zou in theorie hetzelfde moeten zijn.

Raytracing werkt op basis van het trekken van zogenoemde stralen uit het zichtpunt door
de pixels in de canvas. Vervolgens wordt gekeken of deze stralen snijden met primitieven.
Rasterisation beeldt de vertices van primitieven af op de canvas met behulp van de 
perspectiefprojectie. Vervolgens wordt bepaald welke pixels overlappen met het primitief.
In de volgende secties zal ingegaan worden op beide algoritmes.

