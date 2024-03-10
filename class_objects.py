'''
An Object Oriented Programming language such as Python, is a way of programming that focuses on using objects and classes to design and build applications.
a class is a blueprint for objects.
an object is an instance of a class.
for example, you have a class called Car. A car has properties like weight and color, and methods like start and stop.


To create a class in python, use the keyword class:
Once you have a class, you can use it to create objects.
To create an object of a class, you use the class name followed by parenthesis:
'''

# Example.  The __init__() Function
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# The __str__() Function
# The __str__() function is used to return a string representation of the object.
# The __str__() function is called when you use the print() function to print an object:


# Objects can also contain methods. Methods in objects are functions that belong to the object.

class MyClass:
    x = 5

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
    this_is_an_attribute = 'Just an example'
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"I am {self.name}"
    
    def calculate(self, x: int, y: int) -> int:
        return x*y
    
    def say_hi(self) -> str:
        return f"Hello everyone: My name is {self.name} and I am {self.age}."
        





if __name__ == '__main__':
    # first = MyClass()
    fperson = Person(name="Paul", age=14)
    sperson = Person(name="Jules", age=15)

    print(fperson.say_hi())
    print(sperson.say_hi())
    print(sperson.this_is_an_attribute)
    print(f"I called the function calculate an I got {sperson.calculate(x=2, y=5)}")


