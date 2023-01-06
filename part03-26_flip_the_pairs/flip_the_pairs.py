 Write your solution here
number = int(input("Please type in a number: "))
 
if number == 1:
    print(number)
counter = 2
while counter <= number:
    
 
    print(counter)
    
    if counter % 2 == 0:
        counter -= 1
        print(counter)
    counter += 3
    if counter > number:
        counter -= 1 
