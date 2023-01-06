limit = int(input("Limit:"))
number = 1
sum = 1
print("The consecutive sum: 1", end = " ")
while sum < limit:
    number += 1
    sum +=  number
    print(f'+ {number}', end = " ")
 
print(f'= {sum}') 
