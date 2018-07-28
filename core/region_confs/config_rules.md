this is object type for region configs that is inherited by each type of region
contains all the data needed to initialized a new region for a problem domain given the specific input/output constraints of the PD
    - destination/connection data
        - layer to layer connections
        - substitution spots for cross-PD connections
        - region to regions connections
    - cell types for each layer
    - plasticity data (if differs from generic)
    - resource constraints (if differs from generic)
it is perhaps the case that l1-6 naming convention works fine normally, something more descriptive may be nice
What should be used as the destination between semantically named layers? The order? What about cross-region references?
The destinations should use the path data schema with appropriate substitution slots, and relative paths

Path Substitutions
Each part of the 
Formats of a full path

- [pd_key, region_key, region_loc, layer_key]
- [pd_key, region_key, region_loc, layer_key, cell_index]

Config Destination Substitutions

Config destinations are patterns that indicate where cells in a layer can project outputs. Substitution keywords are replaced during init with generated info.

- same : reuse current path data for the matching level of the new path
- output : substitute output paths for the destination
- "name" : use the name as the key in the path
- none : layer serves as a destination without any cells in the layer
-- in other words, the layer will have dendrites that receive from it but it won't return any outputs

