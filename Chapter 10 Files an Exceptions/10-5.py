# Guest Book
from pathlib import Path

names = ''
while True:
    print("Enter 'quit' to end the program.")
    name = input("What's your name?")
    if name == 'quit':
        break
    else:
        names += name
        names += '\n'

path = Path('text_files/guest_book.txt')
path.write_text(names)
