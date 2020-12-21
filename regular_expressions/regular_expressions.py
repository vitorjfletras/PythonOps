# https://regex101.com/

import re

with open('names.txt') as file:
    lines = file.read()
    pattern = r'[\w]+ Silva'
    regex = re.findall(pattern, lines)
    print(regex)

    regex = re.search(pattern, lines)
    print(regex.group()) # .group() to print all matches

    regex = re.match(pattern, lines)
    print(regex.group())