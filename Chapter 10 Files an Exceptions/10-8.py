# Cats and Dogs
from pathlib import Path


filenames = ['text_files/cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
    else:
        print(contents)



