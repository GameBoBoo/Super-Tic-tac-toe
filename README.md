import pygame, sys
import numpy as np

# init pygame
pygame.init()

# define game dimension
WIDTH = 600
HEIGHT = 700  # เพิ่มความสูงเพื่อให้มีพื้นที่สำหรับแสดงคะแนน
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# define game color
RED = (255, 0, 0)
BG_COLOR = (20, 200, 160)
LINE_COLOR = (150, 150, 150)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
PINK = (255, 182, 193)
BUTTON_COLOR = (255, 255, 255)  # Button color
BUTTON_HOVER_COLOR = (180, 180, 180)  # Button hover color
BUTTON_TEXT_COLOR = (0, 0, 0)  # Button text color
SCORE_TEXT_COLOR = (50, 50, 50)
BUTTON_RECT = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 60)  # ปรับขนาดและตำแหน่งปุ่มไปกลางจอ

class TicTacToeGame:
    def __init__(self):
        # setup display
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('TIC TAC TOE')
        
        # set background
        self.screen.fill(BG_COLOR)

        # draw frame for tic tac toe
        self.draw_frame()

        # setup game array
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))

        # setup game over state
        self.game_over = False

        # setup turn
        self.player = 1

        # score
        self.score = {1: 0, 2: 0}  # Player 1 (O) and Player 2 (X) score

        # font settings
        self.font = pygame.font.Font(None, 36)

        # draw pink background for specific squares
        self.draw_pink_background()

    # draw frame for tic tac toe
    def draw_frame(self):
        # horizontal line
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

        # vertical line
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)

        # draw outer border for score area
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(0, 600, WIDTH, 100), LINE_WIDTH)  # ขอบรอบนอกสำหรับแสดงคะแนน

    # draw pink background for specific squares
    def draw_pink_background(self):
        # Color the specific squares with pink
        pink_squares = [0, 2, 4, 6, 8]  # Square indices to color

        for index in pink_squares:
            row = index // BOARD_COLS
            col = index % BOARD_COLS
            pygame.draw.rect(self.screen, PINK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # draw score for both players
    def draw_score(self):
        # Draw a background for the score area
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 600, WIDTH, 100))
        
        # Player X score (on top)
        score_text_x = f"Player X: {self.score[2]}"
        text_x = self.font.render(score_text_x, True, SCORE_TEXT_COLOR)
        self.screen.blit(text_x, (WIDTH // 4 - text_x.get_width() // 2, 640))  # จัดตำแหน่งสำหรับ Player X

        # Player O score (at bottom)
        score_text_o = f"Player O: {self.score[1]}"
        text_o = self.font.render(score_text_o, True, SCORE_TEXT_COLOR)
        self.screen.blit(text_o, (WIDTH * 3 // 4 - text_o.get_width() // 2, 640))  # จัดตำแหน่งสำหรับ Player O
