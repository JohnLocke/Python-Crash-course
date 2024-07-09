# Favorite Number: reads in this value and prints a message.
from pathlib import Path
import json


path = Path('text_files/favourite_num.json')
contents = path.read_text()
favourite_num = json.loads(contents)

print(f"I know your favourite number! It’s {favourite_num}.")

