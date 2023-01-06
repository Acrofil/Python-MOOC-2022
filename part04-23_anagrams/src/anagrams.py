# Write your solution here

def anagrams(word1: str, word2: str):


    if sorted(word1) != sorted(word2):
        return False
    else:
        return True




if __name__ == "__main__":
    print(anagrams("tame", "meta"))

