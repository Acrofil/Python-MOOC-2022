# Write your solution here

def final_statistic(grades: list, average: int, fails: int, submisions):

    fail = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0

    for grade in grades:

        if grade == 0:
            fail += 1
        elif grade == 1:
            one += 1
        elif grade == 2:
            two += 1
        elif grade == 3:
            three += 1
        elif grade == 4:
            four += 1
        elif grade == 5:
            five += 1

    passing = one + two + three + four + five
    pass_percent = float((100 / submisions) * passing)

    print("Statistics:")
    print(f"Points average: {average}")
    print(f"Pass percentage: {pass_percent:.1f}")
    print("Grade distribution:")
    print("5:", five * "*")
    print("4:", four * "*")
    print("3:", three * "*")
    print("2:", two * "*")
    print("1:", one * "*")
    print("0:", (fail + fails) * "*")



def grade(point_total: list, less_than_ten: list, submisions: int):

    submisions = submisions
    grades = []
    average = (sum(point_total) + sum(less_than_ten)) / submisions

    for points in point_total:
        
        if points <= 14:
            grades.append(0)
        elif points >= 15 and points <= 17:
            grades.append(1)
        elif points >= 18 and points <= 20:
            grades.append(2)
        elif points >= 21 and points <= 23:
            grades.append(3)
        elif points >= 24 and points <= 27:
            grades.append(4)
        elif points >= 28 and points <= 30:
            grades.append(5)


    fails = len(less_than_ten)


    final_statistic(grades, average, fails, submisions)


def main():

    submisions = 0
    less_than_ten_points = []
    points_total = []
    
    
    while True:

        statistic_input = input("Exam points and exercises completed: ")

        if statistic_input == "":
            break

        points_from_exam_and_exercises = statistic_input.split(" ")

        exams_points = int(points_from_exam_and_exercises[0])
        exercises_points = int(points_from_exam_and_exercises[1])


        if exams_points > 20 or exercises_points > 100:
            break

        points_exercises = calculate_exercise_points(exercises_points)

        if exams_points < 10:
            total = exams_points + points_exercises
            less_than_ten_points.append(total)

        elif exams_points >= 10:
            total_points = exams_points + points_exercises
            points_total.append(total_points)

        submisions += 1

    
    

    grade(points_total, less_than_ten_points, submisions)

def calculate_exercise_points(exercises: int):
    

    point_for_exercises = 0

    if exercises >= 10 and exercises <= 19:
        point_for_exercises = 1
    elif exercises >= 20 and exercises <= 29:
        point_for_exercises = 2
    elif exercises >= 30 and exercises < 39:
        point_for_exercises = 3
    elif exercises >= 40 and exercises < 49:
        point_for_exercises = 4
    elif exercises >= 50 and exercises < 59:
        point_for_exercises = 5
    elif exercises >= 60 and exercises < 69:
        point_for_exercises = 6
    elif exercises >= 70 and exercises < 79:
        point_for_exercises = 7
    elif exercises >= 80 and exercises < 89:
        point_for_exercises = 8
    elif exercises >= 90 and exercises < 100:
        point_for_exercises = 9
    elif exercises >= 100:
        point_for_exercises = 10


    return point_for_exercises




main()