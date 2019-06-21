import sys, pygame
from board import Board

pygame.init()

screen = pygame.display.set_mode((960, 960))
print("hi")

if __name__ == '__main__':
    board = Board()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        for tile in board.board:
            pygame.draw.rect(screen, (20,20,20), )




# if __name__ == '__main__':
#     board = Board()
#     for i in board.board:
#         print(i)
#
#     tree = Tree()
#     player = Player(tree, 0)
