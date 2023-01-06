# Write your solution here
while True:
    #Ask the user what editor they use
    user_input = input("Editor: ")
 
    if "visual studio code" == user_input.lower():
        print("an excellent choice!")
        break
    elif  "vim" == user_input.lower() or "atom" == user_input.lower() or "emacs" == user_input.lower():
        print("not good")
    elif "word" == user_input.lower() or "notepad" == user_input.lower():
        print("awful")
