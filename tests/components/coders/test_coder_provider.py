# import unittest
# from hypothesis import given
# import hypothesis.strategies as st
# from data.axioms.configs import sensor_ids
# from components.sensors.sensor_provider import sensor_services

# class TestSensorProvider(unittest.TestCase):

#   @given(st.sampled_from(sorted(sensor_ids.keys())))
#   def test_get(self, sensor_id):
#     sensor = sensor_services.get(sensor_ids[sensor_id], **{})
#     self.assertTrue(sensor.get_id(), sensor_ids[sensor_id])

# if __name__ == '__main__':
#     unittest.main()