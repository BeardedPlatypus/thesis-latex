In het vorige hoofdstuk is Deferred shading ge\"introduceerd. Hiermee werd de 
geometrische complexiteit ontkoppeld van de shadingcomplexiteit. Er zijn enkele
significante nadelen aan het gebruik van een Deferred pijplijn. Indien gebruik
gemaakt wordt van een stencil optimalisatie, vereist de Deferred pijplijn dat
per licht de informatie van een fragment uit de GBuffer opgehaald dient te 
worden. Dit leidt tot een hoge geheugenbandbreedte. Indien een dergelijke 
optimalisatie niet is ge\"implementeerd, dient voor elk fragment, elk licht in
de scene ge\"evalueerd te worden. 

Om deze problemen tegen te gaan is de techniek Tiled Shading voorgesteld.~\cite{olsson2011tiled}
Het achterliggende idee is om het zichtveld onder te verdelen in tegels 
bestaande uit $n\times n$ pixels, voordat de belichtingsberekening wordt 
uitgevoerd. Een voorbeeld van een dergelijke onderverdeling is weergegeven in 
figuur \ref{fig:ts-grid-intro}. Voor elke tegel wordt bepaald welke lichten gedeeltelijk 
overlappen met de tegel. Deze lichten worden bijgehouden in een lijst 
geassocieerd met de tegel. Vervolgens worden tijdens de belichtingsberekening 
slechts de lichten behandeld van de tegel waartoe het fragment behoort. 

\input{./img/tex/ts-grid-intro.tex}

In dit hoofdstuk wordt de Tiled Shading techniek verder toegelicht. Eerst zal
de achterliggende theorie behandeld worden. Vervolgens zal ingegaan worden op
het algoritme en de bijbehorende datastructuren. Als laatste wordt de 
implementatie ge\"evalueerd aan de hand van de drie testscenes en vergeleken
met de na\"ive shaders.

