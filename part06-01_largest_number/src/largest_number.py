# write your solution here

def largest():

    with open("numbers.txt") as new_file:

        largest = 0
        number = 0
        for i in new_file:
            number = int(i)
            if number > largest:
                largest = number

    return largest


if __name__ == "__main__":

    print(largest())
