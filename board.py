import random
from Tiles import WaterTile, LightTile, EventTile


class Board:

    def __init__(self):
        self.board = []
        for i in range(100):
            x = random.randint(0, 100)
            if x < 45:
                self.board.append(WaterTile())
            elif 45 <= x < 90:
                self.board.append(LightTile())
            else:
                self.board.append(EventTile())

        # for i in range(1, len(self.board)):
        #     if self.board[i] == self.board[i - 1] and self.board[i].isinstance(WaterTile()):
        #         self.board[i] = LightTile()
        #     elif self.board[i] == self.board[i - 1] and self.board[i].isinstance(LightTile()):
        #         self.board[i] = WaterTile()

    def get_tile(self, i):
        return self.board[i]

    def change_season(self, season):
        for i in self.board:
            i.season = season
