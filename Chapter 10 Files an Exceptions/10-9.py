# Silent Cats and Dogs
from pathlib import Path

filenames = ['text_files/cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)
