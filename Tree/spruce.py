from tree import Tree

class Spruce(Tree):

    def __init__(self):
        super(Spruce, self).__init__()
        self.max_movement -= 2
        self.max_health += 3