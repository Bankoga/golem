# Key

## Purpose

This document serves as an overview of all primary terms, and mappings ordered by ? as they are defined, and used within this particular Golem Meta.

> TODO: Have this document, or the connected actual document get generated as part of a dev build task!

- Adaptation/Growth/Plasticity/?: ?
- Cell:
  - Axon: A one-way edge that projects resource production data to one or more other addresses. Cannot project to other axons.
  - Dendrite: A one-way edge that collections resource production data from one or more other addresses. Can be configured to also read from other directly connected dendrites, and not just from Axons.
  - Synapses: A connection between two edges at a specific address with different sources that determines the number of resources to be produced for collection. By default, synapses can only form between axons, and dendrites.
  - ?: ?
  - ?: ?
- Dimensions:
  - Width: ?
  - Height: ?
  - Length: ?
  - Depth: ?
  - Duration: ?
  - Mass: ?
  - Malleability: ?
- Golem: ?
  - Components/Parts/Pieces/Package/?: ?
  - ?: ?
  - ?: ?
  - ?: ?
- Matrix: An operational/cognitive data network/graph of nodes, and edges
  - Node: A unit of data procesing
  - Edge: A data-bearing conduit between two data-processing units
  - Address: ?
  - Destination: ?
  - Layer: ?
  - Module: ?
  - Nodes/Vertices: Cells
  - Edges: Axons, Dendrites
  - Construction: Growth
  - Definition: Language, Documents, and Configs
    - circuit/cycle : closed loop through several modules/layers
    - path : a connected walk through a several modules through a sequence of edges
    - edge : a data bearing connection between two nodes
    - network : ?
  - Operation
  - Load/Save: File Type, Options, etc...
  - Resource Types: Learning Paradigm Value Types
  - Node Resource : Resource Type : Effects on Node
    - Energy : Glutamate : Increases charge which is used like FP from DS3 for spike generation
    - Energy : Gaba : Decreases charge
    - ?(reinforcement) : Dopamine : ?
    - Catalyst(activant/enablist) : Serotonin : Decreases energy level required for a spike to occur
    - ? : Acetylcholine : ?
    - ? : Norepinephrine : ?
  - Node Input: On spike connection strength multiplier (perhaps just calc the diff between injector, and receptor sizes for some sort of loss adjustment that we can leverage for plasticity? This seems like a nifty thing... Wat teh heck. So useful)
  - Node Output: Off/On spike-destination pair
- Matrix Modulation/Resources:
  - Spiking Factors: ?
    - Glutamate: ?
    - GABA: ?: ?
  - Operational Factors: Matrix resources which modulate operational/activity properties of nodes within the Matrix
    - Dopamine: ?
    - Serotonin: ?
    - ?
  - Structural Factors: Matrix resources which module the 
    - ?: ?
    - ?: ?
    - ?: ?
    - ?

## Paradigms

They be useful for framing various aspects of different problems. Many have been used in the construction of this application.

What are _BLANK_?
What purpose do _BLANK_ serve?
How are _BLANK_ useful/what are the benefits of this paradigm?
How are _BLANK_ detrimental/what are the drawbacks of this paradigm?

- Learning Paradigm: Earth-based Organic Neurons
  - Activation: Non-linear combination of past 20 timesteps worth of synapse activity, and chemical concentration in the environment and within the cell
  - Connections: Synapses (axon-dendrite, dendrite-dendrite, axon-cell)
  - Connection Strengths: Num Synapses, Size per synapse
  - Updates: Neuromodulation, Neuroplasticity, Session Replay, ?
  - Value Types: Neurotransmitter Types
- ML System Paradigm: Golem
  - DL Architecture = Golem Type
  - Construction
  - Configuration
  - Deployment
  - Maintenance
  - Modification
  - Training

Growth

    