# Path Problems

How to represent paths to cells, aka indicating cell position, is currently handled adhoc with a list.

## Path Format

> Open Question: Should the location of a component, and the path data be handled via a class?
> Open Question: How many pieces compose a full destination?
We have confirmed that there are at least 4,5 components of a full destination. Most of the time, cells will not be addressed directly for I/O handling. The handling of the brain network graph data will determine if there are more.
These components are as follows:

- pd_key : Problem Domain dictionary Key (**Subject to change based on brain graph**)
- r_key: Region type/name which is used as a dictionary key
- l_key : Layer name which is used as a dictionary key
- l_pos : the index of an entry in a 2D matrix
- c_ind : the index of the cell at a destination

> Open Question: Should we use r_pos or l_pos to indicate the 2D component?
At present, I'm leaning towards l_pos because each layer is in fact a 2D matrix whereas a region is a stack of matrices.
> [pd_key, r_key, l_key, l_pos(i,j), c_ind]

## Brain Network Graph

The brain network is effectively a graph where each node is a problem domain. The brain network itself is a high level abstraction used to better understand what the system does, and how it does it.

> Open Question: How do we indicate the stage of a PD in the brain network?
> Open Question: Are we able to use the graph to represent distinct steps in a processing sequence?