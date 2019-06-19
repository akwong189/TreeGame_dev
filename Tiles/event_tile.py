from tile import Tile


class EventTile(Tile):
    def __init__(self):
        Tile()
        self.color = 'Green'

    def event(self, player):
        # Change all of the players stats
        pass
