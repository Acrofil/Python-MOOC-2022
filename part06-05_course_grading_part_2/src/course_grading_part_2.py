
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")


students = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

#Sum of completed exercises
exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue

        exercises_compleated = 0
        for exercise in parts[1:]:
            exercises_compleated += int(exercise)
        exercises[parts[0]] = exercises_compleated

#Exam points, total exam points per id
ex_points = {}

with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue

        total_points = 0
        for points in parts[1:]:
            total_points += int(points)
            ex_points[parts[0]] = total_points

#Calculating Total points from completed exercises
total_points = {}

for id, name in students.items():
    if id in exercises:
        points_exercise = exercises[id]
        total_points[id] = int(((((points_exercise)/40)*100)//10))

#Sum of exam points + the points from completed exercises
for id, name in students.items():
    if id in ex_points:
        points = ex_points[id]
        total_points[id] += int(points)


# Assigning final grades
final_grade = {}

#Comparing the final score with the grading table and assigning grades to the id
for id in students:

    if id in total_points:
        score = total_points[id]
        
        
        if score <= 14:
            final_grade[id] = 0
        elif score <= 17:
            final_grade[id] = 1
        elif score <= 20:
            final_grade[id] = 2
        elif score <= 23:
            final_grade[id] = 3
        elif score <= 27:
            final_grade[id] = 4
        else:
            final_grade[id] = 5


for id, name in students.items():
    if id in final_grade:
        result2 = final_grade[id]
    print(name, result2)
        