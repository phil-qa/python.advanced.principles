import unittest
from MonitoredSystem import PerformanceMetrics
from PerformanceMonitorSubSystem import *
from SystemAssetManager import *


class assetMangertests(unittest.TestCase):
    '''
    Tests for the asset management module
    '''

    def test_os_platform_is_reported(self):
        asset_manager = SystemAssetManager()
        cpu_type = asset_manager.cpu_type
        self.assertTrue(isinstance(cpu_type, str))

    def test_os_system_reports(self):
        asset_manager = SystemAssetManager()
        operating_system = asset_manager.operating_system
        self.assertTrue('Linux' in operating_system or 'Windows' in operating_system or "Darwin" in operating_system)

    def test_os_version_reports(self):
        asset_manager = SystemAssetManager()
        release_version = asset_manager.release_version
        self.assertTrue(release_version)

    def test_ram_type_reported(self):
        asset_manager = SystemAssetManager()
        ram_type = asset_manager.ram_type
        self.assertTrue(isinstance(ram_type, int))

    def test_ram_capacity_reported(self):
        asset_manager = SystemAssetManager()
        ram_capacity = asset_manager.ram_size
        self.assertTrue(ram_capacity > 0)

    def test_ram_speed_reported(self):
        asset_manager = SystemAssetManager()
        ram_speed = asset_manager.ram_speed
        self.assertTrue(ram_speed > 0)



    if __name__ == '__main__':
        unittest.main()