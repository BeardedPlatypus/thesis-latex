<img src="https://github.com/BeardedPlatypus/thesis-paper/blob/master/teaser.png?raw=true" alt="Teaser image" title="Hashed Shading" align="middle" height="222px" />

# Forward and Deferred Hashed Shading Thesis

## About

This repository houses my master thesis of computer science: 
[Forward and Deferred Hashed Shading for Real-time Rendering of Many Lights](https://github.com/BeardedPlatypus/thesis-latex/blob/master/target/thesis_print.pdf),
as well as all the source files used to create the pdf. The thesis deals with
light assignment algorithms in modern real-time applications. It starts out with
a general introduction to computer graphics, and real-time rendering. It then 
introduces the reader to Deferred Shading, a popular algorithm used to separate
shading complexity from geometrical complexity. In the chapters Tiled Shading 
and Clustered Shading it introduces the respective algorithms currently in use
in many game engines and other real-time applications. The algorithms are 
evaluated with regards to the rendering time and the reduction in light 
calculations achieved. Finally, the new light assignment algorithm, Hashed 
Shading, is introduced.

The thesis text itself is written in dutch, if you prefer an English text, or 
just require a briefer explanation, I recommend reading the accompanying paper,
which can be found [here](https://github.com/BeardedPlatypus/thesis-paper)

The thesis is written in markdown and compiled first into LaTeX with the help
of [Pandoc](http://pandoc.org). If you are interested in how this is done, the
workflow will be described in a future blogpost.

## Abstract

_(as written in the [paper](https://github.com/BeardedPlatypus/thesis-paper/blob/master/paper.pdf))_

This paper introduces the Hashed Shading algorithm, a light assignment algorithm
for forward and deferred shading. It uses a subdivision independent from the view
frustum in order to reuse data structures between frames. The scene is subdivided
into cubes of a specified size and represented using a linkless octree to store
the data efficiently in memory and allow for a fast retrieval of relevant lights
during shading.
The performance of Hashed Shading is compared to both Tiled and Clustered Shading.
Forward Hashed Shading reduces the number of light calculations and the execution
time by a factor of two compared to Forward Tiled Shading. It achieves a similar
reduction in the number of light calculations as Clustered Shading. Furthermore 
the Hashed Shading algorithm scales slightly better in regards to resolution than
Tiled and Clustered Shading due to the camera-independent subdivision.
Currently Hashed Shading does not support dynamic lights, and requires significant
memory to store the linkless octree. Solutions for these issues are proposed but
have not been implemented.

## Table of Contents

1. Inleiding: pag 1.
2. Theorie: pag 5.
3. Methode-overzicht: pag 29.
4. Forward en Deferred Shading: pag 37.
5. Tiled Shading: pag 45.
6. Clustered Shading: pag 67.
7. Hashed Shading: pag 85.
8. Besluit: pag 133.

## Algorithm

The Hashed Shading algorithm uses an octree to subdivide the scene space. In each
leaf node, the intersecting finite lights are stored. This octree can be queried 
when frames are subsequently rendered, with the scene positions of pixels. Each
query returns the set of lights which intersect with the leaf node the pixel falls
within. Thus reducing the set of lights that needs to be evaluated.  

This octree data structure is independent from the view frustum, and thus the 
creation of the initial octree can executed as a pre-process. 

In order to efficiently access the octree on the GPU, the 
[linkless octree implementation](https://hub.hku.hk/bitstream/10722/134617/2/content.pdf?accept=1) 
is used. This approach utilises spatial hash maps which are saved in textures, 
to represent each layer of the octree. Because each layer is represented by a
texture, it can be efficiently accessed on the GPU. 

## Technique comparisons

Hashed Shading is compared with Tiled Shading, Clustered Shading and runs 
without any light assignment algorithms. The results of these experiments
are visualised in the following videos. On the left the actual rendered 
frame is displayed, on the right the number of light calculations per pixel
is visualised, where a white pixel corresponds with the maximum number of 
light calculations, and black with no light calculations. These experiments
were executed for three demo scenes, which can be found in the 
[data repository](https://github.com/BeardedPlatypus/thesis-data).

### Indoor Spaceship Scene

[![Indoor Space Ship Video](https://img.youtube.com/vi/u9o_V4ynB_A/0.jpg)](https://www.youtube.com/watch?v=u9o_V4ynB_A)

*Based upon: [3D Render Challenge #18](http://www.3drender.com/challenges/) modelled by Juan Carlos Silva.*

### Piper's Alley Scene

[![Piper's Alley Video](https://img.youtube.com/vi/nIyifYvU9vI/0.jpg)](https://www.youtube.com/watch?v=nIyifYvU9vI)

*Based upon: [CGSociety Lighting Challenge #42](http://forums.cgsociety.org/showthread.php?t=1309021) made by Clint Rodriues.*

### Ziggurat Scene

[![Ziggurat Video](https://img.youtube.com/vi/HrqiPATdB0Y/0.jpg)](https://www.youtube.com/watch?v=HrqiPATdB0Y)

*Based upon: [Sintel Open Movie Ziggurat Scene](https://durian.blender.org).*


## See also

* [The repository of the software implementing the Hashed Shading algorithm.](https://github.com/BeardedPlatypus/nTiled)
* [The repository of the paper (in english).](https://github.com/BeardedPlatypus/thesis-paper)
* [The repository of all the data gathered presented in this paper.](https://github.com/BeardedPlatypus/thesis-data)


