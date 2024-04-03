try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("My name is Edmund\n")
        file.write("I study Mechanical Engineering\n")
        file.write("I am part if the 2024 cohort at PLP\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("I am learning python\n")
        file.write("We are currently learning file handling\n")
        file.write("This is my assignment\n")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File handling completed.")