from abc import ABC, abstractmethod

class OsInfo(ABC):
    @abstractmethod
    def get_cpu(self):
        pass

    @abstractmethod
    def get_memory(self):
        pass