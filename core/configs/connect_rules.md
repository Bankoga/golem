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

From one Cell || Destination to:
is there a diff?

Cell -> Dest
Cell <- Dest

Cells tell their container where to read from. The destination collects a list of all other destinations to read from at each timestep.
All cells in a container read from that container
Cells go to different places, with different spreads
Dests tell their cells where to go based on a mapping of lxw's, and fill props for relevant PDs

self/same dest

- all cells project to dests as described in the relevant config
  - output dests are filled based on the output pds input layers arrays
- all cells read from their container

same layer

- for projection: 
- for reading: use the dendrite spread rules

same region (regions are assumed to have 1:1 LxW)

- for projection: reuse self layer coords in the target layer
- for reading: use the dendrite spread rules

diff region

- for projection: 
- for reading: 

diff PD:

- for projection, always use input layers array mapping
- for reading, always use raw LxW's ratio mapping(?)

## Dendrite Spread Rules

## Adjacency Rules

Oh my...