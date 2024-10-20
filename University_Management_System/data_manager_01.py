import csv
from student_01 import Student
from faculty_01 import Faculty


# save Students to CSV
def save_students_to_file(students, filename= "students.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "WhatsApp Number", "Department", "Semester"])
        for student in students:
            writer.writerow([student.name, student.age, student.whatsApp_number, student.department, student.semester])

# load Student Data from CSV
def load_students_from_file(filename = "students.csv"):
    students = []
    try:
        with open(filename, mode= "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    name = row["Name"],
                    age = int(row["Age"]),
                    whatsApp_number = int(row["WhatsApp Number"]),
                    department = row["Department"],
                    semester = int(row["Semester"])
                )
                students.append(student)
    except FileNotFoundError:
        print(f"{filename} not found: Starting with empty list.")
    return students


# Save faculty Data to CSV

def save_faculty_to_file(faculty_members, filename = "faculty.csv"):
    with open(filename, mode= "w", newline= "") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "WhastApp Number", "Department"])
        for faculty in faculty_members:
            writer.writerow([faculty.name, faculty.age, faculty.whatsApp_number, faculty.department])


#load faculty data from CSV

def load_faculty_from_file(filename= "faculty.csv"):
    faculty_members = []
    try:
        with open(filename, mode= "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                faculty = Faculty(
                    name = row["Name"],
                    age = row["Age"],
                    whatsApp_number = row["WahtsApp Number"],
                    department = row["Department"]


                )

            faculty_members.append(faculty)
    except FileNotFoundError:
        print(f"{filename} not found: Starting from empty list.")
    return faculty_members


 

