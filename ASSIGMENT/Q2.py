2. Reading Data from Keyboard


Theory:
    
• Using the input() function to read user input from the keyboard.

•Using the input() function to read user input from the keyboard.

name = input("Enter your name: ")
print(f"Hello, {name}!")


• Converting user input into different data types (e.g., int, float, etc.).

1. Converting to an Integer (int)

age = int(input("Enter your age: "))
print(f"Next year, you will be {age + 1} years old.")

2. Converting to a Float (float)

height = float(input("Enter your height in meters: "))
print(f"Your height is {height}m.")

3. Converting to a Boolean (bool)

is_student = bool(input("Are you a student? (Press Enter for No, type anything for Yes): "))
print(f"Student status: {is_student}")


Lab:
    
• Write a Python program to read a name and age from the user and print a formatted output.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")
print("Hello, {}! You are {} years old.".format(name, age))


Practical Example: 2) Write a Python program to read a string, an integer, and a float from
the keyboard and display them

name = input("Enter a string (your name): ")
age = int(input("Enter an integer (your age): "))
height = float(input("Enter a float (your height in meters): "))


print(f"\nYou entered:\nName: {name}\nAge: {age}\nHeight: {height} meters")

