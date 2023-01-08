from datetime import datetime, timedelta

def cheaters():

    start_file = "start_times.csv"
    submision_file = "submissions.csv"

    with open(start_file) as start_times:

        cheaters = []

        for line in start_times:
            line = line.replace("\n", "")
            part = line.split(";")
            
            
            start_time = datetime.strptime(part[1], "%H:%M")
            
            
            
    with open(submision_file) as end_times:

        for line in end_times:
            line = line.replace("\n", "")
            part = line.split(";")
            
            end_time = datetime.strptime(part[-1], "%H:%M")

    
    print(students_dic)

def main():

    
    cheaters()


main()