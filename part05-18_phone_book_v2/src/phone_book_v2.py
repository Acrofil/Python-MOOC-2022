def search(phonebook):

    name_search = input("name: ")


    if name_search not in phonebook:
        print("no number")
    else:
        for number in phonebook[name_search]:
            print(number)
       

def add(phonebook):

    name_input = input("name: ")
    number_input = input("number: ")

    if name_input not in phonebook:
        phonebook[name_input] = []
    phonebook[name_input].append(number_input)

    
    print("ok!")

def main():

    phonebook = {}

    while True:

        main_menu = input("command (1 search, 2 add, 3 quit): ")

        if main_menu == "3":
            print("quitting...")
            break
        elif main_menu == "2":
            add(phonebook)
        elif main_menu == "1":
            search(phonebook)

main()