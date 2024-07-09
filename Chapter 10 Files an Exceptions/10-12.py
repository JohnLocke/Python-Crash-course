# Favorite Number Remembered
from pathlib import Path
import json

path = Path('text_files/favourite_num.json')

if path.exists():
    contents = path.read_text()
    favourite_num = json.loads(contents)
    print(f"I know your favourite number! It’s {favourite_num}.")
else:
    prompt = "Please tell me your favourite number: "
    favourite_num = input(prompt)
    contents = json.dumps(favourite_num)
    path.write_text(contents)



