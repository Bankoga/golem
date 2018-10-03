# Config File Properties

## Brains

```yaml
---
key: NULL
decoders:
  - name: NULL
    type: image | text_stream | character | keyboard_stream | mouse_stream | NULL
    size: NULL
    output_dest: filename | directory | NULL
encoders:
  - key: NULL
    type: image | video | audio | NULL
    size: NULL
    input_source: NULL
    outputs: [pd_key]
general:
  - key: NULL
    type: NULL
    outputs: [NULL]
...
```

### Size Objects

Descriptions/examples of the different size objects for each decoder & encoder type
image
length: NULL
width: NULL
num_channels: NULL

## Problem Domain Types

Decoders, and Encoders are handled via code. They do not have config type files. General, or internal, problem domain types have config files which specify crucial information. TODO: ADD MORE EXPLANATION!

### General

```yaml
---
key: NULL
size: NULL
input_layers: [region_key, region_key]
regions:
  - key: region_key
    type: region_type
    stitch_type: NULL
...
```

PDs determine fill boundaries of output shape for Regions, and Layers
Regions determine fill rules for between its Layers
Layers determine how to fill the output shape via their config
Destinations use the map to build axons & dendrites

> **Currently, stitch type, fill, and pairing config details are still up in the air!**

## Regions

```yaml
---
type: cortex
input_layers: [layer_key, layer_key]
stitch_type: NULL
in_fill_props:
  order: ascending | descending | random | manual(explicit)
  pattern: row | column | square | etc
  density|saturation: full | min_ratio(1:1 etc) | repeat_n_times | random
out_fill_props:
  order: ascending | descending | random | manual(explicit)
  pattern: row | column | square | etc
  density|saturation: full | min_ratio(1:1 etc) | repeat_n_times | random
pairing_props:
  type: solo | shared
  personality: distinct | overlap
input_shapes:
  shape_name (like pyramid):
    dendrites: SEE_CELL_TYPES_PROPS
layers:
  - SEE_LAYERS_PROPS
...
```

## Layers

```yaml
---
key: one
point_size: f(n) = (int(n) >= 0)
cell_types:
  - key: NULL (this does not seem a necessary prop to have for cell types in a layer)
    type: SEE_CELL_TYPES_PROPS
    pct: f(n) = (0 < n <= 1 && all pct in layer sum to 1)
    len: overrides default type length
...
```

per output location fill (i.e. per cell type)
per layer output fill
per region output fill

## Cell Types

```yaml
---
key: NULL
activation_type|behavior|?:
  type: direct
  effect:
    value: f(n) = +1|-1
  type: meta
  effect:
    property: name of property affected
    selector: query to choose which cells are effected
    value: strength of the effect
axon:
  core_targets: []
  spread: none | LxW | NULL
dendrites:
  - shape: predefined_input_shapes_key
    len: f(n) = (int(n) >= 0)
  - spread: cone|line|tree|NULL
    directions: [Cardinals[N|S|E|W|NW|SW|NE|SE] | Levels[A(bove)|B(elow)] | Combos[AxCardinal|BxCardinal] | R(epeat)]
    len: f(n) = (int(n) >= 0)
  - NULL
primary_sources: [NULL]
...
```