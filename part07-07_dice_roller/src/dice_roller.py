from random import randint, choice, sample

def roll(die: str):

    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }

    return sample(dices[die], 1)[0]

def play(die1: str, die2: str, times: int):
    
    die_one_wins = 0
    die_two_wins = 0
    die_tie = 0

    for i in range(times):

        roll_one = roll(die1)
        roll_two = roll(die2)
        

        if roll_one > roll_two:
            die_one_wins += 1
        elif roll_two > roll_one:
            die_two_wins += 1
        elif roll_one == roll_two:
            die_tie += 1

  
    return (die_one_wins, die_two_wins, die_tie)

if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
     
