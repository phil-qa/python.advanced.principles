import platform
import subprocess

from ManageWindows import ManageWindows


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


class SystemAssetManager:
    def __init__(self):
        self.os_interface = ManageWindows()

    @property
    def cpu_type(self):
        return platform.processor()


    @property
    def operating_system(self):
        return platform.system()


    @property
    def release_version(self):
        return platform.version()

    @property
    def ram_type(self):
        return self.os_interface.ram_information['type']

    @property
    def ram_size(self):
        return self.os_interface.ram_information['capacity']

    @property
    def ram_speed(self):
        return self.os_interface.ram_information['speed']