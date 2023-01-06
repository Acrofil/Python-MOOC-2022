
#if False:
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_information = input("Course information: ")
#else:
#    student_info = "students1.csv"
#    exercise_data = "exercises1.csv"
#    exam_points = "exam_points1.csv"
#    course_information = "course1.txt"


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
exercise_points = {}

for id, name in students.items():
    if id in exercises:
        points_exercise = exercises[id]
        total_points[id] = int(((((points_exercise)/40)*100)//10))
        exercise_points[id] = int(((((points_exercise)/40)*100)//10))

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

open("results.csv", 'w').close()
with open("results.csv", "w") as final_results:

    for id, name in students.items():

        final_results.write(f"{id};{name};{final_grade[id]}\n")

    




with open(course_information) as new_file:

    course = []
    

    for line in new_file:

        parts = line.split(":")
        line = line.replace("\n", "")
        
        course.append(parts)


    crd = course[1][1].strip()
    
#Delete old data
open("results.txt", 'w').close()
with open("results.txt", "w") as file:

    nm = "name"
    exc = "exec_nbr"
    exc_pts = "exec_pts."
    exm = "exm_pts."
    tot = "tot_pts."
    grade = "grade"
    underline = "="

    file.write((f"{course[0][1].strip()}, {crd} credits"))
    file.write(f"\n")
    file.write(38 * "=")
    file.write("\n")
    file.write((f"{nm:30}{exc:<10}{exc_pts:10}{exm:<10}{tot:10}{grade:10}\n"))
    for id, name in students.items():
        if id in exercises and id in exercise_points and id in ex_points and id in total_points and id in final_grade:
            exs = exercises[id]
            excp = exercise_points[id]
            exmp = ex_points[id]
            ttp = total_points[id]
            fng = final_grade[id]
            
            file.write((f"{name:30}{exs:<10}{excp:<10}{exmp:<10}{ttp:<10}{fng:<10}\n"))
            

print("Results written to files results.txt and results.csv")





