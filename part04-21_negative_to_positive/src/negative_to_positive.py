# Write your solution here

positive_number = int(input("Please type in a positive integer: "))

for i in range(-positive_number, positive_number + 1, 1):
    if i == 0:
        continue
    print(i)