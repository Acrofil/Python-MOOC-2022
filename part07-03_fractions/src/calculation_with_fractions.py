def fractionate(amount: int):

    from fractions import Fraction
    
    frac = []
    
    for a in range(amount):
        frac.append(Fraction(1, amount))
        


    return frac
    
if __name__ == "__main__":
    
    for p in fractionate(3):
        print(p)


    print(fractionate(5))