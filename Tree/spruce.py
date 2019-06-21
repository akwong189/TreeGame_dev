from tree import Tree

class Spruce(Tree):

    def __init__(self):
        """Spruce Tree
        Base max movement of 4
        Base max health of 13
        Init water level of 13
        Init light level of 15
        """
        super(Spruce, self).__init__()
        self.max_movement -= 2
        self.max_health += 3
        self.init_light += 2
        self.init_water += 5