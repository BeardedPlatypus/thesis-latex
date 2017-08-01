## Hash functies 

Nu vastgesteld is dat de octree-datastructuur de basis zal vormen voor het 
lichttoekenningsalgoritme, is het nodig om deze effici\"ent op de grafische
kaart voor te stellen. Hiervoor zal gebruik gemaakt worden van hashfuncties.
In deze sectie zal ingegaan worden op de theorie achter hashfuncties. 
Vervolgens zal ingegaan worden hoe hashfuncties gebruikt kunnen worden om 
spatiale data op te slaan. Daarna zal een octreevoorstelling op basis van
dergelijke spatiale hashfuncties ge\"introduceerd worden.

\input{./img/tex/hs-hashfunctie.tex}

Het doel van een hashfunctie is om een set van waarden verspreid over een ruimte
af te beelden op een compactere ruimte. Een hashfunctie kan als volgt gedefinieerd
worden: gegeven een ruimte $U = \left\lbrace 0, 1, 2, \dots, \mathit{u} - 1 \right\rbrace$
bestaande uit $\mathit{u}$ positieve integers. Binnen deze ruimte U is een set S
gedefinieerd van $\mathit{n}$ unieke elementen waar $\mathit{n} \leq \mathit{u}$.
De hashfunctie $\mathit{h}$ beeldt de elementen van $S$ af op een interval 
$M = \left[0, \mathit{m} - 1 \right]$:

$$ h : U \to M $$

\noindent hierbij worden de elementen van $S$ sleutelwaarden genoemd. Deze 
afbeelding is ge\"illustreerd in figuur \ref{fig:hs-hashfunctie}.

Hashfuncties kunnen gebruikt worden om dunverspreide data effici\"ent op te slaan. 
Stel de situatie waar enkele elementen in $U$ data bevatten, en deze 
data wordt opgevraagd aan de hand van deze elementen. Wanneer voor elk element in
$U$ geheugen gereserveerd dient te worden waarin de data opgeslagen kan worden, 
leidt dit tot een onnodig groot geheugengebruik, gezien het merendeel van de elementen
leeg zullen zijn. Indien nu de elementen van $U$ waarmee data geassocieerd is,
worden genomen als de sleutelwaardes, en een hashfunctie wordt opgesteld voor
deze sleutelwaarden, dan hoeft slechts voor elk element van $M$, waarop de 
sleutelwaarden worden afgebeeld, geheugen gereserveerd worden.
Indien $\mathit{m} < \mathit{u}$ leidt dit tot een lager geheugengebruik.
In dit geval wordt $M$ de adresruimte genoemd, en het opslagvolume waarin de data 
wordt opgeslagen, een hashtabel\cite{cormen2009introduction, kleinberg2006algorithm}.

Indien twee sleutels op een zelfde adres worden afgebeeld, wordt gesproken van
een botsing. De sleutels corresponderende met dit adres worden synoniemen van 
elkaar genoemd. Botsingen leiden er toe dat waardes geassocieerd met synoniemen
niet meer in een enkele stap uit de hashtabel kunnen worden opgehaald.
Er zijn verschillende manieren om om te gaan met dergelijke botsingen.

Indien elke sleutel op een uniek adres wordt afgebeeld, wordt gesproken van een
perfecte hashfunctie, of een 1-probe hashfunctie. Dergelijke functies zijn
dus gedefinieerd als:

$$
\mathit{h} : U \rightarrow [ 0, \mathit{m} -1 ] \forall \mathit{x}, \mathit{y} \in S: x \neq y \rightarrow \mathit{h}(x) \neq \mathit{h}(y)
$$

\noindent Hieruit volgt dat de adresruimte $M$ geassocieerd met de set van sleutelwaardes
$S$, groter of gelijk aan de de set van sleutelwaardes dient te zijn, $m \geq n$.

Wanneer geldt dat $m = n$ wordt de gesproken van een perfecte minimale hashfunctie. 
Een dergelijke minimale hashfunctie bestaat voor elke set van sleutelwaarden, 
doordat geldt dat voor twee eindige sets $X$ en $Y$ van gelijke
grootte die lineair geordend zijn er altijd een injectie functie bestaat zodanig
dat $X$ op $Y$ wordt afgebeeld\cite{czech1997perfect}: 

Het blijkt echter niet triviaal om dergelijke functies te vinden. Dit wordt
verder gecompliceerd doordat het geheugengebruik en de rekentijd die het opstellen van
dergelijke functies vereist ook van belang is. In de praktijk is het veelal niet doenlijk om
minimale perfecte hashfuncties op te stellen. Er zal dus veelal voor gekozen worden
om perfecte hashfuncties op te stellen die slechts zorgen voor een kleine toename in
geheugen gebruik ten opzichte van de minimale perfecte hashfunctie.

## Spatiale hashfuncties

In Lefebvre en Hoppe\cite{lefebvre2006perfect} wordt een algoritme ge\"introduceerd om
een perfecte hashfunctie op te stellen met behulp van twee hashfuncties en een hashtabel.
Hierdoor is het mogelijk om $\mathit{d}$-dimensionale ruimtes compact op te slaan. 
Door het gebruik van perfecte hashfuncties kan de GPU effici\"ent data ophalen uit
de hashtabel, doordat er geen conditietakken nodig zijn om botsingen op te lossen.
Lefebvre et al. noemen deze perfecte $\mathit{d}$-dimensionale hashfuncties spatiale 
hashfuncties. Er zal in deze sectie eerst ingegaan worden op de terminologie en definitie
van deze spatiale hashfuncties. Daarna zal de constructie en gebruik worden toegelicht.

### Terminologie

Omdat deze thesis zich richt op drie dimensionale \mbox{sc`enes} zal slechts ingegaan
worden op de drie dimensionale spatiale hashfunctie. De ruimte $U$ is gedefinieerd als
een drie dimensionaal rooster met grootte $\mathit{u} = \mathit{\dot{u}}^3$. Posities
binnen dit rooster zijn gedefinieerd als een vertor van drie integers met waarden 
kleiner dan $\mathit{\dot{u}}$ :

$$ \mathbf{p} = \mathbb{Z}_{\dot{u}}^3 = \begin{pmatrix}\mathit{p_x}\\ \mathit{p_y}\\ \mathit{p_z}\end{pmatrix} \vert \mathit{p_i} \in \left[0, \left(\mathit{\dot{u}} -1\right)\right] $$

\noindent Binnen dit rooster bevindt zich een set $S \subseteq U$ met $\mathit{n}$ 
elementen. Met elk element op positie $\mathbf{p} \in S$ is een 
data-element $d$ geassocieerd, zodanig dat

$$ D\left(\mathbf{p}\right) = d $$

### Definitie

\input{./img/tex/hs-spatiale-hashfunctie.tex}

Het idee is om de perfecte hashfunctie $\mathit{h}$ op te bouwen met behulp van 
twee simpele imperfecte hashfuncties, $\mathit{h}_0$ en $\mathit{h}_1$. De 
eerste hashfunctie, $\mathit{h}_0$, beeldt elementen uit $U$ af op $M$. De sleutelwaarden 
zijn voor deze hashfunctie mogelijk synoniemen. De tweede hashfunctie beeldt 
de sleutelwaarden af op de adressen van een kleine hashtabel $\Phi$, die offset-waardes 
bevat. De synoniemen in de eerste hashfunctie dienen geen synoniemen in de tweede
hashfunctie te zijn. Hierdoor worden synoniemen van $\mathit{h}_0$ op verschillende
adressen in $\Phi$ afgebeeld door hashfunctie $\mathit{h}_1$. Vervolgens wordt de 
offset-waarde opgehaald uit $\Phi$, gebruikt om de botsingen in $M$ door de hashfunctie $\mathit{h}_0$
te voorkomen. Doordat de synoniemen voor $\mathit{h}_0$ een verschillende offset toegewezen krijgen,
zullen deze niet langer op hetzelfde adres vallen. Hierdoor wordt een perfecte hashfunctie
gerealiseerd. Dit principe is ge\"illustreerd in figuur \ref{fig:hs-spatiale-hashfunctie}.
De perfecte hashfunctie $\mathit{h}$ wordt als volgt gedefinieerd:

$$ \mathit{h}\left(\mathbf{p}\right) = \mathit{h}_0\left(\mathbf{p}\right) + \Phi\left[\mathit{h}_1\left(\mathbf{p}\right) \right] \operatorname{mod} \mathit{\dot{m}} $$

\noindent De offset-waardetabel $\Phi$ heeft een grootte van $\mathit{r} = \mathit{\dot{r}}^3$. De
hashfuncties $\mathit{h}_0$ en $\mathit{h}_1$ worden als simpele modulo-operaties gedefinieerd:

\begin{align*}
  \mathit{h}_0 &: \mathbf{p} \mapsto \mathbf{p} \operatorname{mod} \mathit{\dot{m}} \\
  \mathit{h}_1 &: \mathbf{p} \mapsto \mathbf{p} \operatorname{mod} \mathit{\dot{r}} 
\end{align*}

\noindent De offset waardes worden voorgesteld als drie dimensionale 8-bit integer vectoren.

### Constructie

Voor de constructie van de spatiale hashfunctie $\mathit{h}$ dienen eerst de parameters
$\mathit{\dot{m}}$ en $\mathit{\dot{r}}$ vastgesteld te worden. De keuze voor $\mathit{\dot{m}}$
left de grootte van de hashtabel $H$ vast en de hashfunctie $\mathit{h}_0$. Om het geheugengebruik
te minimaliseren dient de hashtabel $H$ zo klein mogelijk gehouden te worden. Hiervoor wordt $\mathit{\dot{m}}$
zo klein mogelijk gekozen, zodat nog steeds geldt:

$$ \mathit{m} = \mathit{\dot{m}}^3 \geq \begin{cases} \mathit{n},& \text{ als } \mathit{n} \leq 255 \\
                                                      \mathit{n} \cdot 1.01,& \text{ anders}\end{cases} $$
                                                      
\noindent De extra ruimte voor $n > 255$ is nodig om een perfecte hashfunctie mogelijk te maken met 8-bit
offset-waardes.

De grootte van $\mathit{\dot{r}}$ kan op twee manieren worden vastgesteld:

* Voor een computationeel snelle constructie wordt $\mathit{\dot{r}}$ zo klein mogelijk gesteld
  zodanig dat nog steeds geldt
  
  $$ \mathit{r} = \mathit{\dot{r}}^3 \geq \sigma \mathit{n} $$
  
  \noindent waar $\sigma$ initieel wordt gesteld op $\frac{1}{6}$. Omdat de offset waardes bestaan
  uit drie 8-bit integers leidt dit tot een toename van vier bits per sleutelwaarde. Indien
  geen perfecte hashfunctie kan worden opgebouwd wordt $\mathit{r}$ geometrisch vergroot.
* Voor een zo laag mogelijk geheugengebruik kan gebruik gemaakt worden van een binaire 
  zoekfunctie over $\mathit{\dot{r}}$. Hierbij wordt gebruik gemaakt van een gretig 
  probabilistisch algoritme om $\mathit{\dot{r}}$ zo klein mogelijk te defini\"eren. 
  De gevonden waarde voor $\mathit{\dot{r}}$ zorgt ervoor dat de spatiale hashfunctie
  de minimale perfecte hashfunctie zo dicht mogelijk benadert.
  
Nadat de waardes voor $\mathit{\dot{m}}$ en $\mathit{\dot{r}}$ zijn gekozen liggen de 
hashfuncties $\mathit{h}_0$ en $\mathit{h}_1$ vast. De tweede stap in de opbouw van
de perfecte hashfunctie $\mathit{h}$ is het toekennen van de waardes in de offset-hashtabel $\Phi$,
zodanig dat er geen botsingen meer voorkomen in $\mathit{h}$. Deze offset-waardes zullen iteratief
worden toegevoegd.

\input{./img/tex/hs-spatiale-hashfunctie-update.tex}

De ruimte $O$ definieert de mogelijk adresruimte van de offset-hashtabel $\Phi$:

$$ O: \mathbb{Z}_{\mathit{\dot{r}}}^3 = \left[0, (\mathit{\dot{r}} -1) \right]^3 $$

\noindent Indien een offset-waarde wordt toegekend aan positie $\mathbf{o} \in O$ dan ligt
het adres van alle punten $\mathbf{p}\in U$ die afgebeeld worden op $\mathbf{o}$ vast voor
de hashfunctie $\mathit{h}$. Deze set kan gedefinieerd worden als:

$$ V = \left\lbrace \mathbf{p}\in S \land \mathit{h}_1\left( \mathbf{p} \right) = \mathbf{o} \right\rbrace $$

\noindent De data geassocieerd met deze sleutelwaardes kunnen vervolgens worden opgeslagen
in hashtabel $H$ zodat geldt:

$$ \forall \mathbf{p} \in V: D\left(\mathbf{p}\right) = H\left[\mathit{h}_0\left(\mathbf{p}\right) + \Phi\left[\mathit{h}_1\left(\mathbf{p}\right)\right]\right] $$

\noindent Indien de offset-waarde correct gekozen is zal geen van deze waardes een botsing 
veroorzaken in $\mathit{h}$.

$$ \forall \mathbf{p} \in V: \nexists \mathbf{p}^\prime \in S^\prime: \mathit{h}\left(\mathbf{p}\right) = \mathit{h}\left(\mathbf{p}^\prime\right) $$

\noindent waar $S^\prime$ de set van reeds toegekende sleutelwaarden is. Dit proces is voor een enkele stap
weergegeven in figuur \ref{fig:hs-spatiale-hashfunctie-update}.

Wanneer de set $V$ van synoniemen voor $\mathbf{o}$ groot is, zal het vinden van een 
correcte offset-waarde moeilijker worden\cite{fox1992practical}. Om een correcte toekenning
te vergemakkelijken zullen de punten $\mathbf{o} \in O$ geordend worden op basis van
de grootte van de corresponderende synoniemensets. De waardes $\mathbf{o}$ met de 
grootste synoniemensets zullen als eerste worden toegekend.

De offset-waardes dienen verder zodanig gekozen te worden dat de ruimtelijke coherentie
behouden blijft. Hierdoor zal het raadplegen van de hashtabellen ook coherent blijven, wat
de performantie van de spatiale datastructuren ten goede komt. Coherentie tussen twee elmenten
kan gedefinieerd worden als:

$$ N_S\left(\mathbf{p}_0, \mathbf{p}_1\right) := \begin{cases} 1, & \text{ als } \lVert \mathbf{p}_0, \mathbf{p}_1 \rVert = 1 \\ 0, & \text{ anders } \end{cases} $$

\noindent De coherentie binnen de hashtabel H kan vervolgens worden gedefinieerd als:

\begin{align*}
\mathcal{N}_H &= \sum_{\mathbf{p}_0,\mathbf{p}_1 \vert N_S(\mathbf{p}_0, \mathbf{p}_1) = 1} N_H(h\mathbf{p_0}), h(\mathbf{p_1}) \\
              &= \sum_{\mathbf{p}_0,\mathbf{p}_1 \vert N_H(h\mathbf{p_0}), h(\mathbf{p_1}) = 1} N_S(\mathbf{p}_0, \mathbf{p}_1)
\end{align*}

De laatste uitdrukking kan gemeten worden tijdens constructie. Wanneer deze 
gemaximaliseerd leidt dit tot de uitdrukking:

$$
\max_{\Phi[\mathbf{o}]} (\mathcal{C}(\Phi[\mathbf{o}])),  \mathcal{C}(\Phi[\mathbf{o}] = \sum_{\mathbf{p} \in h_{1}^{-1}(\mathbf{o})), |Vert \Delta \Vert = 1} N_{S}\left( h^{-1}\left( h_0(\mathbf{p}) + \Phi[\mathbf{o}] + \Delta \right), \mathbf{p} \right).
$$

De modulo-operatie van $\mathit{h}_1$ is per definitie coherent, hierdoor zal het ophalen
van de offset-waardes dan ook altijd coherent zijn. Het is mogelijk om de coherentie van $\mathit{h}$ 
te berekenen voor elke mogelijke offset-waarde. Echter  dit zou computationeel te veeleisend zijn. Om
deze reden wordt gebruik gemaakt van de aanname dat indien de offset-hashtabel $\Phi$ lokaal constant is,
de hashfunctie $\mathit{h}$ zich coherent zal gedragen. Wanneer een offset-waarde toegekend wordt aan
positie $\mathbf{o}$, zal eerst gekeken worden of naburige adressen een offset-waarde bevatten die correct 
is voor $\mathbf{o}$. Indien geen van de omliggende toegekende offset-waardes correct is, wordt een 
willekeurige kandidaat gevonden.

## Verbindingloze octree {#sec:theorie-verbindingloze-octree}

Met behulp van deze spatiale hashfunctie is het mogelijk om de octreestructuur effici\"ent
op de GPU voor te stellen\cite{choi2009linkless}. In de standaard CPU implementatie worden
de verbindingen tussen knopen van de octree voorgesteld met behulp van pointers. Vervolgens kan
een waarde uit de octree opgehaald worden door recursief af te dalen totdat een bladknoop
wordt bereikt. Dergelijke implementaties zijn veelal niet effici\"ent op de GPU. De
ruimtelijke coherentie gaat verloren door het gebruik van pointers, en het gebruik
van veel controlestructuren leidt tot performantieverlies voor meerdere-data-enkele-instructie
(SIMD) operaties\cite{Han:2011:RBD:1964179.1964184}. In plaats hiervan zal geen gebruik gemaakt 
worden van pointers, maar wordt elke laag voorgesteld met behulp van een spatiale hashfunctie. 
Deze datastructuur wordt de verbingingloze octree genoemd.

\input{./img/tex/hs-octree-layers.tex}

Indien elke laag van een octree apart bekeken wordt, bestaat deze uit een set discrete
volumes, binnen een bepaalde ruimte, zie figuur \ref{fig:hs-octree-layers}. Hierin zijn de takknopen weergegeven
in blauw, de gevulde bladknopen in groen, en de lege bladknopen in rood. Omdat de grootte van elke volume
vastligt per laag, is het mogelijk om de Euclidische ruimte voor te stellen als 
de ruimte $U_l = \mathbb{Z}^3$, waarbij elk van de knopen overeenkomt met een 
discrete positie in deze ruimte $U_l$. De set van knopen binnen de laag $l$ kan dan voorgesteld
worden als $S_l$. 

\input{./img/tex/hs-linkless-octree-representation.tex}

Doordat de set van knopen per laag $S_l$ veelal kleiner is dan de gehele ruimte $U_l$, helemaal voor diepere
lagen, kunnen deze effici\"ent afgebeeld worden op de ruimte $M_l$. Om een spatiale hashfunctie op te stellen
die de octreestructuur van een laag beschrijft, dient dan slechts nog de data 
$D_l(\mathbf{p}) \vert \mathbf{p} \in S_l$ opgesteld te worden. Het data-element $D_l(\mathbf{p}) = k$ 
geassocieerd met een punt $\mathbf{p}$ in laag $l$ dient de beschrijving van knoop $k$ op punt $\mathbf{p}$ 
in laag $l$ te geven. Indien de data opgeslagen binnen de octree zich slechts bevindt in de bladknopen 
zijn er drie mogelijke knooptypes voor knoop $k$. Knoop $k$ is een takknoop, gevulde bladknoop of 
lege bladknoop. In dit geval kan knoop $k$ worden voorgesteld met twee Booleaanse waardes:

1. knoop $k$ is een bladknoop
2. knoop $k$ is gevuld

\noindent Om het geheugengebruik terug te dringen worden steeds acht knopen behorende tot dezelfde
takknoop in de bovenliggende laag, samengenomen. De acht kinderen van een dergelijke takknoop kunnen dan 
voorgesteld worden met behulp van twee 8-bit integers. 
De waarde in hashtabel $H_l$ op punt $\mathbf{p}$ beschrijft vervolgens dus alle kinderen van de 
takknoop in laag $l$ op positie $\mathbf{p}$. Dit is weergegeven in figuur \ref{fig:hs-linkless-octree-representation}.

Naast de octreebeschrijving dient ook de data geassocieerd met knopen van de octree te worden opgeslagen.
Wanneer het merendeel van de knopen data met zich geassocieerd heeft, en deze data weinig geheugen inneemt, 
kan deze data direct worden opgeslagen in de hashtabellen $H_l$. Hiervoor wordt voor elke knoop een ruimte
ter grootte van de data gereserveerd naast de twee 8-bit integers. Wanneer een knoop wordt opgehaald uit
de hashtabel $H_l$ wordt gelijk de geassocieerde data mee teruggeven. 
Wanneer de data-elementen groot zijn, of slechts een klein deel van de knopen een data-element bevat, leidt
deze aanpak tot een groot onnodig geheugenverbruik. In deze gevallen kan de data apart worden opgeslagen.
Hiervoor wordt per laag een tweede spatiale hashfunctie opgesteld, waarin voor elke knoop met data
een element wordt voorzien. Vervolgens kan de gevuld-bit gebruikt worden om na te gaan of met een punt 
$\mathbf{p}$ data geassocieerd is. Is dit het geval dan zal het punt $\mathbf{p}$ opgehaald worden uit 
de tweede spatiale hashtabel.

Wanneer data voor een punt $\mathbf{p} \in \mathbb{R}^3$ opgehaald dient te worden, wordt 
per laag de corresponderende discrete positie bepaald. Vervolgens wordt de beschrijving van
de knoop berekend. Op basis hiervan wordt of wel verder afgedaald in de verbindingloze octree
en wordt de octreebeschrijving voor punt $\mathbf{p}$ in de volgende opgehaald, ofwel wordt
de data geassocieerd met punt $\mathbf{p}$ in laag $l$ teruggegeven. Afhankelijk van de implementatie
wordt deze data gelijk uit hashtabel $H_l$ opgehaald, ofwel dient de tweede spatiale hashfunctie van
laag $l$ raad gepleegd te worden. 

Doordat de verbindingloze octree alle knopen in een laag opslaat, is het mogelijk om op een diepte 
dieper dan 0 te beginnen. Deze begindiepte wordt de startdiepte $\mathit{d_s}$ genoemd. Indien deze 
niet gelijk is aan nul, worden alle knopen op diepte $\mathit{d_s}$ opgeslagen in de eerste spatiale 
hashfunctie van de verbindingloze octree.

Doordat de hashtabellen van de spatiale hashfuncties simpel voor te stellen zijn als buffers of texturen
kan de verbindingloze octree effici\"ent voorgesteld worden op de GPU. Hierdoor is het 
mogelijk om deze datastructuur als basis te gebruiken voor het Hashed Shading algoritme.
Dit algoritme zal ge\"introduceerd worden in de volgende sectie.

