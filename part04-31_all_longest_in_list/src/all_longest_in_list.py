# Write your solution here
def all_the_longest(strings: list):

    result = []
    
    for string in strings:
        
        if len(string) > len(result):
            result = string
    
    return result

    