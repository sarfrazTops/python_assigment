3. Opening and Closing Files


Theory:

• Opening files in different modes ('r', 'w', 'a', 'r+', 'w+').

1. Read Mode ('r')

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

2. Write Mode ('w')

with open("example.txt", "w") as file:
    file.write("Hello, World!")

3. Append Mode ('a')

with open("example.txt", "a") as file:
    file.write("\nAppended text.")

4. Read & Write Mode ('r+')

with open("example.txt", "r+") as file:
    print(file.read())  # Read existing content
    file.write("\nNew text added.")  # Write new content

5. Read & Write Mode ('w+')

with open("example.txt", "w+") as file:
    file.write("Fresh Start!")  # Writing new content
    file.seek(0)  # Move cursor to start
    print(file.read())

• Using the open() function to create and access files.

1. Creating a File in Python

file = open("myfile.txt", "w")  # Creates a file if it doesn't exist
file.write("Hello, this is a test file.")  # Writing data
file.close()  # Closing the file

2. Opening and Reading a File

file = open("myfile.txt", "r")  # Open file in read mode
content = file.read()  # Read file content
print(content)  # Display content
file.close()  # Close file

•Closing files using close().

file = open("example.txt", "w")  # Open file in write mode
file.write("Hello, World!")  # Write to file
file.close()  # Close the file




Lab:
• Write a Python program to open a file in write mode, write some text, and then close it.

# Open the file in write mode
file = open("example.txt", "w")

# Write some text into the file
file.write("Hello, this is a sample text.\n")
file.write("Python makes file handling easy!\n")

# Close the file
file.close()

print("File written and closed successfully.")


Practical Example: 3) Write a Python program to create a file and write a string into it.

with open("myfile.txt", "w") as file:
         file.write("hello world!")



