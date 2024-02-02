
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi {self.name}, you're {self.age} y/0")


class Student(Person):

    def welcome_student(self):
        print(f"Hi {self.name}, you're a great student!")


# class WorkingStudent(Student):

#     def welcome_working_student(self):
#         print(f"Hi {self.name}, you're a great working student!")


alice = Person("Alice", 30)
bob = Student("Bob", 23)

alice.greet()
bob.greet()
bob.welcome_student()

# sara = WorkingStudent("Sara", 23)
# sara.welcome_student()
# sara.welcome_working_student()
