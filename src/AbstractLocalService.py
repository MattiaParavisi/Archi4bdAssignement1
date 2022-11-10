from abc import ABC, abstractmethod

class AbstractLocalService(ABC):

    @abstractmethod
    def connect(self, url):
        pass

    @abstractmethod
    def read_data(self, table, timestamp):
        pass

    @abstractmethod
    def write_data(self, table, data):
        pass