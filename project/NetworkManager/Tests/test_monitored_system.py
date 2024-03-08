import unittest
from MonitoredSystem import PerformanceMetrics
from PerformanceMonitorSubSystem import *
from SystemAssetManager import *

class PerformanceTests(unittest.TestCase):
    #setup


    def test_performance(self):
        performance = PerformanceMetrics()
        self.assertTrue(performance)
        self.assertIsNotNone(performance.cpu_utilisation, "The cpu utilisation did not initialise")
        self.assertIsNotNone(performance.ram_utilisation, "The ram utilisation did not initialise")

    def test_performance_monitor_subsystem(self):
        performance_monitor = PerformanceMonitorSubsystem()
        self.assertTrue(performance_monitor)
        self.assertIsNotNone(performance_monitor.cpu_utilisation, "The cpu utilisation did not initialise")
        self.assertIsNotNone(performance_monitor.ram_utilisation, "the ram utilisation was not initialised")
        self.assertIsNotNone(performance_monitor.disk_utilisation, "The disk utilisation did not initialise")

    def test_processor_information(self):
        asset_manager = SystemAssetManager()
        self.assertTrue(isinstance(asset_manager.cpu_type,str))
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
