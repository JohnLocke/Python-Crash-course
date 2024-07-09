# Changing Guest List
guests = ['Marx', 'Locke', 'Cowboy']
message = "May I have the pleasure of inviting you to dinner"
print(f"{guests[-1]} can not come to dinner.")
guests[-1] = "Daniel"
print(f"{message}, {guests[0]}?")
print(f"{message}, {guests[1]}?")
print(f"{message}, {guests[-1]}?")