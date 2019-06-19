from tree import Tree

class Poplar(Tree):

    def __init__(self):
        super(Poplar, self).__init__()
        self.max_movement += 3
        self.max_health -= 2 