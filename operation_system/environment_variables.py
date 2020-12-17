import os

print(os.environ['HOME'])
print(os.environ['SHELL'])

print(os.getenv('HOME'))
print(os.getenv('MYHOME', '/root')) # If don't find a variable, you can set one as the default