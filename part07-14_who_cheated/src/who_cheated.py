from datetime import datetime, timedelta

def cheaters():

    start_file = "start_times.csv"
    submision_file = "submissions.csv"

    with open(start_file) as start_times:

        students_start_times = {}

        for line in start_times:
            line = line.replace("\n", "")
            part = line.split(";")
            
            
            start_time = datetime.strptime(part[1], "%H:%M")

            students_start_times[part[0]] = datetime.strptime(part[1], "%H:%M")
       

        students_end_times = {}
        cheaters = []  

    
    with open(submision_file) as end_times:

        for line in end_times:
            line = line.replace("\n", "")
            part = line.split(";")
            
            end_time = datetime.strftime(part[-1], "%H:%M")

            if part[0] in students_start_times:
                students_end_times[part[0]] = datetime.strptime(part[-1], "%H:%M")
    
    
    for student in students_end_times:
        if student in students_start_times:
            if students_end_times[student] - students_start_times[student] > timedelta(hours=3):
                cheaters.append(student)

    print(cheaters)
def main():

    
    cheaters()


main()