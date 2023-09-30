from  import WHITE
from  import count_check
import numpy as np
import pygame
import sys
import math
import random

BLUE=(0,0,255)
BLACK=(0,0,0)
RED =(255,0,0)
YELLOW=(255,255,0)

WHITE=(255,255,255)

ROW_COUNT = 6
COLUMN_COUNT = 7

count_check = 0


PLAYER = 0
AI = 1


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def Drop_Piece(board, row, Col, piece):
    board[row][Col] = piece

def is_valid_location(board, Col):
    return board[ROW_COUNT-1][Col] == 0

def get_next_open_row(board, Col):
    for r in range(ROW_COUNT):
        if board[r][Col] == 0:
            return r

def print_board(board):
    print (np.flip(board, 0))

def winning_move(board, piece):
    # Check Horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check Vertical Locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True


    #Check negatively sloped diagonals for win
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()
board = create_board()
print_board(board)
Game_over = False

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width,height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont =pygame.font.SysFont("Arial", 75 , bold=True, italic=False)
turn = random.randint(PLAYER,AI)

while not Game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
         
         
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,WHITE,(0,0,width,SQUARESIZE))
            posx = event.pos[0]
            
            if turn == PLAYER:
                pygame.draw.circle(screen,RED,(posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            #Ask for player 1 input
            if turn == PLAYER:
                posx = event.pos[0]
                Col = int(math.floor(posx/SQUARESIZE))
                

                if is_valid_location(board, Col):
                    row = get_next_open_row(board, Col)
                    Drop_Piece(board, row, Col, 1)
                    
                    if winning_move(board, 1):
                        label = myfont.render("PLAYER 1 WINS!",1,RED)
                        screen.blit(label,(40,10))
                        Game_over = True
                        
                    turn += 1
                    turn %= 2
                    print_board(board)
                    draw_board(board)



    #Ask for player 2 input
    if turn == AI and not Game_over:
        Col = random.randint(0,COLUMN_COUNT-1)
        
        if is_valid_location(board, Col):
            pygame.time.wait(500)
            row = get_next_open_row(board, Col)
            Drop_Piece(board, row, Col, 2)

            if winning_move(board, 2):
                label = myfont.render("PLAYER 2 WINS!",1,BLUE)
                screen.blit(label,(40,10))
                Game_over = True

            print_board(board)
            draw_board(board)
            turn += 1
            turn %= 2
            
    if Game_over:
        pygame.time.wait(1000)



