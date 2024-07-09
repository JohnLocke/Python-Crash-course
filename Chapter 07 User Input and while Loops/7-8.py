# Deli
sandwich_orders = ['Reuben sandwich', 'Submarine sandwich', 'oyster poboy',
                   'Philly cheesesteak']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Finished_sandwiches ---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
