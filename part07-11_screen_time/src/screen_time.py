from datetime import datetime, timedelta
#Write to file 
def write_to_file(filename: str, starting_date: datetime, end_date: datetime, sc_time: int, avg_sc_time: int, days: list, times: tuple):
#Start & end date format ddmmyy 
    write_start_date = starting_date.strftime("%d.%m.%Y")
    write_end_date = end_date.strftime("%d.%m.%Y")
#Open filename
    open(filename, "w").close()
    with open(filename, "a") as my_file:
        #Write date period, total & avg time
        my_file.write(f"Time period: {write_start_date}-{write_end_date}\n")
        my_file.write(f"Total minutes: {sc_time}\n")
        my_file.write(f"Average minutes: {avg_sc_time}\n")
#Enumerate over days and times
        for index, day in enumerate(days):
            
            my_file.write(f"{day}: {times[index][0]}/{times[index][1]}/{times[index][2]}\n")


def date_format(days_count: int, starting_date):

    days_from_starting_date = timedelta(days=days_count)
    days_calc = starting_date + days_from_starting_date

    return days_calc

def screen_time():

    filename = input("Filename: ")
    st_date = input("Starting date: ")
    total_days = int(input("How many days: "))


    starting_date = datetime.strptime(st_date, "%d.%m.%Y")
    end = timedelta(days=total_days)
    end2 = timedelta(days=1)
    end_date = starting_date + end - end2


    count = 0
    total_scr_time = []
#Add days to a list and times to a list as tuple
    days = []
    times = []

    print("Please type in screen time in minutes on each day (TV computer mobile)")

    while count < total_days:

        new_date = date_format(count, starting_date)

        display_date = new_date.strftime("%d.%m.%Y")
        days.append(display_date)
#Append days and times
        scr_time = input(f"Screen time {display_date}:")
        times.append(tuple(scr_time.split(" ")))

        scr_time_split = scr_time.split(" ")
        total_scr_time.append(scr_time_split)
        

        count += 1

#Calculate total screen time and avg sc time    
    total_screen_time = screen_time_minutes(total_scr_time)
    average_screen_time = total_screen_time / total_days

    write_to_file(filename, starting_date, end_date, total_screen_time, average_screen_time, days, times)

def screen_time_minutes(scr_time: list):

    total_minutes = 0

    for num in scr_time:
        print(num)

        for min in num:
            total_minutes += int(min)

    return total_minutes

def main():

    screen_time()

main()