
#Writing to the file persons.csv on new line without deleting
def open_and_write(name, age, heigh):
    
    with open("people.csv", "a") as file:

        file.write(f"{name};{age};{heigh}\n")



#Assigning names and passing it to be writen
def store_personal_data(person: tuple):

    name = person[0]
    age = person[1]
    heigh = person[2]

    open_and_write(name, age, heigh)

            



#Person data as tuple
if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))