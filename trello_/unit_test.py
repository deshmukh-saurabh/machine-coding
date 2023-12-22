import unittest
from services.board_service import BoardService
from services.user_service import UserService
from services.card_service import CardService
from models.privacy import Privacy


class TrelloTest(unittest.TestCase):
    def test_add_board(self):
        bs = BoardService()
        name = "New project"
        privacy = Privacy.PUBLIC
        b1 = bs.create_board(name, privacy)
        self.assertEqual(b1.get_name(), name)
        self.assertEqual(b1.get_privacy(), privacy)

    def add_user(self):
        us = UserService()
        name = "John"
        email = "john@abc.com"
        u1 = us.create_user(name, email)
        return u1, name, email

    def test_add_user(self):
        u1, name, email = self.add_user()
        self.assertEqual(u1.get_name(), name)
        self.assertEqual(u1.get_email(), email)

    def test_add_card(self):
        cs = CardService()
        title = "Setup Github repo"
        description = "Setup project boilerplate"
        u1, name, email = self.add_user()
        c1 = cs.create_card(title, description, u1)
        self.assertEqual(c1.get_title(), title)
        self.assertEqual(c1.get_description(), description)


if __name__ == "__main__":
    unittest.main()
