# Write your solution here
word = input("Word: ")
 
frame = 30
frame_center = word.center(28)
word_lenght = len(word)
#space = ((frame_center - word_lenght) / 2)
 
print(frame * "*")
#print("*" + (" " * int(space) + word + (" " * int(space) + "*")))
print("*" + frame_center + "*")
print(frame * "*") 
