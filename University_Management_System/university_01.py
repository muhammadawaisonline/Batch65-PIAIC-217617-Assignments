from data_manager_01 import save_students_to_file, save_faculty_to_file, load_faculty_from_file, load_students_from_file

class Panaversity:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculty = []
        self.courses = []
    
    def add_student(self, student):
         self.students.append(student)
        

    def add_faculty(self, faculty):
        self.faculty.append(faculty)
        
    def add_course(self, course):
        self.courses.append(course)

# Save Data to CSV file
    def save_data(self):
        save_students_to_file(self.students, "students.csv")
        save_faculty_to_file(self.faculty, "faculty.csv")
        print("Data Saved to Files.")

    #load Data from csv file
    def load_data(self):
        self.students = load_students_from_file("students.csv")
        self.students = load_faculty_from_file("faculty.csv")
        print("Data loaded from Files")

    def __str__(self):
        return f"University: {self.name}"
    
panaversity = Panaversity("Panaversity Urdu")
print(panaversity)