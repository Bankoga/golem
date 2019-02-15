---
type_data:
  id: PICG
  name: Parts Input Coder Group
  type: coder
stage_to_groups_dict:
  - type_data:
      id: fw_method
      purpose: represents the function used to move data into or out of the matrix
    groups: [sensor]
    total_count: 1
group_details:
  - id: sensor
    node_details:
      - node_type: function
        func_name: parts_to_spikes
        func_parameters:
          min_num_parts: 1
          min_part_size: 1
          max_num_parts: 3
          max_part_size: 8
    pct_of_stage: 1
inputs: null
outputs: null
hooks_into: null
hooks_outof: null
links_defined: null
links_used: null
...