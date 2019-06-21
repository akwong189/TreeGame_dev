from tree import Tree

class Poplar(Tree):

    def __init__(self):
        """Poplar Tree
        Base max movement of 9
        Base max health of 8
        Init water level of 13
        Init light level of 13
        """
        super(Poplar, self).__init__()
        self.max_movement += 3
        self.max_health -= 2 
        self.init_light += 3
        self.init_water += 3
