from tile import Tile


class LightTile(Tile):

    def __init__(self):
        Tile()
        self.color = 'Yellow'

    def event(self, player):
        # Change light/food
        pass
