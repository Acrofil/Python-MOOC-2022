from datetime import datetime

def date_birth(day: int, month: int, year: int):

    eve_milenium = datetime(1999, 12, 31)
    born_year = datetime(year, month, day)

    days_old_at_eve = eve_milenium - born_year


    if year >= 2000:
       return print("You weren't born yet on the eve of the new millennium.")

    return print(f"You were {days_old_at_eve.days} days old on the eve of the new millennium.")


def main():

    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))


    date_birth(day, month, year)


main()

