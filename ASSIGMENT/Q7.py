7. Inheritance


Theory:

    
• Single, Multilevel, Multiple, Hierarchical, and Hybrid inheritance in Python.

•Single, Multilevel, Multiple, Hierarchical, and Hybrid inheritance in Python.

Single Inheritance

-One child class inherits from one parent class.

Multilevel Inheritance

-A class inherits from a child class which is itself derived from another class.

Multiple Inheritance

-A class inherits from more than one parent class.

Hierarchical Inheritance

-Multiple child classes inherit from the same parent class.

Hybrid Inheritance

-A combination of two or more types of inheritance (like multilevel + multiple).


• Using the super() function to access properties of the parent class.

-super() is a built-in function used to access methods and properties of the parent class.

-It’s commonly used inside the child class’s methods, especially the __init__() constructor
 
Lab:
    
• Write Python programs to demonstrate different types of inheritance (single, multiple,
multilevel, etc.)

-Single Inheritance

# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object
d = Dog()
d.speak()
d.bark()

-Multilevel Inheritance

class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.move()
p.bark()
p.weep()

-Multiple Inheritance

class Father:
    def skill_father(self):
        print("Father: Plays cricket")

class Mother:
    def skill_mother(self):
        print("Mother: Sings songs")

class Child(Father, Mother):
    def skill_child(self):
        print("Child: Learns coding")

c = Child()
c.skill_father()
c.skill_mother()
c.skill_child()

-Hierarchical Inheritance

class Vehicle:
    def show_type(self):
        print("I am a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class Bike(Vehicle):
    def bike_info(self):
        print("This is a bike")

c = Car()
b = Bike()

c.show_type()
c.car_info()

b.show_type()
b.bike_info()

-Hybrid Inheritance (Combination of multiple + multilevel)

class Person:
    def basic_info(self):
        print("I am a person")

class Employee(Person):
    def emp_info(self):
        print("I work in a company")

class Freelancer:
    def freelance_info(self):
        print("I work as a freelancer")

class Hybrid(Employee, Freelancer):
    def hybrid_info(self):
        print("I do both freelancing and job")

h = Hybrid()
h.basic_info()
h.emp_info()
h.freelance_info()
h.hybrid_info()



Practical Examples: 13) Write a Python program to show single inheritance.

class father:
    def lands(self):
        print("i am father class")
class son(father):
    def money(self):
        print("i am father son")

obj=son()
obj.lands()
obj.money()

14) Write a Python program to show multilevel inheritance.

class Father:
    surname="khan"
class son(Father):
    def Show(self):
        print("sarfraz",self.surname)
class gsson(Father):
    def Disp(self):
        print("babu",self.surname)

obj=son()
obj.Show()

obj=gsson()
obj.Disp()

15) Write a Python program to show multiple inheritance.


class Sarfraz:
    Back="oracle DB & java"
    def Backend(self):
        print("Backend Task implemented using: ",self.Back)
class Babu:
    Front="HTML CSS javaScript"
    def Fronted(self):
        print("Fronted Task implemented using: ",self.Front)
class Teamlead(Khan,Babu):
    def show(self):
        print("Dyanmic Website created...")


T.Teamlead()
T.Backend()
T.Fronted()
T.show()

16) Write a Python program to show hierarchical inheritance.

class Father:
    surname="khan"
    def Show(self):
        print("MY surname is",self.surname)
        
class Son1(Father):
    def Disp(self):
        print("MY name is sarfraz",self.surname)


class Son2(Father):
    def out(self):
        print("MY name is sarfraz",self.surname)

s1=son1()
s2=son2()

s1.Disp()
s2.out()

17) Write a Pythonprogram to show hybrid inheritance.
class A:
    def display_A(self):
        print("Class A")


class B(A):
    def display_B(self):
        print("Class B")


class C(A):
    def display_C(self):
        print("Class C")


class D(B, C):
    def display_D(self):
        print("Class D")


obj = D()


obj.display_A()  
obj.display_B()  
obj.display_C() 
obj.display_D()  


18) Write a Python program to demonstrate the use of super() in inheritance.

class Parent:
    def show(self):
        print("This is the Parent class.")


class Child(Parent):
    def show(self):
        super().show() 
        print("This is the Child class.")


obj = Child()
obj.show()
