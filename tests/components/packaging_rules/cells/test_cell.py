import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packaging_rules.cells.cell import Cell
from data.axioms.cell_types import CellType,cell_data
from data.axioms.enums import RuleType, RsrcType, PackType, FieldType

from utils.helpers.packer import build_address, build_meld, build_datapack

class TestCell(unittest.TestCase):
  # def setUp(self):
  #   self.id = CellType.PYRAMID
  #   self.cell = Cell(self.id)
  #   # self.type_data = cell_data[str(self.id)]
  
  # def test_base(self):
  #   self.assertEqual(self.cell.type, RuleType.CELL)
  #   self.assertEqual(self.cell.id, self.id)
  
  @given(st.sampled_from(CellType))
  def test_cell_data(self,inp_id):
    """
    here we test that every cell type we have defined, has all of its properties
    """
    cell = Cell(inp_id)
    if (not inp_id in CellType) or inp_id == CellType.UNSET:
      type_data = cell_data[str(CellType.PYRAMID)]
      self.assertEqual(cell.id, CellType.PYRAMID)
    else:
      type_data = cell_data[str(inp_id)]
      self.assertEqual(cell.id, inp_id)

    self.assertEqual(cell.type, RuleType.CELL)
    self.assertEqual(cell.cnv_tmplts, type_data['cnv_tmplts'])
    self.assertEqual(cell.freq_range, type_data['freq_range'])
    self.assertEqual(cell.init_freq, type_data['init_freq'])
    self.assertEqual(cell.pct_of_pod, type_data['pct_of_pod'])
    self.assertEqual(cell.init_threshhold, type_data['init_threshhold'])
    self.assertEqual(cell.activation_function, type_data['activation_function'])
  
  # @given()
  # def test_pack(self,inputs):
  #   """
  #  packing may be done in func groups
  #   but I need a guaranteed order to some of the inputs don't I?
  #   Why? Bc agg type datapacks get combined in a spatially oriented way
  #   Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
  #   Given that each sender has a position, this can be added to the datapack along with sender address (or in place of?)
  #   Given that we are sent inputs
  #   When we prepare to evaluate them
  #   Then we sort them using a guaranteed sort by pos first!

  #   Where does this sort live? In utils.helpers.pos_help?

  #   Specifiying inputs for testing datapacks, and things that rely on them is growing more complex
  #   At this point, I think it makes the most sense to begin work on a datapack series of custom hypothesis strategies

  #   aggregate datapacks can't exist or not exist as they please
  #   they must always exist in the correct order to be processed
  #   Thus we assume that an order id list or dict has been generated which we can compare against
  #   """
  #   # build a
  #   st.lists(st.builds(build_datapack, st.sampled_from(['SenderModuleId','self','Self']),
  #       st.sampled_from(['sender_group_id','self','Self', '']),
  #       st.sampled_from(RsrcType),
  #       st.sampled_from(PackType),
  #       st.sampled_from(FieldType),
  #       st.sampled_from(['SenderModuleId','self','Self']),
  #       st.sampled_from(['sender_group_id','self','Self',''])))
  #   pass


  """
  What happens before a localized conv
   patch = we extract a part of the shape
    - How do we select which part of the shape to process?
  """
  def test_localized_conv(self, patch):
    """
    What happens during a localized convolution?
    - active_connect = get_random_fill_from(base_weights,mod_weights, other_mods) which incorps the * can_be_active_now
    - acutal_inputs = patch * active_connect
        the patch is where we can leverage resources from
        each resource index, has an independent % chance of being activated though
        thus, we must calc the inputs to be used this timestep before doing anything
    - 
    total_compute_per_simulated_ts = avg_latency_per_simulated_ts + avg_compute_per_simulated_ts
    simulated_fps = num_ts_per_simulated_sec + total_compute_per_simulated_ts
    there is going to be a slew of timestep logic that spans many components
    Not sure as to what needs to be abstracted though
    """
    pass
  
  def test_get_activity_data(self, inputs, timestep):
    """
    each nearby cell, has a % chance of raising the current cells activation probability
    chance = Input_Strength - Distance_factor
    """
    pass

  def test_process(self):
    pass
  # def test_get_random_fill_from(self):

  def test_setup_convs(self):
    pass

if __name__ == '__main__':
  unittest.main()