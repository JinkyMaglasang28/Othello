from collections import deque
from pickle import FALSE, FRAME
from tkinter.tix import WINDOW
import pygame




# variables for board game
BLOCK_SIZE = 50
PADDING_SIZE = 5
BOARD_WIDTH = BLOCK_SIZE * 8
BOARD_HEIGHT = BLOCK_SIZE * 8 + 20
FRAME_PER_SECOND = 40
WINDOWWIDTH = BLOCK_SIZE * 10
WINDOWHEIGHT = BLOCK_SIZE * 10
XMARGIN = int(((8 * BLOCK_SIZE)) / 2)
YMARGIN = int(((8 * BLOCK_SIZE)) / 2)
HINT_TILE = 'HINT_TILE'
retract_moves = deque(maxlen = 5)

#variables for players
MCTS_NUM = 2
MAX_THINK_TIME = 5
debug = False 
player = 1
victory = 0
whiteTiles = 2
blackTiles = 2
useAI = True
changed = True
AIReadyToMove = False

#variables for board
board = [[0 for x in range(8)] for x in range(8)]
board[3][3] = 1
board[3][4] = 2
board[4][3] = 2
board[4][4] = 1

#Creating a board
pygame.init()
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Othello')
font = pygame.font.SysFont("Helvetica", 48)
icon = pygame.image.load("boardIcon.png")
pygame.display.set_icon(icon)
boardground = pygame.image.load('boardground.png')
black = (pygame.image.load('black.png'))
white = pygame.image.load('white.png')
BGIMAGE = pygame.image.load('background.jpg')
BGIMAGE = pygame.transform.smoothscale(BGIMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
black_color= (0,0,0)
menuFont = pygame.font.SysFont("comicsansms", 15)

