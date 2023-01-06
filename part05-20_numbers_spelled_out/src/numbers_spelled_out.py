# Write your solution here

def dict_of_numbers():


    numbers = {}

    singles = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    between = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    tens = { 10:"ten", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

    for key in range(0, 100):

        if key < 10:
            numbers[key] = singles[key]
        elif key > 10 and key < 20:
            numbers[key] = between[key]
        elif key % 10 == 0:
            numbers[key] = tens[key]
        elif key % 10 != 0:
            number = key % 10
            number2 = key - number
            numbers[key] = tens[number2] + "-" + singles[number]

    return numbers

    
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[11])
   