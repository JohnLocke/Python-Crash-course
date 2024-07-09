# Restaurant Seating
people_number = input("How many people are in your dinner group? ")
people_number = int(people_number)
if people_number > 8:
    print("Sorry, we don't have empty table now, you'll have to wait for a table.")
else:
    print("Sure, your table is ready now.")
