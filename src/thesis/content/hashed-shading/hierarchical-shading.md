# Hierarchische Shading

## Building the octree algorithm

Input : 
* Set van lichten $L$
* minimum leaf node size $m_s$

Algorithme:
1. Bereken de oorsprong van de octree $\mathbf{p}_\mathtt{orig}$.  
   De oorsprong $\mathbf{p}_\mathtt{orig}$ is gedefinieerd als het grootste
   mogelijk punt dat kleiner is dan alle licht volumes.  
   $$ \mathbf{p}_\mathtt{orig} = \max(\mathbf{p}) \land \not\exists l \in L : (l_{\mathtt{orig}} - l_{\mathtt{radius}} < p) $$
   
2. Bereken de maximale dimensie van 
