# Write your solution here
number = int(input("Limit: "))
 
counter = 1
sum_cons = 1
 
while sum_cons <  number:
    counter += 1
    sum_cons += counter
 
 
print(sum_cons) 
