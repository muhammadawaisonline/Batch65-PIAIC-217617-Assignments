from student_01 import Student
from course_01 import Course
from faculty_01 import Faculty
from university_01 import Panaversity

def main():
    university = Panaversity("Panaversity Urdu")

    # Loading Unverity data
    university.load_data()

    # Add Courses
    course1 = Course(course_name= "Python", course_code="CS301", credits= 32)
    course2 = Course(course_name= "LangChain", course_code= "CS302", credits= 32)
    course3 = Course(course_name= "Microservices", course_code= "CS303", credits=32)

    university.add_course(course1)
    university.add_course(course2)
    university.add_course(course3)

    # Add new students and Faculty

    student1 = Student(name= "Muhammad Awais", age= 18, whatsApp_number= 923001234567, department= "Statistics", semester= 1)
    student2 = Student(name="Bilal", age= 19, whatsApp_number= 923003456789, department= "Mathematics", semester=1)
    
    faculty1 = Faculty(name= "Sir Zia Khan Sb", age= 50, whatsApp_number= 923002345678, department= "Computer Science")
    faculty2 = Faculty(name= "Sir Naveed Sb", age= 35, whatsApp_number=923004567890, department= "statistics")
    faculty3 = Faculty(name= "Sir Abu Hurrairah Sb", age=28, whatsApp_number=9230045678901, department= "Food Sciences")

    # Enroll Students in Courses
    student1.enroll_in_course(course1)
    student2.enroll_in_course(course2)

    
    faculty1.assign_course(course1)
    faculty2.assign_course(course2)
    faculty3.assign_course(course3)

    university.add_student(student1)
    university.add_student(student2)


    university.add_faculty(faculty1)
    university.add_faculty(faculty2)
    university.add_faculty(faculty3)

    # Save data to file
    university.save_data()

    print(university)
    print(university.students)
    print(university.faculty)
if __name__ == "__main__":
    main()


