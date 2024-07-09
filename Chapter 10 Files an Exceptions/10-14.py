# Verify User
from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("\nWhat is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('text_files/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")

        while True:
            flag = input(f"Are you {username}, by the way? (y/n)")

            if flag == 'y':
                break
            elif flag == 'n':
                username = get_new_username(path)
                print(f"We'll remember you when you come back, {username}!")
                break
            else:
                print("\nPlease input 'y' or 'n'.")
                continue

    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
