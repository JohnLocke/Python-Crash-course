"""A class that can be used to represent a admin."""

from user import User


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