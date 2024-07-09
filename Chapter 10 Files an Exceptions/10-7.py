# Addition Calculator
prompt = "Give me two numbers, and I'll add them together.\n"
prompt += "Enter 'q' to quit."
print(prompt)

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You need to provide numbers instead of text.")
    else:
        print(answer)
