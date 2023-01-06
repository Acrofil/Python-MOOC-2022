# Write your solution here

counter = 1
my_list = []

while True:
    

    print(f"The list is now {my_list}")

    user_input = input("a(d)d, (r)emove or e(x)it: ")

    if user_input == "x":
        break
    elif user_input == "d":
        my_list.append(counter)
        counter += 1
    elif user_input == "r":
        my_list.pop(len(my_list) - 1)
        counter -= 1
    

print("Bye!")