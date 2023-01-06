# Write your solution here

def add_student(students: dict, name: str):
    
    students[name] = {}

def print_student(students: dict, name: str):

    print(students)
    if name not in students:
        print(f"{name}: no such person in the database")
        
    elif name in students:
        print(f"{name}:")
        print(" no completed courses")
            

def add_course(students: dict, name: str, course_info: tuple):
    
    if students[name] == "no completed courses" or students[name] == "": 
        students[name] = []

    students[name].append(tuple(course_info))

    print(students)

        

    
    


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")



