# Write your solution here
 
string_input = input("Please type in a string: ")
 
lenght = len(string_input)
 
if string_input[1] == string_input[lenght - 2]:
    print(f"The second and the second to last characters are {string_input[1]} ")
else:
    print("The second and the second to last characters are different") 
