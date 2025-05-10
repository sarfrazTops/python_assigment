6. Class and Object (OOP Concepts)

Theory:
    
• Understanding the concepts of classes, objects, attributes, and methods in Python.


1. Class

A class is like a blueprint for creating objects. It defines the attributes (data)
and methods (functions) an object will have.

2. Object

An object is an instance of a class. It’s like a real-world example of the blueprint.

3. Attributes

Attributes are variables that belong to a class or object. They hold the data about the object

4. Methods

Methods are functions defined inside a class. They describe what an object can do.


• Difference between local and global variables.

local variables are define within the function that can access inside function.

Golbal variablrs are define out side the function can be accesed outside the function.



Lab:
• Write a Python program to create a class and access its properties using an object.

class Student:
    
    def __init__(self, name, grade):
        self.name = name      
        self.grade = grade     


student1 = Student("John", "A")


print("Student Name:", student1.name)
print("Student Grade:", student1.grade)


Practical Examples: 11) Write a Python program to create a class and access the properties
of the class using an object.

class A:
    def __init__(self, name, age):
        self.name = name  # Property 1
        self.age = age    # Property 2
        print(name,age)
        
obj=A("sarfraz",21)

12) Write a Python program to demonstrate the use of local and
global variables in a class.

a=500 #global variable
def demo(c):
    b=100     #local variable
    sum1 = b + c
    print(sum1)
demo(200)
print(a)
