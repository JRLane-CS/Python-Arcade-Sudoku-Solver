# import libraries
import arcade
import os

# set file path so arcade can find local cursor image
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# constants
SCREEN_WIDTH = 820
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sudoku"

# Sudoku game class for arcade visuals
class Sudoku(arcade.Window):

    # initialization function
    def __init__(self, puzzle = None):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, 
                         resizable=True)

        # declare cursor sprite list
        self.cursor_list = None

        # declare the cursor sprite
        self.cursor_sprite = None

        # hide the mouse cursor to use the sprite cursor
        self.set_mouse_visible(False)

        # set the background color
        arcade.set_background_color(arcade.color.BEIGE)

        # set the reference puzzle array
        if puzzle != None:
            self.reference_puzzle = []
            for row in puzzle:
                self.reference_puzzle.append(row.copy())
        else:
            self.reference_puzzle =  [
                [0, 2, 0, 0, 5, 0, 0, 8, 9],
                [0, 0, 6, 0, 8, 0, 0, 0, 3],
                [7, 0, 0, 0, 0, 3, 4, 5, 0],
                [2, 0, 0, 0, 0, 7, 0, 0, 1],
                [5, 6, 0, 0, 9, 0, 2, 0, 0],
                [8, 0, 1, 2, 0, 4, 0, 6, 0],
                [0, 0, 0, 6, 0, 8, 9, 1, 0],
                [0, 7, 0, 0, 0, 0, 3, 4, 0],
                [9, 1, 0, 3, 4, 5, 0, 7, 0]
            ]

        self.puzzle = None
        
        # set location variable defaults
        self.locations = {}
        number = 0

        # map board locations by x, y coordinates, match to puzzle locations
        for y in range(532, 2, -66):
            for x in range(3, 596, 66):
                self.locations[number] = [y + 64, y, x, x + 64] 
                number += 1

        # add the solve puzzle location
        self.locations[number] = [400, 350, 615, 785]

        # set location border values
        self.border_display = False
        self.border_coords = None

        # selected location value
        self.selected_location = None

        # create variables to check for solved puzzle
        self.solve_puzzle = False
        self.solved = None
        self.completed = None
        self.user_solved = None

        # create default puzzle location text array
        self.location_text = []
        for i in range(81):
            self.location_text.append(
                arcade.Text(" ", 0, 0,
                arcade.color.YANKEES_BLUE, 36    
                ))
    

    # set initial game state
    def setup(self):
        
        # set working puzzle 
        self.puzzle = []
        for row in self.reference_puzzle:
            self.puzzle.append(row.copy())

        # set location border values
        self.border_display = False
        self.border_coords = None

        # selected location value
        self.selected_location = None

        # create variable to trigger solve puzzle
        self.solve_puzzle = False
        self.solved = False
        self.completed = False
        self.user_solved = False
        
        # create cursor sprite list
        self.cursor_list = arcade.SpriteList()
        
        # create the cursor sprite
        # hand image public domain from: 
        # https://publicdomainvectors.org/en/free-clipart/Hand-cursor-vector-illustration/13428.html
        self.cursor_sprite = arcade.Sprite("hand.png", 0.1)
        self.cursor_sprite.center_x = 850
        self.cursor_sprite.center_y = 80
        self.cursor_list.append(self.cursor_sprite)
        
    
    # check game logic during update
    def on_update(self, delta_time):
       
        # if solve puzzle flag is set, solve the puzzle
        if self.solve_puzzle == True:
           self.solved = solve_sudoku(self.puzzle)

        # check to see if the user has completed the puzzle and check if solved
        else:

            # assume user has completed the puzzle
            self.completed = True
            
            # loop through columns and rows to see if there are any zeroes, if not
            #  the puzzle has been completed, so check to see if it is solved
            for column in range(9):
                column_list = []
                for row in self.puzzle:
                    if 0 in row:
                        self.completed = False
                    column_list.append(row[column])
                if 0 in column_list:
                    self.completed = False
            if self.completed == True and self.solve_puzzle == False:
                self.user_solved = puzzle_solved(self.puzzle)
    
    
    # function to draw the window with its elements
    def on_draw(self):
        
        # prepare for drawing by clearing earlier drawings
        self.clear()

        # draw sudoku board locations
        for y in range(532, 2, -66):
            for x in range(3, 596, 66):
                arcade.draw_lrtb_rectangle_filled(x, x + 64, y + 64, y, 
                    arcade.color.AMAZON)
        
        # draw the 3 X 3 grid boundaries
        arcade.draw_line(2, 200, 595, 200, arcade.color.BLACK_BEAN, 2)
        arcade.draw_line(2, 398, 595, 398, arcade.color.BLACK_BEAN, 2)
        arcade.draw_line(200, 3, 200, 596, arcade.color.BLACK_BEAN, 2)
        arcade.draw_line(398, 3, 398, 596, arcade.color.BLACK_BEAN, 2)

        # draw puzzle numbers onto board using puzzle array rows and columns
        # loop through all rows and columns of the puzzle
        for r, row in enumerate(self.puzzle):
            for c in range(len(row)):

                # calculate the puzzle location
                location = r * 9 + c

                # get x, y coords from the locations dictionary
                x = self.locations[location][2] + 17
                y = self.locations[location][0] - 49

                # set the output text of location
                if self.puzzle[r][c] != 0:
                    output = str(self.puzzle[r][c])
                else:
                    output = " " 

                # set the color of the text based on whether it can be changed
                if self.reference_puzzle[r][c] != 0:
                    color = arcade.color.RED
                else:
                    color = arcade.color.YANKEES_BLUE

                # update and draw the puzzle location text object                
                self.location_text[location] = arcade.Text(
                output, x, y, color, 36)
                self.location_text[location].draw()

        # if a location is selected, draw the border
        if self.border_display == True:
            start_x = self.border_coords[2]
            start_y = self.border_coords[1]
            stop_x = self.border_coords[3]
            stop_y = self.border_coords[0]
            arcade.draw_line(start_x, start_y, stop_x, start_y, 
                             arcade.color.RED_PURPLE, 2)
            arcade.draw_line(start_x, stop_y, stop_x, stop_y, 
                             arcade.color.RED_PURPLE, 2)
            arcade.draw_line(start_x, start_y, start_x, stop_y, 
                             arcade.color.RED_PURPLE, 2)
            arcade.draw_line(stop_x, start_y, stop_x, stop_y, 
                             arcade.color.RED_PURPLE, 2)

        # draw solve button
        arcade.draw_lrtb_rectangle_filled(615, 785, 400, 350, 
                                     arcade.color.AMARANTH_PINK)
        arcade.Text("Solve Puzzle", 628, 368, arcade.color.BLACK, 18).draw()

        # draw true solve puzzle response 
        if self.solve_puzzle == True and \
            self.solved == True and \
            self.completed == False:
            arcade.Text("Puzzle Solved!", 620, 320, 
                        arcade.color.AMAZON, 18).draw()
        
        # draw false solve puzzle response
        elif self.solve_puzzle == True and \
            self.solved == False and \
            self.completed == False:
            arcade.Text("Puzzle Unsolvable!", 600, 320, 
                        arcade.color.RASPBERRY_ROSE, 18).draw()
            
        # draw true user completed puzzle response
        if self.completed == True and \
            self.user_solved == True and \
            self.solve_puzzle == False:
            arcade.Text("Puzzle Solved!", 620, 320, 
                        arcade.color.AMAZON, 18).draw()
        
        # draw false user completed response
        elif self.completed == True and \
            self.user_solved == False and \
            self.solve_puzzle == False:
            arcade.Text("Incorrect Solution!", 600, 320, 
                        arcade.color.RASPBERRY_ROSE, 18).draw()
            
        # TODO create save button

        # TODO create load button
        
        # draw cursor
        self.cursor_list.draw()

    
    # actions to take when mouse moves
    def on_mouse_motion(self, x, y, dx, dy):

        # move the center of the cursor sprite to match the mouse x, y
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y

    
    # actions to take when user presses the mouse buttons
    def on_mouse_press(self, x, y, button, modifiers):

        # adjust for drawn rectangle and cursor center coordinates offset value
        y += 26
        x -= 6

        # determine which location is being clicked
        for location in self.locations:
            if y <= self.locations[location][0] and\
               y >= self.locations[location][1] and\
               x >= self.locations[location][2] and\
               x <= self.locations[location][3]:
                
                # remember selected location
                self.selected_location = location

                # TODO if location cannot be changed, make sound

                # TODO else, signal draw function to draw the border at border coords
                self.border_display = True
                self.border_coords = self.locations[location]

                # when user presses solve puzzle button verify user has not
                #  completed the puzzle to avoid conflicting messages
                if location == 81 and self.completed == False:
                    self.solve_puzzle = True


    # handle key presses
    def on_key_press(self, symbol, modifiers):
       
        # in case user tries to change something after a failed solve,
        #  unset the solve puzzle flag
        self.solve_puzzle = False

        # if user has selected a location and valid 1-9 number input
        if self.selected_location != None and \
            ((symbol >= 48 and symbol <= 57) or symbol == 32):

            # convert symbol to number and store in array
            row = int(self.selected_location / 9)
            column = self.selected_location % 9

            # change location value in array to the selection
            if symbol == 32 and self.reference_puzzle[row][column] == 0:
                self.puzzle[row][column] = 0

            # change location value if available in the reference puzzle
            elif self.reference_puzzle[row][column] == 0:    
                self.puzzle[row][column] = symbol - 48

            # clear last selected location and turn off location border
            self.selected_location = None
            self.border_display = False
            self.border_coords = None

        # reset game when user presses the ESC key
        elif symbol == 65307:
            self.setup()


##### Funtions to be used to check for puzzle solved by user #####
# function to see if the rows are solved
def rows_solved(puzzle):

    # loop through each row
    for row in range(9):

        # verify numbers 1 through 9 are in the row or return false
        for number in range(9):
            if number + 1 not in puzzle[row]:
                return False
            
    # if above passed, then rows are complete
    return True


# function to see if the columns are solved
def columns_solved(puzzle):
    
    # loop through all rows and get column values
    for column in range(9):

        # start with empty array and add column values from each row to it
        column_array = []
        for row in range(9):
            column_array.append(puzzle[row][column])

        # verify all numbers match 1 through 9 or return false    
        for number in range(9):
            if number + 1 not in column_array:
                return False
            
    # if above passed, then columns are complete
    return True


# function to see if the grids are solved
def grids_solved(puzzle):
    
    # set defaults
    columns = [0, 3, 6]
    rows = [0, 3, 6]
    row_number = 0
    
    # loop through each of the nine mini-grids
    for grid in range(9):

        # clear the array for appending grid values
        grid_array = []

        # determine which column values are to be added to array
        column_number = columns[grid % 3]

        # loop through each row and append column values to the grid array
        for row in range(row_number, row_number + 3):
            for column in range(column_number, column_number + 3):
                grid_array.append(puzzle[row][column])

        # verify numbers 1 through 9 are in the array or return false
        for number in range(9):
            if number + 1 not in grid_array:
                return False
            
        # if the grid is evenly divisible by 3, increase row number to get
        # the next set of 3 grids
        if (grid + 1) % 3 == 0:
            row_number += 3

    # if all the checks above passed, then the grids are complete
    return True


# this function calls the rows, columns, and grids solved functions
def puzzle_solved(puzzle):
    
    # call rows_solved, columns_solved, and grids_solved, return results
    return rows_solved(puzzle) and columns_solved(puzzle) and grids_solved(puzzle)
        

##### Functions used to automatically solve a Sudoku puzzle #####
# this function is a helper for solve_puzzle and finds the next empty location
def next_empty(puzzle):
    
    # loop through all the locations in the puzzle to find the next empty place
    # if found, return location as row, column tuple, if not, return 0, 0 tuple
    for r, row in enumerate(puzzle):
        for column in range(len(row)):
            if row[column] == 0:
                return (r, column)
            
    # the puzzle is solved, send back nonexistent coordinates to indicate this
    return (10, 10) 


# a helper function for solve_puzzle and checks if a number is valid for a row
def valid_for_row(puzzle, row, number):
    return not number in puzzle[row]


# a helper function for solve_puzzle and checks if number is valid for a column
def valid_for_column(puzzle, column, number):
    for row in puzzle:
        if number == row[column]:
            return False
    return True


# a helper function for solve_puzzle, checks if a number is valid for a grid
def valid_for_grid(puzzle, row, column, number):
    
    # set row and column start and stop points for correct grid
    row_start = int((row) / 3) * 3
    row_end = row_start + 3
    column_start = int((column) / 3) * 3
    column_end = column_start + 3

    # loop through the grid and ensure the number is not in it
    for row in range(row_start, row_end):
        for column in range(column_start, column_end):
            if number == puzzle[row][column]:
                return False
            
    # if the number was not in the grid, return true
    return True


# a helper function for solve_puzzle calls valid for row, column, and grid
def check_number_validity(puzzle, row, column, number):
    return valid_for_row(puzzle, row, number) \
       and valid_for_column(puzzle, column, number) \
       and valid_for_grid(puzzle, row, column, number)
    

# this function uses recursion to solve the sudoku puzzle by using all numbers
#  that can possibly go into a location one at a time until either the puzzle
#  is solved or all number combinations have been exhausted
def solve_sudoku(puzzle, row = 0, column = 0):
       
    # find next empty spot in puzzle
    get_next = next_empty(puzzle)
    
    # if get next is (10, 10), the puzzle is solved
    if get_next == (10, 10):
        return True
    
    # else, continue trying to solve it
    else:

        row = get_next[0]
        column = get_next[1]

        for number in range(1, 10):
            if check_number_validity(puzzle, row, column, number):

                # attempt to assign the number
                puzzle[row][column] = number

                # if the statement is true, the puzzle is solved
                if solve_sudoku(puzzle, row, column):
                    return True
                
                else:
                    
                    # show row, column location as empty again
                    puzzle[row][column] = 0
            
        # the number failed, so return to try the next or puzzle is unsolvable
        return False


# main function to set the puzzle or simply start the game with its default
def main():

    # set a completed puzzle
    almost_completed_puzzle = [
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 2, 6, 7, 8, 9, 1, 5],
        [6, 7, 5, 9, 1, 2, 3, 4, 8],
        [9, 1, 8, 3, 4, 5, 6, 7, 2]
    ]
    
    # set an unsolvable test puzzle
    unsolvable_puzzle = [    
        [0, 2, 0, 0, 5, 0, 0, 8, 9],
        [0, 0, 6, 0, 8, 0, 0, 0, 3],
        [7, 0, 0, 0, 0, 3, 4, 5, 0],
        [2, 0, 0, 0, 0, 7, 0, 0, 1],
        [5, 6, 0, 0, 9, 0, 2, 0, 0],
        [8, 0, 1, 2, 0, 4, 0, 6, 0],
        [0, 0, 0, 6, 0, 8, 9, 1, 0],
        [0, 7, 2, 0, 0, 0, 3, 4, 0],
        [9, 1, 0, 3, 4, 5, 0, 7, 0]
    ]

    # set a valid test puzzle
    test_puzzle = [
        [0, 2, 0, 0, 5, 0, 0, 8, 9],
        [0, 0, 6, 0, 8, 0, 0, 0, 3],
        [7, 0, 0, 0, 0, 3, 4, 5, 0],
        [2, 0, 0, 0, 0, 7, 0, 0, 1],
        [5, 6, 0, 0, 9, 0, 2, 0, 0],
        [8, 0, 1, 2, 0, 4, 0, 6, 0],
        [0, 0, 0, 6, 0, 8, 9, 1, 0],
        [0, 7, 0, 0, 0, 0, 3, 4, 0],
        [9, 1, 0, 3, 4, 5, 0, 7, 0]
    ]
    
    # create Sudoku object with test puzzle
    game = Sudoku(unsolvable_puzzle)

    # set up the game
    game.setup()
    
    # run the game
    arcade.run()


# if the program is run directly, call main
if __name__ == "__main__":
    main()