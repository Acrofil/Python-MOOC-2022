# Write your solution here
def shortest(strings: list):

    shortest_word = min(strings, key=len)

    return shortest_word

if __name__ == "__main__":
    shortest(["abc", "ab"])
    print(shortest(['Alan', 'Kim', 'Susan', 'Seymour', 'Kim', 'Susan']))