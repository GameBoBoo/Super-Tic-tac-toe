import pygame, sys
import numpy as np

# init pygame
pygame.init()

# define game dimension
WIDTH = 600
HEIGHT = 1000

TABLE_WIDTH = 600
TABLE_HEIGHT = 600

LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
DECK_SIZE = 120

CIRCLE_RADIUS = {
  3 : 60,
  2 : 40,
  1 : 20
}

CIRCLE_WIDTH = {
  3 : 15,
  2 : 11,
  1 : 7
}

CROSS_SIZE = {
  3 : 120,
  2 : 80,
  1 : 40
}

CROSS_WIDTH = {
  3 : 25,
  2 : 21,
  1 : 17
}

# define game color
RED = (255, 0, 0)
BG_COLOR = pygame.image.load("Photo/Background.png")
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (0, 71, 171)
CROSS_COLOR = (255, 44, 44)
SELECTING_COLOR = (237, 191, 33)

class TicTacToeGame:
  def __init__(self):
    # setup display
    self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption( 'TIC TAC TOE' )

    # set background
    self.screen.blit(BG_COLOR, (0, 0))

    # draw frame for tic tac toe
    self.draw_frame()

    # store center coordinates
    self.center_x_list = []

    # setup turn 1 for O
    self.player = 1
