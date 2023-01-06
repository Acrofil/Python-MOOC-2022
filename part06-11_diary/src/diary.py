# Write your solution here

def add_to_diary(diary_entry: str):

    with open("diary.txt", "a") as my_file:

        my_file.write(f"{diary_entry}\n")
        print("Diary saved")



def read_diary():

    with open("diary.txt") as my_file:

        print("Entries: ")
        
        for line in my_file:
            
            print(line.strip())


def menu():

    while True:

        print("1 - add an entry, 2 - read entries, 0 - quit")
        choice = input("Function: ")

        if choice == "0":
            print("Bye now!")
            break
        
        elif choice == "1":
            diary_entry = input("Diary entry: ")
            add_to_diary(diary_entry)
        
        elif choice == "2":
            read_diary()



menu()