# Shading: implementatie

Alle shading binnen deze thesis is uitgevoerd met dezelfde rendering functie. 
Deze functie wordt berekend voor alle relevante lichten binnen de fragment shader.
De gebruikte rendering functie is een simpele direchte licht benadering van 
een Lambertiaans wit oppervlakte, zoals beschreven in het theorie hoofdstuk.
Deze is als volgt gedefinieerd:

```
struct Light {
  vec4 position;
  vec3 intensity;
  float radius;
};

struct GeometryParam {
  vec4 position;
  vec3 normal;
  vec3 colour;
};

vec3 computeLight(Light light,
                  GeometryParam param) {
  vec3 light_direction = 
    vec3(light.position - param.position);
  float d = length(L);
  light_direction /= d;

  float attenuation = 
    clamp(1.0 - ( d / light.radius ), 0.0f, 1.0f);
  attenuation *= attenuation;

  float cos_angular_incidence = 
    clamp(dot(param.normal, light_direction), 0.0f, 1.0f);
  return (param.colour * light.intensity * 
          cos_angular_incidence * attenuation);
}
```

Deze functie komt overeen met de volgende formule

$$
\mathit{L}(l_{i}, \mathbf{p}) = \mathit{c}_\mathbf{p} * \mathit{I_i} * \cos\theta * \mathit{f_\mathtt{att}}
$$

waar

$$
\mathit{f_\mathtt{att}} = ( 1 - \left.\frac{\mathit{d}}{\mathit{r_i}}\right|_{{0, 1}})
$$

Om de volledige kleur van een fragment te berekenen dient deze functie uitgevoerd te worden voor 
elk licht dat invloed heeft op dit fragment. Hiervoor is het nodig om de positie en de normaal
van het punt te hebben. Deze worden doorgegeven vanuit de vertex shader. 

\input{./img/tex/imp-lambert.tex}

Dit alles gecombineerd leidt tot oppervlaktes zoals weergegeven in figuur \ref{fig:imp-lambert}.

