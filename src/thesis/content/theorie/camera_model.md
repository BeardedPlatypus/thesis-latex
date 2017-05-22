## Camera model {#sec:camera-model}

\input{./img/tex/cm-camera.tex}

Het gezichtspunt, of *camera* binnen deze thesis is het standaard camera 
model binnen computer graphics. Zoals geillustreerd in figuur  
\ref{fig:cm-camera}.  

De volgende vectoren en punten zijn hiervoor gedefinieerd

Up
  ~ De locale y-as van de camera.

Eye
  ~ (x, y, z) positie van de camera in wereld coordinaten.
  
Centre
  ~ (x, y, z) positie waarnaar de camera kijkt
  
Z-near
  ~ de near z plane waarop het beeld wordt geprojecteerd.
  
Z-far
  ~ Het vlak waarachter fragmenten niet meer worden weergegeven.
  
De *Z-near* en *Z-far* in combinatie met *Eye* creeert de view frustrum. Slechts
Primitieven binnen dit view frustum zullen worden gerenderd.

