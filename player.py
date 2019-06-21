import random


class Player:

    def __init__(self, tree_type):
        self.speed = tree_type.get_max_movement()
        self.max_health = tree_type.get_max_health()
        self.curr_health = self.max_health
        self.water = tree_type.get_init_water()
        self.light = tree_type.get_init_light()
        self.turn_count = 0
        self.position = 0

    def update_health(self):
        regen_val = (self.water + self.light) % self.max_health
        if self.curr_health + regen_val < self.max_health:
            self.curr_health += regen_val

    def roll_die(self, max_speed):
        self.position += random.randint(max_speed + 1)
        self.turn_count += 1

    def get_position(self):
        return self.position

    def get_turn_count(self):
        return self.turn_count
