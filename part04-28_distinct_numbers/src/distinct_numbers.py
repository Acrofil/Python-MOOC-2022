# Write your solution here
def distinct_numbers(my_list: list):

    new = sorted(my_list)

    for i in my_list:

        if new.count(i) > 1:
            new.remove(i)
        
    print(new)
    return new

