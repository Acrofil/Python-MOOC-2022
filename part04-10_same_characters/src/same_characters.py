# Write your solution here

def same_chars(string: str, index1: int, index2: int):

    if len(string) <= index2 or len(string) <= index1:
        return False
    
    if string[index1] == string[index2]:
        return True
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))