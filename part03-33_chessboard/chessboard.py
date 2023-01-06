def chessboard(number):
 
    row = ""
    column = ""
 
    counter = 0
 
    while counter < number:
        if counter % 2 == 0:
            row += "1"
            column += "0"
        else:
            row += "0"
            column += "1"
        
        counter += 1
    
    counter2 = 0
 
    while counter2 < number:
        if counter2 % 2 == 0:
            print(row)
        else:
            print(column)
        counter2 += 1
 
# Testing the function
if __name__ == "__main__":
    chessboard(3) 
