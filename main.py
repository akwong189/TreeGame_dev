import pygame

from Tree import Tree
from board import Board
from player import Player

if __name__ == '__main__':
    board = Board()
    for i in board.board:
        print(i)

    tree = Tree()
    player = Player(tree, 0)
