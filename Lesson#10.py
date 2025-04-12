# LESSON # 10  FILE HANDLING

# Task 1: Create a new file and write some text to it

def write_to_file():
    with open("myfile.txt", "w") as file:
        file.write("Hello, this is Lesson 10 - File Handling in Python!\n")
        file.write("This is the second line of the file.\n")
    print("Task 1 completed: File created and data written.")

write_to_file()


# Task 2: Read the content of the file and display it

def read_file():
    try:
        with open("myfile.txt", "r") as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print("File not found.")

read_file()


# Task 3: Append new lines to the file

def append_to_file():
    with open("myfile.txt", "a") as file:
        file.write("This line is appended.\n")
        file.write("Appending more content for practice.\n")
    print("Task 3 completed: Data appended.")

append_to_file()


# Task 4: Read file line by line using a loop

def read_line_by_line():
    with open("myfile.txt", "r") as file:
        print("Reading line by line:")
        for line in file:
            print(line.strip())

read_line_by_line()
