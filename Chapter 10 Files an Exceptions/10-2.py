# Learning C
from pathlib import Path

path = Path('text_files/learning_python.txt')
context = path.read_text()

lines = context.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)
