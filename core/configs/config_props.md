# Config File Properties

## Brains

```yaml
---
key: NULL
decoders:
  - name: NULL
    type: image|text_stream|character|keyboard_stream|mouse_stream|NULL
    size: NULL
    output_dest: filename|directory|NULL
encoders:
  - key: NULL
    type: image|video|audio|NULL
    size:
      length: NULL
      width: NULL
      num_channels: NULL
    input_source: NULL
    outputs: [pd_key]
general:
  - key: NULL
    type: NULL
    outputs: [NULL]
...
```

## Problem Domain Types

Decoders, and Encoders are handled via code. They do not have config type files. General, or internal, problem domains have config files which specify crucial information.

### General

```yaml
---
key: NULL
size: NULL
inputs: [region_key, region_key]
regions:
  - key: region_key
    type: region_type
    stitch_type: NULL
...
```

> **Currently, stitch type, fill, and pairing config details are still up in the air!**

## Regions

```yaml
---
key: cortex
inputs: [layer_key, layer_key]
stitch_type: NULL
in_fill_props:
  order: ascending|descending|random|manual(explicit)
  pattern: row|column|square|etc
  density|saturation: full|min_ratio(1:1 etc)|repeat_n_times|random
out_fill_props:
  order: ascending|descending|random|manual(explicit)
  pattern: row|column|square|etc
  density|saturation: full|min_ratio(1:1 etc)|repeat_n_times|random
pairing_props:
  type: solo|shared
  personality: distinct|overlap
input_shapes:
  key:
    dendrites:
      - spread:
        directions: []
      - spread:
        directions: []
layers:
  - SEE_LAYERS_PROPS
...
```

## Layers

```yaml
---
key: one
point_size: n >= 0
cell_types:
  - key: NULL
    type: SEE_CELL_TYPES_PROPS
    pct: n where 0 < n <= 1 && all pct in layer sum to 1
...
```

## Cell Types

```yaml
---
key: NULL
act_type: NULL
dendrites:
  - shape: NULL
    len: 5
  - spread: NULL
    directions: []
    len: NULL
destinations: [NULL]
primary_source: NULL
...
```