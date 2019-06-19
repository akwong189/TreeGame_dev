import random
from Tiles import WaterTile, LightTile, EventTile


class Board:

    def __init__(self):
        self.board = []
        for i in range(100):
            x = random.randint(0, 10)
            if x < 4:
                self.board[i] = WaterTile()
            elif 4 <= x < 8:
                self.board[i] = LightTile()
            else:
                self.board[i] = EventTile()

    def get_tile(self, i):
        return self.board[i]

    def change_season(self, season):
        for i in self.board:
            i.season = season
