# write your solution here

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

    for word in new_words:
        if word.lower() in all_words:
            corrected_word += word + " "
        else:
            corrected_word += "*" + word + "* "

            
            
    
    print(corrected_word)
    


spellcheck()