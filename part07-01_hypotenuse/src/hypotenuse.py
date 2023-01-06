def hypotenuse(leg1: float, leg2: float):

    from math import sqrt

    c = sqrt(leg1 ** 2 + leg2 ** 2)
    

    return c



if __name__ == "__main__":
    print(hypotenuse(3,4))