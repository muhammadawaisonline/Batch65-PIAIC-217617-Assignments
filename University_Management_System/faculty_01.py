from person_01 import Person

class Faculty(Person):
    def __init__(self, name:str, age:int, whatsApp_number:int, department:str):
        super().__init__(name, age, whatsApp_number)
        self.department = department
        self.courses = []

    def assign_course(self, course: str):
        self.courses.append(course)

    def __str__(self):
        return f"{self.__class__.__name__}(Faculty Name: {self.name}, Department: {self.department}, Courses: {self.courses})"
    

faculty = Faculty(name="Sir Zia Khan Sb", age= 45, whatsApp_number= 923121234567, department="Computer Science")
faculty.assign_course(course="LangGraph")

print(faculty)