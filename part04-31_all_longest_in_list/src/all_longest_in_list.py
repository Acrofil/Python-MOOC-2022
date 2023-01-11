# Write your solution here
def all_the_longest(strings: list):

    result = []
    word = 0


    for i in strings:
        if len(i) > word:
            word = len(i)

    for i in strings:
        if len(i) == word:
            result.append(i)
        
    
    return result

if __name__ == "__name__":

    words = ['Alan', 'Grace', 'Steve', 'Susan']
    all_the_longest(words)