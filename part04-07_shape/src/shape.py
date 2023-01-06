# Copy here code of line function from previous exercise and use it in your solution
def line(lenght: int, text: str):
 
    if text == "":
        print("*" * lenght)
    else:
        print(text[0] * lenght)
 
#Main part of the exercise
def shape(width: int, symbol: str, height: int, filler: int):
 
    index = 0
 
    while index <= width:
        line(index, symbol)
 
        index += 1
    
    index2 = 0
 
    while index2 < height:
        line(width, filler)
 
        index2 += 1
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    shape(2, "o", 4, "+")
    shape(3, ".", 0, ",") 
