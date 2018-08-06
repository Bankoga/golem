# Config Questions

These are open problems concerning config files, and thoughts on how to resolve them.

## Brain Network Config

The top level abstraction is the brain network. A graph whose nodes are individual problem domains.

> Open Question: Do we define the brain network in the code, or do we use a config? **use a config**

If we want to continue with the same approach that we have been using, then going with a config seems to be the best route.

## Problem Domain Configs

> Open Question: Do we need configs for the problem domain types? **YES. See below for reason why.**

Problem domain type information has to be stored somewhere, be it in an object that lives in the framework, or in a config of some sort. Since we have decided on a config based approach in order to separate specific connection details from general framework behaviour, then we should continue with this approach for problem domains.

> Open Question: Is it necessary for each problem domain type to have a unified config?
> Open Question: Can we have problem domain type configs that indicate the external input destinations, and otherwise leverage the region configs?

If we have generic patterns that exist across all problem domains of a type for the numbers of layers, then it is unclear if we should have all the region data live in the pd type config, or a separate config. At present, we have region types living inside their own config files.
The answer to these questions will be determined by the approach used for cell types, and destinations. Essentially, the format of interlayer, and interregion connection details inform how it's possible to evolve a specific problem domain of a type without changing the general type definition.

PD type has region types, and cell type distributions with connections details for each layer. In that case region config would trivially have num layers
For a fully evolutionary approach, it seems like each problem domain would be a unified config built from atoms instead of using general problem domain and region types.

## Cell Type Configs

> Open Question: What determines cell type for our model?
> Open Question: Is there a master list of all possible cell types?

Given that in a human brain, a single region like the Hippocampus can easily have over 20 different types of cells. Though because of the complexities of implementation via organic chemistry leads to a greater number of cell types, it's still easy to have tons of cells in a region. For now we are going with major cell types using generic patterns with the intent to use evolutionary algs to design configs later on. That being said, what cell types should be implemented, and how to implement them is still an open question.

Biological neuron typing is in fact an open question in neuroscience. The shape of the dendrites, the different receptors in the dendrites, the shape of the cell body, the number of axons, and the types of outputs from the axon are all considered relevant to the type of neuron. Neuron typing is further complicated by structural plasticity in the brain that causes changes to all of those properties on an individual neuron basis according to usage based on poorly understood plasticity rules. Moreover, these changes are predominant during development which stops ~25 years of age in humans.

> Open Question: do all cell types with basal dendrites accept inputs from their neighbors at the destination?
> Open Question: how are the lengths of dendrites determined?
Random length between 1 and some max based on type?
Do apical dendrites have different lengths in different regions, and layers? This seems like a yeah
So how is the length of a given apical dendrite determined?
