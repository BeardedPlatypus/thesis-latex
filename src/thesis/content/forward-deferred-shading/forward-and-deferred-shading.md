# Forward en deferred shading

\input{./img/tex/fds-scene.tex}

Binnen sectie \ref{moderne-grafische-pipeline} is vastgesteld dat bij standaard
uitvoering, pas na uitvoering van de fragment shader wordt bepaald welke
fragmenten daadwerkelijk zichtbaar zijn. Dit betekent dat ook voor fragmenten
die geen enkele invloed zullen hebben op de scene, de shading berekening worden
uitgevoerd. De shading complexiteit is dus direct gekoppeld aan de scene
complexiteit. Voor simpele scenes is dit geen probleem, echter wanneer scenes
complexer worden kan dit leiden tot een grote mate van verspilde rekenkracht.
Een simpel voorbeeld van een dergelijke scene, waar belichtingsberekening
onnodig worden uitgevoerd is weergegeven in figuur \ref{fig:fds-scene}.  

Een logische stap om dit probleem op te lossen is het ontkoppelen van
visibiliteit en shading. Dit leidt tot twee discrete stappen, een 
visibiliteitsstap waar rasterisatie plaats vindt en de informatie van de
zichtbare fragmenten als uitvoer wordt gegeven.  

Deze oplossing is niet nieuw binnen computer graphics, zo werd in de scan-line
polygon renderer van Watkins (\cite{watkins1970real}) in de jaren 70 al 
bepaald welke oppervlakte het dichtst bij de camera lag en slechts hiervoor
de lichtberekeningen uitgevoerd. Andere hardware en software implementaties
zijn tevens in de jaren 80 geintroduceerd \cite{}. Een specifieke beschrijving
van deferred shading is gegeven in \cite{}. Moderne deferred shading algoritmes
maken veelal gebruik van het concept GBuffers. GBuffers waren oorspronkelijk
geintroduceerd in de context van het non-photorealistsch renderen om visuele
begrijpbaarheid te verbeteren.\cite{} Echter het concept van GBuffers leent
zich om de data tussen de visibiliteitsstap en de shading stap op te slaan.  

In deze sectie zal ingegaan worden op het algoritme van deferred shading om
de koppeling tussen geometrie complexiteit en shading op te lossen. Vervolgens
zal gekeken worden naar nieuwe algoritmes die verder bouwen op deferred 
shading.  

## Definities

Binnen deze thesis zal de volgende terminologie gebruikt worden. 
*Forward shading* beschrijft de standaard uitvoering van de render pijplijn. 
Hier wordt niet expliciet de fragmenten op diepte gefilterd, en dus zal voor
elk fragment de belichtingsberekeningen uitgevoerd worden.  

*Deferred shading* beschrijft het algoritme waarbij expliciet de render pijplijn
wordt onderverdeeld in twee discrete stappen, een geometriestap en een 
belichtingsstap. De visibiliteitsstap maakt hierbij gebruik van een *GBuffer* om
de geometrie data op te slaan.  

*Light-pre pass* beschrijft het algoritme waarbij eerst een z-pass wordt
uitgevoerd voordat de shading stap wordt uitgevoerd.  

## Deferred shading

Zoals besproken in sectie \ref{shading}, is de rendering vergelijking gegeven
door: 

$$ 
\mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \int_{2\pi^{+}} \mathit{f_{r}}(\mathbf{p}, \omega_{i}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, \omega_{i})\cos\theta_{i}d\omega_{i} 
$$

Uitgaande dat een punt geen licht uitstraalt, dan zou de rendering vergelijking
benaderd kunnen worden door middel van een beschrijving van directe belichting:

$$ 
\mathit{L_{o}}(\mathbf{p}, \omega_{o}) = \sum_{\mathit{k}=1}^{\mathit{n}} \mathit{f_{r}}(\mathbf{p}, l_{\mathit{k}}, \omega_{o})\mathit{L_{i}}(\mathbf{p}, l_{\mathit{k}})\cos\theta_{i} 
$$

Hierbij is licht $\mathit{k}$ gedefinieerd als $l_{\mathit{k}}$. Een licht bevat
alle relevante informatie, positie, intensiteit, etc. De inkomende radiantie van
een enkel licht $l_\mathit{k}$ kan gedefinieerd worden als:

$$ 
\mathit{L_{i}}(\mathbf{p}, l_{\mathit{k}}) = \mathit{f}_{\mathtt{att}}(d) L_{\mathit{k}}
$$

waar $\mathit{d}$ gedefinieerd als de afstand tussen punt $\mathbf{p}$ en licht 
$l_{\mathit{k}}$. Zoals beschreven in de definitie van licht.  

Binnen forward shading wordt deze radiantie berekening uitgevoerd in fragment
shader. Dit betekent zowel dat voor elk fragment deze berekening dient te worden
uitgevoerd, en dat alle informatie per fragment beschikbaar is. Pas nadat de
radiantie berekening is uitgevoerd, wordt bekeken of een fragment daadwerkelijk
wordt opgeslagen of niet. Om deze berekening te ontkoppelen, moet de lichtstap
na de zichtbare fragment bepaling worden uitgevoerd. Dit betekent dat de 
verwerking van fragmenten al is voltooid, voordat de radiantie wordt berekend.
Hierdoor zijn de gegevens over elk fragment niet meer impliciet beschikbaar, en
zullen deze expliciet moeten worden opgeslagen ten tijde van de visibiliteit
bepaling.  

Bij inspectie van de functie om $\mathit{L_{o}}$ te berekenen, kunnen de 
volgende attributen geidentificeerd worden:

* De geometrie informatie van punt $\mathbf{p}$.
    * De positie van punt $\mathbf{p}$
    * De normaal in punt $\mathbf{p}$
* Informatie met betrekking tot de oppervlakte in punt $\mathbf{p}$
    * De kleur van het oppervlakte
    * Eventuele extra attributen zoals reflectie coefficient, ruwheid etc.
* Informatie van de lichten
    * Positie
    * Intensiteit
    * Afstandsdempingfunctie
    
Binnen de geometrie stap is het nodig om de benodigde informatie van de 
geometrie en oppervlakte expliciet op te slaan. De informatie van de lichten
is niet afhankelijk van de fragmenten en kan op een zelfde manier voor de
shading stap beschikbaar gemaakt worden als gedaan wordt in forward shading.
Indien deze eigenschappen worden bepaald voor elk van de fragmenten, zullen de 
per pixel operaties ervoor zorgen dat slechts voor de zichtbare fragmenten deze
attributen zijn opgeslagen. De shading stap zal vervolgens deze waardes uit het
geheugen uitlezen en gebruiken om de radiantie te berekenen.

### Gbuffer

\input{./img/tex/fds-gbuffer.tex}

Om het opslaan van deze attributen te faciliteren wordt een techniek gebruik die
GBuffers genoemd wordt. Dit is een object bestaande uit meerdere textures, elk
verantwoordelijk voor een attribuut dat opgeslagen dient te worden tussen 
geometry en shading pass. Een voorbeeld van deze textures voor een enkel frame
is gegeven in figuur \ref{fig:fds-gbuffer}. Hierin zijn de positie, normaal,
diffuse kleur en textuur coordinaten weergegeven.  

Moderne grafische kaarten hebben de mogelijkheid om te renderen naar meerdere
texturen in een enkele uitvoering van de pijplijn. Deze mogelijkheid wordt 
meerdere render doelen (Multiple Render Targets (MRT)) genoemd. Hiervan wordt
gebruik gemaakt om de GBuffer te vullen met informatie in de geometrie pass.
Deze textures zullen in het geheugen van de grafische kaart beschikbaar zijn,
en opgevraagd kunnen worden gedurende de shading stap.  

### Algoritme

Als een laatste optimalisatie kan opgemerkt worden dat veelal lichten slechts, 
een beperkte invloed hebben op de scene. Slechts pixels binnen het lichtvolume
kunnen worden gekleurd door een licht. Het is mogelijk om de lichtvolumes te
rasteriseren, en slechts de licht benadering uit te voeren voor deze fragmenten.
Dit leidt tot het volgende algoritme.

```
# Geometry pass
# ------------------------------------------------
for obj in scene_objects:
    fragments = rasterise(obj)
    
    for frag in fragments:
        write_to(gbuffer, frag.attributes)
        
per_pixel_operations()

# Shading pass
# ------------------------------------------------
for light in scene_lights:
    fragments = rasterise(light.volume)
    
    for frag in fragments:
        attributes = look_up(gbuffer, frag.pos)
        canvas[frag.pos] += do_shade(frag, attributes, light)

per_pixel_operations()
```

### Nadelen

Het grootste probleem met het gepresenteerde algoritme is de hoge bandbreedte
vereiste. Bij een toenemend aantal lichten zal voor elk fragment de attributen
meerdere malen moeten worden opgevraagd. Doordat de geheugenbandbreedte binnen
een grafische kaart beperkt is kan dit een knelpunt worden. Tevens zal de
GBuffer bij toenemende complexiteit van de shader, meer attributen moeten 
opslaan, wat leidt tot een groter geheugen verbruik.  

Een tweede belangrijk minpunt is dat dit algoritme slechts werkt voor 
ondoorzichtige objecten. De GBuffers zijn niet in staat om meer dan een laag
geometrie op te slaan, in het geval dat er transparantie nodig is binnen een
is het niet mogelijk om de attributen hiervan op te slaan. Om transparantie
te ondersteunen binnen deferred shading zullen of wel meerdere gbuffers nodig 
zijn, of wel een aparte rendering pass voor alle transparante objecten.
Het bijhouden van meerdere GBuffers leidt tot groot geheugenverbruik, en is
daarom veelal onbruikbaar.  

Een derde probleem is dat anti-aliasing niet meer triviaal ondersteun wordt.
Binnen de shading pass is het niet mogelijk om sub-pixels te bemonsteren, gezien
ook deze data expliciet opgeslagen moet worden. Hiervoor bestaan wel 
alternatieve anti-aliasing technieken die werken binnen een deferred shading 
context, voorbeelden hiervan zijn ....

## Forward+ shading

Forward+ shading, lighting pre-pass, deferred lighting, zijn een collectie van
vergelijkbare algoritmes die verder bouwen op deferred shading, met als 
belangrijkste doel het geheugen verbruik en bandbreedte te verminderen.

Het gaat uit van het concept dat de set van BRDFs die de kleur van een
oppervlakte bepaald veelal bestaat uit individuele lichttermen, difuus en
speculair. Indien de benadering van de rendering vergelijking wordt herschreven
in een vorm van een diffuus en een speculair component, dan wordt de functie:

$$ 
\mathit{L_{o}}(\mathbf{p}) = \sum_{\mathit{k}=1}^{\mathit{n}}\big( \mathbf{c}_{\mathtt{diff}} * \mathit{f}_{\mathtt{diff}}(\mathit{L_{i_{\mathit{k}}}}, \mathbf{l}_{\mathit{k}}, \mathbf{n}) + \mathbf{c}_{\mathtt{spec}} * \mathit{f}_{\mathtt{spec}}(\mathit{L_{i_{\mathit{k}}}}, \mathbf{l}_{\mathit{k}}, \mathbf{n}, \mathbf{p}, \mathit{m})) 
$$

waarbij $\mathit{f}_{\mathtt{spec}}$ en $\mathit{f}_{\mathtt{diff}}$ de shading 
functies zijn, onafhankelijk van de mogelijke kleur van een punt. Deze worden
bepaald door de intensiteit van het licht $\mathit{L_{i_{\mathit{k}}}}$, de 
lichtinvals hoe op het punt $\mathbf{p}$ en de normaal $\mathbf{n}$ in punt 
$\mathbf{p}$. Doordat de speculaire en diffuse term onafhankelijk zijn is het
mogelijk om de benadering van de rendering vergelijk te herschrijven tot:


$$
\mathit{L_{o}}(\mathbf{p}) = \mathbf{c}_{\mathtt{diff}} * \sum_{\mathit{k}=1}^{\mathit{n}}\big( \mathit{f}_{\mathtt{diff}}(\mathit{L_{i_{\mathit{k}}}}, \mathbf{l}_{\mathit{k}}, \mathbf{n})) + \mathbf{c}_{\mathtt{spec}} * \sum_{\mathit{k}=1}^{\mathit{n}}\big(\mathit{f}_{\mathtt{spec}}(\mathit{L_{i_{\mathit{k}}}}, \mathbf{l}_{\mathit{k}}, \mathbf{n}, \mathbf{p}, \mathit{m})) 
$$

### Algoritme

Deze opdeling leidt tot het volgende algoritme

1. Rasteriseer de ondoorzichte geometrie, waarbij de normaal vector $\mathbf{n}$
   en schrijf per fragment de speculaire spreiding $\mathit{m}$ weg naar een 
   texture. Deze $\mathbf{n}\mathit{m}$ buffer is vergelijkbaar met een GBuffer 
   maar bevat signifacant minder geheugen.
2. Rasteriseer de licht volumes en bereken per fragment de shading functies 
   $\mathit{f}$. In het geval dat $\mathit{f}_{\mathtt{spec}}$ en 
   $\mathit{f}_{\mathtt{diff}}$ berekend dienen te worden, zullen hier twee
   textures voor nodig zijn, waarin de waardes geaccummuleerd worden.
   
   $$
   \begin{aligned}
     \mathit{G}_{\mathtt{diff}} &= \sum_{\mathit{k}=1}^{\mathit{n}}\big( \mathit{f}_{\mathtt{diff}}(\mathit{L_{i_{\mathit{k}}}}, \mathbf{l}_{\mathit{k}}, \mathbf{n})) \\
     \mathit{G}_{\mathtt{spec}} &= \sum_{\mathit{k}=1}^{\mathit{n}}\big(\mathit{f}_{\mathtt{spec}}(\mathit{L_{i_{\mathit{k}}}}, \mathbf{l}_{\mathit{k}}, \mathbf{n}, \mathbf{p}, \mathit{m}))
   \end{aligned}
   $$
   
3. Rasteriseer opnieuw de ondoorzichte geometrie, ditmaal wordt de data uit de
   accumulatie fase uitgelezen en vermenigvuldigd met de kleuren van het punt
   $\mathbf{p}$, tevens worden in deze stap andere licht berekening gedaan die
   niet uitgevoerd zijn in de accumulatie fase.
   Dit leidt tot:
   
   $$
   \mathit{L_{o}}(\mathbf{p}) = \mathbf{c}_{\mathtt{diff}} * \mathit{G}_{\mathtt{diff}} + \mathbf{c}_{\mathtt{spec}} * \mathit{G}_{\mathtt{spec}} 
   $$
   
## Conclusie

In deze sectie zijn twee algoritmes geintroduceerd als oplossing voor de 
koppeling tussen geometrie complexiteit en shading complexiteit. Beide delen
het renderprocess op in meerdere stappen, zodat slechts de shading berekeningen
uitgevoerd hoeven te worden voor de zichtbare elementen.  

