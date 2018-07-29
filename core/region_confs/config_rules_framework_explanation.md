# Config Rules and Framework Explanations

## Overview

Biological brains are 3D objects with complex patterns of connectivity. However, because each cell is effectively a processor, brains are highly parallel, and seemingly modular. The human brain for instance has a routine pattern of connectivity between the neocortex and the thalamus. Although wetware brains have the software of intelligence expressed via the hardware, it's possible to implement said software in a different hardware substrate though with contraints. The hierarchical, modular, and ordered nature of wetware brains led to the notions defined below of problem domains, regions and layers. Connecitivty is the major paradigm of a processor graph like a human brain. In our framework, the connectivity patterns of cells are determined by the higher level organizational properties of their containers, with the framework code implementing generic behaviours based upon the organization. In essence, configuration is separate from 

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

Currently, I plan to extend for a subcortical series of problem domains, though it may just be one domain with lots of regions. As well as add a brain stem problem domain
> The issue with single PD subcort is that a single level of a problem domain could actually be multiple regions which breaks the current region paradigm. Does it?

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

- activation_type : controls the type of value returned by the axon
  - -1, 1, or modulatory chemical
- cell_morphology : controls the number of dendrites, and their direction
  - pyramid : 4 adjacent dendrites, a local dendrite, and a long apical dendrite
  - interneruon : apical dendrite
  - ?

> The different supported cell morphologies are still a WIP
> What determines the length of each dendrite?

The two major properties, determine the general other properties of the cell like the plasticity properties, resource constraints, etc... 

## Region Config Files

Since the framework is, for the most part, region, and layer agnostic, the specifics of each region are determined by a configuration yaml which contains all the data needed to initialize the region with all of its layers given the specific input/output constraints of the problem domain object.

- aside from layer data, what other data needs to be stored in a region config?
- Layer Data
  - cell morphology
    - lengths of dendrites?
    - plasticity data (if differs from generic)
    - resource constraints (if differs from generic)
  - connection data
    - types of cells that can project to the destination
    - layer to layer connections within the region
    - substitution spots for cross-PD connections

> Note on Cortex Region: it is perhaps the case that l1-6 naming convention works fine normally, though something more descriptive may be nice

## Destination Keys

The destination of a cells axon can't be absolutely determined before initialization due to the relative nature of the connectivity patterns. Consequently, we need to use keys in the config that are parsed during init, and replaced with the absolute path data. For example, if a layer has cells that project to adjacent columns, we won't know the indices of the adjacent columns until we know the size of the region which is determined during initialization.

> What should be used as the destination between semantically named layers? The order? What about cross-region references?
> The destinations should use the path data schema with appropriate substitution slots, and relative paths

Path Substitutions
Each part of the (what was the purpose of this sentence?)

### Formats of a full path

- [pd_key, region_key, region_loc, layer_key]
- [pd_key, region_key, region_loc, layer_key, cell_index]

### Format of Config

- [activation_key, [pd_key, region_key, region_loc, layer_key]]
- [activation_key, [pd_key, region_key, region_loc, layer_key, cell_index]]

region_loc is either (x, y) or (x, y, z). If layer_key's are enumerable then we can use (x, y, z)
Not all region_locs @ the layer_key will have multiple cell indices. Some layers have a cell at each point instead of an array of cells at each point

### Config Destination Substitutions

Config destinations are patterns that indicate where cells in a layer can project outputs. Substitution keywords are replaced during init with generated info.
Furthermore, each destination applies to one or more activation type of cells. 

- pair : project to mirrored location in the paired problem domain
- same : reuse current path data for the matching level of the new path
- output : substitute output paths for the destination
- "name" : use the name as the key in the path
- none : layer serves as a destination without any cells in the layer
  - in other words, the layer will have dendrites that receive from it but it won't return any outputs
