# Path Problems

How to represent paths to cells, aka indicating cell position, is currently handled adhoc with a list.

## Path Format

> Open Question: Should the location of a component, and the path data be handled via a class?

Answer: This doesn't seem necessary. Though it could be useful.

> Open Question: How many pieces compose a full destination?
We have confirmed that there are at least 4,5 components of a full destination. Most of the time, cells will not be addressed directly for I/O handling. The handling of the problem graph graph data will determine if there are more.
These components are as follows:

- pd_key : Problem Domain dictionary Key (**Subject to change based on brain graph**)
- r_key : Region type/name which is used as a dictionary key
- l_key : Layer name which is used as a dictionary key
- l_pos : the index of an entry in a 2D matrix
- c_ind : the index of the cell at a destination

> Open Question: Should we use r_pos or l_pos to indicate the 2D component?
At present, I'm leaning towards l_pos because each layer is in fact a 2D matrix whereas a region is a stack of matrices.
> [pd_key, r_key, l_key, l_pos(i,j), c_ind]

If necessary, we can turn the location arrrays into string keys by joining with a '-' or ':' between each item.

### Destination Keys

> Open Question: What should be used as the destination between semantically named layers? The order? What about cross-region references?
The destinations should use the path data schema with appropriate substitution slots, and relative paths. Though that does not answer the question.

Answer: ?

## Object Level Representation

> ~~Open Question: For each level of the network, do we represent the current location or path to the current location? In other words, does the current location include the name of the location, or just the precursors to the location?~~

Answer: The location stored at each level should include it's own key or position. Thus each new level does not need to look up it's source, and can just append it's own data to the location.

The levels of a problem graph in this framework are as follows from highest to lowest:

| **Level Name** | **Description** | **Location** |
| --- | --- | --- |
| problem graph | the I/O processing graph | [] |
| problem domain | a node for processing data in the graph<br>composed of multiple processing components | [pd_key] |
| region | a stack of interconnected layers for transforming inputs to outputs | [pd_key, r_key] |
| layer | a 2D matrix of destinations for cell projections | [pd_key, r_key, l_key] |
| destination | the address of a list of cells that handles I/O processing for it's cells | [pd_key, r_key, l_key, l_pos] |
| cell | a unit of I/O processing | [pd_key, r_key, l_key, l_pos, c_ind] |

The top 3 levels are basically meta.

> ~~Open Question: How are distances calculated for the top 3 levels of the hierarchy?~~

Answer: Layers can be though of as an ordered list, or stack. The length of the list then would represent the height of the region. Each layer though is still another level of meta that encapsulates the lowest level vertices in the problem graph graph, the destinations. All the higher level vertices bound the connection possibilities for any given destination.
Regions in a problem domain are themselves very much like a graph. Each region is a vertice, and connection profiles of the regions determines how the edges between regions are built. Though that's redundant, and doesn't explain why a layer connects to a different region, or how it connects.

## problem graph Graph

The problem graph is effectively a graph where each node is a problem domain. The problem graph itself is a high level abstraction used to better understand what the system does, and how it does it.

> Open Question: How do we determine distance between two cells? (i.e. How do we indicate the stage of a PD in the problem graph?)
Animal brains are literal processing graphs. Unlike abstract graphs which can be drawn in many ways because its structure is based solely on edges, each biological vertex in the graph has an intrinsic volume, and position in space. This constrains the rendered representations of the graph, and determines distances between vertices. Consequently, while two vertices may have an edge, the length of the edge either in our graph must be stored explicitly or as a property of a difference between their positions if we are to implement distance based signal propagation. The stage of a PD is one way to handle this though it may not be the best or most intuitive solution. There are two questions here, do we want to determine distance between cells, and what structure should we use to calculate distance?

Answer: ?

> ~~Open Question: Are we able to use the graph to represent distinct steps in a processing sequence?~~
This question is related to the distance between cells question.

Answer: Yes though it is unclear what value doing so brings. All cells are evaluated at each time step so the step in a sequence is a high level abstraction useful for building brain configs. It makes more sense to talk about position in the graph than it does steps in a sequence. Though it is unlikely that a node near the "back" (closest to external input domains) of the graph would directly be one of the last steps in the processing sequence. In such a case, said node probably is receiving feedback.