def lottery_numbers(amount: int, lower: int, upper: int):
    from random import sample

    numbers_pool = list(range(lower, upper))
    draw = sample(numbers_pool, amount)

    return sorted(draw)



if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)