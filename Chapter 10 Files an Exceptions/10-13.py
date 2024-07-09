# User Dictionary


from pathlib import Path
import json


def get_stored_userinfo(path):
    """Get stored user's info if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_userinfo(path):
    """Prompt for a new user's info."""
    user_info = {}
    user_info['username'] = input("What is your name? ")
    user_info['gender'] = input("What is your gender? ")
    user_info['age'] = input("What is your age? ")

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def show_userinfo():
    """Showing all the information about the user."""
    path = Path('text_files/userinfo.json')
    user_info = get_stored_userinfo(path)
    if user_info:
        for k, v in user_info.items():
            print(f"{k}: {v}")
    else:
        user_info = get_new_userinfo(path)
        print(f"We'll remember your info when you come back, {user_info['username']}!")


show_userinfo()
