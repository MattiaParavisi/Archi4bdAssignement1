from abc import ABC, abstractmethod

class AbstractCloudService(ABC):

    @abstractmethod
    def connect(self, connString):
        pass

    @abstractmethod
    def read_data(self, table, timestamp):
        pass
        