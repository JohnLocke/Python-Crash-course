# Pizza Toppings
prompt = "Please tell me what toppings do you want? "
prompt += "\n(Enter 'quit' when you are finished.)\n"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I’ll add {topping} to your pizza.\n")
