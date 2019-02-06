# What makes this framework different

This is a short document for detailing the differences between this approach to a deep learning network, and other approaches.

## Value Types

A neuron is not represented by a continuous value. It is an energy spike in a continuous flow of information. However, in organic brains not all neurons have the same type of value. This allows them to serve different purposes. Our neural networks can support multiple types of cells in the network, which have different effects based on the type.

Node Types

- Charge/Direct : cells that affect the current charge of a cell
  - Activate : Applies a positive charge to a neuron which increases the likelihood of an action potential
  - Inhibit : Applies a negative charge to a neuron which decrease the likelihood of an action potential
- Chemical/Meta : cells that don't affect the current charge of a cell, and apply some other effect
  - ?

## Messaging

An organic brain is a highly parallel, and extremely modular network of processors. Each neuron serves as a localized microprocessor that parses inputs, and produces outputs. It sends data to other cells via axons, which can only be intercepted along unmyelinated portions of the axon. So largely where it spanws on the cell, and where it terminates. Each cell receives messages from other cells via dendrites, which are localized webs of connection. Cells in our system send messages to specific destinations, and read messages destined to nearby cells. Effectively, our network has a push, and subscribe system that each cell leverages to determine the inputs it uses. Thus we have a directed graph.

- Directed Edges
  - Axons
    - push data to addresses
    - sends messages
  - Dendrites
    - pulls data from addresses
    - read message at & receive messages from addresses

## Positioning System

While an organic brain is a graph, in CS a graph is an abstract data type with no notions of physicallity. Organic brains are physical implementations of the abstract type, and whose growth is guided by physical constraints. While we don't need a physical positioning system for our graph if we ignore distance based decay of signal strength, and distance based timing, it is still useful to leverage the relative positions of other cells to build structures as well as help determine structural plasticity. To that end, our framework contains a system for structurally representing regions in the graph, and using those structures to determine things like adjacency, distance, and proximity.

Distance is determined by a function of number of edges between two points in the graph, the lengths of those edges, and the adjacency/arrangement of the structures in the graph relative to one another.

**There is a growing body of evidence which suggests that dendrites weaken signals based on distance from the soma. Thus, distance based decay becomes necessary for dendrites.**

## Scalability

Brain neuron counts across earth-like animals, span many orders of magnitude. From small 100K brains to large 100B brains. In many cases, this will happen with brains that are roughly of similar architecture. Thus, our framework includes a system for arbitrarily scaling brain-like architectures without a need to change the architecture. Sizes of regions are a function of their place, and purpose in an architecture.

Interpretation of inputs to a pd/region?
each point maps a part of the input space that is usually many:1 (**what about output space?**)

multiple - overlapping, distint
individual - distinct, dense