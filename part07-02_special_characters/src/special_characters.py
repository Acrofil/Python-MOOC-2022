def separate_characters(my_string: str):
    import string

    upper_lower = string.ascii_letters
    punctuoation = string.punctuation

    u_and_l = ""
    punct = ""
    other = ""

    for char in my_string:
        if char in upper_lower:
            u_and_l += char
        elif char in punctuoation:
            punct += char
        else:
            other += char

    result = (u_and_l, punct, other)


    return result
    

   

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")