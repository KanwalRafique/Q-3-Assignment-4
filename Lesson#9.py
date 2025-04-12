# LESSON # 9 EXCEPTION HANDLING
#🔹 Task 1: Handle Division by Zero

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Division operation completed.")

divide_numbers(10, 0)



# 🔹 Task 2: Handle Invalid Input
def get_integer_input():
    try:
        value = int(input("Enter a number: "))
        print(f"You entered: {value}")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")

get_integer_input()



# 🔹 Task 3: File Not Found Error Handling

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")

read_file("sample.txt")



# 🔹 Task 4: Use of else and finally

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Division successful. Result = {result}")
    finally:
        print("Execution of safe_divide completed.")

safe_divide(12, 3)
