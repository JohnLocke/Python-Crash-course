# Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_list = ['jen', 'edward', 'lily', 'kevin']

for person in poll_list:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}.")
    else:
        print(f"Welcome to take the poll, {person.title()}.")
