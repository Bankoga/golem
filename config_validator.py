class ConfigValidator():
  """
  Responsible for validating an architecture after all of the configs have been successfully loaded
  Occurs before evaluation
  And is separate from evaluation for strictness, and completeness.
  """
Individual Properties to Validate before an architectures config can be loaded
---
Name
LayerRules
LayersDetails
Purpose
Pipeline
InputMelds
Generated Shapes
OutputMelds
Links
Function
Links it defines
Channels
...

    VALID_NAME_CHARS = ascii_lowercase + '_-.'
    
    def valid_name():
        return st.text(alphabet=letters, min_size=1, max_size=112).map(lambda t: t.lower()) | st.just("master")

  def validate_layer_rule():
  def validate_layer_details():
    valid