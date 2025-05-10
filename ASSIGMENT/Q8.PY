8. Method Overloading and Overriding

Theory:
    
• Method overloading: defining multiple methods with the same name but different parameters.


-Method Overloading

Definition:
    
Method overloading is when you define multiple methods with the same name in a class,
but each has a different set of parameters (type, number, or both).

• Method overriding: redefining a parent class method in the child class.

Definition:
    
Method overriding is when a child class provides its own version of a method that is already
defined in its parent class.

Purpose:
To modify or extend the behavior of a method inherited from a parent class.



Lab:

• Write Python programs to demonstrate method overloading and method overriding.


method overloading


class A:
    def show(self):
        print("welcome")
        
    def show(self, firstname=''):
        print("welcome", firstname)
        
    def show(self, firstname='', lastname=''):
        print("welcome", firstname, lastname)

    
obj=A()
obj.show()
obj.show('sarfraz')
obj.show('sarfraz', 'khan')    

method overriding

class A:
    def disp(self):
        print("This is parent class method")
        
class B(A):
    def disp(self):
        super().disp()
        print("This is child class mehtod")
obj=B()
obj.disp()


Practical Examples: 19) Write a Python program to show method overloading.

class A:
    def Show(self):
        proint("Welcome")

    def Show(self,firstname=''):
        print("Welcome",firstname)

    def Show(self,firstname='',lastname=''):
        print("Welcome",firstname,lastname)

obj=A()
obj.Show()
obj.Show('sarfraz')
obj.Show('sarfraz','khan')



20) Write a Python program to show method overriding.

class A:
    def Disp(self):
        print("This is parent class method")
        
class B:
    def Disp(self):
        super().Disp()
        print("This is child class method")

obj=B()
obj.Disp()
