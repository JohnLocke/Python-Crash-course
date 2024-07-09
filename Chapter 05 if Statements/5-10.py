# Checking Usernames
current_users = ['admin', 'John', 'Lily', 'Mary', 'David']
new_users = ['Kevin', 'James', 'Anna', 'Mary', 'David']

for new_user in new_users:
    if new_user in current_users:
        print(f"The username '{new_user}' has already been used, you need to enter anew username.\n")
    else:
        print(f"The username '{new_user}' is available.\n")
