# Write your solution here

my_phonebook = {}

while True:

    main_menu = input("command (1 search, 2 add, 3 quit): ")

    if main_menu == "3":
        print("quitting...")
        break

    elif main_menu == "2":

        name_input = input("name: ")
        number_input = input("number: ")


        my_phonebook[name_input] = number_input

        print("ok!")

    elif main_menu == "1":


        name_search = input("name: ")


        if name_search not in my_phonebook:
            print("no number")
        else:
            name = my_phonebook[name_search]
            print(name)

        