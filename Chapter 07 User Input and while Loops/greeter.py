# Each time you use the input() function, you should include a clear, easy-to-follow prompt
# that tells the user exactly what kind of information you’re looking for.
name = input('Please enter your name: ')
print(f"\nHello, {name}!")

# You can assign your prompt to a variable and pass that variable to the input() function.
# This allows you to build your prompt over several lines, then write a clean input() statement.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?\n"

name = input(prompt)
print(f"\nHello {name}!")
