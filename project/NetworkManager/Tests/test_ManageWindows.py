import unittest

import ManageWindows
from ManageWindows import *

class TestingWindows(unittest.TestCase):
    def test_wmi_reports(self):
        manager = ManageWindows()
        self.assertIsNotNone(manager)

    def test_system_ram_is_reported(self):
        asset_manager = ManageWindows()
        self.assertTrue(isinstance(asset_manager.ram_information, dict))

    def test_cpu_reported(self):
        asset_manager = ManageWindows()


if __name__ == '__main__':
    unittest.main()
