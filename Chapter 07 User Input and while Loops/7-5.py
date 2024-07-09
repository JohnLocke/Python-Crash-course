# Movie Tickets
prompt = "How old are you?"
prompt += "\n(Enter 'quit' when you are finished.)\n"

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            print("The ticket is free.\n")
        elif age < 12:
            print("The ticket is $10.\n")
        else:
            print("The ticket is $15.\n")
