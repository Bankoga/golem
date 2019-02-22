# Key

## Purpose

This document serves as an overview of all primary terms, and mappings ordered by ? as they are defined, and used within this particular Golem Meta.

> TODO: Have this document, or the connected actual document get generated as part of a dev build task!

### Misc

- Dimensions Correspondences:
  - Input Width: Num Columns in Layer
  - Input Height: Num Rows in Layer
  - Input Length: ?
  - Input Duration: ?
  - I/O Processing Stage: ?
  - Module Depth: Number of Layers
  - Module Mass: Memory Consumption based on (num nodes, num edges, ?)
  - Malleability: Plasticity props/degree, and Crystallization degree

### Golem

- Golem: Goal oriented logos encapsulation matrix
  - Components/Parts/Pieces/Package/?: ?
  - Matrix: Golem paradigm specific matrix terminology
  - ?: ?
  - ?: ?

Modes:
These are all hybrid matrix-command functions

- Maintenance: reset, cleanup, initialization, transience and crystallization mechanics, and session memory is consolidated
  - purpose: during this mode, some modules are totally reset, and others are plastically reset
  - Interrupts lead to a loss of maintenance changes and restore to pre-maintenance
  - Completion leads to the mode that triggered it
- Sleep_low: most external input, and output actions are suspended for a number of cycles based on a fraction of the time chosen to sleep.
  - Interrupts lead to operation
  - Cycles determine the number of rounds of low-high-low-maintenance-low before returning to Operation. Cycle pattern TBD!
- Sleep_deep: an internal compositional session replay system is active for a set duration unless interupted.
  - Interrupts lead to operation
  - Duration completion leads to sleep_low
- Operation: the system receives continuous input, and can trigger external output freely
- Suspend: upon triggering, the system halts timestep evaluation, and waits for further comman lind input
- Save: upon triggering, it first suspends operation, then writes the instance to disk
- Load: reads an instance from disk, and upon completion enters the suspend state

#### A note on Training

- Data:
  - Per type paired with question answer pairs
  - Per permutation of types paired with question answer pairs
- Types:
  - Screen (interpreted, reads files via screen sensor into matrix)
  - File (injected, reads file directly into matrix)
    - Image
    - Audio
    - Video
    - Text

During training each duration of sensory input should be overlapped with input to the question response sensor for some specific question:answer pair
Each question:answer pair can have a flag used to determine which output channels we expect to have output, and what we expect those outputs to be because output channels go through hard coded or preconfigured languages that it doesn't need to learn.
The difference in actual outputs vs expected outputs, is the loss.
Which is used by the modulation groups to determine how much to change the system.

Degree of Reward Loss - Impact on Behaviour - Impact on Weights - Direction of change
High - Repeat the behaviour less - greater impact - inverse
Low - Repeat behaviour more - less impact - linear
None - Always repeat behaviour - none - none

#### A note on Module Inputs and Config Revamp

Every word is a function
Every function is a concept
Every concept is some shape
Same shape concepts can be directly added together

Input Symbol Rates
Internal Sampling Rates
Output Sampling Rates

NOTE: Because of how well defined each piece is, we can statically check all the lowest level pieces!

Need to come up with a naming schema for fields, circuits, and melds as functions of module names. Perhaps Type_ModuleName
Though there is a high degree of overlap between many. perhaps most, circuits and a specific module. In fact, I think almost every module defines it's own circuit! Repos, and the two DM used controllers are the only exceptions!

#### Parts to pay attention to when designing a GOLEM

List of Semantic Fields (The basic higher level spaces that are used within the golems cognitive matrix. Closely related to input and output melds)
List of Problem Domains (black boxes that can be turned into specific algorithms or functions. I've taken to calling them modules most of the time)
List of Pipelines (Higher Level Categories of Semantically Connected Problem Domains, that may or may not be internally connected. That's sort of problematic actually because it feels like there should be another word than pipeline there)
List of Input and Output Melds (the circuits, which are either pipeline or module defined, that are responsible for carrying semantic fields between and within modules)

### Resources

| Label | Items Effected | Purpose | Biological Correspondent |
| --- | --- | --- | --- |
| Positive Charge | Charge Level | Used to convey an increase in charge level | Glutamate |
| Negative Charge | Charge Level | Used to convey a decrease in charge level | GABA |
| Focus Points | Processing,Plasticity | Used to indicate which things are currently being attended to by the decision making system. Could be used in one place to increase processing priority and in other to enhance encoding weight |  |
| Similarity Points | Similarity Level | --- | Noradrenaline || AcetylCholine |
| Likelihood Points | Likelihood Level | Used to indicate likelihood of some component being used or activated in the near future. The difference between the likelihood level and the likelihood max at time of spiking can be used to help drive plasticity by indicating the difference between expected possibility of output to the actuality of output. Low value diffs are less interesting than high value diffs. | Noradrenaline || AcetylCholine |
| Repetition Points | Plasticity | strengthens weights, makes current??past behaviour more likely, and lowers barriers to activity (in the bg directly, but unsure of impact in cortex), effects mood (i.e. state of decision making goal matrix component which is designed to minimize the amount of dopamine lost during activity?) | Dopamine |
| Mode Level Points | ? | could be used to affect the degree of impact the mode has during operation? | --- |
| Attractor | Goal Alignment | Used to shift the goal weight closer to the currently viewed weight. I.E. when the system that produces this resource is triggered, the recipient of it's projections will have its goal (or baseline?) weights shifted closer to the weight that triggered the resource production | --- |
| Repulsor | Goal Alignment | Used to shift the goal weight further away from the current weight | --- |
| Activant | Baseline Energy | Used to raise the baseline activity level. Concentrations drain with use, over time, or when cancelled by deactivants. Requires periodic replenishment during operation in order to stave off consolidation mode. This can serve as a hook for a wake/sleep cycle. Exists in low concentrations during maintenance, and consolidation/sleep modes. Concentrations of activant during operation correspond to overall activity level of the matrix. | Noradrenaline System |
| Deactivant | Baseline Energy | MAY NOT BE NEEDED. Though using static levels of activant for operation could be more cost effective. Used to decrease the baseline activity level. Concentrations drain over time, with use, or when cancelled by activants. | --- |
| Catalyst | Threshhold Level | Used to indicate a decrease in threshhold level proportional to the concentrations of catalyst. Specific catalyst systems can be used to control mood, passiveness, aggression, etc... by magnifying the effects of or bias toward specific subsystem or system states. Consequently, could be used to control resource availability by toggling different activity/foraging states. | --- |
| AntiCatalyst | Threshhold Level | Used to indicate an increase in the threshhold level proportional to the concentrations of the catalyst. | --- |
| --- | --- | --- | --- |

Each cells activation change set could be stored in a tensor of some sort?

- Golem Matrix Modulation/Resources:
  - Definition: Resource(label, decay_rate_in_sim_seconds, value_range, value_increments)
  - Resource Function: Each type of node in a matrix can process any non-data and non-energy resource based on it's own rules. Consequently, OPERATION_ON_NODE_FUNCTION_DEF for each resource type a Node accepts, needs to be defined by the Node.
  - If a resource isn't consumed or reclaimed by some node after getting shunted into the environment around the ports, then it moves around until consumed or it decays
  - Resource Types: Learning Paradigm Value Types
  - Node Resource : Resource Type : Effects on Node
    - Energy : Glutamate : Increases charge which is used like FP from DS3 for spike generation
    - Energy : Gaba : Decreases charge
    - All Nodes have an energy level which is being modeled like heat.
    - ?(reinforcement) : Dopamine : ?
    - Catalyst(activant/enablist) : Serotonin : Decreases energy level required for a spike to occur
    - ? : Acetylcholine : ?
    - Activity Level : Norepinephrine : Raises the baseline energy level of a node
  - Node Input: On spike connection strength multiplier (perhaps just calc the diff between injector, and receptor sizes for some sort of loss adjustment that we can leverage for plasticity? This seems like a nifty thing... Wat teh heck. So useful)
  - Node Output: Off/On spike-pod pair
  - Plasticity Factors: Matrix resources which modulate the level of malleability of nodes within the Matrix.
  - Spiking Factors: ?
    - Glutamate: ?
    - GABA: ?: ?
  - Operational Factors: Matrix resources which modulate operational/activity properties of nodes within the Matrix.
    - Dopamine: Activity repetition inducer, and activity inducer
    - Serotonin: Spike rate control
  - Structural Factors: Matrix resources which modulate structural changes within, and between modules. Structural changes impact module composition, shape, size, and I/O(i.e edge) profiles, but don't directly impact cell state, or connection plasticity aside from adding or removing cells, and/or intersection points where synapses can form.
    - Port: The amount of port growth factor in a cell determines how large of an impact current input has on plasticity changes
    - Afferent: The amount of afferent growth factor in a cell determines the % chance of a change in the projection profile of the cell
    - ?: The amount of ? growth factor in a module determines the % chance of a change in the reception profile of the cell

### Matrix

Maximum Rate of Reward : Perfect Reward
Curr Rate of Reward : Current Reward Activity Level
Minimum Rate of Reward : Zero Reward

The diff between max and current is the objective loss.
Intrinsic Max is predefined
System derived max rate of reward ?

> Matrix: A flow-based operational/cognitive data network/graph of nodes, and edges.The hierarchy follows the compositional levels of matrix component description.

- Compositional Levels of States (top-down): Golem, Matrix/Graph/Pair(Gen or Advers, Left or right), Melds, Pipeline, Stage, Module, Layer, pod, Node, Edge, Port.
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
  - Internal: Power sources that allow the matrix to operate in the absence of external input. The sources of energy that provide for internally-driven, or spontaneous activity. However, these both require some way to draw resources from their environment in order to allow for activity driven modulation of the spike timing via inhibition unless inhibiting such a cell simply causes delays the timer by some number of time steps?
    - Pacemakes/Temporal Alternators: Sources which fire spontaneously at some frequency thus contributing to baseline activity levels within the Matrix.
    - Mode Regulators: Sources whose fire rate determines the overall activity level of the Matrix.
  - External: The primary sources of activity generation.
    - ?
- Sampling: A matrix processes input predominantly in waves via sampling. Each Region of a Module is a distinct sampler.
  - Subsample Size: The shape of the basic discrete tokens of/continuous views||windows into the Semantic Field which is enc.apsulated by the region/module with corresponding unit meta. Subsample size determines the dynamic range of each subsample. The Dynamic range of human hearing can be roughly modeled using a sample size of ~24 bits. Whereas the dynamic range of an english phrase could be reasonably bounded at 256 tokens.
  - Sample Rate: The number of time to update the samples per second. The range of values this property can occupy are determined by the Dynamic Range of the sampler. Human speech tends to correspond to an ~8K sample rate.
  - Sample Size: The number of different subsamples to take per sampling.

### Matrix Components

> Matrix Components: Specific components of a matrix.

- Matrix Resource: The units of interaction/currency between nodes within the matrix. An object that triggers specific changes in cell behavior by manipulating dynamic modifiers in the operation method definitions. Can only affect cells which possess a corresponding type of port. All bound resources are either consumed on use, or freed and reused. Because this is digital, it may be more efficient to simply consume non-energy bound input, and internal resources on Node Activation. This also may play nicely with determining the timing based strenghts of port specific activation plasicity.
- Node: An arbitrary type unit of data procesing. In other words, a function of some sort. Nodes operate on matrix resources.
  - Node Type: There are many different types of nodes, which are determined by the differences in how they consume the input, process it internally, and return the output.
    - Cell: A node that corresponds to something one might see in an organic lifeforms body
    - Function: A node that correspons to a specific function
- Charge & Energy: The matrix operates on an abstracted notion of energy. Each of it's bottom-level components (nodes) use energy, and generate heat. Each level of the matrix hierarchy absorbs, and discards excess heat, and chemicals. The background heat level corresponds to a nodes baseline/homeostatic energy charge. Node operation costs a certain amount of energy, which is defined by it's current/evaluated threshhold charge, and triggers automatically once the threshhold is exceeded. This causes the excess energy to be discharged into the local environment, occupied upstream ports modified then released(or does this occur after the reader has conveyed the info from the upstream port?), and the downstream axon ports to be triggered. Nodes maintain their evaluated baseline energy charge via charge differential gated chemical &| energy sharing channels with the local environment/state.

WHERE DOES THE ENERGY THAT DRIVES PACEMAKERS COME FROM? Many nodes fire spontaneously at a dynamic or mutable minimum frequency.

- Heat: Node sub-component activation driven heat generation is a matrix option which enables the Node Heat Effect system. It introduces heating rate propertie, and heat effect on system properties to Node sub-components. This is primarily designed to be used as a way to help drive minimally-bounded connection plasticity which can lead to configs that would be impossible to manually specify.
  - Node components could have the below properties that are used in the function that determines transience, crystallization, and decay. These could be affected by the Heat generated by activity, and the resource production/chemical distribution/pressure from other Nodes, and it's environments
    - Ductility : indicates a nodes degree of resistance to state changes per Blank without affecting the baselines.
      - Null: No Ductility means it cannot change state per BLANK without affecting the baselines, and null Ductility means it cannot remain in any state without affecting the baselines.
      - Low: Low general Ductility means it can only stay in a new state for a short time per BLANK without affecting the baselines.
      - High: High Ductility means it can stay in altered states for extended periods of time per BLANK without affecting the baselines.
    - Malleability : indicates the degree to which a component can change shape per transience cycle or per session before affecting the baselines?
      - Null: Null Malleability means no amount of change per BLANK can affect the baseline.
      - Low: low Malleability means it can only make small changes in shape in any given direction per BLANK before affecting the baselines.
      - High: High Malleability means it can change a lot in shape per BLANK before affecting the baselines. Imagine nodes that have axons which walk the entire matrix based on the current inputs, and outputs but resets after each session, only changing starting positiuon slightly.
    - Elasticity: indicates a components ability to resist a distorting influence (resources that lead to activation or state change) and to return to it's original shape and size when the influce is removed.
      - Each Pod produces a matrix which represents the strain energy on each of it's components, and their sub-components shapes which can be used during a specific maintenance stage in a multi-stage operational cycle to drive long-term plasticity (this requires more research into Cauchy stress tensors). The 3x3x3 cauchy matrix may be sufficient if we can represent the axons, dendrites, and soma as 3 dimensions of stress. However, axons and dendrites are both distinct 3D Shapes, with the soma being more an abstract shape that isn't directly addressable, to an extent. So each axon, and dendrite may produce their own tensor.....
- Edge: A data-flow directing conduit from one Node to a specific address which can form connections with other edges at their unbound destinations (or replace myelination with expanded destination sets?) via ports.
  - There are 3 types of Edges:
    - Read/Consume: Takes resources and adds them to the cells state
    - Write/Produce: Creates resources producing connections at Pods
    - Execute/Instruct: ?
- Port: A data-bearing conduit between the edges of two nodes. Each reading edge is responsible for handling all of the ports for it's connections
- Address: A uniquely generated string which serves as a shorthard representation for each pod within the Matrix.
- Pod: A discretely addressable sub-set of a layer. It is the container/environment which hosts, operates, and prepares any number of nodes. Each pod represents some percentage of the input and output areas it in which it participates. Pods within the same layer cannot coexist in the same indices.
  - State: Represents the environment which affects the operations of a small set of cells. Need different mixing rules for pods within the same layer, across layers within the module, across layers between modules, and across cells between pods
    - Resource Level: An array of real numbers, each betwen [0,256], which represents the background level of an enumerated list of resources within the operating environment of some small set of cells
    - Definition: Pod(size=% of layer area occupied, misc=the rest of the details which are a WIP)
- Layer: An I/O area is called a layer, and is akin to a layer in BP neural nets. More specifically it is a set (2D-matrix) of pods produced by the same production rules. All layers in a module share the same length, and width. However each layer can support a different density of cells. Thus, when projecting to an input area, the connection/indexing functions must take into account the density of the layer which determines the actual number of indices. A 100x100 layer could conceivably be divided among a much smaller number of pods than its maximum pod area, like say 10, with each pod corresponding to 1000 indices worth of projections instead of limit set for the number of pods per index. Thus a projection can be defined in way that specifies a single index, or a rule for selecting subsequent indices!
  - IMPORTANTE NOTE: Intramodule plasticity is polynomially distance attenuated by some undecided func while Intermodule plasticity has a linear distance decrease
  - Definition: Layer(length, width, num_pods)
- Module: A collection of inter-, and intra-connected layers which serve as a distinct semantic whole/sub-set of the graph.
  - Definition: Module(length=max number of rows, width=max number of columns, height=number of layers, depth=circuitry complexity)
- Composition: The components used/responsible for connecting different organizational and functional components
  - Composition Application/Creation Types: Compositions can be applied via a meld, or directly. The manner in which it is done determines how it impacts input size initialization functions. Melds affect input size, whereas circuits do not.
  - Circuit: A set of rules for building a continuous path of cells across multiple pod stacks (layer matrix i,j). They operate based on hook tags. A modules circuit support is determined by the hooks described in the module.
  - Cycle: A set of rules for building a special type of circuit which eventually returns to the starting pod.
  - Pipeline: A set of modules, and rules for building a continuous path of information through them, and sometimes along with other modules. All pipelines have 4 sets of connections/parts: input(s), output(s), internal(s), and state(s) which can span an arbitrary number of stages between input, and output.
    - Pipeline Type determines how the defined wave flow interacts with the other pipelines. Is this the source of the package types we have been using: core, regulator, shell, framework?
      - Data||I/O: a pipeline that handles the processing, and transport of resources in to, and out of the Matrix.
      - Problem Domain: a pipeline that handles the processing, and transport of resources about, and within a specific sub-set of the modules within the Matrix contained by itsel,  in a shared repository, or in another pipeline.
      - Framework: a pipeline that handles the processing, and transport of resources about, and within the Matrix.
      - Modulator: a pipeline that handles the processing, and transport of resource that affect the operation of the Matrix, and any of it's sub-components.
  - Meld: A set of rules for building a continuous path of information through several pipelines, and modules. As with all matrix components, it has 4 sets of parts. Melds are the highest level of compositional structure within a matrix.

### Hooks

- Hooks: ?
  - Ontology Level: hooks can be described at each ontological level of matrix organization.
  - What configs are used to define hooks?
  - What defines a hook?
  - How do we define a hook?

### Cells

Adaptation/Growth/Plasticity/?: ?

> Cell: ?

- Afferents: ?
- Efferents: ?
- Charge: A real numer betwen [-256,256] that represents the energy level of the cell
- Port Type : A type of conditional gateway that connects a cells Chemical State to another pods chemical state via an edge, or to its container pods chemical State directly that gets evaluated every time step.
- Port Properties: The properties that determine how a Port operates.
  - Open Conditions: A list of boolean clauses which can cause the Port to open when true. Examples of properties used in conditionals in human neurons are membrane voltage, chemical shape, and the motion of internal fluids in the cell.
  - Close Conditions: A list of boolean clauses which can cause the Port to open when true. Examples of properties used in conditionals in human neurons are membrane voltage, chemical shape, and the motion of internal fluids in the cell.
  - Effect-Value pairs on State: What operations are performed using which properties between the two states, and the increment by which change can occur at each time step. A pair of examples are listed below:
    - Flow Direction: the direction of the effect on state for pressure differential based properties.
    - Flow Volume: the size of the pressure based equilization Port.
  - Component Size Difference: the difference in size between the two sides of the Port. Any overflow bleeds into the env of the pod where the Port occurs with effects based on the direction and magnitude of the difference
  - Component Growth Factor Difference: the difference in the growth factor for the projecting and receiving cells which drives changes in the size differential during plasticity
- Axon: A one-way edge that projects resource production data to one or more other Pods. Cannot form connections with other axons.
  - There are 2 types of axons: Guided, and Directed
  - Guided axons can only form connections at their source, and destination pods. All pods receive data immediately.
  - Directed axons can from connections anywhere between their source, and destination pods.
    - It takes N = ???????? timesteps for data to make it all the way to the furthest pod.
- Dendrite: A one-way edge that collections resource production data from one or more other Pods. Can be configured to also read from other directly connected dendrites, and not just from Axons.
- Spike: A real number between [0,1] that used by all synapses to determine the number of resources generated. The distance of the spike value from 1 represents the refreshedness/cooldown/fatigue/? of the resource production source, i.e. the axons level of fatigue.
- Chemical State: Represents the cells internal environment which drives cell operations.
- Synapses: A specific type of Port that forms between two edges at a specific address with different sources which determines the number of resources to be produced for collection in the reading edge. By default, synapses can only form between axons, and dendrites.
- Threshhold: The energy level required to generate resources at directly down-stream synapses.
- ?: ?
- ?: ?

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