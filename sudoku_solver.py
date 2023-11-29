import arcade


def draw_background():

    # Draw the Sudoku background
    arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.BEIGE)


def draw_sudoku_space(x, y):

    # Draw the Sudoku number placement backgrounds
    arcade.draw_lrtb_rectangle_filled(x, x + 64, y + 64, y, arcade.color.AMAZON)

def draw_grid():

    # Draw the 3 X 3 grid boundaries
    arcade.draw_line(2, 200, 595, 200, arcade.color.BLACK_BEAN, 4)
    arcade.draw_line(2, 400, 595, 400, arcade.color.BLACK_BEAN, 4)
    arcade.draw_line(200, 3, 200, 596, arcade.color.BLACK_BEAN, 4)
    arcade.draw_line(398, 3, 398, 596, arcade.color.BLACK_BEAN, 4)

def main():

    # Open the Sudoku window
    arcade.open_window(800, 600, "Python Arcade Sudoku Solver")

    # Start the render process. 
    arcade.start_render()

    # Draw the Sudoku gameboard
    draw_background()
    for x in range(3, 597, 66):
        for y in range(4, 580, 66):
            draw_sudoku_space(x, y)
    draw_grid()

    # Finish the render.
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


if __name__ == "__main__":
    main()