import pygame
from board import Board

if __name__ == '__main__':
    board = Board()
    for i in board.board:
        print(i)