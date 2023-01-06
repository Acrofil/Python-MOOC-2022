# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
 
first = string.find(substring)
second = -1
 
if first != -1:
    string = string[first + len(substring):]
    second = string.find(substring)
 
 
if second == -1:
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " + str(first + len(substring) + second) + ".")
