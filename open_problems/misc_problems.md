# Miscellaneous Problems

## Graph Storage

It has come to my attention that even a modestly sized graph as an adjacency list of just the cells, and their edges would consume tons of memory. Thus the issue of the data structure of the graph has become imperative. Regardless of how many other questions are answered, if the final object is of an unrealizable size then the enterprise is doomed to failure. This is not acceptable! While some memory usage optimizations will result once we move to another language after validating the test framework in python, the space complexity of the system still matters for the python implementation. In order to have a successful proof of approach that can be optimized, we must decide on the data structure of the destination graph.

> ~~Open Question: Go with the object nesting approach, where each layer is a matrix of destinations, unify all destinations into a single adjacency list, or some other data structure?~~

Answer: **Stay the course! For now anyway...**

Refactoring the code to use a single list for all destinations seems doable later on. For now, manifesting the conceptual aspects of each destination as actual code objects, helps with implementation. If it is necessary to reduce the number of objects to a single list of destinations with the meta levels merely used to build the list, then we can handle that later.

> ~~Open Question: Does every destination/cell need to be touched during each timestep?~~

Answer: **Yes because we need to know if the cell activated based on the inputs it received**

> Open Question: What data structure should be used for storing destinations, and cells?

Previously, each destination was going to live inside of an actual 2D matrix, and contain a list of cells. **The 2D matrix may live on in concept being used during the init, but it may not be efficient enough for use as the actual data structure to store destinations.**
Cells would use lists of edges to grab the data sets they needed for dendrite summation from the universe of outputs. Grabbing the source sets for each destinations requires sorting the outputs into a bucket per source set, then looping through each cell while grabbing the outputs by source set key.

Cost_of_sort = num_destinations + num_outputs (i.e num_edges) or Merge_sort(num_destinations) + num_outputs
Cost_source_grab = sum_all_cells(sources_to_grab) = num_cells * num_sources_to_grab (i.e. num_edges)
ops_input_to_cell_per_ts = Cost_of_Sort + Cost_source_grab

num_cells = 1 * Math.pow(10,9)
edges_per_cell = 3000
num_edges = num_cells * edges_per_cell
ops_prep_cells_per_ts = num_edges + num_cells + (num_edges + num_cells)

var num_cells = 16 * Math.pow(10,9)
var edges_per_cell = 3000
var num_edges = num_cells * edges_per_cell
var ops_prep_cells_per_ts = (num_edges + num_cells + (num_edges+num_cells))
var ops_cell = edges_per_cellMath.pow(3,2) + edges_per_cell3 + edges_per_cellMath.pow(3,2)
var pflops_per_sec = 1000(ops_cell*num_cells+ops_prep_cells_per_ts )/Math.pow(10,15)

The actual number of operations is larger because we have not accounted for the number of operations it takes to activate a cell.
This is simply a rough estimate of the number of operations it takes to get all the data to each cell

Iterate through, and activate all cells which returns a list of destination-result pairs
Each cell then has to multiply the input sources by the corresponding dendrite arrays, sum the results, and calculate plasticity changes for each synapse...
ops_cell = edges_per_cell*Math.pow(3,2) + edges_per_cell*3 + edges_per_cell*Math.pow(3,2)

**The problem we have is that biological brains are exemplars of the fact that hardware is an expression of software.**
Implementing software optimized for specific hardware in a substrate with different paradigms is inefficient. A biological brain is a highly efficient implementation of a graph. The computational cost is distributed because each vertex is a processor. Modern computer architectures rely on centralized, serial processing with parallel implemented via increasing the core count.

## Signal Propagation Speed

Myelination of axons determines how quickly a signal propgates through the axon terminal. Though it takes time for signals to propagate through dendrites as well. In both cases, the number, and sizes of ion channels, and pumps in the respective parts also directly affect signal speed. Myelination is considered to be a very important part of structural plasticity because our neurons are timing dependent, and myelination directly affects timing. In the brains of martial arts experts, there is more white matter between the cerebellum, and the neocortex. In humans myelination changes seems to, with some exceptions, stop after the brain stops developing.

Not only does myelination affect signal speed, synapses with other cells can only form on unmyelinated sections of the axon. The two segments that are almost universally unmyelinated, are the segment where the axon connects to the cell body, and the treelike endpoint terminal. In our model, this means that all cells with basal dendrites may be able to accept inputs from their neighbors in the destination.

> Open Question: Is distance based propagation timing to outputs based on distance necessary for, or does improve the effeciency of an stdp network?

## Input Batching

The problem of input batching has been looming for a while now, and I'm at the point where the layer config approach will affect the input batching approach. This is because of cell type distribution in a layer. Where cell_type = {activation_type[-1,1], cell_morphology, destinations[]}. I plan to eventually expand to modulatory cell types that return objects (chems) which affect cell operations so as to proxy the affect of various neurotransmitters in the brain. Most of the neurotransmitters in the brain don't directly pertain to cell activation.
At present, we have the following possibilities depending on whether or not cell_type contains destinations, and the allowed morphology variance

- all cells go to the same destinations
- all cells go to potentially distinct destinations
- all cells receive from the same destinations (for each morphology pyramid vs binary would be different but all pyramid would have the same input sources)
- all cells receive from potentially distinct destinations

The choice made for to/from lead to the following considerations
Language note: when receiving outputs that go to some destination it's called a source. When projecting an output to some destination or referring to point type, it's called a destination. The axon projections to a source from other destinations are the number of possible inputs @ a source.

- Every point in a layer (ij of a 2D matrix), can have one or more cells. We generally call these points destinations.
- Each cell @ a destination, depending on cell type, can receive inputs from different source, in addition to the destination in which it lives.
- Consequently, if each cell has a different list of sources, then input batching has greater complexity. Further, if each cell can have a different list of output destinations we can reduce the size of each source.
    If we want to avoid passing around the actual location for each possible activation to a source, then I don't currently see a way to avoid guaranteeing activation ordering.
    Consequently, all of this is determined during init so when the network is running the source input order won't change. The list of activations to each source needs to be built with the same order so that we can do array multiplication with the # of projections to a source by the # of synapses at a receiving cells dendrite. This is to avoid interpretation changes. Unfortunately, this means that even inactive cells will have to indicate that they were not active.

Now let us say we have dests 1 - 5, and dest 2 has 3 cells (A,B,C, D) with each cell receiving from potentially different sets of sources

A <- 1, 2, 3 (i.e. A can form connections to cells that output to 1 & 3)
B <- 1, 2, 4
C <- 2, 4, 5
D <- 1, 2, 4

Which are three different batches of source across 5 different sources for 4 different cells...
1) We could have a unique list for each top level container (problem domain) of the sources required, then when activating each destination, grab the destinations required for it in a new object, which is split into new objects for each cell activation.
2) We could prepare a distinct object for each cell during input batching by the I/O server.
3) We could prepare a distinct object for destination, layer, region (whichever level we want to stop splitting at) during input batching, then during destination activation do the splitting, and again split at the cell

I'm not sure what degree of uniformity is acceptable across destinations, and sources for cells @ a destination. Regardless, 2 seems like the worst case scenario. That being said, all from same dests does simplify things, but it only sort of affects the complexity of input batching. Whereas all to same dests seems to limit the potential complexity of the network without any real affect on runtime complexity while marginally affecting init complexity. Init complexity doesn't matter all that much. It's always going to take longer than evaluating a single timestep

> Open Question: Should all cells at a destination, receive from the same sources?

This question can also be reframed as, to what degree does this cut down on the amount of processing required, to what extent does this affect capability, and are the reductions worth the cost to network capability?

> Open Question: Should all cells at a destination, project to the same destinations?

Partial Answer: **No. Each cell type should have different destinations, and output distributions.**
Why: Good question!