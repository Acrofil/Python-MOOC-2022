import difflib

def put_file_lines_list(file_name):

    with open(file_name) as file:
        file_as_list = []

        for line in file:
            line = line.replace("\n", "")
            file_as_list.append(line)
        return file_as_list



def spellcheck():

    words = input("Write text: ")

    new_words = words.split(" ")

    corrected_word = ""

    all_words = put_file_lines_list("wordlist.txt")

    wrong_words = []

    for word in new_words:
        if word.lower() in all_words:
            corrected_word += word + " "
        else:
            corrected_word += "*" + word + "* "
            wrong_words.append(word)


    print(corrected_word)
    print("suggestions: ")
    for word in wrong_words:
        
    
        close = ", ".join(difflib.get_close_matches(word, all_words))


        suggestions = close
        print(f"{word}: {suggestions}")

   
        
    
    


spellcheck()