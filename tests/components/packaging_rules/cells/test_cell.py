# import unittest

# from hypothesis import given
# from hypothesis import strategies as st

# from components.packaging_rules.cells.cell import Cell
# from data.axioms.cell_types import CellType,cell_data
# from data.axioms.enums import RuleType, RsrcType, PackType, FieldType

# from utils.helpers.packer import build_address, build_meld, build_datapack

# class TestCell(unittest.TestCase):
#   # def setUp(self):
#   #   self.id = CellType.PYRAMID
#   #   self.cell = Cell(self.id)
#   #   # self.type_data = cell_data[str(self.id)]
  
#   # def test_base(self):
#   #   self.assertEqual(self.cell.type, RuleType.CELL)
#   #   self.assertEqual(self.cell.id, self.id)
  
#   @given(st.sampled_from(CellType))
#   def test_cell_data(self,inp_id):
#     """
#     here we test that every cell type we have defined, has all of its properties
#     """
#     cell = Cell(inp_id)
#     if (not inp_id in CellType) or inp_id == CellType.UNSET:
#       type_data = cell_data[str(CellType.PYRAMID)]
#       self.assertEqual(cell.id, CellType.PYRAMID)
#     else:
#       type_data = cell_data[str(inp_id)]
#       self.assertEqual(cell.id, inp_id)

#     self.assertEqual(cell.type, RuleType.CELL)
#     self.assertEqual(cell.cnv_tmplts, type_data['cnv_tmplts'])
#     self.assertEqual(cell.freq_range, type_data['freq_range'])
#     self.assertEqual(cell.init_freq, type_data['init_freq'])
#     self.assertEqual(cell.pct_of_pod, type_data['pct_of_pod'])
#     self.assertEqual(cell.init_threshhold, type_data['init_threshhold'])
#     self.assertEqual(cell.activation_function, type_data['activation_function'])
  
#   @given()
#   def test_pack(self,inputs):
#     """
#     but I need a guaranteed order to some of the inputs don't I?
#     Why? Bc agg type datapacks get combined in a spatially oriented way
#     Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
#     Given that each sender has a position, this can be added to the datapack along with sender address (or in place of?)
#     Given that we are sent inputs
#     When we prepare to evaluate them
#     Then we sort them using a guaranteed sort by pos first!

#     Where does this sort live? In utils.helpers.pos_help?

#     Specifiying inputs for testing datapacks, and things that rely on them is growing more complex
#     At this point, I think it makes the most sense to begin work on a datapack series of custom hypothesis strategies

#     aggregate datapacks can't exist or not exist as they please
#     they must always exist in the correct order to be processed
#     Thus we assume that an order id list or dict has been generated which we can compare against
#     """
#     # build a
#     st.lists(st.builds(build_datapack, st.sampled_from(['SenderModuleId','self','Self']),
#         st.sampled_from(['sender_group_id','self','Self', '']),
#         st.sampled_from(RsrcType),
#         st.sampled_from(PackType),
#         st.sampled_from(FieldType),
#         st.sampled_from(['SenderModuleId','self','Self']),
#         st.sampled_from(['sender_group_id','self','Self',''])))
#     pass

# if __name__ == '__main__':
#   unittest.main()