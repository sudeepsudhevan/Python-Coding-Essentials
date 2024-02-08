text_file = open('sample.txt','r')

line_list = text_file.readlines()

for line in line_list:
    print(line)

text_file.close()

#####################################################

# Using with statement to automatically close the file
with open('sample.txt', 'r') as text_file:
    line_list = text_file.readlines()

    for line in line_list:
        print(line)
    
# File is automatically closed outside the 'with' block

######################################################################

def file_operations(filename):
    # Writing to a file
    with open(filename, 'w') as write_file:
        write_file.write("Hello, this is a sample file.\n")
        write_file.write("Python is a powerful programming language.")

    # Opening the file in read mode
    with open(filename, 'r') as read_file:
        # Using tell() to get the current file position
        current_position = read_file.tell()
        print(f"\nCurrent file position after opening: {current_position}")

        # Reading content from the file
        content = read_file.read()
        print("Content of the file:")
        print(content)

        # Using tell() again to get the file position after reading
        current_position = read_file.tell()
        print(f"\nCurrent file position after reading: {current_position}")

        # Using fileno() to get the file descriptor
        file_descriptor = read_file.fileno()
        print(f"\nFile descriptor: {file_descriptor}")

        # Using seek() to move the file position to the beginning
        read_file.seek(0)

        # Using tell() to get the file position after seeking
        current_position = read_file.tell()
        print(f"\nCurrent file position after seeking to the beginning: {current_position}")

        # Using seekable() to check if the file is seekable
        is_seekable = read_file.seekable()
        print(f"\nIs the file seekable? {is_seekable}")

# Example usage of the function
file_operations('sample.txt')