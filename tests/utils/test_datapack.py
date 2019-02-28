import unittest

from hypothesis import given
import hypothesis.strategies as st

from tests.strategies.packing_strats import datapack_inputs, datapack_arbitrary,datapack_address,valid_resource_data,valid_datapack_arbitrary

from utils.datapack import Datapack
from utils.helpers.packer import build_address, build_meld, build_datapack_inputs, build_datapack
from data.axioms.configs import dest_key_pattern
from data.enums.prop_types import PackType,RsrcType,FieldType

from numpy import array_equal

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
    self.var = None

  # def setUp(self):
    # In order to test all the variants for the integration, we will need BDD tests
    # addr = build_address('GLG','noise_from')
    # self._read_data_(inputs[0],inputs[1])

  @given(datapack_inputs()) # pylint: disable=no-value-for-parameter
  def test_read_data(self,inputs):#meld_tuple,sender_address):
    # st.tuples(st.from_regex(dest_key_pattern),st.text(),st.text()), st.from_regex(dest_key_pattern)
    meld = inputs[0]
    sender_address = inputs[1]
    # meld = ";".join(meld_tuple)
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
  @given(datapack_inputs()) # pylint: disable=no-value-for-parameter
  def test_sampled_msg_read(self, inputs):
    self._read_data_(inputs[0],inputs[1])

  @given(datapack_inputs()) # pylint: disable=no-value-for-parameter
  def test_compare_equal_datapacks(self, inputs):
    datp1 = Datapack(inputs[0],inputs[1])
    datp2 = Datapack(inputs[0],inputs[1])
    self.assertEqual(datp1,datp2)

  
  @given(datapack_arbitrary()) # pylint: disable=no-value-for-parameter
  def test_unbuilt(self, input_pack):
    self.assertFalse(input_pack.is_built())
    with self.assertRaises(RuntimeError):
      input_pack.process()

  @given(datapack_arbitrary(), valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_build(self, input_pack, data):
    self.assertFalse(input_pack.is_built())
    input_pack.build(data)
    self.assertTrue(input_pack.is_built())
    self.assertTrue(array_equal(input_pack.var, data))
    input_pack.process()

  @given(datapack_arbitrary()) # pylint: disable=no-value-for-parameter
  def test_get_meld(self,input_pack):
    meld = f'{input_pack.sender};{input_pack.address};{input_pack.resource};{input_pack.type};{input_pack.shape}'
    self.assertEqual(input_pack.get_meld(),meld)

  @given(valid_datapack_arbitrary(), datapack_address()) # pylint: disable=no-value-for-parameter
  def test_update_address(self,input_pack, new_addr):
    input_pack.update(new_addr)
    self.assertEqual(input_pack.address, new_addr)
    self.assertFalse(input_pack.is_built())
    self.assertIsNone(input_pack.var)

  # def test_format_address_on_valid_data(self):
  #   # self.assertTrue(self.datp.address, 'glg-destination_id-subdestination_id')

  # def test_format_address_on_well_formed_invalid_data(self):
  #   pass

  # def test_format_address_on_random_data(self):
  #   pass

if __name__ == '__main__':
    unittest.main()