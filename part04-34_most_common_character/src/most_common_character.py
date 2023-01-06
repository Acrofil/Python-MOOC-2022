# Write your solution here
def most_common_character(my_string: str):

    counter = 0
    most_chars = ""

    for char in my_string:
        
        if my_string.count(char) > counter:
            counter = my_string.count(char)
            most_chars = char
    
    return most_chars

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))