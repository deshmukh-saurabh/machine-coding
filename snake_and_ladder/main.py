from models.board import Board
from models.snake import Snake
from models.ladder import Ladder
from models.player import Player
from services.snake_and_ladder_service import SnakeAndLadderService

# create snake objects
s1 = Snake(23, 11)
s2 = Snake(34, 20)
s3 = Snake(15, 6)
s4 = Snake(18, 3)

# create ladder objects
l1 = Ladder(14, 36)
l2 = Ladder(10, 19)
l3 = Ladder(21, 26)

# create player objects
p1 = Player("1", "P1")
p2 = Player("2", "P2")
p3 = Player("3", "P3")
p4 = Player("4", "P4")
p5 = Player("5", "P5")
p6 = Player("6", "P6")

# start game
sns = SnakeAndLadderService(size=50)
sns.init_snake_data([s1, s2, s3, s4])
sns.init_ladder_data([l1, l2, l3])
sns.init_player_data([p1, p2, p3, p4, p5, p6])
sns.start_game()
