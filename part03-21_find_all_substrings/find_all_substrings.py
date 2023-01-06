word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
counter = 0
 
#while len(word) >= 3:
#
 #       index = word.find(character)
  #      if index == -1:
   #             break
    #    if index + 3 > len(word):
     #           break
      #  print(word[index:index+3])
       # word = word[index+1:]
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1 
