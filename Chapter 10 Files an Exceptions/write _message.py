# Writing to a File
from pathlib import Path


# Writing a Single Line
path = Path('text_files/programming.txt')
path.write_text("I love programming.")


# Writing Multiple Lines
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

# If the file already exists, write_text() will erase the current contents
# of the file and write new contents to the file.
path = Path('text_files/programming.txt')
path.write_text(contents)
