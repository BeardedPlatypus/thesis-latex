# Meet methodes

Alle testen zijn uitgevoerd op dezelfde hardwarde onder zelfde omstandigheden. 
Voor alle testen zijn de executie tijden van individuele functies binnen elke
lichttoekennings methode, gemeten.
Hiervoor is gebruik gemaakt van de `QueryPerformanceCounter`, functionaliteit
aangeboden binnen `Windows.h`. Hierdoor is het mogelijk om waardes te rapporteren
in de orde van grootte van $\micro s$.

Elke test is drie maal uitgevoerd, indien niet anders vermeld. De gerapporteerde
waardes zijn gemiddelden.[^rauw].

[^rauw]: De rauwe data kan gevonden worden in de repository: \url{https://github.com/BeardedPlatypus/thesis-data-suite}.

## Hardware

Alle testen zijn uitgevoerd op de hardware in de volgende tabel:

\input{./tbl/imp-hardware.tex}

