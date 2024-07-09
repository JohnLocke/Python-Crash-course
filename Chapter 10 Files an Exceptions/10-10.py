# Common Words
from pathlib import Path


def common_words(filename, word):
    """Find out how many times a word or phrase appears in a text."""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


common_words('text_files/alice.txt', 'the')
