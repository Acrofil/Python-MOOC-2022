# Write your solution here
number = int(input("Please type in a number: "))
 
increase = 1
 
while increase <= number:
    print(increase)
 
    if number > increase:
        print(number)
        number -= 1
    increase += 1 
