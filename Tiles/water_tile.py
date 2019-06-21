from .tile import Tile


class WaterTile(Tile):

    def __init__(self):
        Tile()
        self.color = (0, 0, 255)

    def event(self, player):
        # Change water
        pass
