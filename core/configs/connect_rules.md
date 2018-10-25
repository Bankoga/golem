# Connect Rules

The rules used to map connections between descriptions of regions of graphs.

## General Rules

PD Level

- Overlapping PDs / structures to connect are within the same region
- Structures to connect are in different PDs

From one Region to:

- another region
  - in another PD
  - in the same PD
- within the same region

From one Layer to:

- another Layer
  - Region
    - within the same region
    - in a different region
  - PD
    - within the same PD
    - in a different PD

Diff rules/ways for connecting/stitching: Stitching (nxm -> cxr), Convolving (nxn -> 1, dilate, skips)

From one Cell || Destination to:
is there a diff?

Cell -> Dest
Cell <- Dest

Cells tell their container where to read from. The destination collects a list of all other destinations to read from at each timestep.
All cells in a container read from that container
Cells go to different places, with different spreads
Dests tell their cells where to go based on a mapping of lxw's, and fill props for relevant PDs

PD level maps of different levels of destination to destination mapping
Dest -> Dest mapping are used by cells for projection & reception filling of connection paths

Cells to/from:

- self/same dest
  - all cells project to dests as described in the relevant config
    - output dests are filled based on the output pds input layers arrays
  - all cells read from their container
- same layer
  - for projection: ???? and use the Axon spread rules
  - for reading: use the Dendrite spread rules
- same region (regions in the same PD are assumed to have 1:1 LxW mapping between Layers)
  - for projection: reuse self layer coords in the target layer
  - for reading: use the Dendrite spread rules
- diff region in the same PD
  - for projection: use the identity mapping between LxW (raw LxW ratio mapping(?))
  - for reading: use the Adjacency rules
- diff PD:
  - for projection: always use input layers array mapping
  - for reading: always use raw LxW's ratio mapping(?)

Cross PD axons go through designated input layers, and require entry mappings
Cross PD dendrites pass through boundaries, and cross matrices. They require adjacency Position to Position mappings. I.E. we need to know what the terrain looks like.

### Alg of creation

- count outgoing edges, LxW of destination PDs, shape of output per destination PD
- count incoming edges, LxW of each input PD, shape of each input PD
- map destinations of layers within each region to layers within the same region (UNNECESSARY?)
- map destinations of layers with output paths to destination PD layers+LxW coords
  - f(a,r_a,l_a,x_a,y_a,d) => d, (d,r_d,l_d,x_d,y_d)

## Axon Spread Rules

Axons have core target Destinations set as per the relevant mapping via the layers cell type axon config. At these destinations, the axon can branch out in shapes (like a square) of some size (like 4x4). So it will put the target in the middle of the shape, and add all dests that fit inside the shape to the axons projections. Axons can also project specifically to a single destination without spreading upon arrival. Spreading is handled at each axon branch terminal/end point.
Cells thus handled output spread from core targets, and are separate from layer filling.

## Dendrite Spread Rules

Oh me...

## Adjacency Rules (physicality rules)

Oh my...

