import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.sensors.sensor_provider import sensor_services
from data.axioms.configs import file_type, sensor_ids
from tests.components.sensors.test_sensor import TestSensor
from utils.config_reader import read

class TestPartsSensor(TestSensor):

  def setUp(self):
    self.sensor_id = sensor_ids['ps']
    self.sensor =  sensor_services.get(self.sensor_id, **{})
    self.sensor_conf = read(self.sensor_id,file_type['sensor'])
  
if __name__ == '__main__':
  unittest.main()