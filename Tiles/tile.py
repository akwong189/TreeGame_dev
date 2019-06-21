class Tile:
    multipliers = {'Spring': 2, 'Summer': -1, 'Fall': 1, 'Winter': 0}

    def __init__(self):
        self.height = 10
        self.width = 10
        self.color = 'White'
        self.season = ''

    def event(self, player):
        pass
