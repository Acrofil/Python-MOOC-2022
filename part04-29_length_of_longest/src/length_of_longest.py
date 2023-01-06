# Write your solution here
def length_of_longest(my_list: list):

    longest = 0
    word = ""

    for i in range(len(my_list)):

        word = my_list[i]

        if len(word) > longest:
            longest = len(word)

    return longest