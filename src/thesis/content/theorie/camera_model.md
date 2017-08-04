## Camera-model {#sec:camera-model}

\input{./img/tex/cm-camera.tex}

Om een afbeelding te genereren moet het zichtpunt en 
ori\"entatie gedefinieerd worden. Hiervoor wordt gebruik gemaakt
van een cameramodel\cite{CGF:CGF1181}. Dit cameramodel is een
beschrijving van een virtuele camera die zich bevindt binnen
de \mbox{sc\`ene}. Om deze camera te defini\"eren worden de 
volgende attributen opgesteld:

$\mathcal{O}_mathtext{camera}$ 
  ~ De positie van de camera in de \mbox{sc\`ene}.
  
up
  ~ De lokale $mathbf{y}$-as van de camera.
  
kijkrichting
  ~ De lokale $mathbf{z}$-as van de camera, waarin de camera kijkt.
  
Z-near
  ~ De afstand van de oorsprong tot het zichtvenster.
  
Z-far
  ~ De maximale afstand tot waar objecten worden weergegeven.
  
gezichtsveld $\theta$
  ~ De hoek die bepaald hoeveel van de wereld zichtbaar is.
  
aspectratio
  ~ De ratio breedte $\mathit{w}$ tot hoogte $\mathit{h}$ van het zichtvenster.
  
\noindent Dit specificeert de volledige camera, zoals weergegeven in figuur \ref{fig:cm-camera:vec}.
  
De *Z-near*, *Z-far*, oorsprong $\mathcal{O}_\mathtt{camera}$, gezichtsveld en
aspectratio defini\"eren het zogenoemde zichtfrustum. Dit frustum specificeert
de ruimte waarbinnen alle zichtbare objecten in de \mbox{sc\`ene} zich bevinden.

De kijkrichting kan vervangen worden met een centerpunt. Dit is dan de positie waar
de camera naar kijkt. De kijkrichting kan vervolgens gedefinieerd worden als
$\mathcal{O}_\mathtt{camera} - \mathbf{c}$. Dit is weergegeven in figuur \ref{fig:cm-camera:punt}.

