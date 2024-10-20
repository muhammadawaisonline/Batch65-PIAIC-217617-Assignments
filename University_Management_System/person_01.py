class Person:
    def __init__(self, name:str, age:int, whatsApp_number:int):
        self.name = name
        self.age = age
        self.whatsApp_number = whatsApp_number

    def __str__(self):
        return f"{self.__class__.__name__}(Name: {self.name}, Age: {self.age}, WhatsApp Number: {self.whatsApp_number})"

person = Person( name= "Muhammad Ahsan", age= "26", whatsApp_number= 923211234567 )
print(person)
if __name__ == "__person__":
    Person()