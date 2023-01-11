import string
import re

def change_case(orig_string: str):

    new_string = ""

    for char in orig_string:
        if char == char.upper():
            new_string += char.lower()
        elif char == char.lower():
            new_string += char.upper()


    return new_string


def split_in_half(orig_string: str):

    firstpart, secondpart = orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:]

    return firstpart, secondpart

def remove_special_characters(orig_string: str):
    
    
    new_string = re.sub(r"[^a-zA-Z0-9 ]", "", orig_string)

    return new_string

if __name__ == "__name__":
    str = "HellO WorlD"
    change_case(str)
    print(str)