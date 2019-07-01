import sys, pygame
from pygame.locals import *
from board import Board

def draw_board(surface, board):
    items = []
    x = 0
    y = 0

    for index, tile in enumerate(board.board):
        print("drawing board")
        pygame.draw.rect(surface, tile.color, (x, y, 50, 50))
        if index < 12:
            x += 50
        elif index < 23:
            y += 50
        elif index < 35:
            x -= 50
        else:
            y -= 50

def make_screens(screen):
    canvas = pygame.Surface((800, 600))
    board = pygame.Rect(0, 0, 400, 300)
    player = pygame.Rect(400, 0, 400, 300)
    info = pygame.Rect(0, 300, 400, 300)
    
    screen.blit(canvas, (0, 0), board)
    screen.blit(canvas, (400, 0), player)
    screen.blit(canvas, (0, 300), info)


def main():
    x = 0
    y = 0
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((960, 960))
    players = {}
    board = Board(players)

    screen.fill(WHITE)
    canvas = pygame.Surface((800, 600))
    draw_board(canvas, board)
    screen.blit(canvas, (0, 0))

    # for index, tile in enumerate(board.board):
    #     print("drawing board")
    #     pygame.draw.rect(screen, tile.color, (x, y, 50, 50))
    #     if index < 12:
    #         x += 50
    #     elif index < 23:
    #         y += 50
    #     elif index < 35:
    #         x -= 50
    #     else:
    #         y -= 50
    # make_screens(screen)
    
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()        

if __name__ == '__main__':
    main()




# if __name__ == '__main__':
#     board = Board()
#     for i in board.board:
#         print(i)
#
#     tree = Tree()
#     player = Player(tree, 0)
