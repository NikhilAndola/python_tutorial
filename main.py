import os
import shutil

# os.mkdir("os_operation/test3")
# os.rmdir("os_operation/test2")

# os.rename("os_operation/test3", "os_operation/test")

# use of os.remove to delete a file
# os.remove("os_operation/gb.py")

# use of os to check if a file exists
# print(os.path.exists("os_operation/gb.py"))

# use of os to check if a directory exists
# print(os.path.exists("os_operation/test"))

# use of os to list all files and directories in the current directory
# print(os.listdir())

# use of os to get the current working directory
# print(os.getcwd())

# use of os to change the current working directory
# os.chdir("os_operation")
# print(os.getcwd())

# use of os to create files
# with open("os_operation/file1.txt", "w") as f:
#     f.write("This is file 1")

# with open("os_operation/gb.py", "w") as f:
#     f.write("print('Hello, World!')")

# use of os to read a file
# with open("os_operation/file1.txt", "r") as f:
#     content = f.read()
#     print(content)

# use of os to append to a file
# with open("os_operation/file1.txt", "a") as f:
#     f.write("\nThis is an appended line.")

# use of os to read a file line by line
# with open("os_operation/file1.txt", "r") as f:
#     for line in f:
#         print(line.strip())


# use of os to check if a file is empty
# with open("os_operation/file1.txt", "r") as f:
#     content = f.read()
#     if not content:
#         print("The file is empty.")
#     else:
#         print("The file is not empty.")


# use of os to get the size of a file
# file_size = os.path.getsize("os_operation/file1.txt")
# print(f"The size of the file is: {file_size} bytes")

# use of os to get the last modified time of a file
# last_modified_time = os.path.getmtime("os_operation/file1.txt")
# print(f"The last modified time of the file is: {last_modified_time}")

# use of os to get the absolute path of a file
# absolute_path = os.path.abspath("os_operation/file1.txt")
# print(f"The absolute path of the file is: {absolute_path}")

# use of os to check if a path is a file or a directory
# print(os.path.isfile("os_operation/file1.txt"))  # True
# print(os.path.isdir("os_operation/test"))  # True

# use of os to walk through a directory
# for dirpath, dirnames, filenames in os.walk("os_operation"):
#     print(f"Directory: {dirpath}")
#     print(f"Subdirectories: {dirnames}")
#     print(f"Files: {filenames}")
#     print()


# use of os to create a directory if it does not exist
# if not os.path.exists("os_operation/new_dir"):
#     os.mkdir("os_operation/new_dir")
#     print("Directory created.")
# else:
#     print("Directory already exists.")

# use of os to remove a directory if it exists
# if os.path.exists("os_operation/new_dir"):
#     os.rmdir("os_operation/new_dir")
#     print("Directory removed.")
# else:
#     print("Directory does not exist.")

# use of os to remove a file if it exists
# if os.path.exists("os_operation/file1.txt"):
#     os.remove("os_operation/file1.txt")
#     print("File removed.")
# else:
#     print("File does not exist.")

# use of os to rename a file if it exists
# if os.path.exists("os_operation/gb.py"):
#     os.rename("os_operation/gb.py", "os_operation/hello.py")
#     print("File renamed.")
# else:
#     print("File does not exist.")

# use of os to rename directory if it exists
# if os.path.exists("os_operation/test"):
#     os.rename("os_operation/test", "os_operation/test_renamed")
#     print("Directory renamed.")
# else:
#     print("Directory does not exist.")

# use of os to copy a file
# shutil.copy("os_operation/gb.py", "os_operation/hello_copy.py")

# use of os to copy a directory
# shutil.copytree("os_operation/test", "os_operation/test_copy")

# use of os to move a file
# shutil.move("os_operation/hello.py", "os_operation/test/hello_moved.py")

print("Current working directory:", os.getcwd())

# os.system("ls -l")
