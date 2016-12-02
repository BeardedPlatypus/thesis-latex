# Conclusie en verder informatie

In dit hoofdstuk is een introductie gegeven tot real-time computer graphics.
De perceptie en fysische eigenschappen van licht vormen de onderliggende basis
voor computergraphics. Hierbij dienen de eigenschappen van licht en perceptie
gesimuleerd te worden om geloofwaardige afbeeldingen te creeeren. 
Deze simulatie kan grofweg in twee problemen worden opgedeeld. 

* Wat is zichtbaar
* Hoe wordt het zichtbare waargenomen. 

Het eerste probleem leidt tot perspectief, en het visibiliteit probleem. 
Het tweede probleem wordt opgelost doormiddel van het benaderen van 
de renderingvergelijking. Binnen realtime graphics wordt dit alles gerealiseerd
door middel van de moderne grafische pijplijn. Om deze pijplijn te gebruiken 
wordt binnen deze thesis gebruik gemaakt `openGL`.  

Voor een uitgebreidere beschrijving van de behandelde problemen, is het mogelijk
om te referen naar de volgende boeken. Voor de psychologische grondslag van 
kleur en perceptie, kan gerefereerd worden naar Wolfe's Sensation 
and Perception (\cite{wolfe2015sensation}). De fysica die ten grondslag ligt 
aan computer graphics kan gevonden worden in Optics door Eugene Hecht 
(\cite{hecht2016optics}). Meer toegepast op computer graphics, en tevens voor de 
behandeling van shading en raytracing, zijn de boeken Raytracing
from the ground up (\cite{suffern2007ray}), en Physical Based Rendering 
(\cite{pharr2016physically}), een goede basis. Voor de basis van real-time 
rendering en de moderne grafische pijplijn vormt Real-Time Rendering 
(\cite{akenine2016real})een goede basis. De basis voor `Direct3D` en `openGL` kan
het beste begonnen worden bij hun respectievelijke documentatie websites.  

