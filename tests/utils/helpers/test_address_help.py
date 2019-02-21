import unittest

from hypothesis import given
from hypothesis import strategies as st
from data.axioms.enums import FieldType,PackType,RsrcType
from utils.helpers.address_help import build_address, build_meld

class TestAddressHelp(unittest.TestCase):
  @given(st.text(),st.text())
  def test_build_address(self, m_id, g_id):
    addr = build_address(m_id, g_id)
    if g_id is None:
      self.assertEqual(addr, f'{m_id}')
    else:
      self.assertEqual(addr, f'{m_id}-{g_id}')

  @given(st.text(),st.text(),st.sampled_from(RsrcType),st.sampled_from(PackType),st.sampled_from(FieldType))
  def test_build_meld(self, rm_id,rg_id,dp_resource,dp_type,dp_shape):
    addr = build_address(rm_id,rg_id)
    meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
    if dp_shape is None:
      self.assertEqual(meld, f'{addr}:{dp_resource}:{dp_type}')
    else:
      self.assertEqual(meld, f'{addr}:{dp_resource}:{dp_type}:{dp_shape}')