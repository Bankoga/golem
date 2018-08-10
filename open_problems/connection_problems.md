# Open Problems

There are plenty of open problems with the framework at the moment. For code changes that need implementation, and decisions on how to proceed.

## External I/O

The brain is an open system, that has dedicated routes for external input, and output.

> Open Question: How do we translate external sensor data into spikes for the corresponding problem domains?
> Open Question: Does the translation change based on the available input slots for the corresponding problem domain?
> Open Question: Where and how do we pass the translated data into the brain network?

Images -> Spikes
Spikes -> numbers, images, sounds, etc...

## Wiring Together Problem Domains

The top level abstraction for a single node in the brain network is the problem domain. Currently we have several types of problem domains, with the Cortical type being the most prevalent. The others may have 1 paired usage at most based on current thinking.

There are several different problems associated with wiring domains together

- How to indicate where external outputs should connect to a problem domain
  - i.e. How to declare input slots
- How to distribute outputs across the available input slots
- How to distribute outputs to subsequent problem domains

**Does size of PD change based on the number of inputs to the PD?**
They do seem to be correlated.

### Indicating Input Slots for a Problem Domain

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

### Input Distribution Between Domains

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

> Open Question: Why would there be fewer output slots than there are points in a layer?

### Output Distribution to other Domains

Each problem domain type has a set number of dedicated output layers for the general case. Furthermore, it is possible for a problem domain type to connect to other problem domains of the same type based on adjacency, pair existence, and **something else**.

While these problems are affected by the solution to the input distribution problem, it does require separate handling.

> Open Question: How is the distribution of outputs to multiple domains handled?
> Open Question: Are all the outputs sent to all the subsequent domains?
> Open Question: Are the outputs split across the subsequent domains?

For example, we have 1 PD (a) that outputs to 3 other PDs (b, c, d)

| **Domain**    | **Num Slots** |
|---------------|---------------|
| A             | 20            |
|---------------|---------------|

| **Domain**    | **Num Slots** |
|---------------|---------------|
| B             | 10            |
| C             | 40            |
| D             | 20            |
|---------------|---------------|

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

In the human neocortex, this would be having adjacent broadmann areas connect to each other near the borders via the layers that handle adjacency.

## Unique vs Split Destinations

> Open Question: How are split destinations represented?
> Open Question: How can an axon plasticly split by usage?