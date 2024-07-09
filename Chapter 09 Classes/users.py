"""A set of users used to represent user and admin."""


class User:
    """A simple attempt to model a restaurant."""

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user’s information."""
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0


class Privileges:
    """Stores the administrator’s set of privileges."""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Lists the administrator’s set of privileges."""
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """An administrator is a special kind of user."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize first_name, last_name, age, gender and privilege attributes."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges(["can add post", "can delete post", "can ban user"])
