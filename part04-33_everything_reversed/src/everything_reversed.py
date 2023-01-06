# Write your solution here
def everything_reversed(strings: list):

    new_list = []

    for word in strings:

        new_list.append(word[::-1])



    return new_list[::-1]



if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

    
    everything_reversed(['abc', 'def'])