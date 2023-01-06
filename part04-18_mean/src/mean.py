# Write your solution here

def mean(my_list: list):

    lenght = len(my_list)
    list_sum = sum(my_list)

    return list_sum / lenght

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3]
    result = mean(my_list)
    print(result)