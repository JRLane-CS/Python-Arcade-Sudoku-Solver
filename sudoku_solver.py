"""
Python Arcade Sudoku Solver
"""
# import libraries
import arcade
import os

# set file path so arcade can find local cursor image
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sudoku"

class Sudoku(arcade.Window):

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

        # set the puzzle array
        if puzzle != None:
            self.puzzle = puzzle.copy()
        else:
            self.puzzle =  [
                [9, 8, 7, 6, 5, 4, 3, 2, 1],
                [2, 4, 6, 1, 7, 3, 9, 8, 5],
                [3, 5, 1, 9, 2, 8, 7, 4, 6],
                [1, 2, 8, 5, 3, 7, 6, 9, 4],
                [6, 3, 4, 8, 9, 2, 1, 5, 7],
                [7, 9, 5, 4, 6, 1, 8, 3, 2],
                [5, 1, 9, 2, 8, 6, 4, 7, 3],
                [4, 7, 2, 3, 1, 9, 5, 6, 8],
                [8, 6, 3, 7, 4, 5, 2, 1, 9]
            ]

        # set reference puzzle (so only values of 0 can be changed)
        self.reference_puzzle = []
        for row in puzzle:
            self.reference_puzzle.append(row.copy())
        
        # set location variable defaults
        self.locations = {}
        number = 0

        # map board locations by x, y coordinates, match to puzzle locations
        for y in range(532, 2, -66):
            for x in range(3, 596, 66):
                self.locations[number] = [y + 64, y, x, x + 64] 
                number += 1

        # set location border values
        self.border_display = False
        self.border_coords = None

        # selected values
        self.selected_location = None
        
        # create default puzzle location text array
        self.location_text = []
        for i in range(81):
            self.location_text.append(
                arcade.Text(" ", 0, 0,
                arcade.color.YANKEES_BLUE, 36    
                ))
    

    # set initial game state
    def setup(self):
        
        # create cursor sprite list
        self.cursor_list = arcade.SpriteList()
        
        # create the cursor sprite
        # hand image public domain from: 
        # https://publicdomainvectors.org/en/free-clipart/Hand-cursor-vector-illustration/13428.html
        self.cursor_sprite = arcade.Sprite("hand.png", 0.1)
        self.cursor_sprite.center_x = 850
        self.cursor_sprite.center_y = 80
        self.cursor_list.append(self.cursor_sprite)
        
    # TODO put game logic here during update
    def on_update(self, delta_time):
        pass
    
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

        # TODO create solve button

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


    # handle key presses
    def on_key_press(self, symbol, modifiers):
        
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

        # TODO elif allow for a reset option here


def main():
    
    # set a default test puzzle
    test_puzzle = [    
        [0, 0, 0, 0, 5, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 3],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 9]
    ]
    
    # create Sudoku object with test puzzle
    game = Sudoku(test_puzzle)

    # set up the game
    game.setup()
    
    # run the game
    arcade.run()


if __name__ == "__main__":
    main()