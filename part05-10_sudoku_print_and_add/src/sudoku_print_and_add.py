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






def add_number(sudoku: list, row_no: int, column_no: int, number:int):

    sudoku[row_no][column_no] = number






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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)