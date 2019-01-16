# Key

## Purpose

This document serves as an overview of all primary terms, and mappings ordered by ? as they are defined, and used within this particular Golem Meta.

> TODO: Have this document, or the connected actual document get generated as part of a dev build task!
- Graph/Matrix
- Adaptation/Growth/Plasticity/?: ?
- Cell:
  - Afferents: ?
  - Efferents: ?
  - Charge: A real numer betwen [-256,256] that represents the energy level of the cell
  - Channel Type : A type of conditional gateway that connects a cells Chemical State to another pods chemical state via an edge, or to its container pods chemical State directly that gets evaluated every time step.
  - Channel Properties: The properties that determine how a channel operates.
    - Open Conditions: A list of boolean clauses which can cause the channel to open when true. Examples of properties used in conditionals in human neurons are membrane voltage, chemical shape, and the motion of internal fluids in the cell.
    - Close Conditions: A list of boolean clauses which can cause the channel to open when true. Examples of properties used in conditionals in human neurons are membrane voltage, chemical shape, and the motion of internal fluids in the cell.
    - Effect-Value pairs on State: What operations are performed using which properties between the two states, and the increment by which change can occur at each time step. A pair of examples are listed below:
      - Flow Direction: the direction of the effect on state for pressure differential based properties.
      - Flow Volume: the size of the pressure based equilization channel.
  - Axon: A one-way edge that projects resource production data to one or more other addresses. Cannot project to other axons.
  - Dendrite: A one-way edge that collections resource production data from one or more other addresses. Can be configured to also read from other directly connected dendrites, and not just from Axons.
  - Spike: A real number between [0,1] that used by all synapses to determine the number of resources generated. The distance of the spike value from 1 represents the refreshedness/cooldown/fatigue/? of the resource production source, i.e. the axons level of fatigue.
  - Chemical State: Represents the cells internal environment which drives cell operations.
  - Synapses: A specific type of channel that forms between two edges at a specific address with different sources which determines the number of resources to be produced for collection in the reading edge. By default, synapses can only form between axons, and dendrites.
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
- Golem Matrix Modulation/Resources:
  - Resource Types: Learning Paradigm Value Types
  - Node Resource : Resource Type : Effects on Node
    - Energy : Glutamate : Increases charge which is used like FP from DS3 for spike generation
    - Energy : Gaba : Decreases charge
    - ?(reinforcement) : Dopamine : ?
    - Catalyst(activant/enablist) : Serotonin : Decreases energy level required for a spike to occur
    - ? : Acetylcholine : ?
    - ? : Norepinephrine : ?
  - Node Input: On spike connection strength multiplier (perhaps just calc the diff between injector, and receptor sizes for some sort of loss adjustment that we can leverage for plasticity? This seems like a nifty thing... Wat teh heck. So useful)
  - Node Output: Off/On spike-pod pair
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
- Matrix: A flow-based operational/cognitive data network/graph of nodes, and edges.The hierarchy follows the compositional levels of matrix component description.
  - Compositional Levels of States (top-down): Golem, Matrix/Graph/Pair(Gen or Advers, Left or right), Meld, Pipeline, Stage, Module, Layer, pod, Node, Edge, Port.
  - Components: Matrices are broken down into two sets of primary structures.
    - Organizational: (modules, layers, and composition)
    - Functional: (nodes, edges, operations)
  - Component Pieces: Each graph/matrix component is made of the same pieces across different scales. From nodes and edges, to submodules and modules.
    - Input Shape: The graph of available (direct/send, and indirect/read) input sources gated by accepted input types.
    - Output Shape: The graph of potential (direct/send only) output sources gated by possible output types.
    - Internal Function: The sequence of steps that a piece takes when transforming input into output.
    - State: Objects at each organizational scale of a matrix, shares a homeostatic environment. This shared environment is a state object. Thus each component has a state which interacts with its parent, and child component states. The hierarchy follows the compositional level of component states.
  - Properties of Matrix Pieces: Each matrix component has the same primary property sets.
    - Definition/Description: The initial form of the matrix component.
      - Is it a copy of the config, or the post init state?
    - Initialization: The rules for creating the initial object.
    - State: The current state of the component.
    - Usage Rules: The rules for changing the object according to usage, homeostasis operations, and activity modulation.
  - Power source: The sources of flow which drive the processing. Externally, and Internally generated inputs can be leveraged to drive the spike flow system of the Matrix.
    - Internal: Power sources that allow the matrix to operate in the absence of external input.
      - Pacemakes/Temporal Alternators: Sources which fire spontaneously at some frequency thus contributing to baseline activity levels within the Matrix.
      - Mode Regulators: Sources whose fire rate determines the overall activity level of the Matrix.
    - External: The primary sources of activity generation.
      - ?
- Matrix Components: Specific components of a matrix.
  - Node: An arbitrary type unit of data procesing. In other words, a function of some sort.
  - Edge: A data-bearing conduit between two nodes.
  - Address: A uniquely generated string which serves as a shorthard representation for each pod within the Matrix.
  - Pod: The container/environment which hosts, operates, and prepares several set of nodes.
    - State: Represents the environment which affects the operations of a small set of cells
      - Charge: A real numer betwen [-256,256] that represents the background energy level of the operating environment of some small set of cells
      - Chemical : An object that triggers specific changes in cell behavior by manipulating dynamic modifiers in the operation method definitions. Can only affect cells which possess a corresponding type of channel.
  - Layer: A group/set/2d matrix of pods produced by the same production rules. Akin to a layer in BP neural nets.
  - Module: A collection of inter-, and intra-connected layers which serve as a distinct semantic whole/sub-set of the graph.
  - Composition: The components used/responsible for connecting different organizational and functional components.
    - Circuit: A set of rules for building a continuous path of cells across multiple pod stacks (layer matrix i,j). They operate based on hook tags. A modules circuit support is determined by the hooks described in the module.
    - Cycle: A set of rules for building a special type of circuit which eventually returns to the starting pod.
    - Pipeline: A set of rules for building a continuous path of information through several modules. All pipelines have 4 sets of connections/parts: input(s), output(s), internal(s), and state(s) which can span an arbitrary number of stages between input, and output.
    - Meld: A set of rules for building a continuous path of information through several pipelines, and modules. As with all matrix components, it has 4 sets of parts. Melds are the highest level of compositional structure within a matrix.
- Hooks: ?
  - Ontology Level: hooks can be described at each ontological level of matrix organization.
  - What configs are used to define hooks?
  - What defines a hook?
  - How do we define a hook?

Misc stuff to be incorporated

- Construction: Growth
- Definition: Language, Documents, and Configs
  - ?
- Path : A connected walk between pods (containers for small sets of cells) through a series of edges or edge production rules.
- Path Templates: The different ways to define connections between non-adjacent modules, layers, and pods within any arbitrary Matrix. Does not allow for arbitrary/manual edge specification between packages to help reduce specific package dependencies. However, in-matrix adjacency can lead to growth outside the initialization paradigm which is restricted to edge distribution formation rules/templates.
  - circuits/cycles : A type of path template that makes a closed directly linked loop of cells, by type, through different pods.
  - network : A type of path template where some set of input source(s) (pipelines or modules) are distributed across a distinct set of directed paths that operate in conjunction to provide one or more unified output edges.
  - pipeline : A type of path template which is composed of a sequence of modules that form one or more distinct routes.
  - relay : A type of path template where an output from one pod, A, to another, B, is gated by a third, C, which either is controlled externally and thus passes the input from A to B directly, or temporally aggregates input from A before passing it on to B. Interestingly, when viewed under this definition, Neurons in organic entities appear to act as contextually sensitive/dynamic relays with the entire brain being built out of networks of relays
- Operation
- Load/Save: File Type, Options, etc...

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