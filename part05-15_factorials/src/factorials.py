# Write your solution here

def factorials(n: int):

    factorials = {}
    factorial = 1
    for i in range(1, n + 1): #5
        factorial = factorial * i
        factorials[i] = factorial
        


    return factorials

if __name__ == "__main__":

    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])