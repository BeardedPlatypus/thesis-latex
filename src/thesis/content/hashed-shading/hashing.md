## Hash functies 

Stel $U = \lbrace 0, 1, 2, \dots, \mathit{u} - 1 \rbrace$ is een ruimte voor 
een positieve integer $\mathit{u}$. Neem $S$ een set van $\mathit{n}$ unieke
elmenten (sleutelwaardes) binnen $U$. Een hash functie is gedifinieerd als een 
functie $h: U \rightarrow M$ die de sleutelwaarden in $S$ afbeeldt op een gegeven
interval $[0, \mathit{m} -1]$. 

Het is mogelijk om de ruimte $M$ te gebruiken als adres ruimte geassocieerd met
een opslagvolume. De adressen in deze ruimte $M$ kunnen gebruikt worden om
elementen geassocieerd met de sleutelwaardes op te slaan in het opslagvolume.
Het opslag volume wordt in dit geval een hash table genoemd.
Het gebruik van hash functies in combinatie met hash tables maakt het mogelijk om
data verspreidt over een grote ruimte compact op te slaan en op deze manier 
geheugen gebruik terug te brengen.\cite{cormen2009introduction, kleinberg2006algorithm}

Indien twee sleutels op een zelfde adres worden afgebeeld, wordt gesproken van
een botsing. De sleutels corresponderende met dit adres worden synoniemen van 
elkaar genoemd. Botsingen leiden er toe dat waardes geassocieerd met synoniemen
niet meer in een enkele stap uit de hash table kunnen worden opgehaald.
Er zijn verschillende manieren om om te gaan met dergelijke botsingen.


Indien elke sleutel op een uiniek adres wordt afgebeeld, wordt gesproken van een
perfecte hash functie, of een 1-probe hash functie. Dergelijke functies zijn
dus gedefinieerd als:

$$
h : U \rightarrow [ 0, \mathit{m} -1 ] \forall \mathit{x}, \mathit{y} \in S: x \neq y \rightarrow h(x) \neq h(y)
$$

Hieruit volgt dat de adres ruimte $M$ geassocieerd met de set van sleutelwaardes
$S$, een grootte gelijk of groter dan de set van sleutel waardes dient te 
hebben, $m \geq n$.

Wanneer geldt dat $m = n$ wordt de gesproken van een perfecte minimale hash 
functie. Een dergelijke minimale hash functie bestaat voor elke set van
sleutel waardes, doordat geldt dat voor twee eindige sets $X$ en $Y$ van gelijke
grootte die lineair geordend zijn er altijd een injectie functie bestaat zodanig
dat $X$ op $Y$ wordt afgebeeld\cite{czech1997perfect}: 

$$ 
h : X \rightarrow Y 
$$

hiervoor geldt dat

$$ 
\forall \mathit{x_1}, \mathit{x_2} \in X : \mathit{x_1} \leq \mathit{x_2} \Leftrightarrow h(\mathit{x_1}) \leq^\ast h(\mathit{x_2}) 
$$

waar $\leq$ en $\leq^\ast$ de respectievelijke lineaire orde functies zijn.

Het blijkt echter niet triviaal om dergelijke functies te vinden. Dit wordt
verder gecompliceerd doordat het geheugen gebruik en rekentijd die dergelijke
functies gebruiken ook van belang zijn.
In de praktijk is het veelal niet doenlijk om minimale perfecte hash functies op
te stellen.

Er zijn verschillende algoritmes om perfecte hash functies op te stellen die
slechts zorgen voor een klein extra geheugen gebruik ten opzicht van de minimale 
perfecte hash functie.

## Ruimtelijke hash functies

In Levebvre en Hoppe\cite{lefebvre2006perfect} wordt een algoritme besproken dat verder bouwt op perfecte 
hash functies gedefinieerd met behulp van hulp tabellen. Het gepresenteerde 
algoritme spitst zich toe op grafische applicaties. Het heeft als doel om
verspreide data binnen $d$-dimensionale ruimtes compact op te slaan, en effici\"ent
op te halen uit geheugen. Er wordt gebruik gemaakt van een perfecte hash functie, 
zodat de grafische kaart effici\"ent gebruik kan maken van de datastructuur,
doordat er geen conditietakken ontstaan.

### Terminologie

Het ruimte $U$ is gedefinieerd als een drie dimensionaal rooster met grootte
$u = \dot{u}^3$, waarbij de posities zijn gedefinieerd als

$$ 
\mathbf{p} \in \mathbb{Z}_{\dot{u}}^3 = [0, (\dot{u} -1)]^3 
$$

Binnen dit rooster bevindt zich een set $S \subset U$ met $n$ elementen, waarbij
voor elke positie $\mathbf{p} \in S$ een data element is geassocieerd zodanig dat 
$D(\mathbf{p}) = d$.

Het doel van de ruimtelijke hash functie is om de data in $D$ op te slaan in een 
compacte hash tabel $H$, zodanig dat

$$ 
D(\mathbf{p}) = H[h(\mathbf{p})] 
$$

Hash tabel $H$ heeft een grootte van $m = \dot{m}^3 \leq n$ en bevat de data 
elementen uit $D$. De hash functie $h(\mathbf{p})$ is gedefinieerd als

$$ 
h = h_0(\mathbf{p}) + \Phi[h_1(\mathbf{p})] \mod \dot{m} 
$$

Zowel $h_0$ als $h_1$ zijn imperfecte hash functies. De offset die volgt uit
de offset tabel $\Phi$ zorgt er voor dat botsingen in $h_0$ worden voorkomen. Hierdoor
gedraagd $h(\mathbf{p})$ zich als een perfecte hash functie.
De offset tabel $\Phi$ is gedefinieerd als een hash tabel bevattende offset 
co\"ordinaten in de vorm van drie dimensionale vectoren. De grootte van offset 
tabel $\Phi$ wordt gesteld op $r = \dot{r}^3 \leq \sigma n$. 
De hash functies in $h(\mathbf{p})$ zijn gedefinieerd als

\begin{align*}
h_{0}: & \mathbf{p} \rightarrow \mathbf{p} \ \mathtt{mod}\ \dot{m} \\
h_{1}: & \mathbf{p} \rightarrow \mathbf{p} \ \mathtt{mod}\ \dot{r}
\end{align*}

De eisen aan deze functies en hash tabellen zijn:

1. $h(\mathbf{p})$ is een perfecte hash functie.
2. $\Phi$ en $H$ zijn zo compact mogelijk.
3. De toegang tot de hash tabellen, $\Phi[h_1(\mathbf{p})]$ en $H[h(\mathbf{p})]$ 
   moet goede ruimtelijke coherentie tonen rekeninghoudend met $\mathbf{p}$.
   
### Constructie

De eerste stap in de constructie van een ruimtelijke hash functie is het vast 
stellen van de parameters van de hash tabellen. 
$\dot{m}$ wordt gesteld op de kleinste waarde zodat voldaan wordt aan 
$m = \dot{m}^3 \leq n$. De offset waardes worden voorgesteld met behulp van drie
8 bit integers. In het geval dat $\dot{m} > 255$ dan wordt $m$ gesteld op 
$m = \dot{m}^3 \leq n * 1.01$, om een perfecte hash functie mogelijk te maken.

De grootte van $\dot{r}$ kan op twee manieren worden geconstrueerd, verschillend
in berekeningstijd en compactheid van de offset tabel. 

* Voor snelle constructie wordt $\dot{r}$ initieeel gesteld op 
  $r = \dot{r}^3 \leq \sigma n$ waarbij de factor $\sigma$ gesteld wordt op
  $\frac{1}{6}$. Omdat elke offset uit 8 bits per dimensie bestaat, leidt dit
  tot vier extra bits per data element. Indien geen perfecte hash functie 
  gevonden kan worden, wordt $\dot{r}$ geometrisch vergroot.

* Voor een optimale constructie met betrekking tot geheugenverbruik wordt
  gebruik gemaakt van een binaire zoek functie over $\dot{r}$. Er wordt gebruik 
  gemaakt van een gretig probabilistisch algoritme om $\dot{r}$ zo klein mogelijk 
  te definieren, zodanig dat de gevonden hash functie de perfecte minmale 
  hashfunctie benadert.
  
Nadat de groottes van de data tabel en offset tabel gedefinieerd zijn, dienen de
expliciete wardes te worden toegekend aan de hash tabel elementen. Zoals eerder
vermeld dienen de offset waardes in de offset tabel $\Phi$ botsingen in 
$h(\mathbf{p})$ te voorkomen. Elke waarde in de offset tabel dient zodanig 
gekozen te worden, dat de synoniemen voor een locatie in $\Phi$ geen 
botsingen veroorzaken in $h(\mathbf{p})$. De ruimte $O$ definieert het 
mogelijke domein van $\Phi$.

$$
O: \mathbb{Z}_{\dot{r}}^3 = [0, (\dot{r} - 1)]^3 
$$

Vervolgens kan deze eis gedefinieerd worden als

$$ 
\forall \mathbf{o} \in O : \forall \mathbf{p} \in \lbrace \mathbf{e} \vert \mathbf{e} \in S \land h_1(\mathbf{e}) = 0 \rbrace : \not \exists \mathbf{p^\prime} h(\mathbf{p^\prime}) = ((h_0(\mathbf{p}) + \Phi(o)) \mod \dot{m}) 
$$

Wanneer de set $\lbrace \mathbf{e} \in S \land h_1(\mathbf{e}) = o \rbrace$ van
synoniemen van een waarde $o$ groot is, zal het vinden van een offset die botsingen
in $h(\mathbf{p})$ voorkomt moeilijker worden.\cite{fox1992practical}
Om een correcte toekenning van offset waardes te vergemakkelijken, zullen de 
elementen $o \in O$ geordend worden op de grootte van hun respectievelijke 
synoniemen set. De waardes $o$ met de grootste synoniemen sets zullen als eerste
toegekend worden. 

De toegekende offset waardes dienen verder zodanig gekozen te worden dat 
de ruimtelijke coherentie, en daarmee de textuur raadpleging in $H$, coherent 
blijven. Doordat $h_1(\mathbf{p})$ slechts een modulus operatie is, is deze per 
definitie coherent. 

Coherentie tussen twee elementen kan worden gedefinieerd als

\begin{align*}
N_S(\mathbf{p_0},\mathbf{1}) \mathop{:=} 
  \begin{cases} 
    1 & : \vert\vert \mathbf{p_0}, \mathbf{p_1}\vert\vert = 1 \\ 
    0 & : \mathnormal{otherwise}
  \end{cases}
\end{align*}

Het doel is om de coherentie van data queries in hash tabel $H$ te maximaliseren.
De coherentie in hash tabel $H$ kan gedefinieerd worden als

\begin{align*}
\mathcal{N}_H &= \sum_{\mathbf{p}_0,\mathbf{p}_1 \vert N_S(\mathbf{p}_0, \mathbf{p}_1) = 1} N_H(h\mathbf{p_0}), h(\mathbf{p_1}) \\
              &= \sum_{\mathbf{p}_0,\mathbf{p}_1 \vert N_H(h\mathbf{p_0}), h(\mathbf{p_1}) = 1} N_S(\mathbf{p}_0, \mathbf{p}_1)
\end{align*}

De laatste uitdrukking kan gemeten worden tijdens constructie. Wanneer deze
gemaximaliseerd leidt dit tot de uitdrukking

$$
\max_{\Phi[\mathbf{o}]} (\mathcal{C}(\Phi[\mathbf{o}])),  \mathcal{C}(\Phi[\mathbf{o}] = \sum_{\mathbf{p} \in h_{1}^{-1}(\mathbf{o})), |Vert \Delta \Vert = 1} N_{S}\left( h^{-1}\left( h_0(\mathbf{p}) + \Phi[\mathbf{o}] + \Delta \right), \mathbf{p} \right).
$$

Doordat het testen van alle mogelijke waardes computationeel te veel eisend
zou zijn, wordt in plaats hiervan een heuristiek gebruikt.
Indien de offset tabel lokaal constant is, dan is de afhankelijke hash functie
coherent. Dus wordt bij het toewijzen van een offset bij $\mathbf{o}$ eerst
gekeken naar de naburige cellen van $\mathbf{o}$, wanneer deze een offset
bevatten die tevens correct is voor $\mathbf{o}$, wordt deze ook aan $\mathbf{o}$
toegewezen. 

$$
\Phi[\mathbf{o}] \in \left\{ \Phi[\mathbf{o^\prime}] \vert \| \mathbf{o} - \mathbf{o^\prime} \| < 2 \right\}
$$

Indien geen van de omliggende offset waardes correct is, wordt willekeurig een
correcte kandidaat gevonden.

## Verbindingloze octree {#sec:theorie-verbindingloze-octree}

\input{./img/tex/hs-octree-example.tex}

Met behulp van de ruimtelijke hash functie is het mogelijk om een efficiente
octree implementatie voor GPUs op te stellen.\cite{choi2009linkless}
Zoals eerder vermeld werkt de standaard CPU implementatie met pointers, waarbij
recursief in de boom wordt afgedaald. Dergelijke datastructuren die sterk 
leunen op controle structuren zijn niet erg effici\"ent wanneer deze gebruikt
worden op de GPU.

De data die opgeslagen wordt in een octree is in zeer grote mate verspreid over
de drie dimensionale ruimte. Indien gekeken wordt naar figuur 
\ref{fig:hs-octree-example}, is te zien dat een groot deel van de cellen
in deze octree leeg zijn, hiervoor dient dus geen data opgeslagen te worden. 
Het is mogelijk om de octree voor te stellen als een stapel van lagen, met elk
een fijnere granulariteit. Elk van deze lagen kan gecodeerd worden als een
ruimtelijke hash functie. Dit is weergegeven in figuur \ref{fig:hs-linkless-octree-example}

\input{./img/tex/hs-linkless-octree-example.tex}

Elke cel die zich bevindt in een octree laag dient te worden voorgesteld.
Een cel kan ofwel een blad, of wel een tak knoop zijn binnen de octree. Verder
kunnen blad knopen of wel leeg zijn, of wel data bevatten. Een cel kan dus 
worden voorgesteld met twee bits, de eerste bit die aangeeft of een cel een
blad knoop is, en de tweede bit die aangeeft of een cel data bevat of niet.
Om effeciency redenen worden hierbij acht nodes samengenomen, zodat deze 
voorgesteld kunnen worden met behulp van twee integers van elk acht bits. Omdat
elke tak knoop acht kinderen bevat, geeft deze representatie dus een tak 
knoop weer, waarin elk van de kinderen is geencodeerd.

De data geassocieerd met elke knoop in de octree kan worden opgeslagen binnen
het data element in de hash tabel van deze knoop, hiervoor wordt dan boven
op de twee 8 bits integers een set van 8 data elementen toegevoegd. 
Echter in het geval dat dergelijke data elementen groot zijn, of indien een
groot aantal knopen geen data bevat, is het efficienter om niet per cel data
ruimte te reserveren, maar deze apart op te slaan. Hiervoor kan per laag, 
een tweede ruimtelijke hash functie worden bijgehouden, die alle relevante
data elementen compact op slaat. Dit leidt tot een voorstelling zoals 
weergegeven in figuur \ref{fig:hs-linkless-octree-representation}. 
De hash tabel die de octree encodeerd zal de octree tabel genoemd worden,
en de hash tabel die de data encodeerd zal de data tabel genoemd worden.

\input{./img/tex/hs-linkless-octree-representation.tex}

Indien data dient te worden opgehaald uit een verbindingloze octree, wordt per 
laag de knoop uit de octreetabel berekend, en bepaald of de knoop in deze laag 
een blad knoop is. Is dit niet het geval dan wordt de knoop in de octreetabel 
van de volgende laag berekend. Is dit wel het geval, dan wordt gekeken of deze
blad knoop ook data bevat. Indien de knoop niet leeg is wordt ofwel de data 
geassocieerd met de gevonden knoop in de octreetabel teruggegeven, ofwel wordt
de knoop in de datatabel van deze laag berekend en teruggegeven.
Dit algoritme is visueel weergegeven in figuur \ref{fig:hs-linkless-octree-algorithm}. 

\input{./img/tex/hs-linkless-octree-algorithm.tex}

Doordat de basis van de ruimtelijke hash functie een combinatie van simpele
berekeningen en texturen is in plaats van het recursief doorlopen van een
boom structuur, kan deze efficient worden geimplementeerd op de grafische kaart.
Dit maakt het mogelijk om deze datastructuur als basis te gebruiken voor
het hashed shading algoritme. Deze is beschreven in de volgende sectie.

