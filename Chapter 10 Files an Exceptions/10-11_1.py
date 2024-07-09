# Favorite Number: prompts for the user’s favorite number.
from pathlib import Path
import json


prompt = "Please tell me your favourite number: "
favourite_num = input(prompt)

path = Path('text_files/favourite_num.json')
contents = json.dumps(favourite_num)
path.write_text(contents)




