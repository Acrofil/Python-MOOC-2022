# Write your solution here

def first_word(word1: str):
# 1.Finding the first word in a sentence

    word_start = 0
    word_end = word1.find(" ")
    word1 = word1[word_start:word_end]
    return word1

def second_word(word2: str):

# Check the sentence if its only of two words and return second word
    two_words = ""
    
    if word2.count(" ") == 1:
        two_words = word2.find(" ")
        word2 = word2[two_words +1::]

        return word2

# Return the second word of a sentence
    start_word2 = first_word(word2) # Once
    word2_start = len(start_word2) + 1
    word2_end = 0

    i = len(start_word2) + 1

    while i < len(word2):
        if word2[i] == " ":
            word2_end = i
            break
        i += 1
            
        
    word2 = word2[len(start_word2) + 1:word2_end]
    return word2

def last_word(word3: str):

# Finding the last word of a sentence with for loop using negative itteration  
    last_word = ""
    
    for i in range(len(word3)- 1, -1, -1):
        if word3[i] == " ":
            last_word = word3[i + 1:]
            break

    return last_word
            

# You can test your function by calling it within the following block


if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))