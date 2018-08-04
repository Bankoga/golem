# Random Thoughts about Configs

## Open Problems

There are plenty of open problems with the framework at the moment. For code changes that need implementation, and decisions on how to proceed.

### Connection Distribution Between Domains

> Open Question: How is the distribution of inputs from disparate sources spread across the finite input slots of a single problem domain?

- Does each distinct source of inputs, correspond to a subrange of the total num of input slots?
  - What happens when there are more inputs from a source than there are input slots?
  - What happens when the sum of inputs from all sources exceed the number of input slots?
- ?

For example, we have 3 pds (a, b, c) as inputs to 3 pds (d, e, f)

| **Domain**    | **Num Slots** |
|---------------|---------------|
| A             | 20            |
| B             | 10            |
| C             | 40            |
|---------------|---------------|
Total Inputs: 60

| **Domain**    | **Num Slots** |
|---------------|---------------|
| D             | 30            |
| E             | 40            |
| F             | 60            |
|---------------|---------------|

### Problem Domain Configs

> Open Question: Do we need configs for the problem domain types? YES. See below for reason why.

Problem domain type information has to be stored somewhere, be it in an object that lives in the framework, or in a config of some sort. Since we have decided on a config based approach in order to separate specific connection details from general framework behaviour, then we should continue with this approach for problem domains.

> Open Question: Is it necessary for each problem domain type to have a unified config?
> Open Question: Can we have problem domain type configs that indicate the external input destinations, and otherwise leverage the region configs?

If we have generic patterns that exist across all problem domains of a type for the numbers of layers, then it is unclear if we should have all the region data live in the pd type config, or a separate config. At present, we have region types living inside their own config files.
The answer to these questions will be determined by the approach used for cell types, and destinations. Essentially, the format of interlayer, and interregion connection details inform how it's possible to evolve a specific problem domain of a type without changing the general type definition.

PD type has region types, and cell type distributions with connections details for each layer. In that case region config would trivially have num layers
For a fully evolutionary approach, it seems like each problem domain would be a unified config built from atoms instead of using general problem domain and region types.

### Wiring Together Problem Domains

The top level abstraction for a single node in the brain network is the problem domain. Currently we have several types of problem domains, with the Cortical type being the most prevalent. The others may have 1 paired usage at most based on current thinking.

Given that a brain network is a graph of problem domains
AND each domain is a point in the graph
When a point projects to another point
AND the init needs to build the output destinations
AND this is not for a paired output connection
Then we need to know the pd type of the subsequent node
AND we need to know the specific layers, and regions designated as input by the pd type

Consequently, we know that each problem domain type requires specific layers within certain region for accepting output from other PDs.

> Open Question: How are the specific input destinations indicated, and how does the framework handle this during init?
> Open Question: When building connections between cells and destinations, how does we indicate that a problem domain type receives all inputs to a specific location or set of locations?

For example, the Cortical type accepts external inputs via the cort_relay layer in the relay region which then passes input to the cortex region. Doing so starts a cascade of signal passing between layers of the two regions.

> **During init, how does the framework know to build a path to a cort_relay dest, and with what distribution?**
> **How do we indicate for a problem domain type that an external input goes to three seperate layers across 2 regions?**

### Cell Types

Given that in a human brain, a single region like the Hippocampus can easily have over 20 different types of cells. Though because of the complexities of implementation via organic chemistry leads to a greater number of cell types, it's still easy to have tons of cells in a region. For now we are going with major cell types using generic patterns with the intent to use evolutionary algs to design configs later on. That being said, what cell types should be implemented, and how to implement them is still an open question.

Biological neuron typing is in fact an open question in neuroscience. The shape of the dendrites, the different receptors in the dendrites, the shape of the cell body, the number of axons, and the types of outputs from the axon are all considered relevant to the type of neuron. Neuron typing is further complicated by structural plasticity in the brain that causes changes to all of those properties on an individual neuron basis according to usage based on poorly understood plasticity rules. Moreover, these changes are predominant during development which stops ~25 years of age in humans.

> Open Question: What determines cell type for our model?
> Open Question: Is there a master list of all possible cell types?

### Signal Propagation Speed

Myelination of axons determines how quickly a signal propgates through the axon terminal. Though it takes time for signals to propagate through dendrites as well. In both cases, the number, and sizes of ion channels, and pumps in the respective parts also directly affect signal speed. Myelination is considered to be a very important part of structural plasticity because our neurons are timing dependent, and myelination directly affects timing. In the brains of martial arts experts, there is more white matter between the cerebellum, and the neocortex. In humans myelination changes seems to, with some exceptions, stop after the brain stops developing.

Not only does myelination affect signal speed, synapses with other cells can only form on unmyelinated sections of the axon. The two segments that are almost universally unmyelinated, are the segment where the axon connects to the cell body, and the treelike endpoint terminal. In our model, this means that all cells with basal dendrites may be able to accept inputs from their neighbors in the destination.

> Open Question: whether or not to include distance based propagation timing to outputs based on distance
> Open Question: do all cell types with basal dendrites accept inputs from their neighbors at 

### Input Batching

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

- Now let us say we have dests 1 - 5, and dest 2 has 3 cells (A,B,C, D) with each cell receiving from potentially different sets of sources

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