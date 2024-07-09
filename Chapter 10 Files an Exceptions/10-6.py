# Addition
prompt = "Give me two numbers, and I'll add them together."
print(prompt)

first_number = input("\nFirst number: ")
second_number = input("Second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("You need to provide numbers instead of text.")
else:
    print(answer)
