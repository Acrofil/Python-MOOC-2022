# Write your solution here

def create_tuple(x: int, y: int, z: int):


    a_tuple = (x, y, z)
    
    minn = min(a_tuple)
    maxx = max(a_tuple)
    summ = sum(a_tuple)
    
    new_tuple = (minn, maxx, summ)

    return new_tuple


        


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))