from AbstractCloudService import AbstractCloudService
from AbstractLocalService import AbstractLocalService

class ConcreteServiceWrapper():
    
    def __init__(self, cloudService: AbstractCloudService, localService: AbstractLocalService):
        self.cloudService = cloudService
        self.localService = localService

    def copyFromCloudToLocal(self, cloudTable, localTable, timestamp):
        data = self.cloudService.read_data(cloudTable, timestamp)
        for d in data:
            self.localService.write_data(localTable, d)

    def getAllData(self, localTable):
        data = self.localService.read_data(localTable, "")
        for d in data:
            print(d)