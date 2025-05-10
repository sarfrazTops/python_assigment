5. Exception Handling

Theory:
    
• Introduction to exceptions and how to handle them using try, except, and finally.

a=int(input("Enter the first number: "))
b=int(input("Enter the secnd number: "))

try:
    c=a/b
    print("Result :",c)
except:
    print("cant divide is to zero")
    
finally:
    print("Done")





Lab:
    
• Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
input).

def calculator():
    try:
        print("Simple Calculator")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
    except Exception as e:
        print("Something went wrong:", e)
    finally:
        print("Calculation finished.")


calculator()


• Write a Python program to demonstrate handling multiple exceptions

def multiple_exception_demo():
    try:
        print("Multiple Exception Handling Demo")
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        
        result = num1 / num2
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid integers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        print("Program execution completed.")


multiple_exception_demo()


Practical Examples: 7) Write a Python program to handle exceptions in a calculator.

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print(""" 
    Press 1 for Addition
    Press 2 for Subtraction
    Press 3 for Multiplication
    Press 4 for Division
    """)

    choice = int(input("Enter the number: "))

    if choice == 1:
        print("Result:", num1 + num2)
    elif choice == 2:
        print("Result:", num1 - num2)
    elif choice == 3:
        print("Result:", num1 * num2)
    elif choice == 4:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        print("Result:", num1 / num2)
    else:
        print("Error: Enter a valid choice (1-4)")

except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError as e:
    print("Math Error:", e)
except Exception as e:
    print("Unexpected Error:", e)




9) Write a Python program to handle file exceptions and use the finally block for closing
the file.

try:
    # Attempt to open a file that may not exist
    file = open("example.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except IOError:
    print("Error: An I/O error occurred.")

finally:
    
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so no need to close it.")

9) Write a Python program to print custom exceptions.

a=int(input("Enter the bumber between 1 to 5"))
     if a<1 and a>5:
         raise ValueError("value should between 1 to 5 ")










