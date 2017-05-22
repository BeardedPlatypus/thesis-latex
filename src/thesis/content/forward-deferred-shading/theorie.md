# Theorie

De afhankelijkheid tussen geometrische complexiteit en de complexiteit van de 
belichtingsberekening werd al in de begin jaren van computer graphics herkend 
als probleem. De opsplitsing van visibiliteit en belichtingsberekeningen werd toen
al voorgesteld. Zo werd in de scan-line polygon renderer van Watkins 
(\cite{watkins1970real}) in de jaren 70 al bepaald welke oppervlakte het dichtst
bij de camera lag en slechts hiervoor de lichtberekening uitgevoerd. Andere 
hardware en software-implementaties zijn tevens in de jaren 80 ge\"introduceerd.\cite{deering1988triangle, fuchs1989pixel, perlin1985image, glassner1988algorithms} 
Tebbs, Neumann, Eyles, Turk and Ellsworth (\cite{tebbs1989parallel}) geven een
gedetailleerd overzicht van deferred shading in 1990.  

Moderne deferred shading algoritmes maken veelal gebruik van GBuffers. 
GBuffers waren oorspronkelijk ge\"introduceerd in de context 
van het non-fotorealistisch renderen om visuele begrijpbaarheid te verbeteren.
\cite{saito1990comprehensible} Echter GBuffers lenen zich tevens goed om de data
tussen  de visibiliteitsstap en de lichtberekeningsstap op te slaan.  

Deferred shading is een veel gebruikt algoritme in moderne game engines. Voorbeelden
van engines die gebruik maken van deferred shading zijn: Unreal 4\cite{karis2013real}, 
Frostbyte 2\cite{magnusson2011lighting},
Unity\cite{pranckevivcius2014physically} en CryEngine 3\cite{mittring2009bit}.

In deze sectie zal ingegaan worden op het algoritme van deferred shading om
de koppeling tussen geometrie complexiteit en shading op te lossen. Vervolgens
zal gekeken worden naar nieuwe algoritmes die verder bouwen op deferred 
shading.  


## Definities

Binnen deze thesis zal de volgende terminologie gebruikt worden.  

*Forward shading* beschrijft de standaard uitvoering van de renderpijplijn. 
Hier wordt niet expliciet de fragmenten op diepte gefilterd, en dus zal voor
elk fragment de belichtingsberekeningen uitgevoerd worden.  

*Deferred shading* beschrijft het algoritme waarbij expliciet de render pijplijn
wordt onderverdeeld in twee discrete stappen, een geometriestap en een 
belichtingsstap. De visibiliteitsstap maakt hierbij gebruik van een *GBuffer* om
de geometrie data op te slaan.  


## Deferred shading

Zoals besproken in sectie \ref{sec:shading}, is de rendering vergelijking gegeven
door: 

$$ 
\mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \int_{2\pi^{+}} \mathit{f_{r}}(\mathbf{p}, \omega_{i}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, \omega_{i})\cos\theta_{i}d\omega_{i} 
$$

Uitgaande dat een punt geen licht uitstraalt, dan zou de rendering vergelijking
benaderd kunnen worden door middel van een beschrijving van de directe belichting\cite{akenine2016real}:

$$ 
\mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \sum_{\mathit{k}=1}^{\mathit{n}} \mathit{f_{r}}(\mathbf{p}, l_{\mathit{k}}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, l_{\mathit{k}})\cos\theta_{i} 
$$

Hierbij is licht $\mathit{k}$ gedefinieerd als $l_{\mathit{k}}$. Een licht bevat
alle relevante informatie, positie, intensiteit, etc. De inkomende radiantie van
een enkel licht $l_\mathit{k}$ kan gedefinieerd worden als:

$$ 
\mathit{L_{i}}(\mathbf{p}, l_{\mathit{k}}) = \mathit{f}_{\mathtt{att}}(d) L_{\mathit{k}}
$$

waar $\mathit{d}$ de afstand tussen punt $\mathbf{p}$ en licht 
$l_{\mathit{k}}$ is, zoals beschreven in de definitie van licht.  

Binnen forward shading wordt deze radiantieberekening uitgevoerd in fragment
shader. Dit betekent dat voor elk geproduceerd fragment deze berekening dient 
te worden uitgevoerd, en dat alle informatie per fragment beschikbaar is. Pas 
nadat de radiantie berekening is uitgevoerd, wordt bekeken of een fragment 
daadwerkelijk wordt opgeslagen of niet. Om deze berekening te ontkoppelen, moet de 
lichtberekeningsstap na de bepaling van zichtbare fragmenten worden uitgevoerd. 
Dit betekent dat de verwerking van fragmenten al is voltooid, voordat de radiantie 
wordt berekend. Dit heeft als bijkomend effect dat de gegevens over elk fragment 
niet meer impliciet  beschikbaar zijn. Het is dus nodig om deze expliciet op te slaan
ten tijde van de visibiliteitbepaling.  

Bij inspectie van de functie om belichting $\mathit{L_{o}}$ te berekenen, kunnen de 
volgende attributen ge\"identificeerd worden:

* De geometrie informatie van punt $\mathbf{p}$.
    * De positie van punt $\mathbf{p}$
    * De normaal in punt $\mathbf{p}$
* Informatie met betrekking tot de oppervlakte in punt $\mathbf{p}$
    * De kleur van het oppervlakte
    * Eventuele extra attributen zoals reflectie co\"efficient, ruwheid etc.
* Informatie van de lichten
    * Positie
    * Intensiteit
    * Afstandsdempingfunctie
    
Binnen de geometriestap is het nodig om de benodigde informatie van de 
geometrie en de oppervlakte expliciet op te slaan. De informatie van de lichten
is niet afhankelijk van de fragmenten en kan op een zelfde manier voor de
shading stap beschikbaar gemaakt worden als gedaan wordt in forward shading.
Indien deze eigenschappen worden bepaald voor elk van de fragmenten met behulp 
van de grafische pipeline, zullen de per-pixel-operaties ervoor zorgen dat 
slechts voor de zichtbare fragmenten deze attributen zijn opgeslagen. De 
belichtingsstap zal vervolgens deze waardes uit het geheugen lezen en gebruiken 
om de radiantie te berekenen.


## Gbuffer

\input{./img/tex/fds-gbuffer.tex}

Om het opslaan van deze attributen te faciliteren wordt een datastructuur 
gebruik die de *GBuffer* genoemd wordt. Dit is een object bestaande uit meerdere
texturen, elk verantwoordelijk voor een attribuut dat opgeslagen dient te worden
in de geometriestap zodat deze beschikbaar is in de belichtingsstap. Een 
voorbeeld van deze texturen zoals deze gebruikt worden in het computerspel 
Killzone 2 van Guerrilla Games is gegeven in figuur \ref{fig:fds-gbuffer}. 
Hierin zijn de diepte, normaal, diffuse kleur en shinyness weergegeven.  

Moderne grafische kaarten hebben de mogelijkheid om te renderen naar meerdere
texturen in een enkele uitvoering van de pijplijn. Deze mogelijkheid wordt 
meerdere render doelen (Multiple Render Targets (MRT))
\footnote{https://msdn.microsoft.com/en-us/library/windows/desktop/bb147221(v=vs.85).aspx} 
genoemd. Hiervan wordt gebruik gemaakt om de GBuffer te vullen met informatie in
de geometrie pass. Deze texturen zullen in het geheugen van de grafische kaart 
beschikbaar zijn, en opgevraagd kunnen worden gedurende de belichtingsstap.  


