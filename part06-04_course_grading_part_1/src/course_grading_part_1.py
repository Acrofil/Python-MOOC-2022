# write your solution here


# this is never executed
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
    
# hard-coded input
#student_info = "students1.csv"
#exercise_data = "exercises1.csv"


students = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

    
exercises = {}

with open(exercise_data) as new_file2:
    for line in new_file2:
        parts = line.split(";")
        if parts[0] == "id":
            continue

        total_exersises = 0
        for grade in parts[1:]:
            total_exersises = total_exersises + int(grade)
        exercises[parts[0]] = total_exersises


for id, name in students.items():
    if id in exercises:
        total_points = exercises[id]
        print(name.strip(), total_points)