# Write your solution here


def spruce(height: int):

    spruce_end = height
    i = 1
    stars = 1


    print("a spruce!")

    while i <= height:

        if i <= height:
            print( ((i * height - 1) * " ") + (stars * "*"))
            height -= 1
            stars += 2

    print((spruce_end - 1) * " " + "*")

# Write your solution here
 



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)