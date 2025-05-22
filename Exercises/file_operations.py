"""
File Operations Exercises
Fill in each section with appropriate code based on what you learned in class.
"""

import os
import glob
import json

# 5.1 Reading and Writing Text Files
def write_and_read_file():
    # Writing to a file (overwrite mode)
    with open("sample.txt", "w") as file:
        file.write("Hello, Python Students!")
    # Reading from a file
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)  # Output: Hello, Python!


# 5.2 Creating and Listing Directory Structure
def create_and_list_directory():
    # TODO: Create a new folder called "practice_folder"
    # TODO: List all files/folders in the current directory
    # TODO: List contents of "practice_folder"
    # Create a new directory (if it doesn't exist)
    os.makedirs("practice_folder", exist_ok=True)

    # List all files and folders in current directory
    print(os.listdir("."))

    # List all files in a specific directory
    print(os.listdir("practice_folder"))

# 5.3 Globbing (Pattern Matching for File Names)
def list_files_with_glob():
    # TODO: List all .txt files in current folder
    # TODO: List all .py files in current folder
    # List all .txt files in the current directory
    txt_files = glob.glob("*.txt")
    print(txt_files)

    # List all .mp3 files in 'music/' folder
    py_files = glob.glob("*.py")
    print(py_files)

# 5.4 open() Modes for Different Scenarios
def open_file_modes():
    # TODO: Append "This is an appended line.\n" to log.txt
    # TODO: Write binary data to a file (e.g. bytes of 0, 1, 2)
    # TODO: Read that binary file and print the content
    # Append text to file
    with open("log.txt", "a") as f:
        f.write("This is an appended line. \n")
    # Write binary data
    with open("output.bin", "wb") as f:
        f.write(b'\x00\x01\x02')
    # Read binary data
    with open("output.bin", "rb") as f:
        data = f.read()
        print(data)


def append_to_file():
    print("\n--- append_to_file() ---")
    # TODO: Append "This is an appended line.\n" to log.txt
    with open("log.txt", "a") as f:
        f.write("This is an appended line. \n")
    print("Successfully appended to log.txt.")

# 5.4.2 Binary Write and Read
def binary_write_and_read():
    print("\n--- binary_write_and_read() ---")
    # TODO: Write binary data to a file
    binary_data = b'\x00\x01\x02'
    with open("binary_output.bin", "wb") as f:
        f.write(binary_data)
    print("Wrote binary data to binary_output.bin")

    # TODO: Read that binary file and print the content
    with open("binary_output.bin", "rb") as f:
        data = f.read()
    print("Binary file contents:")
    print(data)

# 5.5 Streaming Large Files (Line by Line)
def stream_large_file():
    # TODO: Create a large file with 10 lines ( you can copy large_file.txt below)
    # TODO: Read and print each line using a for loop
    with open("large_file.txt", "r") as file:
        for line in file:
            print(line.strip())

# 5.6 Read File as String or Parse as JSON
def read_and_write_json():
    # TODO: Write a dictionary {"course": "Python", "students": 20} to output.json
    # TODO: Read it back and print the result
    with open("output.json", "w") as file:
        json.dump({"course": "Python", "students": 20}, file)
    with open("data.json", "r") as file:
        data = json.load(file)
    print(data)   # data is now a Python dict

# Run all exercises
if __name__ == "__main__":
    write_and_read_file()
    create_and_list_directory()
    list_files_with_glob()
    open_file_modes()
    append_to_file()
    binary_write_and_read()
    stream_large_file()
    read_and_write_json()