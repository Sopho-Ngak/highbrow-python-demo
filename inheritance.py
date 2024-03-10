'''
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''

from class_objects import Person

#Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class Student(Person):
    # pass
    def __init__(self, name: str, age: int, grade: float, year:int) -> None:
        super().__init__(name=name, age=age)
        self.grade = grade
        self.year = year
    def calculate(self, x: int) -> int:
        return x*5


if __name__ == '__main__':
    student1 = Student("Jean", 23, 12.5, 2024)

    print(student1.grade)
    print(student1.calculate(2))

        
