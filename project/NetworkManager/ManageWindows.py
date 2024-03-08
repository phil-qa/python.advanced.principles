import subprocess
import platform
import wmi
class ManageWindows:
    '''
    This is a class that manages windows specific operations
    Methods
    ram_infortmation() uses wmi to get ram information returns set data
    '''
    def run_command(command):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()

    @property
    def ram_information(self):
        scan_result = wmi.WMI()
        ram_info = {}
        for mem in scan_result.Win32_PhysicalMemory():
            ram_info['capacity'] = int(mem.Capacity)
            ram_info["type"] = mem.MemoryType
            ram_info['speed'] = mem.Speed
        return ram_info
