# 'r' – Read mode (default)
# 'w' – Write mode (creates a new file or truncates an existing file)
# 'a' – Append mode (adds to an existing file)
# 'b' – Binary mode (used with other modes, e.g., 'rb' for reading binary files)
# read from afile using : read(),readLine(),readLines()
# write to a file using write() or writeLines()
# append to a file using append mode 'a'
# use with statement for automatic file closing
# handle file-related exceptions to handle errors more gracefully


try:
    with open('example.txt','r') as file:
        content = file.read()
except FileNotFoundError:
    print("File does not exist nigga!!")
except IOError:
    print("error occured while reading file!!")


file = open('example.txt', 'r')
content = file.read()         # Read the entire file
print(content)
file.close()                  # Close the file when done
