# Config File Properties

## Brains

```yaml
---
key: NULL
nodes:
  - key: NULL
    type: encoder|decoder|
    controller: images|NULL
    outputs:
      - key of problem domain
...
```

## Problem Domain Types

```yaml
---
key: NULL
inputs: [region_key, region_key]
regions:
  - key: region_key
    type: region_type
    stitch_type: NULL
...
```

## Regions

```yaml
---
key: cortex
inputs: [layer_key, layer_key]
stitch_type: NULL
fill_props:
  order: ascending|descending|random|manual(explicit)
  pattern: row|column|square|etc
  density|saturation: full, min_ratio(2:2 etc), repeat_n_times, random
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
      - SEE_CELL_TYPES_PROPS
...
```

## Cell Types

```yaml
---
pct: 1
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