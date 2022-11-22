import pygame
pygame.font.init()

class Board:
    #screen is a window from pygame
    #difficulty will be easy, medium, or hard
    def __int__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.difficulty = difficulty
    #draws an outline of the sudoku grid, with bold lines to delineate the 3x3 boxes
    #draws every cell on the board
    def draw(self):
        width = 550
        height = 550
        line_width = 1
        thick_line = 3
        line_color = (0,0,0)
        for i in range(0,10):
            if (i % 3 == 0):
                pygame.draw.line(self.screen, line_color, (50 + 50 * i, 50), (50 + 50 * i, height - 50), thick_line)
                pygame.draw.line(self.screen, line_color, (50, 50 + 50 * i), (width - 50, 50 + 50 * i), thick_line)

            pygame.draw.line(self.screen, line_color, (50 + 50*i, 50), (50 + 50*i, height - 50), line_width)
            pygame.draw.line(self.screen, line_color, (50, 50 + 50*i), (width - 50, 50 + 50*i), line_width)


        pass
    #marks the cell at(row,col) in the board as the current selected cell
    #once a cell has been selected, the user can edit its value or sketched value
    def select(self, row, col):
        pass
    #if a tuple of (x,y) coordinates is within the displayed board, this function returns a tuple of the cell which was
    #clicked. Otherwise, the function returns none
    def click(self, x, y):
        pass
    #clears the value of the cell. Note that the user can only remove the cell values and sketched filled by themselves
    def clear(self):
        pass
    #sets trhe sketched value of the current selected cell equal to user entered value.
    #it will be displayed in the top left corner of the cell using the draw() function
    def sketch(self, value):
        pass
    #sets the value of the current selected cell equal to the user entered value
    #called when the user presses the enter key
    def place_number(self, value):
        pass
    #reset all cells in the board to their original values(0 if cleared, otherwise the corresponding digit)
    def reset_to_original(self):
        pass
    #returns a Boolean value indicating whether the board is full or not
    def is_full(self):
        pass
    #updates the underlying 2d board with the values in all cells
    def update_board(self):
        pass
    #finds an empty cell and returns its row and col as a tuple(x,y)
    def find_empty(self):
        # x is row and y is col
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 0:
                    return x, y
        return None
        pass
    #check whether the sudoku board is solved correctly
    def check_board(self):
        pass

