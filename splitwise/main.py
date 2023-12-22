from controllers.bill_controller import BillController
from controllers.group_controller import GroupController
from controllers.user_controller import UserController
from services.bill_service import BillService
from services.user_service import UserService
from services.group_service import GroupService


userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser("1", "one")
user2 = userController.addUser("2", "two")
user3 = userController.addUser("3", "three")
user4 = userController.addUser("4", "four")
user5 = userController.addUser("5", "five")
members = [user1, user2, user3, user4, user5]
group1 = groupController.addGroup("1", "avengers", [])
paidBy = {"1": 200, "2": 100, "3": 50, "4": 50, "5": 100}
contribution = {"1": 100, "2": 100, "3": 100, "4": 100, "5": 100}
bill = billController.addBill("11", "1", 500, contribution, paidBy)
for member in members:
    userId = member.getUserId()
    print(f"{userId}: {billController.getUserBalance(userId)}")
