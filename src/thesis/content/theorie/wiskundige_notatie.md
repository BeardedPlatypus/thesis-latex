## Mathematische notaties {#sec:mathematische-notatie}

\input{./tbl/math-notaties.tex}
\input{./tbl/math-operators.tex}

Binnen deze thesis zal veelvuldig gebruik gemaakt worden van verschillende 
mathematische notaties. Tabel \ref{tbl:math-notaties} beschrijft de 
wiskundige betekenis van de verschillende symbolen. Tevens zijn de meest 
gebruikte operatoren gegeven in tabel \ref{tbl:math-operators}. 
In de volgende subsecties zullen de belangrijkste mathematische concepten verder
uitgewerkt worden .

### Euclidische ruimtes

De standaardruimte waarin binnen de computergrafieken gewerkt wordt is de 
Euclidische ruimte, genoteerd als $\mathbb{R}^n$. Een vector binnen deze ruimte
is gedefinieerd als een geordende lijst bestaande uit $n$ re\"ele getallen:

$$ \mathbf{v} \in \mathbb{R}^n \Leftrightarrow \mathbf{v} = \begin{pmatrix}v_0 \\ v_1 \\ \vdots \\ v_{n-1}\end{pmatrix} \text{ waar } v_i \in \mathbb{R} $$

Een vector beschrijft een richting en grootte relatief aan de oorsprong van het 
co\"ordinatenstelsel. 
Een punt wordt tevens voorgesteld als een geordende lijst bestaande uit $n$ 
re\"ele getallen:

$$ \mathbf{p} \in \mathbb{R}^n \Leftrightarrow \mathbf{p} = \begin{pmatrix}p_0 \\ p_1 \\ \vdots \\ p_{n-1}\end{pmatrix} \text{ waar } p_i \in \mathbb{R} $$

\noindent Een punt beschrijft een positie in de ruimte $\mathbb{R}^n$ waartoe deze behoort.

Zowel punten als vectoren kunnen worden gemanipuleerd met matrices. Een matrix 
is gedefinieerd als een blok van $p \times q$ re\"ele getallen:

$$ \mathbf{M} = 
       \begin{bmatrix} 
         m_{00}    & m_{01}    & \dots  & m_{0,q-1}   \\
         m_{10}    & m_{11}    & \dots  & m_{1,q-1}   \\
         \vdots    & \vdots    & \ddots & \vdots      \\
         m_{p-1,0} & m_{p-1,1} & \dots  & m_{p-1,q-1} \\
       \end{bmatrix} = [m_ij]
$$ 

\noindent Enkele veel voorkomende drie dimensionale transformaties die voorgesteld kunnen worden als matrix 
zijn rotatie, schaling en scheer:

\begin{align*}
  \text{Rotatie over hoek $\theta$ } \mathbf{R_x} &= 
    \begin{bmatrix} 1 &          0 &           0 \\
                    0 & \cos\theta & -\sin\theta \\
                    0 & \sin\theta &  \cos\theta
    \end{bmatrix}\\
    \mathbf{R_y} &= \begin{bmatrix} \cos\theta & 0 & -\sin\theta \\
                                            0 & 1 &           0 \\
                                   \sin\theta & 0 &  \cos\theta
                    \end{bmatrix}\\
    \mathbf{R_z} &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\
                                    \sin\theta &  \cos\theta & 0 \\
                                             0 &           0 & 1 
                    \end{bmatrix}\\
  \text{Schaling met $s$ } \mathbf{S} &= 
    \begin{bmatrix} s & 0 & 0 \\
                    0 & s & 0 \\
                    0 & 0 & s 
    \end{bmatrix}\\
  \text{Scheer met $\lambda$ } \mathbf{H}_{0,2} &= 
    \begin{bmatrix} 1 & 0 & \lambda \\
                    0 & 1 &       0 \\
                    0 & 0 &       1 
    \end{bmatrix}
\end{align*}

Matrices kunnen samengesteld worden met behulp van matrix vermenigvuldiging. Dit
leidt er bijvoorbeeld toe dat de transformatie waarbij een vector $\mathbf{v}$
eerst wordt geroteerd over de $x$-as:

$$ \mathbf{v}^\prime = \mathbf{R_x} \mathbf{v} $$

\noindent en vervolgens geschaald met een waarde $s$:

$$ \mathbf{v}^{\prime\prime} = \mathbf{S}\mathbf{v}^\prime $$

\noindent gelijk is aan de samenstelling van de transformaties $R_x$ en $S$.

$$ \mathbf{v}^{\prime\prime} = \mathbf{S}(\mathbf{R_x}\mathbf{v}) = (\mathbf{S}\mathbf{R_x})\mathbf{v} $$

### Homogene co\"ordinaten

In theorie is het mogelijk om zowel punten en vectoren in de drie dimensionale 
Euclidische ruimte, $\mathbb{R}^3$, voor te stellen als een $3$-tupel van 
re\"ele getallen. Echter binnen deze voorstelling is het niet mogelijk om de 
translatietransformatie als matrix voor te stellen. Dit heeft geen invloed op
vectoren, gezien translatie niet gedefinieerd is voor vectoren. Echter 
translaties hebben wel betekenis voor punten. 

Om dit probleem op te lossen worden punten en vectoren in de drie dimensionale
Euclidische ruimte $\mathbb{R}^3$ niet met drie maar met vier re\"ele getallen
voorgesteld. Deze voorstelling van co\"ordinaten wordt het homogene 
co\"ordinatenstelsel genoemd.

Een vector in homogene co\"ordinaten wordt dan voorgesteld als:

$$ \mathbf{v} \in \mathbb{R}^4 \Leftrightarrow \mathbf{v} = \begin{pmatrix}v_x \\ v_y \\ v_z \\ 0\end{pmatrix} \text{ waar } v_i \in \mathbb{R} $$

\noindent Een punt in homogene co\"ordinaten wordt voorgesteld als:

$$ \mathbf{p} \in \mathbb{R}^4 \Leftrightarrow \mathbf{p} = \begin{pmatrix}p_x \\ p_y \\ p_z \\ 1\end{pmatrix} \text{ waar } p_i \in \mathbb{R} $$

\noindent Verder worden de transformatie matrices uitgebreid van $3 \times 3$ elementen
naar $4 \times 4$ elementen:

$$ \mathbf{M}_{4\times4} = \begin{bmatrix} m_{00} & m_{01} & m_{02} & 0 \\
                                  m_{10} & m_{11} & m_{12} & 0 \\
                                  m_{20} & m_{21} & m_{22} & 0 \\
                                       0 &      0 &      0 & 1
                           \end{bmatrix} $$
                  
\noindent waarbij $\mathbf{M}$ vervangen kan worden door de rotatie-, schalings-, en scheermatrices
om de equivalente transformatie matrices in homogene co\"ordinaten te 
verkrijgen.

Nu is het mogelijk om de translatiematrix te defini\"eren als:

$$ \mathbf{T} = \begin{bmatrix} 1 & 0 & 0 & t_x \\
                                0 & 1 & 0 & t_y \\
                                0 & 0 & 1 & t_z \\
                                0 & 0 & 0 &   1 
                \end{bmatrix}$$
       
\noindent Deze transformatie zal geen invloed hebben op vectoren, doordat $p_w = 0$, maar
zal wel punten met $\mathbf{t}$ transleren doordat $p_w = 1$. 

Het is mogelijk dat voor $p_w$ een waarde anders dan $0$ of $1$ gevonden wordt. 
In dat geval dient het punt gedeeld te worden door $p_w$ om de correcte 
Euclidische co\"ordinaten $p_x$, $p_y$ en $p_z$ te verkrijgen. Dit wordt 
homogenisatie genoemd.

