# Write your solution here

def times_ten(start_index: int, end_index: int):

    my_dictionary = {}

    for i in range(start_index, end_index + 1):
        ten = i * 10
        my_dictionary[i] = ten

    
    return my_dictionary
    



if __name__ == "__main__":


    d = times_ten(3, 6)
    print(d)