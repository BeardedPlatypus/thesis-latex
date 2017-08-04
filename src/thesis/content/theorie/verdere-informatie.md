# Conclusie en verdere informatie

In dit hoofdstuk is een introductie gegeven tot real-time computergrafieken.
De perceptie en fysische eigenschappen van licht vormen de onderliggende basis
voor computergrafieken. Hierbij dienen de eigenschappen van licht en perceptie
gesimuleerd te worden om geloofwaardige afbeeldingen te cre\"eren. 
Deze simulatie kan grofweg in twee problemen worden opgedeeld:

* Wat is zichtbaar
* Hoe wordt het zichtbare waargenomen. 

Het eerste probleem komt neer op perspectiefprojectie en het visibiliteitprobleem. 
Het tweede probleem wordt opgelost door middel van het benaderen van 
de rendervergelijking. Binnen real-time computergrafieken wordt dit alles gerealiseerd
door middel van de moderne grafische pijplijn. Om deze pijplijn te gebruiken 
wordt binnen deze thesis gebruik gemaakt `openGL`.  

Voor een uitgebreidere beschrijving van de behandelde problemen kan gerefereerd worden 
aan de volgende boeken. Voor de psychologische grondslag van 
kleur en perceptie, kan gerefereerd worden naar Wolfe's Sensation 
and Perception\cite{wolfe2015sensation}. De fysica die ten grondslag ligt 
aan computergrafieken kan gevonden worden in Optics door Eugene Hecht 
\cite{hecht2016optics}. Meer toegepast op computergrafieken en tevens voor de 
behandeling van shading en raytracing, zijn de boeken Raytracing
from the ground up\cite{suffern2007ray}, en Physical Based Rendering 
\cite{pharr2016physically}, een goede basis.  Real-Time Rendering\cite{akenine2016real}
geeft een goede basis voor real-time rendering en de moderne grafische pijplijn. 
Meer informatie over `Direct3D` en `openGL` kan
gevonden worden op hun respectievelijke documentatiewebsites.  

