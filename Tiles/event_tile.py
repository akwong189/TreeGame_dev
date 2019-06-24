from .tile import Tile
import random


class EventTile(Tile):
    #(water, light); add more events
    events = {'Spring': {'Flood': (3, -1)}, 'Summer': {'Drought': (-3, 2), 'Sea Levels Rise': (2, 0)}, 'Fall': {}, 'Winter': {'Snowstorm': (-1, -1)}}

    def __init__(self):
        super(EventTile, self).__init__()
        self.color = (0, 255, 0)

    def pick_event(self, player):
        s = EventTile.events[self.season]
        i = random.randint(0, len(s) - 1)
        if player.water + s[list(s.keys())[i]][0] < 0:
            player.water = 0
        else:
            player.water += s[list(s.keys())[i]][0]

        if player.light + s[list(s.keys())[i]][1] < 0:
            player.light = 0
        else:
            player.light += s[list(s.keys())[i]][1]
