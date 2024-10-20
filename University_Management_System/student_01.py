from person_01 import Person
class Student(Person):
    def __init__(self, name: str, age: int, whatsApp_number: int, department:str, semester:int):
        super().__init__(name, age, whatsApp_number)
        self.department = department
        self.semester = semester 
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return (f"{self.__class__.__name__}(Name: {self.name}, Age: {self.age}, WhatsApp_Number: {self.whatsApp_number}, "
        f"Department: {self.department}, Semester: {self.semester}, Courses: {self.courses})")
    


student = Student(name="Bilal", age="25", whatsApp_number="03008126945", department= "Computer Science", semester= "1st")

student.enroll_in_course(course="C++")
print(student)
