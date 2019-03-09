# Type Keys

> Purpose: To serve as the index of all types used for golem architecture creation

## Index

- Hook Types: ?
- Proc Types: ?
- Procs: ?
- Golem Type:?
- Matrix Type: ?
- Directions: The list of reading, or projection directions available in node design.
- Dimensions: The list of dimensions that are part of a processing groups location within the matrix. The dimensionality of a func set in a module is part of it's I/O shape.

## Dimensions

Paired items are simply sign flipped in terms of position or use a paired dictionary key keeping the same position data

| Key | Range | Definition | Pattern | Purpose |
| --- | --- | --- | --- | --- |
| Section||S | [cellar=0,basement=1,archive=2,main=3,attic=4] | f'{package_map[package_id]}.{indexof(pipeline_id,pipeline_map)}' | cellar,basement,archive,main,attic | allows us to have overlapping package modules which is really useful for some mappings |
| Room||X | 0-len of all packages on floor | package_modules[module_id].index | int | To represent the length of the package in terms of num modules |
| Room||Y | 0-max num groups in a module across all packages on floor | package_modules[module_id].group | int | To represent the width of each module in terms of number of groups |
| Floor||Z | 0-N | group order | int | To represent how groups are locally distributed in terms of stage height/cardinality |

## Directions

| Key | Pattern | Dimension Change | Purpose |
| --- | --- | --- | --- | --- |
| A | --- | --- | Z+ | Addressing things above |
| B | --- | --- | Z- | Addressing things below |
| N | --- | --- | --- | --- |
| E | --- | --- | --- | --- |
| S | --- | --- | --- | --- |
| W | --- | --- | --- | --- |
| P | --- | --- | --- | Addressing paired things |

## Hook Types

Currently used to indicate which package rule is used and which direction the package is going.

*_to: id for the package aggregation rule used when consuming the package associated with the prefix
*_from: id for the package generation rule used to when building the package associated with the prefix