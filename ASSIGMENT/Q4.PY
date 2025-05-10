4. Reading and Writing Files

Theory:
• Reading from a file using read(), readline(), readlines().

-Using read():

with open("sample.txt", "r") as file:
    content = file.read()  
    print(content)

-Using readline():

with open("sample.txt", "r") as file:
    line1 = file.readline()  
    print(line1, end="")  

    line2 = file.readline()
    print(line2, end="")

-Using readlines():

with open("sample.txt", "r") as file:
    lines = file.readlines() 
    print(lines)

• Writing to a file using write() and writelines().

Python provides two main methods to write data into a file:

write() → Writes a single string to the file.

writelines() → Writes multiple strings (a list of lines) to the file.


1. Using write():

with open("example.txt", "w") as file:  
    file.write("Hello, World!\n")
    file.write("Python makes file handling easy.\n")  

print("Data written successfully!")


2. Using writelines():

lines = ["Line 1: Hello, World!\n", "Line 2: Learning Python.\n", "Line 3: Writing to files is easy.\n"]

with open("example.txt", "w") as file: 
    file.writelines(lines)  

print("Multiple lines written successfully!")


Lab:
    
• Write a Python program to read the contents of a file and print them on the console.


with open("example.txt", "r") as file:
    content = file.read()  
    print(content)  

• Write a Python program to write multiple strings into a file.

with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python makes file handling easy.\n")
    file.write("This is a sample text file.\n")

print("Multiple strings written successfully!")

Practical:4) Write a Python program to create a file and print the string into the file.

with open("output.txt", "w") as file:
    print("Hello, this is a printed string inside the file!", file=file)

print("File created and string printed successfully!")



5) Write a Python program to read a file and print the data on the console.

with open("output.txt", "r") as file:
    data = file.read()  
    print("File Content:\n", data)  



