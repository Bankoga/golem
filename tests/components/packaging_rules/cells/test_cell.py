import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packaging_rules.cells.cell import Cell
from data.axioms.cell_types import CellType,cell_data
from data.axioms.enums import RuleType

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
    # self.assertEqual(cell, type_data[])


if __name__ == '__main__':
  unittest.main()