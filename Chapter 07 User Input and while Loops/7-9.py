# No Pastrami
sandwich_orders = ['Pastrami', 'Tuna', 'Ham', 'Chicken',
                   'Pastrami', 'Ham', 'Pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Finished_sandwiches ---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
