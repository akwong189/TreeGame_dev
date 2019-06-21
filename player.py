import random


class Player:

    def __init__(self, tree_type, position=0):
        self.speed = tree_type.get_max_movement
        self.health = tree_type.get_max_health
        self.position = position

    def set_health(self):
        self.health = self.water + self.light  # TO-DO update the formula for health later

    def roll_die(self, max_speed):
        self.position += random.randint(max_speed + 1)
        #     self.water -= 1
        #     self.light -= 1
        # elif self.water >
        # if (self.health > 0)
