# Miscellaneous Problems

## Graph Storage

It has come to my attention that even a modestly sized graph as an adjacency list of just the cells, and their edges would consume tons of memory. Thus the issue of the data structure of the graph has become imperative. Regardless of how many other questions are answered, if the final object is of an unrealizable size then the enterprise is doomed to failure. This is not acceptable! While some memory usage optimizations will result once we move to another language after validating the test framework in python, the space complexity of the system still matters for the python implementation. In order to have a successful proof of approach that can be optimized, we must decide on the data structure of the pod graph.

> ~~Open Question: Go with the object nesting approach, where each layer is a matrix of destinations, unify all destinations into a single adjacency list, or some other data structure?~~

Answer: **Stay the course! For now anyway...**

Refactoring the code to use a single list for all destinations seems doable later on. For now, manifesting the conceptual aspects of each pod as actual code objects, helps with implementation. If it is necessary to reduce the number of objects to a single list of destinations with the meta levels merely used to build the list, then we can handle that later.

> ~~Open Question: Does every pod/cell need to be touched during each timestep?~~

Answer: **Yes because we need to know if the cell activated based on the inputs it received**

> Open Question: What data structure should be used for storing destinations, and cells?

Previously, each pod was going to live inside of an actual 2D matrix, and contain a list of cells. **The 2D matrix may live on in concept for use during the init, but it may not be efficient enough for use as the actual data structure to store destinations.**
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

Iterate through, and activate all cells which returns a list of pod-result pairs
Each cell then has to multiply the input sources by the corresponding dendrite arrays, sum the results, and calculate plasticity changes for each synapse...
ops_cell = edges_per_cell*Math.pow(3,2) + edges_per_cell*3 + edges_per_cell*Math.pow(3,2)

**The problem we have is that biological brains are exemplars of the fact that hardware is an expression of software.**
Implementing software optimized for specific hardware in a substrate with different paradigms is inefficient. A biological brain is a highly efficient implementation of a graph. The computational cost is distributed because each vertex is a processor. Modern computer architectures rely on centralized, serial processing with parallel implemented via increasing the core count.

## Signal Propagation Speed

Myelination of axons determines how quickly a signal propgates through the axon terminal. Though it takes time for signals to propagate through dendrites as well. In both cases, the number, and sizes of ion channels, and pumps in the respective parts also directly affect signal speed. Myelination is considered to be a very important part of structural plasticity because our neurons are timing dependent, and myelination directly affects timing. In the brains of martial arts experts, there is more white matter between the cerebellum, and the neocortex. In humans myelination changes seems to, with some exceptions, stop after the brain stops developing.

Not only does myelination affect signal speed, synapses with other cells can only form on unmyelinated sections of the axon. The two segments that are almost universally unmyelinated, are the segment where the axon connects to the cell body, and the treelike endpoint terminal. In our model, this means that all cells with basal dendrites may be able to accept inputs from their neighbors in the pod.

> Open Question: Is distance based propagation timing to outputs based on distance necessary for, or does it improve the effeciency of an stdp network?

Answer: ?

## Input Batching

The problem of input batching has been looming for a while now, and I'm at the point where the layer config approach will affect the input batching approach. This is because of cell type distribution in a layer. Where cell_type = {resource_type[-1,1], cell_morphology, destinations[]}. I plan to eventually expand to modulatory cell types that return objects (chems) which affect cell operations so as to proxy the affect of various neurotransmitters in the brain. Most of the neurotransmitters in the brain don't directly pertain to cell activation.
At present, we have the following possibilities depending on whether or not cell_type contains destinations, and the allowed morphology variance

- all cells go to the same destinations
- all cells go to potentially distinct destinations
- all cells receive from the same destinations (for each morphology pyramid vs binary would be different but all pyramid would have the same input sources)
- all cells receive from potentially distinct destinations

The choice made for to/from lead to the following considerations
Language note: when receiving outputs that go to some pod it's called a source. When projecting an output to some pod or referring to point type, it's called a pod. The axon projections to a source from other destinations are the number of possible inputs @ a source.

- Every point in a layer (ij of a 2D matrix), can have one or more cells. We generally call these points destinations.
- Each cell @ a pod, depending on cell type, can receive inputs from different source, in addition to the pod in which it lives.
- Consequently, if each cell has a different list of sources, then input batching has greater complexity. Further, if each cell can have a different list of output destinations we can reduce the size of each source.
    If we want to avoid passing around the actual location for each possible activation to a source, then I don't currently see a way to avoid guaranteeing activation ordering.
    Consequently, all of this is determined during init so when the network is running the source input order won't change. The list of activations to each source needs to be built with the same order so that we can do array multiplication with the # of projections to a source by the # of synapses at a receiving cells dendrite. This is to avoid interpretation changes. Unfortunately, this means that even inactive cells will have to indicate that they were not active.

Now let us say we have dests 1 - 5, and dest 2 has 3 cells (A,B,C, D) with each cell receiving from potentially different sets of sources

A <- 1, 2, 3 (i.e. A can form connections to cells that output to 1 & 3)
B <- 1, 2, 4
C <- 2, 4, 5
D <- 1, 2, 4

Which are three different batches of source across 5 different sources for 4 different cells...
1) We could have a unique list for each top level container (problem domain) of the sources required, then when activating each pod, grab the destinations required for it in a new object, which is split into new objects for each cell activation.
2) We could prepare a distinct object for each cell during input batching by the I/O server.
3) We could prepare a distinct object for pod, layer, region (whichever level we want to stop splitting at) during input batching, then during pod activation do the splitting, and again split at the cell

I'm not sure what degree of uniformity is acceptable across destinations, and sources for cells @ a pod. Regardless, 2 seems like the worst case scenario. That being said, all from same dests does simplify things, but it only sort of affects the complexity of input batching. Whereas all to same dests seems to limit the potential complexity of the network without any real affect on runtime complexity while marginally affecting init complexity. Init complexity doesn't matter all that much. It's always going to take longer than evaluating a single timestep

> ~~Open Question: Should all cells at a pod, receive from the same sources?~~
This question can also be reframed as, to what degree does this cut down on the amount of processing required, to what extent does this affect capability, and are the reductions worth the cost to network capability?
Actually, there is a better reframing because if all cells @ a dest use the same sources, then cell morphology no longer matters within a pod. Thus, do we need different cell morphologies within a pod?

Answer: Without different types of cell morphologies in a layer, the approach here isn't all that different from the mainstream neural networks in use today. Moreover, local connection scheme differentiation matters. Thus, each cell within a pod should have potentially unique sources.

> ~~Open Question: Should all cells at a pod, project to the same destinations?~~

Answer: **No. Each cell type should have different destinations, and output distributions.**
Why: Axons in human brains have specific targets, and tend to not have many branches. Furthermore, different types of cells often project to different locations for different purposes.

> ~~Open Question: Does input batching prepare bundles per cell or per pod?~~

Answer: If we pass a pod bundled reference to each cell, then it can select the sources it requires at activation time. Thus we only need to batch per pod, and not per cell.

## Determining Graph Size

There are several problems that need to be solved before we can know how graph size will be indicated, and where that data will live.

> ~~Open Question: Is the size of one or more problem domains relative to the number of inputs it receives?~~

Answer: For cortical problem domains, this would seem to be the case.

> ~~Open Question: Are there problem domains which have fixed ratio sizes or other absolute sizes?~~

Answer: Yes. Almost all of the structures in subcortex are much smaller than the neocortex, and many accept from a large number of problem domains but don't get larger or smaller based on the number of problem domains. That being said, some subcortical structures have different sizes which are largely unchanged by the size of the brain. Furthermore, certain sequences of regions within the subcortex decrease in size according to fixed ratios, regardless of brain size. Consequently, we need to support the following:

- Regions
  - which have independently determined sizes
  - where size is determined according to some ratio of the size of another region
  - with an absolute size
- Problem domains
  - which are a fixed ratio of the total number columns across all cortical type problem domains
  - which have regions with varying sizes

> Open Question: How do we indicate that a problem domain should have a minimum number of destinations in the input or output layers?
> Open Question: How do we indicate that an output layer has some number of output slots fewer than the number of destinations within the layer?

Answer: We use properties set in the config that indicate which size, and layout case to use for num destinations, inputs, and outputs.

Opts for layer size:

- absolute quantity
- func of sum of inputs
- fixed ratio of brain size

Opts for # avail inputs/outpus for a layer:

- All dests serve as I/O slots
- Subset of dests has 2 cases with 2 options each
  - Cases
    - Absolute number
    - Fixed ratio of total dests
  - Options for positions of I/O
    - randomn postitions within the layer
    - fixed positions
      - largest N indices
      - smallest N indices

> Open Question: How do we indicate what length, and width each region occupies?

Pseudo Answer: We can use a base unit LxW that is set during init. Each config would specify size in terms of base units, sum units from a list of domains, or ???

Pseudo Answer: There are two cases for length x width. We can specify a ratio to use when splitting the number of destinations in the layers, or we can automatically split them into a square. This is indicated by a flag in the config.

From micro to macro, level sizes are determined by the following funcs:

- cell_size = 1
- dest_size = f(num_cells, cell_size)
  - length only
  - determined by the layer configs
- layer_size = f(num_dests, dest_size)
  - length, width
  - is dynamic based on the region_size
- region_size = f(num_layers, layer_sizes[]) each layer can be of different size
  - length, width, & height
  - can be absolute, or ratio of total num destinations avail to the problem domain
- pd_size = f(num_regions, region_sizes[]) each region can be of different size
  - length, width, & height
  - determines what fraction of total is consumed by the pd
    - equal share
    - separate count (does not consume population size, and silently increases the total)
    - ratio sub share (intended for subcortical apparati which have fixed proportions)
- brain_size = f(num_pds, pd_sizes[]) each pd can be of different size
  - length, width, & height
  - determines minimum number of destinations
    - used for building problem domains

Each region, and pd are 3D objects. Distance between two dests is thus determined by the size and layout of each of the pds between them.

> Open Question: Do we want the number of dests to be hard coded for each level?

Answer: No. We want to be able to set a desired number of dests at the top level, then have those split across the problem domains appropriately. **SEE ANSWER TO LENGTH X WIDTH OF REGIONS Q!**

> Open Question: If I want a brain with ~N neurons, how do I indicate that when creating a golem with a given architecture?

Answer: In order to set a desired number of destinations, at the golem level, the configs must contain certain data pertaining to size that can be used as a series of forumlas where we solve for the missing variables.

Layers control their dest size.
Regions have a number of dests based on some ratio, or value that determine how many of the dests allotted to a problem domain are consumed by the specific region. Though it seems possible that, depending on architecture, some regions may need to break this paradigm. **If anything, regions may be able to wholly replace problem domains as a layer of abstraction.**
Problem domains contain multiple dests, and are some fraction of the total number of dests. The fraction of dests consumed by a problem domain, are then split across the various regions according to the region size formulas. All region size formulas in a problem domain should add up to 1. They can not lead to consuming more dests than supplied by the problem domain.
The golem sets a specific number of dests, which are split across the problem domains.
Thus it would seem to be the case that there is a minimum number of reasonably supported dests for any given golem architecture.

### Toy architecture with N PDs of the cortical type

total_dests: 1000

```yaml
---
name: sample architecture
decoders:
  - name: decoder_a
    type: ?
    size: ?
    output_dest: ?
encoders:
  - name: encoder_a
    type: image
    length: ?
    width: ?
    num_channels: ?
    input_source: ?
    outputs: [vis_a]
problem_domains:
  - name: vis_a
    type: cortical
    size: 4
    outputs: [vis_b,vis_c]
  - name: vis_b
    type: cortical
    size: 2
    outputs: [comb_a]
  - name: vis_c
    type: cortical
    size: 2
    outputs: [comb_a]
  - name: comb_a
    type: cortical
    size: 1
    outputs: [decoder_a]
edges:
  - encoder_a:vis_a
  - vis_a:vis_b
  - vis_a:vis_c
  - vis_b:comb_a
  - vis_c:comb_a
  - comb_a:decoder_a
...
```

> ~~Open Question: A good question is how to record the edges. Do we record the edges as a list of edges, or have a list of outputs for each node?~~

Answer: Each Decoder, Encoder, and Problem Domain node has a list of outputs for recording it's outoing edges.

### Simple Way of handling pd size

The base case for pd size can be handled rather simply. When all the pds are of relatively similar size, we can simply assign an integer unit size to each pd, and sum them all together to get the total num units. Then the % of total_dests consumed by a given PD is equal to pd.size/total_num_units.
total_num_units = sum of all pd.size
num_dests_arb_pd = round((arb_pd.size/total_num_units) * total_dests)
Which allows us to then set the length, and width of each region based on the LxW ratio. Or we could simply make them all squares.

> ~~Open Question: How do we handle fractional dests?~~

Answer: We are going to use rounding for now.

> Open Question: Are the External I/O PDs included in the dest consumption?

Answer: While that is one possibility, for now it is easier to have those be separate due to the fact that decoders, and encoders must be handled separately from normal (internal) problem domains. Thus they won't scale with the golem.

**PD size also depends on how we handle pd types. If the thalamus is a region within the subcortex problem domain type, and it specifically needs to have enough slots for every single cortex pd type whereas all the other regions in the domain use a different size paradigm, then how do we indicate that?**

It may be important to have all the thalamic cells in the same area, so they can bleed through adjacently.

### Complex Case for handling PD size

**TO HANDLE AT A LATER TIME**
The simple case for pd size works when all the pds are of relatively similar size. It does not work when 1 or more PDs are not a simple % of the total number of dests.

> Open Question: How do we indicate the size of non-standard problem domains like the subcortex?

Answer: A proper answer to this question would seem to require a greater understanding of the subcortex...

## Order of Destinations in Layer

> Open Question: Do we need the ability to specify a direction of flow through the destinations in a region or layer?

Answer: At a bare minimum, the claustrum seems to either need this flow, or we use a large number of small layers instead. **REQUIRE MORE RESEARCH FOR OTHER EXAMPLES**

> Open Question: How do we indicate the direction of flow through destinations in a region or layer?

## Consciousness

> Open Question: What are the minimum requirements of consciousness?
> Open Question: What is consciousness?

A good starting point is that consciousness relates to "there is a thing that it is like to be the conscious entity". The essence of consciousness is experience. But if I don't need to be aware of why I made some decision, and only need to be aware of the decision, then it would seem that knowledge of memory or memories are not necessary for consciousness.
Awareness seems to be key. External senses do not seem to be necessary for consciousness. I am still conscious when deprived of my external senses.
It seems to be inseparable from processing what is being processed. It seems to be related to focus (selection, and exclusion) on/between different streams of computation.
Processing thoughts (results of computation) that have occurred then may be one of the necessary characteristics of consciousness.
More robust forms of consciousness may be able to affect what is processed, and how.

It is necessary for strong agents to be able to observe their own intent, reflect on it, and then choose to act differently.

## Eye Encoder Size and Distribution

Eye Encoder area distribution calcs
var diam_d = 22
var diam_b = 2.5
var diam_c = 5.5
var diam_blind = 3
var d = (Math.PI*Math.pow(diam_d/2,2))
var B = (Math.PI*Math.pow(diam_b/2,2))
var C = (Math.PI*Math.pow(diam_c/2,2)-B)
var blind = Math.PI*Math.pow(diam_blind/2,2)
var D = d - (B+blind+C)
var sum = D + B + C
var pctD = D / sum
var pctB = B / sum
var cnt = 130e6
var cones = 6e6
var rods = 120e6
var dist = function(pct,n,a){return (pct*n)/a}
var totalCnt = (dist(pctD,cnt,D)+dist(pctB,cnt,B));
(dist(pctB,cones,B))*Math.pow(0.001,2);
totalCnt - ((dist(1,rods,D)) + ((dist(0.5,cones,B))*2));
(pctD*cnt/D)/(cones/(B+C));

var len_abs = 128
var half_len = Math.ceil(len_abs/2)
var len_b = Math.ceil(diam_rat_b*half_len)*2
var len_c = Math.ceil(diam_rat_c*half_len)*2

var diam_rat_b = diam_b/diam_d
var diam_rat_c = diam_c/diam_d

var sz_statblock = function(len_abs,len_b,len_c,len_d) {
  return `Filter Props:
  parafvea_sz: ${len_b}x${len_b}=${Math.pow(len_b,2)}px
  perifvea-macula_sz: ${len_c}x${len_c}=${Math.pow(len_c,2)}px
  window_sz: ${len_abs}x${len_abs}=${Math.pow(len_abs,2)}px`
}
var sz_stat = function (len_abs,hq_sz) {
  var half_len = Math.ceil(len_abs/2)
  var len_b = Math.ceil(diam_rat_b*half_len)*2
  var len_c = Math.ceil(diam_rat_c*half_len)*2
  //var len_d = Math.ceil(diam_rat_d*half_len)*2
  var stats = 'Using len_abs:\n'+sz_statblock(len_abs,len_b,len_c)
  if (typeof hq_sz != 'undefined') {
    half_len = Math.ceil(hq_sz/diam_rat_c)/2
    len_b = Math.ceil(diam_rat_b*half_len)*2
    len_c = Math.ceil(diam_rat_c*half_len)*2
  stats+='Using hq:\n'+sz_statblock(half_len*2,len_b,len_c)
  }
  return stats
}

## Memory in a Machine

an interesting way to think of memory in a neural network is as a well defined, stable set of interdependent activity within, or path through, the network

The cortex then is a bunch of models that are used each day to operate the entity according to the construction the subcortex
When resting, the models are maintained, and updated incorporating data from the new session (record of time spent operating alertly), as well as from stored sessions (temporary, and permanent)
Thus the network prunes what wasn't used, and reinforces that which was used. Along with a variety of homeostasis mechanisms to maintain the models previous cabilities
All help to achieve the primary or basic goals of the system

Thus we have a few types of weight for cells
Session unique - isn't weighted strongly enough to change the network, gets removed during the next rest cycle
Transient - lasts a few sessions because of initial or sporadic reuse, but either gets used sufficiently within a given time period to crystallize (permanently affect the model), or decays long enough to get pruned (think of a weighted moving average that goes away if not used more than some threshold number of times within the past 7 cycles)
Crystallized - changes that have been permanently added
Seed - Inherited weight/random initialization value

Which explains the several forms of memory we see in humans
Working memory - local system memory
Short term - session unique
Mid term - local variance duration (1 - 3 months, temporary sessions limit)
Long term - Habits, Reflexes, Knowledge, etc... (base weights, saved sessions)

As well as models habits, and muscle memory (muscle memory not so much)
Habit formation difficulty - converting transient to crystallized is difficult
Habit loss ease - rapid adaption via deactivation of irrelevant engram weights
Old Habits die hard - Large scale drift difficulty as func of complexity, and degree of integration of change

TIME BASED USAGE CAN BE MODELED AS CHEMICAL CONCENTRATION CHANGES WITH VARIOUS VALUE THRESHHOLDS USED TO MAKE UPDATES

## Extendable Golems

A hugely beneficial feature of most individual organic lifeforms is an innate ability to adapt to a range of local environmental changes via genetic config/setting tweaks, and as a species through genetic configuration drift over time. Being able to extend ones capabilities directly by adding, removing, enabling, or deactivating modular sub-systems over time would be hugely benefical. Cephalopods exemplar this by virtue of a genetic framework that allows for extremely dynamic flexibility of RNA routines.
However, extendable sensorimotor capabilties for a golem requires that the framework and core systems can detect the circuits, and networks in the auxillary or secondary/tertiary cores then integrate them holistically. This may imply an eventual need for a sub-system that handles rewriting alternate cores for compatibility with the primary core.