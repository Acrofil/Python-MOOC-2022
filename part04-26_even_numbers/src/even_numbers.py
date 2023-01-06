# Write your solution here

def even_numbers(my_list: list):

    even_numbers = []
    
    for i in my_list:

        if i % 2 == 0:
            even_numbers.append(i)

    return even_numbers
