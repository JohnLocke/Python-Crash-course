# We’ll define a quit value and then keep the program running as long as the user has not entered the quit value.
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# Add a flag and this flag will monitor whether the program should continue running:
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)



