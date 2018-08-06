# Miscellaneous Problems

## Signal Propagation Speed

Myelination of axons determines how quickly a signal propgates through the axon terminal. Though it takes time for signals to propagate through dendrites as well. In both cases, the number, and sizes of ion channels, and pumps in the respective parts also directly affect signal speed. Myelination is considered to be a very important part of structural plasticity because our neurons are timing dependent, and myelination directly affects timing. In the brains of martial arts experts, there is more white matter between the cerebellum, and the neocortex. In humans myelination changes seems to, with some exceptions, stop after the brain stops developing.

Not only does myelination affect signal speed, synapses with other cells can only form on unmyelinated sections of the axon. The two segments that are almost universally unmyelinated, are the segment where the axon connects to the cell body, and the treelike endpoint terminal. In our model, this means that all cells with basal dendrites may be able to accept inputs from their neighbors in the destination.

> Open Question: whether or not to include distance based propagation timing to outputs based on distance

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
> Open Question: Should all cells at a destination, project to the same destinations?