input_string = input("Please type in a string: ")
 
vowels = ("a", "e", "o")
 
 
counter = 0
 
a = False
e = False
o = False
 
while counter < len(input_string):
 
    #if input_string[counter] in vowels:
        #print(f"{input_string[counter]} found")
    if input_string[counter] == "a":
        a = True
    elif input_string[counter] == "e":
        e = True
    elif input_string[counter] == "o":
        o = True
    counter += 1
 
if a == True:
    print("a found")
else:
    print("a not found")
if e == True:
    print("e found")
else:
    print("e not found")
if o == True:
    print("o found")
else:
    print("o not found") 
