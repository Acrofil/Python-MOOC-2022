# Write your solution here

#Calculating the students result, writing it on the correct or incorrect csv file
def calculation(students_solution: list, correct_file, incorrect_file):

    open(correct_file, "w").close()
    open(incorrect_file, "w").close()

    correct = open(correct_file, "w")
    incorrect = open(incorrect_file, "w")

#Eval() evaluates the expresion "2+2" from string so we can compare it with the student result
    for student in students_solution:
        
        student_sol = ';'.join(student)

        if eval(student[1]) == int(student[2]):
            correct.write(student_sol)
        elif eval(student[1]) != int(student[2]):
            incorrect.write(student_sol)


#Reading solutions.csv and extracting in a list
def open_file(filename):

    students = []
    with open(filename) as new_file:

        for line in new_file:
            parts = line.split(";")
            
            
            numbers = (parts[0], parts[1], parts[2])
            students.append(numbers)
    
    return students

#Main start function
def filter_solutions():

    data = open_file("solutions.csv")
    calculation(data, "correct.csv", "incorrect.csv")



if __name__ == "__main__":
    filter_solutions()