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

    # available size for players
    self.deck = {
      1 : [3, 3, 2],
      2 : [3, 3, 2]
    }

    # draw deck
    self.draw_deck()

    # setup game array
    self.board = np.zeros( (BOARD_ROWS, BOARD_COLS, 2) )

    # setup game over state
    self.game_over = False

    # selecting size
    self.selecting_size = 0

    # show starting text
    print("Starting game")

  # draw frame for tic tac toe
  def draw_frame(self):
    # horizontal line
    pygame.draw.line( self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
    pygame.draw.line( self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
    pygame.draw.line( self.screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH )
    pygame.draw.line( self.screen, LINE_COLOR, (0, 4 * SQUARE_SIZE), (WIDTH, 4 * SQUARE_SIZE), LINE_WIDTH )

    # vertical line
    pygame.draw.line( self.screen, LINE_COLOR, (SQUARE_SIZE, SQUARE_SIZE), (SQUARE_SIZE, HEIGHT - SQUARE_SIZE), LINE_WIDTH )
    pygame.draw.line( self.screen, LINE_COLOR, (2 * SQUARE_SIZE, SQUARE_SIZE), (2 * SQUARE_SIZE, HEIGHT - SQUARE_SIZE), LINE_WIDTH )

  def draw_deck(self):
    if self.player == 1:
      x_row = 0
      o_row = 4
    elif self.player == 2:
      x_row = 4
      o_row = 0

    for i in range(1,4):
      start_position_x = 0
      for j in range(1, i):
        # blank for other mark
        start_position_x += CIRCLE_RADIUS[j] * 3

      # add offset
      start_position_x += CIRCLE_RADIUS[i] * 1.5

      self.center_x_list.append(start_position_x)

      # draw O
      if self.deck[1][i - 1] != 0:
        pygame.draw.circle( self.screen, CIRCLE_COLOR, (int( start_position_x ), int( o_row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS[i], CIRCLE_WIDTH[i] )

      # draw X
      if self.deck[2][i - 1] != 0:
        pygame.draw.line( self.screen, CROSS_COLOR, (start_position_x - CROSS_SIZE[i] // 2, x_row * SQUARE_SIZE + SQUARE_SIZE // 2 - CROSS_SIZE[i] // 2), (start_position_x + CROSS_SIZE[i] // 2, x_row * SQUARE_SIZE + SQUARE_SIZE // 2 + CROSS_SIZE[i] // 2 ), CROSS_WIDTH[i] )
        pygame.draw.line( self.screen, CROSS_COLOR, (start_position_x - CROSS_SIZE[i] // 2, x_row * SQUARE_SIZE + SQUARE_SIZE // 2 + CROSS_SIZE[i] // 2), (start_position_x + CROSS_SIZE[i] // 2, x_row * SQUARE_SIZE + SQUARE_SIZE // 2 - CROSS_SIZE[i] // 2 ), CROSS_WIDTH[i] )
  
  # draw selecting symbol on selecting size
  def draw_selecting_size(self, size):
    pygame.draw.circle( self.screen, SELECTING_COLOR, (int( self.center_x_list[size] ), int( 5 * SQUARE_SIZE - 15 )), 10 )

  # draw X or O in table
  def draw_mark(self):
    for row in range(BOARD_ROWS):
      for col in range(BOARD_COLS):
        # drawing O
        if self.board[row][col][0] == 1:
          pygame.draw.circle( self.screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( (row + 1) * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS[self.board[row][col][1]], CIRCLE_WIDTH[self.board[row][col][1]] )
        # drawing X
        elif self.board[row][col][0] == 2:
          pygame.draw.line( self.screen, CROSS_COLOR, ((col + 0.5) * SQUARE_SIZE - CROSS_SIZE[self.board[row][col][1]] // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2 - CROSS_SIZE[self.board[row][col][1]] // 2), ((col + 0.5) * SQUARE_SIZE + CROSS_SIZE[self.board[row][col][1]] // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2 + CROSS_SIZE[self.board[row][col][1]] // 2 ), CROSS_WIDTH[self.board[row][col][1]] )
          pygame.draw.line( self.screen, CROSS_COLOR, ((col + 0.5) * SQUARE_SIZE - CROSS_SIZE[self.board[row][col][1]] // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2 + CROSS_SIZE[self.board[row][col][1]] // 2), ((col + 0.5) * SQUARE_SIZE + CROSS_SIZE[self.board[row][col][1]] // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2 - CROSS_SIZE[self.board[row][col][1]] // 2 ), CROSS_WIDTH[self.board[row][col][1]] )
        # blank
