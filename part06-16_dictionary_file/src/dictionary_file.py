
def dictionary_add_word(dictionary_file: str, finish_word: str, english_word: str):
    
    with open(dictionary_file, "a") as my_dictionary:

        my_dictionary.write(f"{finish_word};{english_word}\n")
        print("Dictionary entry added")



def dictionary_search_word(dictionary_file, search_term: str):


    with open(dictionary_file) as my_dictionary:

        for line in my_dictionary:
            
            words = line.split(";") 
            words = [word.strip() for word in words]
            if search_term in words[1] or search_term in words[0]:
                print(f"{words[0]} - {words[1]}")



def dictionary_main():

    dictionary_file = "dictionary.txt"
    while True:

        print("1 - Add word, 2 - Search, 3 - Quit")
        user_input = input("Function: ")

        if user_input == "3":
            print("Bye!")
            break
        elif user_input == "1":
            word_finish = input("The word in Finnish: ")
            word_english = input("The word in English: ")

            dictionary_add_word(dictionary_file, word_finish, word_english)
        elif user_input == "2":
            user_search = input("Search term: ")
            dictionary_search_word(dictionary_file, user_search)





dictionary_main()