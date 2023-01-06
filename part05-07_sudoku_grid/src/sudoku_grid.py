# Write your solution here

def row_correct(sudoku: list, row_no: int):

    
    numbers = []

    for number in sudoku[row_no]:

        if number > 0 and number in numbers:
            return False
        numbers.append(number)


    return True

def column_correct(sudoku: list, column_no: int):

    numbers = []

    for number in sudoku:

        if number[column_no] > 0 and number[column_no] in numbers:
            return False

        numbers.append(number[column_no])

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):


    row_end = 3
    column_end = 3

    numbers = []

    for number in sudoku[row_no:row_no + row_end]:
        
        for x in number[column_no:column_no + column_end]:
            if x > 0 and x in numbers:
                return False
            numbers.append(x)


    
    return True

# Use the 3 functions above to check rows, colums and all 3 x 3 blocks

def sudoku_grid_correct(sudoku: list):

    all_correct = True

    # Check if all blocks are correctly filled with 1 to 9

    block_row = 0

    while block_row <= 6:

        block_column= 0

        while block_column <= 6:
            if  block_correct(sudoku, block_row, block_column) == False:
                all_correct = False
            
            block_column += 3
        block_row += 3


    # Check if all rows are filled with numbers 1 to 9 and break the loop if row is incorrect

    row = 0

    while row <= 8:

        if row_correct(sudoku, row) == False:
            all_correct = False
            
        row += 1

    
    # Check if all colums are filled with numbers 1 to 9

    column = 0

    while column <= 8:
        

        if column_correct(sudoku, column) == False:
            all_correct = False
            

        column += 1
        

    return all_correct

if __name__ == "__main__":


    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))
    
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
    [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
    [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
    [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
    [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
    [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
    [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
    [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
    [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
    [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
    ]
    print(sudoku_grid_correct(sudoku3))