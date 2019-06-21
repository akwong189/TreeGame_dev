import tree_constants as constants
class Tree():
    
    def __init__(self):
        """Base Tree
        Base max movement of 6
        Base max health of 10
        Init water level of 10
        Init light level of 10
        """
        self.max_movement = constants.BASE_MOVEMENT
        self.max_health = constants.BASE_HEALTH
        self.init_water = constants.BASE_WATER
        self.init_light = constants.BASE_LIGHT

    def get_max_movement(self):
        """Get max movement"""
        return self.max_movement

    def get_max_health(self):
        """Get max health"""
        return self.max_health

    def get_init_water(self):
        """Get init water level"""
        return self.init_water

    def get_init_light(self):
        """Get init light level"""
        return self.init_light

    def __str__(self):
        """To string function"""
        return "max movement: %s | max health: %s | water: %s | light: %s" % (self.max_movement, self.max_health, self.init_water, self.init_light)

    def get_all(self):
        """Returns all variables in the form of movement, health, light, and water"""
        return (self.max_movement, self.max_health, self.init_light, self.init_water)