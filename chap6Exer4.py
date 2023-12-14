#Exercise 4: Working with JSON File ☑️
#Create a JSON file named 'StudentJson.json' with the following details

#Ask the user to enter the student name, ID, and course and write these
#contents to the JSON file. 2.Read the contents from the JSON file and
#display the individual values.
#Expected Output :
#Details of the Student are
#Name: Alpha
#ID: 1
#course: BSc CC
#Append another dictionary as follows as key value pair for student 1 in
#StudentDetails dictionary to form a nested dictionay. Later update the JSON file.
# "CourseDetails":{
#"Group": "A",
#"Year": 2
#		}
#Print the individual vlaues of the Student details reading from JSON file.
#Expected Output :

#Details of the Student are
#Name: Alpha
#ID: 1
#course: BSc CC
#Group: A
#Year: 2

import json

#Function to get student details from user input
def get_student_details():
    name = input("Enter the student name: ")
    student_id = int(input("Enter the student ID: "))
    course = input("Enter the course: ")

    return {"Name": name, "ID": student_id, "course": course}

#Function to read student details from a JSON file
def read_student_details_from_file(file_path):
    with open(file_path, 'r') as file:
        student_data = json.load(file)
    return student_data

#Function to write student details to a JSON file
def write_student_details_to_file(file_path, student_data):
    with open(file_path, 'w') as file:
        json.dump(student_data, file, indent=2)

#Getting student details from user input
student_details = get_student_details()

#Writting student details to a JSON file
file_path = 'StudentJson.json'
write_student_details_to_file(file_path, student_details)

#Reading student details from the JSON file
read_student_details = read_student_details_from_file(file_path)

#Appending CourseDetails to the StudentDetails dictionary
read_student_details["CourseDetails"] = {
    "Group": input("Enter the group: "),
    "Year": int(input("Enter the year: "))
}

#Updating the JSON file with the new details
write_student_details_to_file(file_path, read_student_details)

#Displaying individual values
print("\nDetails of the Student are")
print(f"Name: {read_student_details['Name']}")
print(f"ID: {read_student_details['ID']}")
print(f"Course: {read_student_details['course']}")
print(f"Group: {read_student_details['CourseDetails']['Group']}")
print(f"Year: {read_student_details['CourseDetails']['Year']}")