# Write your solution here
def sum_of_positives(my_list: list):
    
    positive_numbers_sum = 0

    for i in my_list:
        if i >= 0:
            positive_numbers_sum += i

    return positive_numbers_sum
    