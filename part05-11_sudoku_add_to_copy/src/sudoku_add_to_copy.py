# Write your solution here

def print_sudoku(sudoku: list):


    for row in range(len(sudoku)):
        print()

        for column in range(len(sudoku)):

            if column == 3:
                print(" ", end="")
            if column == 6:
                print(" ", end="")

            if sudoku[row][column] == 0:
                print("_ ", end="")
            elif sudoku[row][column] > 0:
                print(sudoku[row][column], end=" ")


        if row == 2:
            print()
        if row == 5:
            print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):

    sudoku_copy = []

    for row in sudoku:
       
        sudoku_copy.append(row[:])

    sudoku_copy[row_no][column_no] = number
    

   
    return sudoku_copy


if __name__ == "__main__":

    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)