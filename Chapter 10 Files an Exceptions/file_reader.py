# Reading the Contents of a File
from pathlib import Path

path = Path('text_files/pi_digits.txt')
# remove the extra blank line because read_text() returns an empty string when it reaches the end of the file;
# method chaining
contents = path.read_text().rstrip()
print(contents)


# Accessing a File’s Lines
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)
