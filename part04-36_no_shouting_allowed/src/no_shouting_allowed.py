# Write your solution here
def no_shouting(strings: list):

    strings_lower_case = []


   


    for word in strings:

        if word.isupper() != True:
            strings_lower_case.append(word)

    
    return strings_lower_case
