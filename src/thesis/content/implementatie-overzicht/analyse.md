# Data-analyse

\input{./img/tex/da-cubehelix.tex}

Om de tijdscomplexiteit van de verschillende methodes te vergelijken is primair
gekeken naar de volgende drie relaties.

* Executietijd per frame gedurende een uitvoering.
* Gemiddelde executietijd per uitvoering als functie van het aantal lichten.
* Gemiddelde executietijd per uitvoering als functie van de resolutie.

Voor elke real-time toepassing is het belangrijk dat de executietijden 
consistent zijn. Dit kan ge\"evalueerd woorden aan de hand van de executietijd
per frame. Het hoofddoel van lichttoekenningsalgoritmes is het mogelijk maken van grotere
sets van lichten binnen scenes. Hierbij is de tijdscomplexiteit als functie van
het aantal lichten dus belangrijk. Als laatste geeft de tijdscomplexiteit als functie
van de resolutie een indicatie hoe het lichttoekenningsalgoritme zich gedraagt bij een
toenemend aantal fragmenten. Tevens is de resolutie een attribuut dat direct invloed
heeft op de berekeningtijd van camera-afhankelijke lichttoekenningsalgoritmes.

Verder is per lichttoekenningsalgoritme gekeken naar de specifieke parameters 
van de methode, en hoe deze van invloed zijn op de tijdscomplexiteit en het 
geheugengedrag.

Al de analyses zijn gedaan met behulp van SciPy[^scipy], Pandas[^pandas], en Seaborn[^seaborn]. Zowel de
verzamelde data, als de analyses zijn beschikbaar in de data-repository. 
Voor de warmtekaarten is gebruik gemaakt van het Cubehelix kleurpalet\cite{green2011colour},
met een startwaarde van $0.5$, rotaties van $-1.5$, en een tint en gamma waarde van $1.0$.
De kleur overgang van dit kleurpalet is weergegeven in figuur \ref{fig:da-cubehelix}.

[^scipy]: website: www.scipy.org
[^pandas]: website: pandas.pydata.org
[^seaborn]: website: seaborn.pydata.org

