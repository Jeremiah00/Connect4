import pygame
import math 
import numpy as np
ROWS = 6
COLS = 7
WIDTH, HEIGHT = 800, 700
SQUARE_SIZE = WIDTH//COLS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect four")
RED = (255, 1, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
turn = 1
radius = SQUARE_SIZE/2

def check_win(board, piece):
    # Check horziontals
    for col in range(COLS-3):
        for row in range(ROWS):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    # Check Verticals
    for col in range(COLS):
        for row in range(ROWS-3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    
    # Check positive slope
    for col in range(COLS-3):
        for row in range(ROWS-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    # Check negative slope 
    for col in range(COLS-3):
        for row in range(3, ROWS):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
        


def change_turn():
    global turn
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1

def create_board():
    board = []
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            board[row].append(0)
    return np.flip(board, 0)

def get_vaild_position(board, col):
    for row in range(ROWS):
        if board[row][col] == 0:
            return row

def is_valid_position(board, col):
    return board[ROWS-1][col] == 0


def drop_piece(board, row, col, piece):
    board[row][col] = piece

def draw_board(win, board):
    win.fill(BLUE)
    for cols in range(COLS):
        for row in range(ROWS):
            pygame.draw.circle(win, BLACK, (cols* SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE/2), radius )

    for cols in range(COLS):
        for row in range(ROWS):
            if board[row][cols] == 1:
                pygame.draw.circle(win, RED, (cols* SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE/2), radius )
            elif board[row][cols] == 2:
                pygame.draw.circle(win, YELLOW, (cols* SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE/2), radius )
    pygame.display.update()
    return

def display_board(board):
    print(np.flip(board, 0))

def main():
    run = False
    board = create_board()
    print(board)
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 1:    
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARE_SIZE))
                    if is_valid_position(board, col):
                        row = get_vaild_position(board, col)
                        drop_piece(board, row, col, turn)
                        if check_win(board, turn):
                            print("Player red wins")
                            run = True
                
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARE_SIZE))
                    if is_valid_position(board, col):
                        row = get_vaild_position(board, col)
                        drop_piece(board, row, col, turn)
                        if check_win(board, turn):
                            print("Player yellow wins") 
                            run = True
                change_turn()  
                display_board(board)
                
            draw_board(WIN, np.flip(board, 0))

    pygame.quit()
main()

         

    

