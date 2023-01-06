# Write your solution here
string = input("Please type in a sentence: ")
 
space = 0
while space >= 0:
   if len(string) == 1:
      print(string[0])
      break
   else:
      space = string.find(" ")
      word = string[:space]
      string = string[space + 1:]
      print(word[0]) 
