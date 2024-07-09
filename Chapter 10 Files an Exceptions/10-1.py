# Learning Python
from pathlib import Path

path = Path('text_files/learning_python.txt')
context = path.read_text().rstrip()
print(context)

lines = context.splitlines()
for line in lines:
    print(line)
