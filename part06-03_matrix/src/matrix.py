# write your solution here

def matrix_sum():

    with open("matrix.txt") as new_file:
        
        total_sum = 0

        for number in new_file:
            number = number.replace("\n", "")
            part = number.split(",")

            for i in part:
                num = int(i)
                total_sum += num
        
        return total_sum


   # return result
def matrix_max():

    with open("matrix.txt") as new_file:

        largest_number = 0
        for number in new_file:
            number = number.replace("\n", "")
            part = number.split(",")
            
            for i in part:
                num = int(i)
                if num > largest_number:
                    largest_number = num

        return largest_number


def row_sums():

    with open("matrix.txt") as new_file:

        row_sums = []

        for row in new_file:
            number = row.replace("\n", "")
            part = row.split(",")

            total_sum = 0
            for i in part:
                num = int(i)
                total_sum += num
            
            row_sums.append(total_sum)
    
        return row_sums





if __name__ == "__main__":
    print(matrix_max())
    print(matrix_sum())
    print(row_sums())
    