# Shrinking Guest List
guests = ['Marx', 'Locke', 'Cowboy']
message = "May I have the pleasure of inviting you to dinner"

print("I found a bigger table.")
guests.insert(0, 'Frank')
guests.insert(2, 'Lily')
guests.append('Tina')

print("The new table could not be delivered in time")
print(f"I am sorry that I can not invite you to dinner, {guests.pop()}")
print(f"I am sorry that I can not invite you to dinner, {guests.pop()}")
print(f"I am sorry that I can not invite you to dinner, {guests.pop()}")
print(f"I am sorry that I can not invite you to dinner, {guests.pop()}")
print(f"I am still waiting for you to dinner, {guests[0]}")
print(f"I am still waiting for you to dinner, {guests[1]}")

del guests[1]
del guests[0]
print(guests)