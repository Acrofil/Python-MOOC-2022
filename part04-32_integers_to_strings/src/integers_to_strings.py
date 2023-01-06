# Write your solution here

def formatted(numbers: list):

    formated_list = []

    for number in numbers:

        formated_list.append("%.2f"%number)


    return formated_list