# Open Problems

There are plenty of open problems with the framework at the moment. For code changes that need implementation, and decisions on how to proceed.

## External I/O

The brain is an open system, that has dedicated routes for external input, and output.

> ~~Open Question: How do we translate external sensor data into spikes for the corresponding problem domains?~~

Answer: Translation must be done on a sensor type basis, with each sensor having unique code for handling the translation.

> Open Question: Does the translation change based on the available input slots for the corresponding problem domain?

Answer: ?

> ~~Open Question: Where and how do we pass the translated data into the cell map?~~

Answer: For each type of sensor, and output format, we will use predefined interaction code for decoding, and encoding. Because for a given network type, we can know what sensors will be available, and the actions it will be able to take outside the network, we can use unique handling for those problem domain types. Each type serves as a point of interaction with the external world, and can be processed on a per timestep basis to ensure consistency of internally generated data. However, the code that does the processing will look fundamentally different. Most sensors will not serve as destinations for other problem domains, and thus won't have any region or destinations. Those few sensors that do receive some minimal feedback, will use a different method for processing the outputs from other problem domains because the data must be translated.

Sensor Types

- Image
- Audio

Output Types

- characters
- images
- sounds
- etc...

## Wiring Together Problem Domains

The top level abstraction for a single node in the cell map is the problem domain. Currently we have several types of problem domains, with the Cortical type being the most prevalent. The others may have 1 paired usage at most based on current thinking.

There are several different problems associated with wiring domains together

- How to indicate where external outputs should connect to a problem domain
  - i.e. How to declare input slots
- How to distribute outputs across the available input slots
- How to distribute outputs to subsequent problem domains

**Does size of PD change based on the number of inputs to the PD?**
They do seem to be correlated. Though the answer for this problem seems to relate to the answers for input, and output interpretation.

Comment removed from destinations.py
since each region type has it's own layer types, where should destination mappings live?
I feel that it may be best for layer destination mappings to live outside the class in a json, yaml, or other such file
Why?
    the cortical region alone has 6 distinct layers with different output connection patterns, cell morphologys, plasticity rules, (what else?)
    There are at least 3 types of regions that I know need to be created, and at least two problem domains with undetermined regions
    Those other problem domains should at least have 1 type of region each, though they will likely have more than one
    So at this point, we can safely expect 5 or more regions that we need predefined to get info from
    Greater flexibility results from localizing cell morphologys, plas rules, resource constraints, connect patterns, etc... to each layer or region
> NOTE: Removed method stub for collecting all sources from cells in a destination because of cost. Leaving the comments about it here for posterity.

### Indicating Input Slots for a Problem Domain

Given that a cell map is a graph of problem domains
AND each domain is a point in the graph
When a point projects to another point
AND the init needs to build the output destinations
AND this is not for a paired output connection
Then we need to know the pd type of the subsequent node
AND we need to know the specific layers, and regions designated as input by the pd type

Consequently, we know that each problem domain type requires specific layers within certain region for accepting output from other PDs.

> ~~Open Question: How are the specific input destinations indicated/When building connections between cells and destinations, how do we indicate that a problem domain type receives all inputs to a specific location or set of locations?~~
For example, the Cortical type accepts external inputs via the cort_relay layer in the relay region which then passes input to the cortex region. Doing so starts a cascade of signal passing between layers of the two regions.

Answer: Each problem domain type specifies which regions serve as inputs. Furthermore, each region specifies which layers should receive inputs. All projections to the domain type are split according to that data.

> ~~Open Question: How do we indicate for a problem domain type that an external input goes to three seperate layers across 2 regions?~~

Answer: If a problem domain type config specifies which regions serve as input, and those regions specify which layers serve as their inputs, then we don't need to specify at the pd type level which layers are inputs. Though this does seem somewhat clunky. **This question and answer relate to the preceeding question.**

> ~~Open Question: How does the framework handle this during init?~~

Answer: If we do not save the configs at each level of abstraction, and only keep a copy at the highest level, then initialization is more memory intensive than the created network. However, each level of abstraction needs to know about the higher levels of abstraction that it works with. So we pass a reference to the master copy to all lower levels that they use for creation of the network, while saving only the necessary details for the current level.

> Open Question: **During init, how does the framework know to build a path to a cort_relay dest, and with what distribution?**

Partial Answer: The cell map edges are used to determine output replacements for destinations inside a problem domain. How to determine the appropriate distribution is still an open question.

### Input Distribution Between Domains

> Open Question: How is the distribution of inputs from disparate sources spread across the finite input slots of a single problem domain?
This may be a good reason to add a structural plasticity phase to the network eventually. So that we can tune based on usage.

- Does each distinct source of inputs, correspond to a subrange of the total num of input slots?
  - What happens when there are more inputs from a source than there are input slots?
  - **What happens when the sum of inputs from all sources exceed the number of input slots?**
    - This is in fact the case with the striatum, and several other areas within the subcortex!
- ?

**FACT: Axons rarely have large numbers of branches. Concurrently, there is evidence that higher iq brains have more specific axons (i.e. those that branch less or go to fewer cells).**
From this fact we can infer that densely connected layers, like in a conv net, where all cells go to all outputs, are probably not the route to take.

Partial Answer: If we only had D as an output for all 3, and if we ensure that all output slots are used, then, in part, this becomes a question of compression. 70 -> 30 so each domain must have multiple cells connect to the same output proportional to the number of domains. So in 70 -> 30 with 3 domains, each domain would project to a percent of the output cells based on num outputs.

| **Domain**    | **Pct of Outputs** | **Num Cells** |
| --- | --- | --- |
| A | 0.286 | 8.571 |
| B | 0.143 | 4.286 |
| C | 0.571 | 17.143 |

Three options for decimals:

- floor the results, then add the difference between expected and result to the domain with the greatest num cells
- ceil the results, then subtract the difference between expected and result from the domain with the greatest num cells
- round the results, then add/subtract the diff between expected and result to domain with greatest num cells

For example, we have 3 pds (a, b, c) as inputs to 3 pds (d, e, f). Here we have to calculate the num of cells available to each domain for each output, and num avail for input to calculate the ratio of output slots to input slots that would be used to determine the number of destination per output slot.

| **Domain**    | **Num Slots** | **Avail D** | **Avail E** | **Avail F** |
| --- | --- | --- | --- | --- |
| A | 20 | 4.286 | 5.714 | 10 |
| B | 10 | 2.143 | 2.857 | 5 |
| C | 40 | 8.57 | 11.429 | 20 |
| --- | --- | --- | --- | --- |
Total Inputs: 70

| **Domain**    | **Num Slots** | **Num For A** | **Num For B** | **Num For C** |
| --- | --- | --- | --- | --- |
| D | 30 | 8.571 | 4.286 | 17.143 |
| E | 40 | 11.429 | 5.714 | 22.857 |
| F | 70 | 20 | 10 | 40 |
| --- | --- | --- | --- | --- |
Total Outputs: 140

| **Domain** | **Ratio to D** | **Ratio to E** | **Ratio to F** |
| --- | --- | --- | --- |
| A | 4.286 : 8.571 | 5.714 : 4.2868 | 10 : 17.143 |
| B | 2.143 : 11.429 | 2.857 : 5.714 | 5 : 22.857 |
| C | 8.57 : 20 | 11.429 : 10 | 20 : 40 |
| --- | --- | --- | --- |

| **Domain** | **Ratio to D** | **Ratio to E** | **Ratio to F** |
| --- | --- | --- | --- |
| A | 4->9 | 6->4 | 10->17 |
| B | 2->11 | 3->6 | 5->23 |
| C | 9->20 | 11->10 | 20->40 |
| --- | --- | --- | --- |

These ratios represent the actual numbers of output cells to input cells. They would be used to determine the number of destinations each output cell projects to. Though in fact this would be calculated by the destination, and used to create the cells.(?)

var cnt = 70
var sum = 20+10+40
var a = 20/sum*cnt
var b = 10/sum*cnt
var c = 40/sum*cnt
console.log(a)
console.log(b)
console.log(c)
Math.round(a) + Math.round(b) + Math.round(c)

> Open Question: Why would there be fewer output slots than there are points in a layer?
I.E. under what conditions would it be possible for a layer to have fewer output slots than points?

Answer: When the layer is sequential, and returns a sequence. Why would that be a thing though? What other cases are there?
The claustrum may be configured in this manner!

### Output Distribution to other Domains

Each problem domain type has a set number of dedicated output layers for the general case. Furthermore, it is possible for a problem domain type to connect to other problem domains of the same type based on adjacency, pair existence, and **something else**.

While these problems are affected by the solution to the input distribution problem, it does require separate handling.

> ~~Open Question: How is the distribution of outputs to multiple domains handled?~~

Answer: Outside of adjacency, and pairing points, for now we assume that all output slots are split across the output domains. This is because axon sparsity, or branch minimization, is apparently related to the IQ of the network.

> ~~Open Question: Are all the outputs sent to all the subsequent domains?~~

Answer: For now we assume no. Though this does beg the question, what does it mean for the number of outputs to be split across different domains? Very much a matter of the semantics of the numbers, patterns, and timing of spikes.

> Open Question: Are the outputs split across the subsequent domains?

Answer: For now we assume that each subsequent domain, consumes a pct of the number of output slots based on how many total slots are at the destination.

For example, we have 1 PD (a) that outputs to 3 other PDs (b, c, d)

| **Domain**    | **Num Slots** |
|---------------|---------------|
| A             | 20            |
|---------------|---------------|

| **Domain**    | **Num Slots** |
|---------------|---------------|
| B             | 20            |
| C             | 10            |
| D             | 40            |
|---------------|---------------|
Total Output Slots: 70

| **Domain**    | **Pct of Outputs** | **Num Cells** |
| --- | --- | --- |
| B | 0.286 | 5.714 |
| C | 0.143 | 2.857 |
| D | 0.571 | 11.429 |

Diff ways of splitting output across cells in diff domains

- 20 -> 10
  - 2 -> 1 : 2 for each 1
  - higher compression using a subset of the 10
  - lower compression without sending all to the domain
- 20 -> 40
  - 1 -> 2
  - 1 -> 1 for a subset of the 40
  - 1 -> 1 skipping every other cell
- 20 -> 20
  - 1 -> 1
  - alts are same as first item in list

> Open Question: Do we want to have problem domain types that connect adjacently outside of the dedicated output layers?

In the human neocortex, this would be having adjacent broadmann areas connect to each other near the borders via the layers that handle adjacency. Also, it would be having the relays connect to each other. The relay case is more compelling than the broadmann area case.

### Distribution Complexity

> Open Question: Is it a good idea, or even necessary to do the availability based splitting of inputs, and outputs with the ratios used to determine the destinations?

Bad Answer: I currently do not have a clue!

## Unique vs Split Destinations

> ~~Open Question: How are split destinations represented?~~

Answer: As an array with multiple values in the config.

> Open Question: How can an axon plasticly split by usage?

Answer: ?

## Dendrite Sources

Each segment of a dendrite is an edge that connects a cell to some vertex (destination). Most dendrites pass through multiple destinations, and thus create multiple edges.

> Open Question: What determines the length of each dendrite?

Partial Answer: In most cases, it is the type of dendrite. However for apical dendrites, it is the distance from the source. For the local dendrite, it accepts outputs from its neighboring cells. Though each type of dendrite may be able to behave differently based on the its location in the brain. Consequently, it may be necessary to have each layer define its own dendrite types. Which would be a giant pain.

> Open Question: do all cell types with basal dendrites accept inputs from their neighbors at the destination?

Random length between 1 and some max based on type?
Do apical dendrites have different lengths in different regions, and layers? This seems like a yeah
So how is the length of a given apical dendrite determined?

## Cell Threading

Stiching together the vertices of the graph, each cell must handle its own threading which requires knowledge of all other destinations. Thus each level needs to have the corresponding details filled in.

> Open Question: Where to thread cells together?

Answer: Unless we can know the size of each region, and layer independently of their initialization, then we have to thread all the destinations together after the hierarchy is created. Thus, we thread the cells together after all the problem domains have been initialized.

## Mixed number of synapses

Some cells only have one possible connection for a given source. In such cases, we want to ensure that every cell using that source will always have a synapse to that source.

> Open Question: How do we ensure that sources which require all cells using them to fully connect to them, do so?

## Thalamus Region

In the human brain, the thalamus is considered a part of the subcortex. However, it is strongly defined in conjunction with the neocortical columns. Consequently, we have so far been defining it within the cortical problem domain type. This approach makes having thalamic adjacency/bleed more difficult.

> Open Question: Is thalamic adjacency/bleed necessary?

There are several ways to answer this question. One is that this depends on the degree to which we want mimic the architecture of the human brain. Another is that such adjacency may play an important functional role.