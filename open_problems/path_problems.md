# Path Problems

How to represent paths to cells, aka indicating cell position, is currently handled adhoc with a list.

## Path Format

> Open Question: Should the location of a component, and the path data be handled via a class?
> Open Question: How many pieces compose a full destination?
We have confirmed that there are at least 4,5 components of a full destination. Most of the time, cells will not be addressed directly for I/O handling. The handling of the brain network graph data will determine if there are more.
These components are as follows:

- pd_key : Problem Domain dictionary Key (**Subject to change based on brain graph**)
- r_key : Region type/name which is used as a dictionary key
- l_key : Layer name which is used as a dictionary key
- l_pos : the index of an entry in a 2D matrix
- c_ind : the index of the cell at a destination

> Open Question: Should we use r_pos or l_pos to indicate the 2D component?
At present, I'm leaning towards l_pos because each layer is in fact a 2D matrix whereas a region is a stack of matrices.
> [pd_key, r_key, l_key, l_pos(i,j), c_ind]

## Object Level Representation

> Open Question: For each level of the network, do we represent the current location or path to the current location?
> Open Question: Does the current location include the name of the location, or just the precursors to the location?

The levels of a brain network in this framework are as follows from highest to lowest:

| **Level Name** | **Description** | **Location** |
| --- | --- | --- |
| brain network | the I/O processing graph | [] |
| problem domain | a node for processing data in the graph<br>composed of multiple processing components | [pd_key] |
| region | a stack of interconnected layers for transforming inputs to outputs | [pd_key, r_key] |
| layer | a 2D matrix of destinations for cell projections | [pd_key, r_key, l_key] |
| destination | the address of a list of cells that handles I/O processing for it's cells | [pd_key, r_key, l_key, l_pos] |
| cell | a unit of I/O processing | [pd_key, r_key, l_key, l_pos, c_ind] |

The top 3 levels are basically meta.

> Open Question: How are distances calculated for the top 3 levels of the hierarchy?

Layers can be though of as an ordered list, or stack. The length of the list then would represent the height of the region. Each layer though is still another level of meta that encapsulates the lowest level vertices in the brain network graph, the destinations. All the higher level vertices bound the connection possibilities for any given destination.
Regions in a problem domain are themselves very much like a graph. Each region is a vertice, and connection profiles of the regions determines how the edges between regions are built. Though that's redundant, and doesn't explain why a layer connects to a different region, or how it connects.

## Brain Network Graph

The brain network is effectively a graph where each node is a problem domain. The brain network itself is a high level abstraction used to better understand what the system does, and how it does it.

> Open Question: How do we indicate the stage of a PD in the brain network?
> Open Question: Are we able to use the graph to represent distinct steps in a processing sequence?