class Board(object):
    def __init__(self, size):
        self.size = size
        self.snakes = []
        self.ladders = []
        self.player_positions = {}

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_snakes(self):
        return self.snakes

    def set_snakes(self, snakes):
        self.snakes = snakes

    def get_ladders(self):
        return self.ladders

    def set_ladders(self, ladders):
        self.ladders = ladders

    def get_player_positions(self):
        return self.player_positions

    def set_player_positions(self, player_positions):
        self.player_positions = player_positions
