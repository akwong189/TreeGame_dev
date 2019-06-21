from .tile import Tile
import random


class WaterTile(Tile):

    def __init__(self):
        super(WaterTile, self).__init__()
        self.color = 'Blue'
        self.add_water = random.randint(1, 3)

    def event(self, player):
        player.water += self.add_water * Tile.multipliers[self.season]
