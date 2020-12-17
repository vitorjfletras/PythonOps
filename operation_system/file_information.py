import os

FILE_NAME = 'environment_variables.py'

# Convert epoch to human-readable date and vice versa
# https://www.epochconverter.com/


# For unix return the last modification, for other S.O., such as windows create the creation date
print(os.path.getctime(FILE_NAME))

# Return last moditification
print(os.path.getmtime(FILE_NAME))

# Return last access
print(os.path.getatime(FILE_NAME))

# Verify if is a file
print(os.path.isfile(FILE_NAME))

# Verify if is a directory
print(os.path.isdir(FILE_NAME))

# Verify if is a symlink
print(os.path.islink(FILE_NAME))

# Verify if is a mounting point
print(os.path.ismount(FILE_NAME))