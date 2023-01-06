# Write your solution here
def read_input(ask: str, number1, number2):

    while True:

        try:
            number = input(ask)
            number = int(number)
        except ValueError:

            number = -1


        if number <= number1 or number >= number2:
            print(f"You must type in an integer between {number1} and {number2}")
        elif number > number1 or number < number2:
            return number
    
        



if __name__ == "__main__":
    number = read_input("Please type in a number: ", 1, 5)
    print("You typed in:", number)