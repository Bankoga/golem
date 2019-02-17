---
type_data:
  id: POCG
  name: Parts Output Coder Group
  type: coder
stages_to_groups_dict:
  - type_data:
      id: fw_method
      purpose: represents the function used to move data into or out of the matrix
    groups: [motor]
    total_count: 1
group_details:
  - id: motor
    node_details:
      - node_type: function
        func_name: spikes_to_parts
        func_parameters:
          min_num_parts: 3
          min_part_size: 3
          max_num_parts: 3
          max_part_size: 8
    pct_of_stage: 1
inputs: null
outputs: null
hooks_into: null
hooks_outof: null
links_defined: null
links_used: gate_i
...