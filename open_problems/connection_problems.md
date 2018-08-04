# Open Problems

There are plenty of open problems with the framework at the moment. For code changes that need implementation, and decisions on how to proceed.

## Connection Distribution Between Domains

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

## Wiring Together Problem Domains

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