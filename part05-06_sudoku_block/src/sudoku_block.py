# Write your solution here

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

if __name__ == "__main__":

    sudoku = [
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

    print(block_correct(sudoku, 3, 6))
    #print(block_correct(sudoku, 1, 2))
