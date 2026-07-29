import os

# Specify the directory you want to list
directory_path = '/'

# List all file and directories in the specified path 
contents = os.listdir(directory_path)

# print each file and directoruy name
for item in contents:
    print(item)