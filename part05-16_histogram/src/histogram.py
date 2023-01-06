# Write your solution here

def histogram(word: str):

    chars = {}

    for char in word:
        if char not in chars:
            chars[char] = 0

        chars[char] += 1

    for char in chars:
        print(char, chars[char] * "*")

    
if __name__ == "__main__":

    histogram("abba")
