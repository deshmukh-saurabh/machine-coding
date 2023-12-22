from services.board_service import BoardService
from services.card_service import CardService
from services.list_service import ListService
from services.user_service import UserService
from models.privacy import Privacy

# create users
us = UserService()
u1 = us.create_user("John", "john@abc.com")
u2 = us.create_user("Smith", "smith@abc.com")
u3 = us.create_user("Ally", "ally@abc.com")
u4 = us.create_user("Joe", "joe@abc.com")
print(f"Users:\n {us.get_all_users()}\n")

# create cards, assign these to users
cs = CardService()
c1 = cs.create_card("Setup Github repo", "Setup project boilerplate", u1)
c2 = cs.create_card("Setup initial schema", "Add initial DB schema", u2)
c3 = cs.create_card("Add CI/CD pipelines", "Setup project CI/CD", u3)
print(f"Cards:\n {cs.get_all_cards()}\n")

# create lists, add cards to it
ls = ListService()
l1 = ls.create_list("TODO")
ls.add_card(l1.get_id(), c3)
l2 = ls.create_list("In progress")
ls.add_card(l2.get_id(), c2)
l3 = ls.create_list("Done")
ls.add_card(l3.get_id(), c1)
print(f"lists:\n {ls.get_all_lists()}\n")

# create board, add lists to it
bs = BoardService()
b1 = bs.create_board("New project", Privacy.PUBLIC)
bs.add_list(b1.get_id(), l1)
bs.add_list(b1.get_id(), l2)
bs.add_list(b1.get_id(), l3)
print(f"Boards:\n {bs.get_all_boards()}\n")
