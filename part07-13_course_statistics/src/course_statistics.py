import urllib.request
import json
import math

def retrieve_all():

    adress = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
#Requesting,reading and opening file
    my_request = urllib.request.urlopen(adress)
    data = my_request.read()

    courses = json.loads(data)
#List to store the needed data
    active_courses = []
    for course in courses:
        
        
        full_name = course["fullName"]
        name = course["name"]
        year = course["year"]
        exercises_sum = sum(course["exercises"])

        if course["enabled"] == True:

            active_courses.append((full_name, name, year, exercises_sum))

    
    return active_courses

def retrieve_course(course_name: str):

    adress = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    my_request = urllib.request.urlopen(adress)
    data = my_request.read()

    courses = json.loads(data)

    course_info = {}

    weeks = 0
    total_students = 0
    total_hours = 0
    
    total_exercises = 0
    
#This file is dict in dictionaries
    for c in courses:
#Counting how many weeks bases on itterations
        weeks += 1
#Getting the maximum number ever in these weeks
        if total_students < courses[c]["students"]:
            total_students = courses[c]["students"]

        total_hours += courses[c]["hour_total"]
        total_exercises += courses[c]["exercise_total"]


    avg_hours = total_hours / total_students  
    avg_exercises = total_exercises / total_students

#Adding the proccesed data in new dictionary

    course_info["weeks"] = weeks
    course_info["students"] = total_students
    course_info["hours"] = total_hours
    course_info["hours_average"] = math.floor(avg_hours)
    course_info["exercises"] = total_exercises
    course_info["exercises_average"] = math.floor(avg_exercises)
    
    return course_info



if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")