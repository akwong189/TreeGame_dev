import random
from Tiles import WaterTile, LightTile, EventTile


class Board:

    def __init__(self, players):    #players would be {'number': player object}
        self.players = players
        self.rounds_played = 0
        self.upper_bound = 5
        self.lower_bound = [1]
        self.season = ['Spring', 'Summer', 'Fall', 'Winter']
        self.season_num = 0

        self.board = []
        for i in range(48):
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

    def probability(self):
        if self.players[list(self.players.keys())[len(self.players) - 1]].turn_count == self.players[list(self.players.keys())[0]].turn_count:
            self.rounds_played += 1

        if self.rounds_played > 6:
            if random.randint(1,5) in self.lower_bound:
                if self.season_num + 1 > 3:
                    self.end_game()
                else:
                    self.season_num += 1
                    self.change_season(self.season[self.season_num])
                    self.lower_bound = [1]
                    self.rounds_played = 0
            else:
                self.lower_bound.append(self.lower_bound[len(self.lower_bound) - 1] + 1)

    def end_game(self):
        pass
