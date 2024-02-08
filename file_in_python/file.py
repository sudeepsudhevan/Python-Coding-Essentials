# Writing to a file
with open('example.txt', 'w') as write_file:
    write_file.write("Hello, this is a sample file.\n")
    write_file.write("Python is a powerful programming language.")

# Reading from a file
with open('example.txt', 'r') as read_file:
    content = read_file.read()
    print("Content of the file:")
    print(content)

# Appending to a file
with open('example.txt', 'a') as append_file:
    append_file.write("\nAppending more text to the file.")

# Reading the updated content
with open('example.txt', 'r') as updated_read_file:
    updated_content = updated_read_file.read()
    print("\nUpdated content of the file:")
    print(updated_content)