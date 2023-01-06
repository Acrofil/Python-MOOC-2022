# Write your solution here

numbers = []

while True:

    
    number_input = int(input("New item: "))
    
    if number_input == 0:
        print("Bye!")
        break

    numbers.append(number_input)
    in_order = sorted(numbers)

    print(f"The list now: {numbers}")

    print(f"The list in order: {in_order}")
