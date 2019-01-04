# Key

## Purpose

This document serves as an overview of all primary (paradigm) semantic, hierarchical, ontological cornerstone terms, and mappings.

> TODO: Have this document, or the connected actual document get generated as part of a dev build task!

## Paradigms to Concept Mappings

- Graph Paradigm: Matrix
  - Nodes/Vertices: Cells
  - Edges: Axons, Dendrites
  - Construction
  - Definition: Language, Documents, and Configs
    - circuits
    - pathways
    - edges
    - networks
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