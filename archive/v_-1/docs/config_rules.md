# Config Rules and Framework Explanations

## Overview

Biological brains are 3D objects with complex patterns of connectivity. However, because each cell is effectively a processor, brains are highly parallel, and seemingly modular. The human brain for instance has a routine pattern of connectivity between the neocortex and the thalamus. Although wetware brains have the software of intelligence expressed via the hardware, it's possible to implement said software in a different hardware substrate though with contraints. The hierarchical, modular, and ordered nature of wetware brains led to the notions defined below of problem domains, regions and layers. Connecitivty is the major paradigm of a processor graph like a human brain. In our framework, the connectivity patterns of cells are determined by the higher level organizational properties of their containers, with the framework code implementing generic behaviours based upon the organization. In essence, configuration is separate, and could be considered hyperparams.

## The Purpose of Problem Domains, Regions, and Layers

A golem, as implemented by this framework, has 3 levels of brain asbtraction/organization that affect how cells, at the lowest level, operate. The levels, from highest to lowest, are as follows:

- Problem Domain
- Region
- Layer

### Problem Domains

There are several types of problem domains, each with a unique set of regions. Problem domains are high level objects built using lots of smaller shapes. Kind of like polygons for graphics.
As currently conceived, there are several types of problem domains:

| **Type** | **Regions** | **Is_Paired** |
| --- | --- | --- |
| cortical | relay, cortex | True |
| subcortex | Many (undetermined) | True |
| brainstem | Undetermined | ? |
| cerebellum | 1 (revisit) | ? |
| encoder | 0 | ? |
| decoder | 0 | ? |
| --- | --- | --- |

Because brains are highly connected, and strongly interdependent, cleanly separating all the pieces can be difficult. Whenever we hit a rough spot, we will have to refactor.

Encoder domains are unique, and must have predefined support in the framework. This will probably be the same for the decoder type of problem domains. Both are interaction points outside the network, and thus require specific handling that does not apply to the other types of domains.

### Regions

The point of a region is to determine the connection patterns of the layers. Given that cells are the units of Input, and Output, they are the units of connectivity. The type of region determines to what other types of regions cells within it can connect. With the how being governed by the organization of the layers within the region.
Regions are basically rectangles, and so are akin to 3D Matrices. The length, and width of a region determines the length, and width of the layers it contains. Whereas the height of the region/rectangle is determined by the number of layers in the region. Each layer is equal to 1 unit of height.

Known types of regions are currently limited to:

- Cortex
- relay
- Cerebellum (this is a WIP that needs to be revisited)

The cortex and relay regions within the cortical problem domain type have the same dimensions, and thus can be unified into a single region. If we want the thalamus to exist as a separate region inside a subcortical problem domain, then they will have to be stitched together according to some rules.

Regions within a problem domain type, are largely defined by their dimensions rows x columns x layers (length x width x height). Layers with the same number of rows and columns can or should be stacked together inside the same region if they are functionally interconnected.

### Layers

The purpose of a layer is to create destinations for cells, and constrain the possible connections of cells. In essence, a layer is an addressable container for cells. Every point in a layer corresponds to either a single cell XOR an array of cells. For convenience, mixing the paradigms of single vs array of cells within a given type of layer is not supported. Furthermore, a layer is a unit of height for a region.

### Destinations

Each point in a layer is a pod. Destinations are end points for cell axon projections. They contain either one or more cells based on the specs of the relevant config.

### Cells

A cell in a human brain can broadly be described by two categories: neuronal, and glial. Neurons are the processors of the brain, and glial cells serve as maintenance, neuromodulation, and scaffolding. In this framework, the role of glial cells are largely played by the framework itself. Additionally, certain aspects of the brain that are controlled by glial cells, like myelination, are currently excluded in order to reduce the complexity of initializing a network, and the ongoing structural plasticity during activation.

The two major properties of a cell are resource_type, and cell_morphology. Activation type determines how a cell is consumed, and morphology determines how it consumes. We assume that all cells project to some pod(s).

> Randomly generate the lengths of seconday dendrites based on morphology?
> Usage based growth may need to be implemented at some point

- resource_type : controls the type of value returned by the axon
  - -1, 1, or modulatory chemical
- cell_morphology : controls the number of dendrites, and their direction
  - pyramid : 4 adjacent or basal dendrites, a local dendrite, a long apical dendrite, and axon
  - bipolar : 1 dendrite, and axon
  - unipolar : receptor directly to axon (sensory cells)
- inhibitory types in cortex
  - chandelier
  - pv basket
  - long projecting (l6 to relay)
  - martinotti (l2 to l3)
  - interneuron selective (l2/3 to l5/6)
  - cck basket

> The different supported cell morphologies are still a WIP

A Cell Type is a tuple of an resource_type, a single cell_morphology, & one or more destinations.

> cell_type = {resource_type, cell_morphology, destinations[]}

The two major properties, determine the general other properties of the cell like the plasticity properties, resource constraints, etc...

**All cells include receptors for the pod that contains them!**

## Region Config Files

Since the framework is, for the most part, problem domain type, region, and layer agnostic, the specifics of each region are determined by a configuration yaml which contains all the data needed to initialize the region with all of its layers given the specific input/output constraints of the problem domain object.

- aside from layer data, what other data needs to be stored in a region config?
- layers list
  - layer dict
    - name: layer_name
      - used as key for layers dict inside a region
    - point_size: number of cells at a point (i.e. pod) in the layer
    - cells list: a list of tuples of cell type, and percent of cells in layer
      - cell type
        - cell morphology
          - lengths of dendrites?
          - plasticity data (if differs from generic)
          - resource constraints (if differs from generic)
        - connection data
          - types of cells that can project to the pod
          - layer to layer connections within the region
          - substitution spots for cross-PD connections
        - distribution percentage: indicates what % of point_size should be composed of the paired cell type

> Note on Cortex Region: it is perhaps the case that l1-6 naming convention works fine normally, though something more descriptive may be nice

## Pod Keys

The pod of a cells axon can't be absolutely determined before initialization due to the relative nature of the connectivity patterns. Consequently, we need to use keys in the config that are parsed during init, and replaced with the absolute path data. For example, if a layer has cells that project to adjacent columns, we won't know the indices of the adjacent columns until we know the size of the region which is determined during initialization.

**SEE PATH PROBLEMS FOR OPEN QUESTIONS CONCERNING DESTINATION KEYS!**

Some cells project to multiple destinations via the same axon. The axon will branch.

### Format of a full path

- [pd_key, region_key, region_loc, layer_key]
- [pd_key, region_key, region_loc, layer_key, cell_index]

### Format of Pod Config

- [activation_key, [pd_key, region_key, region_loc, layer_key]]
- [activation_key, [pd_key, region_key, region_loc, layer_key, cell_index]]

region_loc is either (x, y) or (x, y, z). If layer_key's are enumerable then we can use (x, y, z)
Not all region_locs @ the layer_key will have multiple cell indices. Some layers have a cell at each point instead of an array of cells at each point

### Config Pod Substitutions

Config destinations are patterns that indicate where cells in a layer can project outputs. Substitution keywords are replaced during init with generated info.
Furthermore, each pod applies to one or more activation type of cells.

#### activation keys

- e_type : excitory neuron only pod
- i_type: inhibitory neuron only pod
- m_type : modulatory neuron only pod
- num_type : excitory and inhibitory neuron only pod
- all_type : all activation types pod

#### path substitution keys

- pair : project to mirrored location in the paired problem domain
- same : reuse current path data for the matching level of the new path
- output : substitute the output paths to other nodes for the pod according to PD type
- "name" : use the name as the key in the path
- none : layer serves as a pod without any cells in the layer
  - in other words, the layer will have dendrites that receive from it but it won't return any outputs
- adjacent : projects to neighboring destinations
  - all vs specific adjacency?
