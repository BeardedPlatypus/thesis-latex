\input{./img/tex/cs-opdeling-voorbeeld.tex}

# Theorie 

Het doel van Clustered Shading is om de lichttoekenning zoals in Tiled Shading
te verbeteren door de twee-dimensionale tegels, verder uit te breiden, zodat
hogere dimensie clusters ontstaan. Hiertoe worden de tegelvolumes onder verdeeld 
in de diepte. Verdere dimensies kunnen toegevoegd worden op basis van andere
attributen, zoals de normaalinformatie van fragmenten. Een voorbeeld van 
een dergelijke onderverdeling is te zien in figuur \ref{fig:cs-opdeling-voorbeeld}
Door de tegels verder op te delen worden de volumes geassocieerd met deze
tegels kleiner, en dus homogener, waardoor de effici\"ency van de 
lichtberekening toeneemt.

## Onderverdeling in de ruimte {#sec:cs-onderverdeling}

De eerste stap in het uitbreiden van tegels naar hogere dimensies is het 
vastleggen hoe de diepte onderverdeeld dient te worden. Voor een effici\"ente
lichttoekenning is het van belang dat de clusters zo klein mogelijk zijn, zodat
deze zo nauwkeurig mogelijk de relevante set van lichten kunnen beschrijven.
Tegelijkertijd moeten clusters zoveel mogelijk (homogene) fragmenten bevatten,
zodat het geheugenverbruik laag blijft, terwijl de clusters effici\"ent 
opgehaald kunnen worden. Tevens is het belangrijk dat de sleutel waarmee een 
cluster ge\"identificeerd kan worden, effici\"ent berekend kan worden, en 
tegelijkertijd weinig bits vereist.

\input{./img/tex/cs-sleutel.tex}

Een belangrijk inzicht is dat fragmenten van een frame altijd in het 
zichtfrustum geassocieerd met het frame zullen vallen. Wanneer de 
lichtoekenningsdatastructuren dus per frame opgebouwd worden, zoals het geval is
bij Tiled en Clustered Shading, is het niet nodig om de gehele wereld op te 
delen in volumes. Alleen het zichtfrustum dient opgedeeld te worden. 
Tiled Shading deelt het zichtvenster op in de $\mathbf{x}$- en $\mathbf{y}$-as.
Dit impliciet een opdeling van het zichtfrustum. Binnen Clustered Shading
wordt de $\mathbf{z}$-as van de camera verder opgedeeld, om zo subfrustra 
te verkrijgen, zoals weergegeven in figuur \ref{fig:cs-opdeling:frustum}. 
Om deze subfrustra zo uniform mogelijk te houden, wordt de diepte van 
\mbox{\'e\'en} subfrustum, $d_k$, gelijk gesteld aan de hoogte van het 
subfrustum, $h_k$ bij bij de diepte $\mathtt{near}_k$ waar het subfrustumvolume 
begint. Dit is weergegeven in figuur \ref{fig:cs-opdeling:sleutel}. De volledige hoogte 
van het zichtfrustum bij diepte $\mathtt{near}_k$ is

$$ h_{\mathtt{frustum}} = 2 \mathtt{near}_k \tan \theta $$

waar $\theta$ de helft van het gezichtsveld is. De hoogte $h_k$ van 
\mbox{\'e\'en} subfrustum is dan gelijk aan de hoogte van het zichtfrustum, 
gedeeld door het aantal onderverdelingen in de $\mathbf{y}$-as.
De afstand van het volgende subfrustum is dan gegeven als

\begin{align*}
\mathtt{near}_{k+1} &= \mathtt{near}_{k} + h_k \\
                    &= \mathtt{near}_{k} + \frac{2 \mathtt{near}_k \tan\theta}{S_y}
\end{align*}

Dit kan herschreven worden tot de volgende exponentiele functie:

$$ \mathtt{near}_k = \mathtt{near}_0 \left( 1 + \frac{2 \tan\theta}{S_y} \right) $$

waarmee de opdeling van de $\mathbf{z}$-as van de camera gespecificeerd wordt.
Op basis hiervan is het mogelijk om elk cluster te identificeren aan de hand
van een tupel van drie integers $\left( i, j, k \right)$, waarbij $i$ en $j$ 
respectievelijk de $\mathbf{x}$ en $\mathbf{y}$ posities van de tegel in het
zichtvenster specificeert, en $k$ de diepte waarop het cluster zich bevindt.
Dit tupel vormt de sleutel van de clusters.

## Onderverdeling op basis van de normalen

\input{./img/tex/cs-normal-cone.tex}

De clusters kunnen verder opgedeeld worden aan de hand van attributen waarmee
fragmenten in discrete groepen onderverdeeld kunnen worden. Nuttige attributen
zorgen hierbij dat de set van relevante lichten geassocieerd met elk cluster 
afneemt. Een voorbeeld hiervan is de normaal informatie. 

Wanneer de fragmenten in een cluster verder worden opgedeeld aan de hand van de
normaalinformatie, is het mogelijk om lichten uit te sluiten die een 
nulcontributie hebben op de fragmenten van het cluster. In het geval van 
Lambertiaanse materialen komt dit voor wanneer de hoek tussen het invallend licht
en de normaal van een fragment groter is dan $90^\circ$. Een veel voorkomende 
situatie waarin dit zich voordoet, is wanneer een licht de achterkant van een
primitief verlicht. Het voorkomen van een dergelijke situatie wordt achtervlak 
lichtruiming (Backface Light Culling) genoemd. 

De normalen worden gegroepeerd aan de hand van een set van normaal kegels.
Voor elk cluster wordt \mbox{\'e\'en} kegel gedefinieerd. Voor de fragmenten
geassocieerd met een cluster geldt dat de normaal van deze fragmenten binnen
de gedefinieerde kegel van de cluster valt. Om de kegels op te stellen wordt
gebruik gemaakt van een onderverdeelde kubus. Voor elk vlak van deze kubus
wordt \mbox{\'e\'en} normaalkegel opgesteld die snijdt met de vier vertices van
het vlak. Dit is weergegeven in figuur \ref{fig:cs-normal-cone}.
Voor elk fragment wordt bepaald met welk vlak de normaal van het fragment snijdt,
indien deze onderverdeelde kubus gecentreerd is op het fragment. 

Vervolgens kunnen lichten die aan geen enkel fragment van het cluster bijdragen
buiten beschouwing van dit cluster worden gelaten. Een licht heeft een 
nulcontributie aan een cluster als:

$$ \omega > \frac{\pi}{2} + \alpha + \delta $$

Waarbij $\omega$ de hoek tussen de lichtdirectie en de as van de normaalkegel is,
$\alpha$ de halfhoek van de normaalkegel is, en $\delta$ de hoek die het licht 
maakt om de gehele cluster te verlichten. Dit is ge\"illustreerd in figuur 
\ref{fig:cs-light-discard-normal}.

\input{./img/tex/cs-normal-cone-discard.tex}

## Bepaling van unieke clusters

Wanneer deze berekening voor alle fragmenten in de framebuffer wordt uitgevoerd,
zal de resulterende textuur alle clusters relevant voor de huidige frame 
bevatten. Deze dienen echter nog wel gegroepeerd te worden zodat een lijst van 
unieke clusters verkregen wordt. Het groeperen van monsters is een veel 
voorkomend probleem binnen GPU rendering\cite{olsson2012clustered}. 

Om de globaal unieke monsters in een textuur, of buffer, te verkrijgen, dient
deze eerst gesorteerd te worden. Vervolgens moet een compact-stap uitgevoerd 
worden. Beide stappen zijn veel gebruikte bouwstenen in parallelle 
algoritmes\cite{billeter2009efficient, satish2009designing}.
Om deze reden bestaan er verschillende effici\"ente GPU implementaties\cite{Schling:2011:BCL:2049814}.

Ondanks dit blijft sorteren een computationeel dure operatie, waardoor het 
veelal nodig is om coherentie aanwezig in de textuur of buffer te gebruiken
om de hoeveelheid data te reduceren.

Voorbeelden hiervan zijn Resolution Matched Shadow Maps\cite{Lefohn:2007:RSM:1289603.1289611}, 
en het Compress-Sort-Decompress algoritme\cite{garanzha2010fast}. Binnen 
Resolution Mapped Shadow Maps moet bepaald worden welke schaduwpaginas gebruikt
worden door zichtmonsters. Om de set van data te verkleinen wordt de coherentie
in het zichtveld gebruikt. Indien naburige pixels gelijke schaduwpaginas 
vereisen, worden deze samengenomen.
In het geval van het Compress-Sort-Decompress algoritme wordt de framebuffer
voorgesteld als een 1-dimensionale sequentie en wordt hierop runtime-encoding
toegepast om duplicaten te voorkomen, voordat sortering plaatsvindt.

Een alternatieve oplossing is om gebruik te maken van virtuele paginatabellen.
Binnen deze paginatabellen wordt expliciet per pagina bijgehouden of deze 
gebruikt worden. De verschillende zichtmonster zetten een bit in het pagina-adres,
vervolgens kan deze bit gebruikt worden in de compactiestap. Omdat monsters
die vervijzen naar hetzelfde adres allen de bit op aanzetten, zullen geen 
duplicaten zich in de paginatabel bevinden\cite{hollemeersch2010accelerating}.

Wanneer de unieke clusters opgesteld zijn, kan voor elk de set van relevante
lichten worden bepaald.

Clustered Shading werd in verschillende recente games gebruikt, waaronder 
in de Avalanche engine, die gebruikt is voor Just Cause 2 en 3\cite{persson2013practical}
en Doom 4\cite{Tatarchuk:2016:ARR:2897826.2940292}.

