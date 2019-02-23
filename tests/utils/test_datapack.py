import unittest

from hypothesis import given
import hypothesis.strategies as st

from utils.datapack import Datapack

from utils.helpers.address_help import build_address, build_meld, build_datapack_inputs, build_datapack
from data.axioms.configs import dest_key_pattern
from data.axioms.enums import PackType,RsrcType,FieldType

class TestDataPack(unittest.TestCase):

  def _read_data_(self, meld,sender_address):
    datp=Datapack(meld,sender_address)
    datp.read_data()
    meld_tuple = meld.split(';')
    self.assertTrue(datp.address==meld_tuple[0])
    if len(meld_tuple)>1 and meld_tuple[1]:
      self.assertTrue(datp.resource == RsrcType.UNSET or datp.resource==RsrcType(meld_tuple[1]))
    else:
      self.assertTrue(datp.resource == RsrcType.UNSET)
    if len(meld_tuple)>2 and meld_tuple[2]:
      self.assertTrue(datp.type == PackType.UNSET or datp.type==PackType(meld_tuple[2]))
    else:
      self.assertTrue(datp.type == PackType.UNSET)
    if len(meld_tuple)>3 and meld_tuple[3]:
      self.assertTrue(datp.shape == FieldType.UNSET or datp.shape==meld_tuple[3])
    else:
      self.assertTrue(datp.shape == FieldType.UNSET)

  # def setUp(self):
    # In order to test all the variants for the integration, we will need BDD tests
    addr = build_address('GLG','noise_from')
    # self._read_data_(inputs[0],inputs[1])

  @given(st.tuples(st.from_regex(dest_key_pattern),st.text(),st.text()), st.from_regex(dest_key_pattern))
  def test_read_data(self,meld_tuple,sender_address):
    meld = ";".join(meld_tuple)
    datp=Datapack(meld,sender_address)
    datp.read_data()
    meld_tuple = meld.split(';')
    self.assertTrue(datp.address==meld_tuple[0])
    
    if len(meld_tuple)>1 and meld_tuple[1]:
      self.assertTrue(datp.resource == RsrcType.UNSET or datp.resource==RsrcType(meld_tuple[1]))
    else:
      self.assertTrue(datp.resource == RsrcType.UNSET)
    if len(meld_tuple)>2 and meld_tuple[2]:
      self.assertTrue(datp.type == PackType.UNSET or datp.type==PackType(meld_tuple[2]))
    else:
      self.assertTrue(datp.type == PackType.UNSET)
    if len(meld_tuple)>3 and meld_tuple[3]:
      self.assertTrue(datp.shape == FieldType.UNSET or datp.shape==meld_tuple[3])
    else:
      self.assertTrue(datp.shape == FieldType.UNSET)

  """
  There are N cases of address description for datapacks
  These descriptions come from the outputs and hooks properties of the configs
  we send a msg to a set of groups (affects whatever reads module context for data)
  we send a msg to an individual group (which forces it to read the data according to packtype)
  we send a msg to our own module
  We send a msg to a group we know of
  we send a new msg to a link
  we send a copy of another msg we sent to a link
  CURRENTLY NO LINK CASES ARE TESTED!
  ['SenderModuleId','','RecipientModuleId',''],
    ['SenderModuleId','noise_from','RecipientModuleId',''],
    ['SenderModuleId','sender_group_id','RecipientModuleId',''],
    ['SenderModuleId','','RecipientModuleId','recipient_group_id'],
    ['SenderModuleId','sender_group_id','RecipientModuleId','recipient_group_id'],
    ['self','','self',''],
    ['SenderModuleId','noise_from','RecipientModuleId',''],
    ['SenderModuleId','sender_group_id','RecipientModuleId',''],
    ['SenderModuleId','','RecipientModuleId','recipient_group_id'],
    ['SenderModuleId','sender_group_id','RecipientModuleId','recipient_group_id']
  """
  @given(st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_group_id','self','Self', '']),
  st.sampled_from(RsrcType),
  st.sampled_from(PackType),
  st.sampled_from(FieldType),
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_group_id','self','Self','']))
  def test_sampled_msg_read(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
    inputs = build_datapack_inputs(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
    self._read_data_(inputs[0],inputs[1])

  @given(st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_group_id','self','Self', '']),
  st.sampled_from(RsrcType),
  st.sampled_from(PackType),
  st.sampled_from(FieldType),
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_group_id','self','Self','']))
  def test_compare_equal_datapacks(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
    datp1 = build_datapack(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
    datp2 = build_datapack(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
    self.assertEqual(datp1,datp2)

  # def test_format_address_on_valid_data(self):
  #   # self.assertTrue(self.datp.address, 'glg-destination_id-subdestination_id')

  # def test_format_address_on_well_formed_invalid_data(self):
  #   pass

  # def test_format_address_on_random_data(self):
  #   pass

if __name__ == '__main__':
    unittest.main()