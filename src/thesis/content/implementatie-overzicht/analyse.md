# Data-analyse

\input{./img/tex/da-cubehelix.tex}

Voor de analyse van de performantie van de verschillende lichttoekenningsalgoritmes
is zowel naar de uitvoeringstijd als het aantal lichtberekeningen gekeken.
Hiervoor zijn voor de volgende relaties ge\"evalueerd:

* De uitvoeringstijd en aantal lichtberekeningen per frame gedurende een volledige uitvoering.
* Gemiddelde uitvoeringstijd en aantal lichtberekeningen per frame gemiddeld over een volledige
  uitvoering als functie van het aantal lichten in de \mbox{sc\`ene}.
* Gemiddelde uitvoeringstijd en aantal lichtberekeningen per frame gemiddeld over een volledige
  uitvoering als functie van de resolutie van de gegenereerde afbeeldingen.
 
Het aantal lichtberekeningen heeft een significante invloed op de uitvoeringstijd, echter
de uitvoeringstijd wordt tevens be\"invloed door de verschillende stappen van 
elk lichttoekenningsalgoritme. Door beide waarde te evalueren wordt een beter inzicht
verkregen in de uitvoeringstijd en performantie van de lichttoekenningsalgoritmes.

Voor elke real-time toepassing is het belangrijk dat de uitvoeringstijden 
consistent zijn. De uitvoeringstijd per frame gedurende een volledige uitvoering geeft
hier inzicht in. 
De performantie van de lichttoekenningsalgoritme ten opzichte van het aantal lichten is
significant omdat een belangrijk doel van de lichttoekenningsalgoritmes is om een groter
aantal lichten mogelijk te maken. Het is dus van belang dat de tijdscomplexiteit als functie
van de lichten zo klein mogelijk is.  
De resolutie is een belangrijke factor voor de hoeveelheid fragmenten die gegenereerd worden.
Verder zal deze waarde een invloed kunnen hebben op de performantie van de camera-afhankelijke
lichttoekenningsalgoritmes.

Verder is per lichttoekenningsalgoritme gekeken naar de specifieke parameters 
van de methode, en hoe deze de tijdscomplexiteit en het  geheugengedrag be\"invloeden.

Al de analyses zijn gedaan met behulp van SciPy[^scipy], Pandas[^pandas], en Seaborn[^seaborn]. Zowel de
verzamelde data, als de analyses zijn beschikbaar in de data-repository. 
Voor de warmtekaarten is gebruik gemaakt van het Cubehelix kleurpalet\cite{green2011colour},
met een startwaarde van $0.5$, rotaties van $-1.5$, en een tint en gamma waarde van $1.0$.
De kleur overgang van dit kleurpalet is weergegeven in figuur \ref{fig:da-cubehelix}.

[^scipy]: website: www.scipy.org
[^pandas]: website: pandas.pydata.org
[^seaborn]: website: seaborn.pydata.org

