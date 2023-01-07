from datetime import datetime

def control_character(pic: str, valid: bool):

    valid = None
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    nine_digits = pic[0:6] + pic[7:10]
    
    control_char = int(nine_digits) % 31

    if control_chars[control_char] != pic[-1]:
        valid = False
    else:
        valid= True
    
    return valid
        
    
def is_it_valid(pic: str):

    is_it_valid = True

# Check if its correct lenght
    if len(pic) > 11:
        is_it_valid = False
        return is_it_valid

    day = int(pic[0:2])
    month = int(pic[2:4])
    
    if "+" in pic:
        year =  "18" + pic[4:6]
        pic_year = int(year)
    elif "-" in pic:
        year = "19" + pic[4:6]
        pic_year = int(year)
    elif "A" in pic:
        year = "20" + pic[4:6]
        pic_year = int(year)
    else:
        return is_it_valid == False

#Check if its correct date format
    try:
        date = datetime(pic_year, month, day)

    except ValueError: return is_it_valid == False 
    
#Check if control character is valid
    is_it_valid = control_character(pic, is_it_valid)

    return is_it_valid

if __name__ == "__main__":
    a = "290200-1239"
    print(is_it_valid(a))