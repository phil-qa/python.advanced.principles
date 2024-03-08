import platform

class SystemAssetManager:
    @property
    def cpu_type(self):
        return platform.processor()