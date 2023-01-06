# Write your solution here

def column_correct(sudoku: list, column_no: int):

    numbers = []

    for number in sudoku:

        if number[column_no] > 0 and number[column_no] in numbers:
            return False

        numbers.append(number[column_no])

    return True

      

