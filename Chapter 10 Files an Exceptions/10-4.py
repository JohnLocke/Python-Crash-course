# Guest
from pathlib import Path

path = Path('text_files/guest.txt')

name = input("What's your name? ")
path.write_text(name)


