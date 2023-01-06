# Write your solution here
# You can test your function by calling it within the following block
 
def line(lenght: int, text: str):
 
    if text == "":
        print("*" * lenght)
    else:
        print(text[0] * lenght)
 
def box_of_hashes(height: int):
    
    index = 0
 
    while index <= height:
        line(height, "#")
 
        index += 1
    
 
    
 
 
 
if __name__ == "__main__":
    line(5, "")
    box_of_hashes(10)
