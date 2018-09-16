# How to Progres

In order to achieve the seemingly impossible, shit needs to get done! To that end, I have created a plan for moving forward:

- Write code for pieces with known solutions
- Research parameters, and solutions to open questions
- whenever there are new open questions, add them to the list of problems
- Repeat 1 to 3 until there are no more open questions
- Review all that has been done
- Optimize for computational efficiency

## What am I doing

What is the brain? It is a physical graph of processors. Axons, and Dendrites cover areas, and intersect to form directed edges in the processor graph.

What am I building? A software framework for building, and running networks of processors/learning units which can emulate physical brains.

## Ready to Code

This document is for tracking which pieces of the framework are ready for implementation. Not necessarily the interaction points between different bits of code. This for pieces where the bulk alg, or sub program can be made functional with little modification necessary to hook it in.

Anything that relies on the completed configs is not ready for implementation. Even then, some pieces that operate on items returned by the config can still be worked on.

### problem graph

Most of the problem graph relies on the form of the configs being finalized. However some of the pieces are ready for work.

- Batch Inputs
- repl

### Activation Methods

Every container level of the framework has the same, or nearly the same, activation method. It takes in certain data about the timestep, the state of the network, and a reference to the dictionary of batched inputs then outputs a flat array of axon terminals.

- Problem Domain
- Region
- Layer
- Destination
- Cell

### Cells

Axons, Cells, and Dendrites do not rely on the configs. Some of the details for their initialization come from the configs, but most of their code is independent of those pieces. The notable exceptions are for determining destinations.

- Axon return
- Axon usage limits
- Activation
- Summation
- Usage Limits
- Dendrite summation
- Per Source plasticity
- STDP
- Refactory period