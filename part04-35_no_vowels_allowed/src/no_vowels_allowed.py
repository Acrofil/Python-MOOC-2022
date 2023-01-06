# Write your solution here

def no_vowels(string: str):

    new_string = string

    counter = 0
    for char in string:

        if char in string[counter] == "a" or char == "e" or char == "o" or char == "i" or char == "u":

            new_string =  new_string.replace(char, "")
        
        counter += 1
            
            
    
    return new_string


if __name__ == "__main__":
    my_string = "this is a longer sentence"
    print(no_vowels(my_string))