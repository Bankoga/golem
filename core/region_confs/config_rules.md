# Config Rules and Framework Explanations

## Overview

Biological brains are 3D objects with complex patterns of connectivity. However, because each cell is effectively a processor, brains are highly parallel, and seemingly modular. The human brain for instance has a routine pattern of connectivity between the neocortex and the thalamus. Although wetware brains have the software of intelligence expressed via the hardware, it's possible to implement said software in a different hardware substrate though with contraints. The hierarchical, modular, and ordered nature of wetware brains led to the notions defined below of problem domains, regions and layers. Connecitivty is the major paradigm of a processor graph like a human brain. In our framework, the connectivity patterns of cells are determined by the higher level organizational properties of their containers, with the framework code implementing generic behaviours based upon the organization. In essence, configuration is separate, and could be considered hyperparams.

## The Purpose of Problem Domains, Regions, and Layers

A brain network, as implemented by this framework, has 3 levels of organization that affect how cells, at the lowest level, operate. The levels, from highest to lowest, are as follows:

- Problem Domain
- Region
- Layer

### Problem Domains

There are several types of problem domains, each with a unique set of regions. Problem domains are high level objects built using lots of smaller shapes. Kind of like polygons for graphics.
As currently conceived, there are 4 types of problem domains:

| **Type**      | **Regions**           | **Is_Paired** |
|---------------|-----------------------|---------------|
| Cortical      | Relay, Cortex         | True          |
| SubCortex     | Many (undetermined)   | True          |
| BrainStem     | Undetermined          | ?             |
| Cerebellum    | 1 (revisit)           | ?             |
|---------------|-----------------------|---------------|

### Regions

The point of a region is to determine the connection patterns of the layers. Given that cells are the units of Input, and Output, they are the units of connectivity. The type of region determines to what other types of regions cells within it can connect. With the how being governed by the organization of the layers within the region.
Regions are basically rectangles, and so are akin to 3D Matrices. The length, and width of a region determines the length, and width of the layers it contains. Whereas the height of the region/rectangle is determined by the number of layers in the region. Each layer is equal to 1 unit of height.

Known types of regions are currently limited to:

- Cortex
- Relay
- Cerebellum (this is a WIP that needs to be revisited)

### Layers

The purpose of a layer is to create destinations for cells, and constrain the possible connections of cells. In essence, a layer is an addressable container for cells. Every point in a layer corresponds to either a single cell XOR an array of cells. For convenience, mixing the paradigms of single vs array of cells within a given type of layer is not supported. Furthermore, a layer is a unit of height for a region.

### Cells

A cell in a human brain can broadly be described by two categories: neuronal, and glial. Neurons are the processors of the brain, and glial cells serve as maintenance, neuromodulation, and scaffolding. In this framework, the role of glial cells are largely played by the framework itself. Additionally, certain aspects of the brain that are controlled by glial cells, like myelination, are currently excluded in order to reduce the complexity of initializing a network, and the ongoing structural plasticity during activation.

The two major properties of a cell are activation_type, and cell_morphology

> Randomly generate the lengths of seconday dendrites based on morphology?
> Usage based growth may need to be implemented at some point

- activation_type : controls the type of value returned by the axon
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
> What determines the length of each dendrite?

A Cell Type is a tuple of an activation_type, a single cell_morphology, & one or more destinations.

> cell_type = {activation_type, cell_morphology, destinations[]}

The two major properties, determine the general other properties of the cell like the plasticity properties, resource constraints, etc...

## Region Config Files

Since the framework is, for the most part, region, and layer agnostic, the specifics of each region are determined by a configuration yaml which contains all the data needed to initialize the region with all of its layers given the specific input/output constraints of the problem domain object.

- aside from layer data, what other data needs to be stored in a region config?
- layers list
  - layer dict
    - name: layer_name
      - used as key for layers dict inside a region
    - point_size: number of cells at a point (i.e. destination) in the layer
    - cells list: a list of tuples of cell type, and percent of cells in layer
      - cell type
        - cell morphology
          - lengths of dendrites?
          - plasticity data (if differs from generic)
          - resource constraints (if differs from generic)
        - connection data
          - types of cells that can project to the destination
          - layer to layer connections within the region
          - substitution spots for cross-PD connections
        - distribution percentage: indicates what % of point_size should be composed of the paired cell type

> Note on Cortex Region: it is perhaps the case that l1-6 naming convention works fine normally, though something more descriptive may be nice

## Destination Keys

The destination of a cells axon can't be absolutely determined before initialization due to the relative nature of the connectivity patterns. Consequently, we need to use keys in the config that are parsed during init, and replaced with the absolute path data. For example, if a layer has cells that project to adjacent columns, we won't know the indices of the adjacent columns until we know the size of the region which is determined during initialization.

> What should be used as the destination between semantically named layers? The order? What about cross-region references?
> The destinations should use the path data schema with appropriate substitution slots, and relative paths

Some cells project to multiple destinations via the same axon. The axon will branch.

### Format of a full path

- [pd_key, region_key, region_loc, layer_key]
- [pd_key, region_key, region_loc, layer_key, cell_index]

### Format of Destination Config

- [activation_key, [pd_key, region_key, region_loc, layer_key]]
- [activation_key, [pd_key, region_key, region_loc, layer_key, cell_index]]

region_loc is either (x, y) or (x, y, z). If layer_key's are enumerable then we can use (x, y, z)
Not all region_locs @ the layer_key will have multiple cell indices. Some layers have a cell at each point instead of an array of cells at each point

### Config Destination Substitutions

Config destinations are patterns that indicate where cells in a layer can project outputs. Substitution keywords are replaced during init with generated info.
Furthermore, each destination applies to one or more activation type of cells.

#### activation keys

- e_type : excitory neuron only destination
- i_type: inhibitory neuron only destination
- m_type : modulatory neuron only destination
- num_type : excitory and inhibitory neuron only destination
- all_type : all activation types destination

#### path substitution keys

- pair : project to mirrored location in the paired problem domain
- same : reuse current path data for the matching level of the new path
- output : substitute the output paths to other nodes for the destination according to PD type
- "name" : use the name as the key in the path
- none : layer serves as a destination without any cells in the layer
  - in other words, the layer will have dendrites that receive from it but it won't return any outputs
- adjacent : projects to neighboring destinations
  - all vs specific adjacency?
