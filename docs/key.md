# Key

## Purpose

This document serves as an overview of all primary terms, and mappings ordered by ? as they are defined, and used within this particular Golem Meta.

> TODO: Have this document, or the connected actual document get generated as part of a dev build task!

- Adaptation/Growth/Plasticity/?: ?
- Cell:
  - Afferents: ?
  - Efferents: ?
  - Axon: A one-way edge that projects resource production data to one or more other addresses. Cannot project to other axons.
  - Dendrite: A one-way edge that collections resource production data from one or more other addresses. Can be configured to also read from other directly connected dendrites, and not just from Axons.
  - Spike: A real number between [0,1], which represents the refreshedness/cooldown/fatigue/ of the resource production source used by all synapses to determine the number of resources generated.
  - State: Represents the cells internal environment which affect cell operation.
  - Synapses: A connection between two edges at a specific address with different sources that determines the number of resources to be produced for collection. By default, synapses can only form between axons, and dendrites.
  - Threshhold: The energy level required to generate resources at directly down-stream synapses.
  - ?: ?
  - ?: ?
- Dimensions Correspondences:
  - Input Width: Num Columns in Layer
  - Input Height: Num Rows in Layer
  - Input Length: ?
  - Input Duration: ?
  - I/O Processing Stage: ?
  - Module Depth: Number of Layers
  - Module Mass: Memory Consumption based on (num nodes, num edges, ?)
  - Malleability: Plasticity props/degree, and Crystallization degree
- Golem: ?
  - Components/Parts/Pieces/Package/?: ?
  - Matrix: Golem paradigm specific matrix terminology
  - ?: ?
  - ?: ?
- Matrix: An flow-based operational/cognitive data network/graph of nodes, and edges
  - Power source: The sources of flow which drive the processing.
    - Internal: Power sources that allow the matrix to operate in the absence of external input
      - Pacemakes/Temporal Alternators: Sources which fire spontaneously at some frequency thus contributing to baseline activity levels within the Matrix.
      - Mode Regulators: Sources whose fire rate determines the overall activity level of the Matrix.
    - External: The primary sources of activity generation.
      - ?
  - Node: An arbitrary type unit of data procesing.
  - Edge: A data-bearing conduit between two nodes.
  - Address: A uniquely generated string which serves as a shorthard representation for each destination within the Matrix.
  - Destination: The container/environment which hosts, operates, and prepares a set of nodes.
  - Layer: A group/set/2d matrix of destinations produced by the same production rules. Akin to a layer in BP neural nets.
  - Module: A collection of inter-, and intra-connected layers which serve as a distinct semantic whole/sub-set of the graph.
  - Nodes/Vertices: Cells
  - Edges: Axons, Dendrites
  - Construction: Growth
  - Definition: Language, Documents, and Configs
    - circuit/cycle : A templated closed path through several modules/layers
    - path : a connected walk between several modules through a series of edges or edge production rules
    - edge : a data bearing connection between two nodes
    - network : A templated distribution of some input source(s) across a distinct set of directed paths that operate in conjunction to provide one or more unified output edges.
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
  - Plasticity Factors: Matrix resources which modulate the level of malleability of nodes within the Matrix.
  - Spiking Factors: ?
    - Glutamate: ?
    - GABA: ?: ?
  - Operational Factors: Matrix resources which modulate operational/activity properties of nodes within the Matrix.
    - Dopamine: ?
    - Serotonin: ?
    - ?: ?
  - Structural Factors: Matrix resources which modulate structural changes within, and between modules. Structural changes impact module composition, shape, size, and I/O(i.e edge) profiles, but don't directly impact cell state, or connection plasticity aside from adding or removing cells, and/or intersection points where synapses can form.
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