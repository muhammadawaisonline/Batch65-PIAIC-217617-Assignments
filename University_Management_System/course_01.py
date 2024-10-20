class Course:
    def __init__(self, course_name: str, course_code : str, credits: int):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits

    def __str__(self):
        return f"{self.__class__.__name__}: (Course Name: {self.course_name}, Course Code: {self.course_code}, Credit Hours: {self.credits})"
    
course = Course(course_name= "LangChain", course_code="CS209", credits=32)

print(course)
