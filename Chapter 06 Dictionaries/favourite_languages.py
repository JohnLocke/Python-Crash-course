# A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

# Looping Through All Key-Value Pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print()

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())
print()

# You can access the value associated with any key you care about inside the loop by using the current key.
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# The keys() actually returns a list of all the keys, so you can check if 'erin' is in this list.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print()

# Looping Through a Dictionary’s Keys in a Particular Order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print()

# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print()

# Use set() to pull out the unique languages in favorite_languages.values().
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print()

# You can build a set directly using braces and separating the elements with commas.
languages = {'python', 'ruby', 'python', 'c'}
print(languages)

# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in
# a dictionary.
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        for language in languages:
            print(f"\n{name.title()}'s favorite languages is {language.title()}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
