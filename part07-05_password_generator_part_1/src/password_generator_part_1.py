def generate_password(lengh: int):

    import random
    import string

    letters = string.ascii_lowercase
    password = ""

    for i in range(lengh):

        password += "".join(random.choice(letters))
    

    return password


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))


