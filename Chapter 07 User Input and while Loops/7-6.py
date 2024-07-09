# Three Exits
# Plan A: Use a conditional test in the while statement to stop the loop.
print("Plan A")
prompt = "How old are you?"
prompt += "\n(Enter 'quit' when you are finished.)\n"

age = ''

while age != 'quit':
    age = input(prompt)

    if age != 'quit':
        age = int(age)

        if age < 3:
            print("The ticket is free.\n")
        elif age < 12:
            print("The ticket is $10.\n")
        else:
            print("The ticket is $15.\n")

# Plan B: Use an active variable to control how long the loop runs.
print("\nPlan B")
prompt = "How old are you?"
prompt += "\n(Enter 'quit' when you are finished.)\n"

active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False

    else:
        age = int(age)

        if age < 3:
            print("The ticket is free.\n")
        elif age < 12:
            print("The ticket is $10.\n")
        else:
            print("The ticket is $15.\n")


# Plan C: Use a break statement to exit the loop when the user enters a 'quit' value.
print("\nPlan C")
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
