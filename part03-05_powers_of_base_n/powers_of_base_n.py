# Write your solution here
up_limit = int(input("Upper limit: "))
base = int(input("Base: "))
 
power_base = 1
 
while power_base <= up_limit:
    print(power_base)
    power_base = power_base * base 
