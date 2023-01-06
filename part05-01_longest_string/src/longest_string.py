# Write your solution here

def longest(strings: list):

    longest = 0
    longest_string = ""

    for string in strings:
        
        if len(string) > longest:
            longest = len(string)
            longest_string = string

    return longest_string
    
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

