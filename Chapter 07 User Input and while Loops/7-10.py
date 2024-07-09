# Dream Vacation
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would you go? "

vacation_poll = {}
poll_active = True

while poll_active:
    name = input(name_prompt)
    place = input(place_prompt)

    vacation_poll[name] = place

    repeat = input("Would you like to ask another person? (yes/no) ")
    if repeat == 'no':
        poll_active = False

print("\n--- Poll Results ---")
for name, place in vacation_poll.items():
    print(f"{name.title()} would like to visit {place}.")
