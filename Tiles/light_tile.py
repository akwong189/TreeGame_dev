from .tile import Tile


class LightTile(Tile):

    def __init__(self):
        Tile()
        self.color = (255, 255, 0)

    def event(self, player):
        # Change light/food
        pass
