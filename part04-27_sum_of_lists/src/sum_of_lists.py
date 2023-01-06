# Write your solution here

def list_sum(numbers1: list, numbers2: list):

    size = min(len(numbers1), len(numbers2))

    sum = 0
    new = []
    for i in range(size):

        sum = numbers1[i] + numbers2[i]
        new.append(sum)



    return new