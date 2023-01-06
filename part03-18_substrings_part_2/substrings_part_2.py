# Write your solution here
string1 = input("Please type in a string: ")
 
lenght = 1
string_end = len(string1) - 1
string_start = string_end - string_end
 
while lenght <= len(string1):
    print(string1[string_end:len(string1)])
    
    string_end -= 1
    lenght += 1 
