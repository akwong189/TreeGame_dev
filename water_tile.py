from tile import Tile


class WaterTile(Tile):

    def __init__(self):
        Tile()
        self.color = 'Blue'

    def event(self, player):
        # Change water
        pass
