from random import choice, sample
def words(n: int, beginning: str):

    with open("words.txt") as file:

        word_list = []

        for line in file:
            line = line.replace("\n", "")
            
            if line.startswith(beginning) and line not in word_list:
                word_list.append(line)
    
    if len(word_list) < n:
        raise ValueError("Not enough suitable words can be found!")
            
    

    return sample(word_list, n)

if __name__ == "__main__":

    word_list = words(3, "ca")
    for word in word_list:
        print(word)