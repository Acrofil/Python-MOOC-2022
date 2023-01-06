# Write your solution here
def longest_series_of_neighbours(numbers: list):

    longest = 0
    total_len = len(numbers) - 1
    current = 0
    counter = 0
    counter2 = 1
    max_numbers = []

    while counter2 <= total_len:

        c = (abs(numbers[counter] - numbers[counter2]))

        if c == 1:
            current += 1
        elif c != 1:
            longest = current + 1
            max_numbers.append(longest)
            current = 0
            

        counter += 1
        counter2 += 1

    if current > 0:
        max_numbers.append(current + 1)
    
    return max(max_numbers)

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))