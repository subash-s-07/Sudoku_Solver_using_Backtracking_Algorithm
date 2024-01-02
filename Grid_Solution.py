import pygame
#from sudokuSolverAlgo import *
from pass1 import *
#from chooseLevel import *
import time
sol1=passgrid()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
L_GREEN = (150, 255, 150)
RED = (255, 0, 0)
L_RED = (255, 204, 203)
GRAY = (60, 60, 60)
L_GRAY = (220, 220, 220)
YELLOW = (255, 255, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = HEIGHT = 50

# This sets the margin between each cell
MARGIN = 5
numbers_1to9 = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
                pygame.K_9]

# Set the width and height of the screen [width, height]
size = (500, 500)
# screen = pygame.display.set_mode(size)
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

# pygame.display.set_caption("Sudoku King")

# Loop until the user clicks the close button.
done = False


def cheatingAllTheWay():
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            Board[row][column] = solvedBoard[row][column]
            addNumToBoard(Board[row][column], row, column, L_GREEN)
            time.sleep(0.05)
            pygame.display.flip()


def addNumToBoard(number, row, column, color):
    addNewRect(row, column, WHITE, 5)
    addNewRect(row, column, color, None)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(number), True, BLACK, )
    textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
    textRect.center = ((MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
    screen.blit(text, textRect)
    drawTheBorder()


def addNewRect(row, col, color, width):
    rectSize = pygame.Rect((MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                           HEIGHT)
    if width is not None:
        pygame.draw.rect(screen, color, rectSize, width)  # coloring only the border
    else:
        pygame.draw.rect(screen, color, rectSize)  # coloring the whole rectangle
def drawTheBorder():
    dif = 500 // 9
    for i in range(10):
        thick = 5
        pygame.draw.line(screen, GRAY, (0, i * dif + 2), (500, i * dif + 2), thick)
        pygame.draw.line(screen, GRAY, (i * dif + 2, 0), (i * dif + 2, 500), thick)
    for i in range(10):
        if i % 3 == 0:
            thick = 8
            pygame.draw.line(screen, BLACK, (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, BLACK, (i * dif, 0), (i * dif, 500), thick)


def drawInitBoard():
    # printBoard(solvedBoard)
    for row in range(0,9):
        for column in range(0,9):
            color = L_GRAY
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # show nothing if the number is 0
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(sol1[row][column]), True, BLACK, )

            textRect = text.get_rect()  # get_rect() -> Returns a new rectangle covering the entire surface.
            textRect.center = (
                (MARGIN + WIDTH) * column + MARGIN + WIDTH / 2, (MARGIN + HEIGHT) * row + MARGIN + WIDTH / 2)
            screen.blit(text, textRect)
            drawTheBorder()
if __name__ == "__main__":
    flag1 = True
    pygame.display.set_caption("Sudoku King1")
    screen = pygame.display.set_mode(size)
    #print("solveBoard")
    #print(sol1)

    # ------ draw the board ------
    pygame.init()
    screen.fill(BLACK)
    drawInitBoard()
    readyForInput = False
    key = None
    while not done:
        # --- Main event loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in numbers_1to9:
                    key = chr(event.key)
                #if event.key == pygame.K_RETURN:
                    #finish()
                if event.key == pygame.K_c:
                    cheatingAllTheWay()
        key = None
        pygame.display.flip()
        pygame.display.update()


# Close the window and quit.
pygame.quit()
