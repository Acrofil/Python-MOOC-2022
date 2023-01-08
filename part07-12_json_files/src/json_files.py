import json

def print_persons(filename: str):

    with open(filename) as my_file:
        data = my_file.read()

    course = json.loads(data)

    for person in course:
        
        name = person["name"]
        age = str(person["age"]) + " years" 
        hobbies = ", ".join(person["hobbies"])
        
        print(f"{name} {age} ({hobbies})")

if __name__ == "__main__":
    print_persons("file1.json")

