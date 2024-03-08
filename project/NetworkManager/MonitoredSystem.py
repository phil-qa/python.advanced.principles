import psutil
class PerformanceMetrics:
    def __init__(self):
        self.cpu_utilisation = None
        self.ram_utilisation = None
        self.Disk_utilisation = None
        self.update()

    def update(self):
        self._update_cpu()
        self._update_ram()

    def _update_cpu(self):
        self.cpu_utilisation = psutil.cpu_times_percent(interval=1)

    def _update_ram(self):
        self.ram_utilisation = psutil.virtual_memory()