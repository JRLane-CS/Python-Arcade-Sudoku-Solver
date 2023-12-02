"""This function checks to see if the rows are complete"""
def rows_solved(puzzle):

    # loop through each row
    for row in range(9):

        # verify numbers 1 through 9 are in the row or return false
        for number in range(9):
            if number + 1 not in puzzle[row]:
                return False
            
    # if above passed, then rows are complete
    return True


"""This function checks to see if the columns are complete"""
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


"""This function checks to see if the grids are complete"""
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


"""This function checks to see if the puzzle has been solved"""
def is_solved(puzzle):
    
    # call rows_solved, columns_solved, and grids_solved, return results
    return rows_solved(puzzle) and columns_solved(puzzle) and grids_solved(puzzle)
        

"""This function finds the next empty location in the puzzle"""
def next_empty(puzzle):
    # loop through all the locations in the puzzle to find the next empty place
    # if found, return location as row, column tuple, if not, return 0, 0 tuple
    for r, row in enumerate(puzzle):
        for column in range(len(row)):
            if row[column] == 0:
                return (r, column)
    return (10, 10) 


"""This function will check to see if a number is valid to go into a row"""
def valid_for_row(puzzle, row, number):
    return not number in puzzle[row]


"""This function will check to see if a number is valid to go into a column"""
def valid_for_column(puzzle, column, number):
    for row in puzzle:
        if number == row[column]:
            return False
    return True


"""This function will check to see if a number if valid to go into a grid"""
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


"""This function verifies whether the number will fit in the location"""
def check_number_validity(puzzle, row, column, number):
    return valid_for_row(puzzle, row, number) \
       and valid_for_column(puzzle, column, number) \
       and valid_for_grid(puzzle, row, column, number)
    

"""This function will print the puzzle array to the terminal"""
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)


"""This function attempts to solve the puzzle"""
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
            
        # the number failed, so return and try the next one
        return False

def determine_difficulty(puzzle):

    count = 0
    for row in puzzle:
        for i in range(len(row)):
            if row[i] != 0:
                count += 1

    if count < 10:
        return ("extreme", count)
    elif count < 20:
        return ("difficult", count)
    elif count < 40:
        return ("moderate", count)
    else:
        return ("easy", count)


"""This is the main function"""    
def main():    

    # # set good test puzzle
    # test_puzzle = [
    #     [1, 2, 3, 4, 5, 6, 7, 8, 9],
    #     [4, 5, 6, 7, 8, 9, 1, 2, 3],
    #     [7, 8, 9, 1, 2, 3, 4, 5, 6],
    #     [2, 3, 4, 5, 6, 7, 8, 9, 1],
    #     [5, 6, 7, 8, 9, 1, 2, 3, 4],
    #     [8, 9, 1, 2, 3, 4, 5, 6, 7],
    #     [3, 4, 5, 6, 7, 8, 9, 1, 2],
    #     [6, 7, 8, 9, 1, 2, 3, 4, 5],
    #     [9, 1, 2, 3, 4, 5, 6, 7, 8]
    # ]

    # completed = [    
    #     [9, 8, 7, 6, 5, 4, 3, 2, 1],
    #     [2, 4, 6, 1, 7, 3, 9, 8, 5],
    #     [3, 5, 1, 9, 2, 8, 7, 4, 6],
    #     [1, 2, 8, 5, 3, 7, 6, 9, 4],
    #     [6, 3, 4, 8, 9, 2, 1, 5, 7],
    #     [7, 9, 5, 4, 6, 1, 8, 3, 2],
    #     [5, 1, 9, 2, 8, 6, 4, 7, 3],
    #     [4, 7, 2, 3, 1, 9, 5, 6, 8],
    #     [8, 6, 3, 7, 4, 5, 2, 1, 9]
    # ]
    
    hard_test_puzzle =  [
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 3, 0, 8, 5],
		  [0, 0, 1, 0, 2, 0, 0, 0, 0],
		  [0, 0, 0, 5, 0, 7, 0, 0, 0],
		  [0, 0, 4, 0, 0, 0, 1, 0, 0],
		  [0, 9, 0, 0, 0, 0, 0, 0, 0],
		  [5, 0, 0, 0, 0, 0, 0, 7, 3],
		  [0, 0, 2, 0, 1, 0, 0, 0, 0],
		  [0, 0, 0, 0, 4, 0, 0, 0, 9]
        ]
    
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

    # print guess of how long it will take
    difficulty = determine_difficulty(test_puzzle)
    print(f"This puzzle is considered {difficulty[0]}.")
    print(f"It has {difficulty[1]} numbers in it.")
    if difficulty[1] < 35:
        print("This may take some time. Please be patient.")

    if solve_sudoku(hard_test_puzzle):
        print("\nHere is the solution:")
        print_puzzle(hard_test_puzzle)
        print()

    else:
        print("\nThis puzzle cannot be solved!\n")
        

    # result = is_solved(test_puzzle)
    # if result:
    #     print("\nThe puzzle is solved.\n")
    # else:
    #     print("\nThe puzzle is not solved.\n")


# run program if called directly
if __name__ == "__main__":
    main()