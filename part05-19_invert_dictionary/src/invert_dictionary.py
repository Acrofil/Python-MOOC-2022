# Write your solution here

def invert(dictionary: dict):

    dictionary_copy = {}

    for key, value in dictionary.items():
        dictionary_copy[value] = key

    dictionary.clear()

    for key, value in dictionary_copy.items():
        dictionary[key] = value


    #for word in dictionary:

        #dictionary[word] = dictionary[word]
    

    


if __name__ == "__main__":

    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)