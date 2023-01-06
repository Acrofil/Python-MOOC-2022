# Write your solution here
number = int(input("Please type in a number: "))
 
counter = 1
 
while number >= counter:
    
    i = counter
    counter2 = 1
    
    while counter2 <= number:
        
        result = i * counter2
        print(f"{i} x {counter2} = {result}")
        counter2 += 1
    counter += 1
 
