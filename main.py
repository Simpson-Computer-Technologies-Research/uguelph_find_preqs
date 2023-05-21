from courses import Courses
import json

# Path: main.py
def main(query: str):
    # get the courses
    courses = Courses.query(query)

    # get the details
    details = Courses.details(courses, query)

    # get the requisites
    requisites = Courses.requisites(details)

    # write requesites to file
    with open("requisites.json", "w") as f:
        f.write(json.dumps(requisites, indent=4))

# run the main function
if __name__ == "__main__":
    main("CIS*4650")