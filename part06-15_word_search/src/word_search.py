# Write your solution here
def find_words(search_term: str):

    with open("words.txt") as file:

#Store the words we find
        words = []
#Read the file
        for word in file:
            line = word.replace("\n", "")
#Find all posible words when the searched word has "."   
            if "." in search_term and len(search_term) == len(line):
                q = []
                for a, j in enumerate(search_term):
                    if j != ".":
                        if j != line[a]:
                            q.append(False)
                        else:
                            q.append(True)
                if False not in q:
                    words.append(line)

            elif line == search_term:
                words.append(line)
            elif search_term[0] == "*" and line.endswith(search_term[1::]):
                words.append(line)
            elif search_term[-1] == "*" and line.startswith(search_term[0:-1]):
                words.append(line)
            
        print(words)
        return words

if __name__ == "__main__":
    find_words("c.d.")