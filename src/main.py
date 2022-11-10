from ConcreteLocalService import ConcreteLocalService
from ConcreteCloudService import ConcreteCloudService
from ConcreteServiceWrapper import ConcreteServiceWrapper

cloudService = ConcreteCloudService()
cloudService.connect("mysql://root:password@127.0.0.1:3306/public")
print("CloudService connected")

localService = ConcreteLocalService()
localService.connect("mysql://root:password@127.0.0.1:3306/public")
print("LocalService connected")

concreteServiceWrapper = ConcreteServiceWrapper(cloudService, localService)

concreteServiceWrapper.copyFromCloudToLocal("prova", "prova2", ("timestamp", ">", "2022-11-10 09:55:45"))
concreteServiceWrapper.getAllData("prova2")
