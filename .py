print("tariq")
print("ameen")
print("Hello")

# Polymorphism:

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    # Polymorphic method
    def display_info(self):
        print(f"User: {self.username}, Email: {self.email}")

class Admin(User):
    def __init__(self, username, email, access_level):
        # Inheriting the parent class properties using super()
        super().__init__(username, email)
        self.access_level = access_level

    # Overriding the polymorphic method
    def display_info(self):
        print(f"Admin: {self.username}, Email: {self.email}, Access Level: {self.access_level}")

# Creating instances of User and Admin
user1 = User("regular_user", "user@example.com")
admin1 = Admin("admin_user", "admin@example.com", "SuperUser")

# Demonstrating polymorphism
def show_user_info(user):
    user.display_info()

# Calling the same method on different objects
show_user_info(user1)   # Calls User display_info()
show_user_info(admin1)  # calls User display_info()
