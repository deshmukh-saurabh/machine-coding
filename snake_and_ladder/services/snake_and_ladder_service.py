from models.board import Board
from services.dice_service import DiceService


class SnakeAndLadderService(object):
    def __init__(self, size=100):
        self.board = Board(size)

    def init_snake_data(self, snakes):
        self.board.set_snakes(snakes)

    def init_ladder_data(self, ladders):
        self.board.set_ladders(ladders)

    def init_player_data(self, players):
        self.player_queue = []
        self.initial_number_of_players = len(players)
        player_positions = {}
        for player in players:
            self.player_queue.append(player)
            player_positions[player.get_id()] = 0
        self.board.set_player_positions(player_positions)

    def get_value_after_dice_roll(self):
        return DiceService().roll()

    def game_completed(self):
        return len(self.player_queue) < self.initial_number_of_players

    def get_new_pos(self, player, pos):
        print(f"{player.get_name()} at pos: {pos}")
        while True:
            for ladder in self.board.get_ladders():
                if ladder.get_start() == pos:
                    pos = ladder.get_end()
                    print(f"{player.get_name()} moved up to {pos} using ladder.")
                    continue

            for snake in self.board.get_snakes():
                if snake.get_start() == pos:
                    pos = snake.get_end()
                    print(f"{player.get_name()} brought down to {pos} by snake!")
                    continue
            break
        return pos

    def move_player(self, player, dice_val):
        old_pos = self.board.get_player_positions().get(player.get_id())
        new_pos = old_pos + dice_val
        if new_pos > self.board.get_size():
            new_pos = old_pos
        else:
            new_pos = self.get_new_pos(player, new_pos)
        self.board.get_player_positions()[player.get_id()] = new_pos

    def has_won_game(self, player):
        return self.board.get_player_positions().get(player.get_id()) == self.board.get_size()

    def start_game(self):
        while not self.game_completed():
            player = self.player_queue.pop(0)
            dice_val = self.get_value_after_dice_roll()
            self.move_player(player, dice_val)
            if self.has_won_game(player):
                print(f"{player.get_name()} wins!")
                self.board.get_player_positions().pop(player.get_id())
            else:
                self.player_queue.append(player)
