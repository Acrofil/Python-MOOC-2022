# Write your solution here

def oldest_person(people: list):

    years = []

    for name in people:
        
        if name[1] not in years:
            years.append(name[1])

    
    oldest = min(years)

    for name in people:
        if oldest in name:
            return name[0]
        

    
    



if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))