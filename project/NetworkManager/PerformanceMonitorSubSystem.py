import psutil

class PerformanceMonitorSubsystem:
    @property
    def cpu_utilisation(self, inter=1):
        return psutil.cpu_times_percent(interval=inter)

    @property
    def ram_utilisation(self):
        return psutil.virtual_memory()

    @property
    def disk_utilisation(self, path=r'/'):
        return psutil.disk_usage(path)



