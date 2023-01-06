from random import choice, randint
from string import ascii_lowercase, digits

def add_char(password: str, chars):
    char = choice(chars)

    if randint(1, 2) == 1:
        return char + password
    else:
        return password + char


def generate_strong_password(leng: int, numbers: bool, special_chars: bool):

    
    spec_chars = "!?=+-()#"

    password = choice(ascii_lowercase)
    choice_set = ascii_lowercase

    if numbers:
        password = add_char(password, digits)
        choice_set += digits

    if special_chars:
        password = add_char(password, spec_chars)
        choice_set += spec_chars

    while leng > len(password):
        password = add_char(password, choice_set)

    
    return password

if __name__ == "__main__":

    for i in range(10):
        print(generate_strong_password(6, True, True))







