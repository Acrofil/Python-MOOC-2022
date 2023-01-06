# Write your solution here
string = input("Please type in a word: ")
char = input("Please type in a character: ")
 
counter = 0
 
while  counter < len(string):
    word = string.find(char)
 
    if word >= 0:
        end = word + 3
        if len(string[word : end]) < 3:
            break
        else:
            print(string[word : end])
            break
        
    counter += 1 
