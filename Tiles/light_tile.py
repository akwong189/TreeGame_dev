from .tile import Tile
import random


class LightTile(Tile):

    def __init__(self):
        Tile()
        self.color = (255, 255, 0)
        self.add_light = random.randint(1, 3)

    def event(self, player):
        player.light += self.add_light * Tile.multipliers[self.season]
