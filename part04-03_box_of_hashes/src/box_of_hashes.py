# Copy here code of line function from previous exercise
def line(lenght: int, text: str):
 
    if text == "":
        print("*" * lenght)
    else:
        print(text[0] * lenght)
 
 
def box_of_hashes(height: int):
    # You should call function line here with proper parameters
 
    index = 0
 
    while index < height:
        line(10, "#")
 
        index += 1
 
 
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5) 
