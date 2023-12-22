from services.store_service import StoreService
from controllers.store_controller import StoreController


storeController = StoreController(StoreService())
obj1 = {"sde_bootcamp": {"title": "SDE-Bootcamp", "price": 30000.00, "enrolled": False, "estimated_time": 30}}
storeController.addStoreObject(obj1)
print(storeController.getValue("sde_kickstart"))
print(storeController.getValue("sde_bootcamp"))
print(storeController.getStoreKeys())
obj2 = {"sde_kickstart": {"title": "SDE-Kickstart", "price": 4000.00, "enrolled": False, "estimated_time": 5}}
storeController.addStoreObject(obj2)
print(storeController.getValue("sde_kickstart"))
print(storeController.getValue("sde_bootcamp"))
print(storeController.getStoreKeys())
print(storeController.searchStore("price", 30000.00))
print(storeController.searchStore("enrolled", False))
storeController.deleteStoreObject("sde_kickstart")
print(storeController.getStoreKeys())
print(storeController.getValue("sde_kickstart"))
print(storeController.getValue("sde_bootcamp"))
